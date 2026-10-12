from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os

from app.config import STATIC_DIR, GROQ_MODEL, JAVA_EXEC
from app.models import (
    ExecuteRequest, ExecuteResponse,
    HintRequest, HintResponse,
    ExplainCauseRequest, ExplainCauseResponse,
    TransferChallengeRequest, TransferChallengeResponse,
    RecordAttemptRequest, UserProfileResponse,
    ParsedError
)
from app.runner import run_code
from app.curriculum_data import get_topics, get_problems, get_problem_by_id
from app.visualizer_engine import get_visual_data_for_error
from app.tutor_engine import generate_hint, explain_cause, generate_transfer_challenge, get_groq_client
from app.database import record_attempt, get_user_profile

app = FastAPI(
    title="CodeSense API",
    description="AI-Powered Debugging Tutor That Teaches You to Think Like a Programmer",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------- CURRICULUM ENDPOINTS -----------------

@app.get("/api/topics")
def list_topics():
    return {"topics": get_topics()}

@app.get("/api/problems")
def list_problems(topic_id: str = None, language: str = None):
    problems = get_problems(topic_id, language)
    # Return summary list
    return {
        "problems": [
            {
                "id": p["id"],
                "topic_id": p["topic_id"],
                "topic_name": p["topic_name"],
                "title": p["title"],
                "difficulty": p["difficulty"],
                "language": p["language"],
                "scenario": p["scenario"],
                "bug_category": p["bug_category"]
            }
            for p in problems
        ]
    }

@app.get("/api/problems/{problem_id}")
def get_problem(problem_id: str):
    problem = get_problem_by_id(problem_id)
    if not problem:
        raise HTTPException(status_code=404, detail="Problem not found")
    return problem

# ----------------- CODE EXECUTION & VISUALIZER -----------------

@app.post("/api/execute", response_model=ExecuteResponse)
def execute_code_endpoint(req: ExecuteRequest):
    success, stdout, stderr, exit_code, elapsed_ms, parsed_err = run_code(
        code=req.code,
        language=req.language,
        user_input=req.user_input
    )
    
    # Check problem matching and test cases if problem_id is given
    problem = get_problem_by_id(req.question_id) if req.question_id else None
    all_tests_passed = False
    
    if problem and success:
        expected = problem.get("expected_output", "").strip()
        actual = stdout.strip()
        if expected in actual or actual == expected:
            all_tests_passed = True
        else:
            all_tests_passed = False
            parsed_err = ParsedError(
                error_type="OutputMismatch",
                line_number=None,
                message=f"Your code ran without syntax errors, but the output did not match the expected test result.\nYour output: '{actual if actual else '[Empty - Nothing was printed]'}'\nExpected goal: '{expected}'"
            )
    elif success and req.expected_output and req.expected_output.strip():
        # Custom student question with target expected output
        expected = req.expected_output.strip()
        actual = stdout.strip()
        if expected in actual or actual == expected:
            all_tests_passed = True
        else:
            all_tests_passed = False
            parsed_err = ParsedError(
                error_type="OutputMismatch",
                line_number=None,
                message=f"Your code ran without syntax errors, but the output did not match your target goal!\nYour output: '{actual if actual else '[Empty - Nothing was printed]'}'\nYour expected goal: '{expected}'"
            )
    elif success and not problem:
        all_tests_passed = True

    # Generate visual data if error occurred or if problem has visualizer
    curriculum_visual = problem.get("visual_data") if problem else None
    visual_data = None
    if parsed_err:
        visual_data = get_visual_data_for_error(
            error_type=parsed_err.error_type,
            code=req.code,
            language=req.language,
            curriculum_visual=curriculum_visual
        )
    elif problem and curriculum_visual:
        # Also provide visualizer on success to inspect clean state
        visual_data = get_visual_data_for_error(
            error_type="None",
            code=req.code,
            language=req.language,
            curriculum_visual=curriculum_visual
        )

    return ExecuteResponse(
        success=success,
        output=stdout,
        error=stderr,
        exit_code=exit_code,
        execution_time_ms=elapsed_ms,
        parsed_error=parsed_err,
        visual_data=visual_data,
        all_tests_passed=all_tests_passed
    )

# ----------------- HINT-FIRST TUTOR ENDPOINTS -----------------

@app.post("/api/hint", response_model=HintResponse)
def get_hint_endpoint(req: HintRequest):
    return generate_hint(
        code=req.code,
        language=req.language,
        hint_level=req.hint_level,
        error_message=req.error_message,
        question_id=req.question_id,
        user_api_key=req.user_api_key,
        custom_title=req.custom_title,
        custom_description=req.custom_description
    )

@app.post("/api/explain-cause", response_model=ExplainCauseResponse)
def explain_cause_endpoint(req: ExplainCauseRequest):
    return explain_cause(
        code=req.code,
        language=req.language,
        error_message=req.error_message,
        error_type=req.error_type,
        line_number=req.line_number,
        question_id=req.question_id,
        user_api_key=req.user_api_key,
        custom_title=req.custom_title,
        custom_description=req.custom_description
    )

@app.post("/api/transfer-challenge", response_model=TransferChallengeResponse)
def get_transfer_challenge_endpoint(req: TransferChallengeRequest):
    return generate_transfer_challenge(
        question_id=req.question_id,
        bug_category=req.bug_category,
        language=req.language,
        user_api_key=req.user_api_key
    )

# ----------------- LEARNER ANALYTICS & PROFILE -----------------

@app.post("/api/record-attempt")
def record_attempt_endpoint(req: RecordAttemptRequest):
    record_attempt(
        question_id=req.question_id,
        language=req.language,
        solved=req.solved,
        hints_used=req.hints_used,
        attempts_count=req.attempts_count,
        error_type=req.error_type,
        code=req.code
    )
    return {"status": "recorded"}

@app.get("/api/profile", response_model=UserProfileResponse)
def get_profile_endpoint():
    data = get_user_profile()
    return UserProfileResponse(**data)

@app.post("/api/settings/verify-groq")
def verify_groq(req: dict):
    key = req.get("api_key", "")
    client = get_groq_client(key)
    if not client:
        return {"valid": False, "message": "Failed to initialize Groq client"}
    try:
        res = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[{"role": "user", "content": "Respond with: OK"}],
            max_tokens=5
        )
        return {"valid": True, "message": f"Connected to Groq ({GROQ_MODEL}) successfully!"}
    except Exception as e:
        return {"valid": False, "message": str(e)}

@app.get("/api/system-status")
def system_status():
    return {
        "status": "online",
        "python": "Python 3.14 (Active)",
        "java_executable": JAVA_EXEC,
        "java_supported": True,
        "groq_configured": bool(os.getenv("GROQ_API_KEY")),
        "default_model": GROQ_MODEL
    }

# ----------------- STATIC FRONTEND MOUNT -----------------

app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

@app.get("/")
def serve_index():
    return FileResponse(os.path.join(STATIC_DIR, "index.html"))

