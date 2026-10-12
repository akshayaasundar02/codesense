from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

class ParsedError(BaseModel):
    error_type: str = "UnknownError"
    line_number: Optional[int] = None
    file_name: Optional[str] = None
    message: str = ""
    snippet: Optional[str] = None
    stack_trace: List[str] = []

class ExecuteRequest(BaseModel):
    code: str
    language: str = "python"  # "python" or "java"
    question_id: Optional[str] = None
    user_input: Optional[str] = None
    custom_title: Optional[str] = None
    custom_description: Optional[str] = None
    expected_output: Optional[str] = None

class VisualData(BaseModel):
    visual_type: str  # "array_bounds", "loop_trace", "stack", "tree", "variable_state"
    title: str = "State Visualizer"
    data: Dict[str, Any] = {}

class ExecuteResponse(BaseModel):
    success: bool
    output: str
    error: Optional[str] = None
    exit_code: int = 0
    execution_time_ms: float = 0.0
    parsed_error: Optional[ParsedError] = None
    visual_data: Optional[VisualData] = None
    all_tests_passed: Optional[bool] = None
    test_results: Optional[List[Dict[str, Any]]] = None
    expected_output: Optional[str] = None

class HintRequest(BaseModel):
    code: str
    language: str = "python"
    question_id: Optional[str] = None
    error_message: Optional[str] = None
    hint_level: int = 1  # 1 (Misconception), 2 (Rule & Concept), 3 (What to Change)
    user_api_key: Optional[str] = None
    custom_title: Optional[str] = None
    custom_description: Optional[str] = None

class HintResponse(BaseModel):
    hint_level: int
    level_name: str
    title: str
    hint_text: str
    suspicious_line: Optional[int] = None
    concept: Optional[str] = None
    independence_cost: int = 10

class ExplainCauseRequest(BaseModel):
    code: str
    language: str = "python"
    question_id: Optional[str] = None
    error_message: str = ""
    error_type: str = ""
    line_number: Optional[int] = None
    user_api_key: Optional[str] = None
    custom_title: Optional[str] = None
    custom_description: Optional[str] = None

class ExplainCauseResponse(BaseModel):
    error_type: str
    line_number: Optional[int] = None
    programmer_intent: str
    actual_execution: str
    divergence_gap: str
    prevention_tip: str
    mental_model_analogy: str

class TransferChallengeRequest(BaseModel):
    question_id: Optional[str] = None
    bug_category: str = "OffByOne"
    language: str = "python"
    user_api_key: Optional[str] = None

class TransferChallengeResponse(BaseModel):
    id: str
    title: str
    scenario: str
    topic: str
    difficulty: str
    language: str
    description: str
    buggy_code: str
    expected_output: str
    hint: str

class RecordAttemptRequest(BaseModel):
    question_id: str
    language: str
    solved: bool
    hints_used: int
    attempts_count: int
    error_type: Optional[str] = None
    code: Optional[str] = None
    user_id: Optional[str] = "student_1"

class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str

class LoginRequest(BaseModel):
    identifier: str
    password: str

class AuthResponse(BaseModel):
    success: bool
    message: str
    user: Optional[Dict[str, Any]] = None

class UserProfileResponse(BaseModel):
    total_solved: int
    total_attempts: int
    overall_independence_score: float
    streak_days: int
    accuracy_rate: Optional[float] = 100.0
    independence_tier: Optional[str] = "Autonomous Coder 🏆"
    python_solved: Optional[int] = 0
    java_solved: Optional[int] = 0
    no_hints_solved: Optional[int] = 0
    total_hints_used: Optional[int] = 0
    recommended_focus: Optional[str] = ""
    error_radar: Dict[str, int]
    topic_progress: Dict[str, Dict[str, Any]]
    recent_attempts: List[Dict[str, Any]]
    username: Optional[str] = None
