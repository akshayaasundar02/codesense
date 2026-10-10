"""
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
