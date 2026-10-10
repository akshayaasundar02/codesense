# Curriculum Builder Script
import os
import json

def generate_curriculum_file():
    from generate_data import ALL_QUESTIONS, TOPICS_DEF

    problems = []

    for item in ALL_QUESTIONS:
        t_id = item["topic_id"]
        t_name = item["topic_name"]
        lvl = item["level"]
        title = item["title"]
        company = item["company"]
        desc = item["description"]
        expected = item["expected_output"]
        
        diff = "Beginner" if lvl <= 3 else "Intermediate" if lvl <= 7 else "Advanced"

        # Python Problem Starter - ONLY description and input setup! NO solution!
        py_starter = f"""# Problem: {title} ({company})
# Task: {desc}
# Expected Goal: {expected}

{item['py_input']}

# TODO: Write your code below to solve this problem:

"""
        problems.append({
            "id": f"py-{t_id[:4]}-{lvl:02d}",
            "topic_id": t_id,
            "topic_name": t_name,
            "level": lvl,
            "title": f"Level {lvl}: {title}",
            "difficulty": diff,
            "language": "python",
            "scenario": f"Practice Challenge: {company}",
            "description": desc,
            "starter_code": py_starter,
            "buggy_code": item["py_bug"],
            "correct_code": item["py_solution"],
            "expected_output": expected,
            "bug_category": item.get("bug_category", "Logic & Bounds"),
            "precomputed_hints": {
                "hint_1": item["hints"][0],
                "hint_2": item["hints"][1],
                "hint_3": item["hints"][2]
            },
            "cause_explanation": {
                "programmer_intent": f"Solve challenge '{title}'.",
                "actual_execution": item["cause"][0],
                "divergence_gap": item["cause"][1],
                "prevention_tip": item["cause"][2]
            },
            "visual_type": item.get("visual_type", "variable_state"),
            "visual_data": item.get("visual_data", {
                "variables": [{"name": "status", "type": "Safe", "value": "Valid"}],
                "reason": "Variable state inspected."
            })
        })

        # Java Problem Starter - ONLY description, class/main shell, and input setup! NO solution!
        java_starter = f"""// Problem: {title} ({company})
// Task: {desc}
// Expected Goal: {expected}

import java.util.*;

public class Main {{
    public static void main(String[] args) {{
{item['java_input']}

        // TODO: Write your code below to solve this problem:
        
    }}
}}"""
        problems.append({
            "id": f"java-{t_id[:4]}-{lvl:02d}",
            "topic_id": t_id,
            "topic_name": t_name,
            "level": lvl,
            "title": f"Level {lvl}: {title}",
            "difficulty": diff,
            "language": "java",
            "scenario": f"Practice Challenge: {company}",
            "description": desc,
            "starter_code": java_starter,
            "buggy_code": item["java_bug"],
            "correct_code": item["java_solution"],
            "expected_output": expected,
            "bug_category": item.get("bug_category", "Logic & Bounds"),
            "precomputed_hints": {
                "hint_1": item["hints"][0],
                "hint_2": item["hints"][1],
                "hint_3": item["hints"][2]
            },
            "cause_explanation": {
                "programmer_intent": f"Solve challenge '{title}' in Java.",
                "actual_execution": item["cause"][0],
                "divergence_gap": item["cause"][1],
                "prevention_tip": item["cause"][2]
            },
            "visual_type": item.get("visual_type", "variable_state"),
            "visual_data": item.get("visual_data", {
                "variables": [{"name": "status", "type": "Safe", "value": "Valid"}],
                "reason": "Variable state inspected."
            })
        })

    # Save to JSON
    json_path = os.path.join("app", "curriculum_data.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({"topics": TOPICS_DEF, "problems": problems}, f, indent=2)

    # Save Python loader app/curriculum_data.py
    py_path = os.path.join("app", "curriculum_data.py")
    with open(py_path, "w", encoding="utf-8") as f:
        f.write('''"""
CodeSense Comprehensive Practice Programming Problem Bank
Loads 10 Topics x 10 Progressive Questions = 100 Real Practice Questions per language (200 total).
Clean starters with NO pre-given solution so junior students write their own logic.
"""

import json
import os
from typing import List, Dict, Any, Optional

_DATA_PATH = os.path.join(os.path.dirname(__file__), "curriculum_data.json")

with open(_DATA_PATH, "r", encoding="utf-8") as f:
    _DATA = json.load(f)

TOPICS: List[Dict[str, Any]] = _DATA["topics"]
PROBLEMS: List[Dict[str, Any]] = _DATA["problems"]

def get_topics() -> List[Dict[str, Any]]:
    return TOPICS

def get_problems(topic_id: Optional[str] = None, language: Optional[str] = None) -> List[Dict[str, Any]]:
    results = PROBLEMS
    if topic_id:
        results = [p for p in results if p["topic_id"] == topic_id]
    if language:
        results = [p for p in results if p["language"].lower() == language.lower()]
    results.sort(key=lambda x: x.get("level", 1))
    return results

def get_problem_by_id(problem_id: str) -> Optional[Dict[str, Any]]:
    for p in PROBLEMS:
        if p["id"] == problem_id:
            return p
    return None
''')

    print(f"Successfully generated {len(problems)} problems in {json_path} and {py_path}!")

if __name__ == "__main__":
    generate_curriculum_file()
