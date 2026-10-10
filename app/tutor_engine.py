import os
import json
from typing import Dict, Any, Optional
from app.config import GROQ_API_KEY, GROQ_MODEL
from app.curriculum_data import get_problem_by_id
from app.models import HintResponse, ExplainCauseResponse, TransferChallengeResponse

try:
    from groq import Groq
    groq_installed = True
except ImportError:
    groq_installed = False

def get_groq_client(user_api_key: Optional[str] = None):
    key = user_api_key or GROQ_API_KEY or os.getenv("GROQ_API_KEY")
    if groq_installed and key:
        try:
            return Groq(api_key=key)
        except Exception:
            return None
    return None

def generate_hint(
    code: str,
    language: str,
    hint_level: int,
    error_message: Optional[str] = None,
    question_id: Optional[str] = None,
    user_api_key: Optional[str] = None,
    custom_title: Optional[str] = None,
    custom_description: Optional[str] = None
) -> HintResponse:
    problem = get_problem_by_id(question_id) if question_id else None
    
    level_names = {
        1: "Clue 1: What Went Wrong in the Logic 🧩",
        2: "Clue 2: The Core Rule & Principle 💡",
        3: "Clue 3: Exact Logical Fix & What to Change 🛠️"
    }
    level_penalties = {1: 5, 2: 15, 3: 30}
    
    # Try Groq AI if key is provided and custom code is used
    client = get_groq_client(user_api_key)
    q_context = ""
    if custom_title or custom_description:
        q_context = f"\nCustom Student Question: {custom_title or 'Practice Problem'}\nDescription/Goal: {custom_description or 'Solve the logic task'}\n"
    elif problem:
        q_context = f"\nCurriculum Problem: {problem.get('title')}\nDescription: {problem.get('description')}\n"

    if client and (not problem or len(code.strip()) > 0 or custom_title):
        try:
            system_prompt = f"""You are CodeSense Friendly Programming Tutor.
Your goal is to guide beginner students in {language} to UNDERSTAND AND FIX THEIR LOGIC independently.
{q_context}
CRITICAL PEDAGOGICAL RULES:
1. NEVER tell them "Look at line X" or give trivial line-number clues. Junior learners need to understand the THOUGHT PROCESS, not just a line pointer.
2. DO NOT use intimidating academic jargon. Speak like an encouraging coding mentor.
3. Keep clues progressive and actionable:

Target Clue Level: {hint_level} of 3.
- Clue 1 (What Went Wrong in the Logic): Explain the logical misconception or false assumption in the code. Describe what the coder assumed would happen versus what the computer actually did.
- Clue 2 (The Core Rule & Principle): Explain the fundamental programming rule or invariant in plain English (e.g. how zero-indexing works, why string immutability matters, how loop boundary ranges stop before the limit).
- Clue 3 (Exact Logical Fix & What to Change): Clearly describe the exact change needed in the logic (e.g., what condition to change, what range boundary to adjust, or what variable needs updating) in {language} without just dumping full solution code.

Format strictly as JSON:
{{
  "title": "Clear educational title (e.g. Off-by-one in mirror index calculation)",
  "hint_text": "Detailed pedagogical explanation following the Clue level instructions",
  "suspicious_line": null,
  "concept": "Core CS Concept Name"
}}
"""
            user_msg = f"Language: {language}\nCode:\n```{language}\n{code}\n```\nError output:\n{error_message or 'Runtime bug'}"
            response = client.chat.completions.create(
                model=GROQ_MODEL,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_msg}
                ],
                response_format={"type": "json_object"},
                temperature=0.3,
                max_tokens=500
            )
            data = json.loads(response.choices[0].message.content)
            return HintResponse(
                hint_level=hint_level,
                level_name=level_names.get(hint_level, f"Clue {hint_level}"),
                title=data.get("title", f"Clue {hint_level}"),
                hint_text=data.get("hint_text", ""),
                suspicious_line=None,
                concept=data.get("concept", "Logic Flaw"),
                independence_cost=level_penalties.get(hint_level, 10)
            )
        except Exception:
            pass

    # Fallback to curriculum precomputed hints
    if problem and "precomputed_hints" in problem:
        hints = problem["precomputed_hints"]
        key = f"hint_{hint_level}"
        hint_text = hints.get(key, hints.get("hint_1", "Analyze the logic assumptions and boundary conditions."))
        return HintResponse(
            hint_level=hint_level,
            level_name=level_names.get(hint_level, f"Clue {hint_level}"),
            title=f"{problem['title']} — Clue {hint_level}",
            hint_text=hint_text,
            suspicious_line=None,
            concept=problem.get("bug_category", "Code Logic"),
            independence_cost=level_penalties.get(hint_level, 10)
        )

    # Simple fallback clues for any custom student code
    prob_label = custom_title or "Your Custom Question"
    simple_clues = {
        1: (f"{prob_label} — Logic Misconception 🧩", f"In your solution for '{prob_label}', the code is attempting an operation where the assumption doesn't match the runtime state—such as checking a condition that always evaluates false, reading past valid boundaries, or exiting before testing all values.", 5),
        2: (f"{prob_label} — Core Principle 💡", f"In {language}, collections are zero-indexed (slots 0 to length - 1), variables must hold the expected types before operators run, and loops stop strictly when their test condition becomes false.", 15),
        3: (f"{prob_label} — What to Change in Logic 🛠️", f"To fix the logic for '{prob_label}': check the loop initialization and termination conditions, verify that update variables accumulate results properly across iterations, and ensure edge cases (like 0, 1, or empty input) are handled.", 30)
    }
    title, text, cost = simple_clues.get(hint_level, simple_clues[1])
    return HintResponse(
        hint_level=hint_level,
        level_name=level_names.get(hint_level, f"Clue {hint_level}"),
        title=title,
        hint_text=text,
        suspicious_line=None,
        concept="Algorithm Logic",
        independence_cost=cost
    )

def explain_cause(
    code: str,
    language: str,
    error_message: str,
    error_type: str,
    line_number: Optional[int] = None,
    question_id: Optional[str] = None,
    user_api_key: Optional[str] = None,
    custom_title: Optional[str] = None,
    custom_description: Optional[str] = None
) -> ExplainCauseResponse:
    problem = get_problem_by_id(question_id) if question_id else None
    
    # Try Groq AI
    client = get_groq_client(user_api_key)
    q_context = ""
    if custom_title or custom_description:
        q_context = f"\nCustom Student Question: {custom_title or 'Practice Problem'}\nDescription: {custom_description or 'Solve the logic task'}\n"
    elif problem:
        q_context = f"\nCurriculum Problem: {problem.get('title')}\nDescription: {problem.get('description')}\n"

    if client:
        try:
            system_prompt = f"""You are CodeSense Beginner Tutor.
Explain the error in {language} in SUPER SIMPLE, FRIENDLY, NON-TECHNICAL terms.
{q_context}
Avoid scary technical jargon! Use everyday real-life metaphors (like mailboxes, grocery carts, or elevator floors).

Provide a JSON object with:
"programmer_intent": "What you were trying to do (in simple everyday words)",
"actual_execution": "What the computer actually tried to do (in simple everyday words)",
"divergence_gap": "Why it got confused or broke (plain, simple explanation)",
"prevention_tip": "Golden rule to remember for life (short and easy to memorize)",
"mental_model_analogy": "A funny or memorable real-world analogy (e.g. trying to push elevator button 5 in a 4-floor building)"
"""
            user_msg = f"Language: {language}\nError: {error_type}: {error_message}\nLine: {line_number}\nCode:\n```{language}\n{code}\n```"
            response = client.chat.completions.create(
                model=GROQ_MODEL,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_msg}
                ],
                response_format={"type": "json_object"},
                temperature=0.2,
                max_tokens=600
            )
            data = json.loads(response.choices[0].message.content)
            return ExplainCauseResponse(
                error_type=error_type,
                line_number=line_number,
                programmer_intent=data.get("programmer_intent", f"Solve {custom_title or 'the problem'} smoothly."),
                actual_execution=data.get("actual_execution", error_message),
                divergence_gap=data.get("divergence_gap", "The code encountered an unexpected runtime state."),
                prevention_tip=data.get("prevention_tip", "Always double check your list sizes and conditions."),
                mental_model_analogy=data.get("mental_model_analogy", "Looking for the 5th floor in a 4-floor building.")
            )
        except Exception:
            pass

    # Friendly rule-based breakdowns
    if "index" in error_type.lower() or "outofbounds" in error_type.lower():
        return ExplainCauseResponse(
            error_type=error_type,
            line_number=line_number,
            programmer_intent="You wanted to grab an item from the list.",
            actual_execution="The computer looked for a slot that doesn't exist.",
            divergence_gap="Remember: computers start counting from 0, not 1! So a list of 4 items has slots 0, 1, 2, and 3. Asking for slot 4 falls right off the edge.",
            prevention_tip="Golden Rule: If a list has N items, the last valid position is always N - 1.",
            mental_model_analogy="🏨 Imagine a 4-floor hotel numbered Floors 0, 1, 2, and 3. If you press elevator button #4, you're trying to step into thin air!"
        )

    if "type" in error_type.lower() or "numberformat" in error_type.lower():
        return ExplainCauseResponse(
            error_type=error_type,
            line_number=line_number,
            programmer_intent="You wanted to calculate or convert numbers.",
            actual_execution="The computer encountered text/characters where it expected a pure number.",
            divergence_gap="Computers treat text ('49.99') differently from numbers (49.99). You can't do math on text without converting it first!",
            prevention_tip="Golden Rule: Always convert strings to numbers (`float(x)` or `Double.parseDouble(x)`) before doing math.",
            mental_model_analogy="🔌 Trying to plug a water hose into an electrical wall outlet—two completely different types of things!"
        )

    if "null" in error_type.lower() or "none" in error_type.lower() or "attribute" in error_type.lower():
        return ExplainCauseResponse(
            error_type=error_type,
            line_number=line_number,
            programmer_intent="You wanted to read a value from an object or node.",
            actual_execution="The variable was completely empty (`null` or `None`).",
            divergence_gap="The code tried to open a box that doesn't exist yet! You can't read attributes from an empty container.",
            prevention_tip="Golden Rule: Always check `if node != null` before trying to read `node.value`.",
            mental_model_analogy="📬 Opening an empty mailbox and trying to read the non-existent letter inside!"
        )

    if "recursion" in error_type.lower() or "stackoverflow" in error_type.lower():
        return ExplainCauseResponse(
            error_type=error_type,
            line_number=line_number,
            programmer_intent="You wanted the function to repeat until the problem was solved.",
            actual_execution="The function kept calling itself without stopping, filling up all memory.",
            divergence_gap="The function was missing a 'stopping condition' (base case). It ran indefinitely like a loop with no exit.",
            prevention_tip="Golden Rule: Always write the `if n <= 0: return` stopping rule first before calling the function again.",
            mental_model_analogy="🪞 Two mirrors facing each other, creating an endless tunnel of reflections until you run out of light!"
        )

    if "languagemismatch" in error_type.lower():
        return ExplainCauseResponse(
            error_type=error_type,
            line_number=line_number,
            programmer_intent="You wrote a valid solution in Java.",
            actual_execution="The Python runner was active and tried to interpret Java keywords.",
            divergence_gap="Python doesn't know what 'public class' or 'int[]' means! Python uses 'class' and colons ':'. Your Java code is great, but it needs the Java runner.",
            prevention_tip="Golden Rule: Click the '☕ Java' toggle in the top header bar to switch to Java mode!",
            mental_model_analogy="🎮 Trying to put a Nintendo Switch cartridge into a PlayStation—both are great gaming machines, but they require their own games!"
        )

    if "syntax" in error_type.lower():
        return ExplainCauseResponse(
            error_type=error_type,
            line_number=line_number,
            programmer_intent="You wanted the computer to parse your code instructions.",
            actual_execution="The computer stopped because it encountered a word or symbol that doesn't follow the language's grammar rules.",
            divergence_gap="Programming languages have strict grammar rules. For example, Python blocks require a colon ':' and indentation, whereas Java uses curly braces '{ }'.",
            prevention_tip="Golden Rule: Check the highlighted line for missing colons ':', unmatched brackets, or words from another language.",
            mental_model_analogy="🗣️ Speaking Italian to someone who only speaks Japanese—they halt immediately at the first unrecognized word!"
        )

    return ExplainCauseResponse(
        error_type=error_type,
        line_number=line_number,
        programmer_intent="You wanted the program to run step-by-step.",
        actual_execution=f"The computer stopped because of {error_type}: {error_message}",
        divergence_gap="A rule was violated—such as looking for an item that isn't there, or performing an operation on the wrong data type.",
        prevention_tip="Golden Rule: Check the highlighted line and trace what value is stored in each variable right before the crash.",
        mental_model_analogy="🚗 Reaching the end of a paved road where the bridge hasn't been built yet!"
    )

def generate_transfer_challenge(
    question_id: Optional[str] = None,
    bug_category: str = "OffByOne",
    language: str = "python",
    user_api_key: Optional[str] = None
) -> TransferChallengeResponse:
    problem = get_problem_by_id(question_id) if question_id else None
    
    if language == "java":
        return TransferChallengeResponse(
            id="java-trans-01",
            title="Prove Mastery: Next Item Peeker",
            scenario="Food Delivery App Order Scanner",
            language="java",
            topic="Arrays & Boundary Safety",
            difficulty="Practice Level",
            description="Fix the loop so it compares current item with the next without falling off the edge of the array.",
            buggy_code="public class Main {\n    public static void main(String[] args) {\n        int[] orders = {10, 20, 30};\n        for(int i = 0; i < orders.length; i++) {\n            // Fix the loop bound so orders[i+1] never crashes!\n            if (orders[i] < orders[i+1]) System.out.println(\"Rising order\");\n        }\n    }\n}",
            expected_output="Rising order\nRising order",
            hint="Remember: Stop one step earlier using i < orders.length - 1!"
        )

    return TransferChallengeResponse(
        id="py-trans-01",
        title="Prove Mastery: Next Item Peeker",
        scenario="Food Delivery App Order Scanner",
        language="python",
        topic="Arrays & Boundary Safety",
        difficulty="Practice Level",
        description="Fix the loop so it compares current item with the next without falling off the edge of the list.",
        buggy_code="orders = [10, 20, 30]\n# Fix range() so orders[i+1] never crashes!\nfor i in range(len(orders)):\n    if orders[i] < orders[i + 1]:\n        print('Rising order')",
        expected_output="Rising order\nRising order",
        hint="Remember: Stop one step earlier using range(len(orders) - 1)!"
    )
