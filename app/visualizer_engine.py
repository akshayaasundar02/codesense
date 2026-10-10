import re
import ast
from typing import Dict, Any, Optional
from app.models import VisualData

def extract_array_data_from_code(code: str, language: str) -> Optional[Dict[str, Any]]:
    """Heuristic / AST extractor to find list/array and out-of-bounds access"""
    try:
        if language == "python":
            # Search for list literal: items = [...]
            list_match = re.search(r'([A-Za-z0-9_]+)\s*=\s*(\[[^\]]+\])', code)
            access_match = re.search(r'([A-Za-z0-9_]+)\[([^\]]+)\]', code)
            
            if list_match:
                list_var = list_match.group(1)
                raw_list = list_match.group(2)
                try:
                    elements = ast.literal_eval(raw_list)
                    if isinstance(elements, list):
                        length = len(elements)
                        attempted_index = length  # default guess
                        
                        if access_match:
                            acc_idx_str = access_match.group(2).strip()
                            if acc_idx_str.isdigit():
                                attempted_index = int(acc_idx_str)
                            elif acc_idx_str == "len(" + list_var + ")" or "len" in acc_idx_str:
                                attempted_index = length
                                
                        return {
                            "visual_type": "array_bounds",
                            "array_name": list_var,
                            "elements": elements[:10],
                            "length": length,
                            "valid_min": 0,
                            "valid_max": length - 1,
                            "attempted_index": attempted_index,
                            "is_out_of_bounds": attempted_index >= length or attempted_index < -length,
                            "note": f"0-based indexing means indices run from 0 to {length - 1}."
                        }
                except Exception:
                    pass
        elif language == "java":
            # Search for int[] arr = { ... } or String[] arr = { ... }
            arr_match = re.search(r'(?:int|String|double|float)\[\]\s+([A-Za-z0-9_]+)\s*=\s*\{([^}]+)\}', code)
            acc_match = re.search(r'([A-Za-z0-9_]+)\[([^\]]+)\]', code)
            if arr_match:
                arr_name = arr_match.group(1)
                items_str = arr_match.group(2).split(",")
                items = [x.strip().replace('"', '') for x in items_str if x.strip()]
                length = len(items)
                attempted_index = length
                if acc_match:
                    acc_idx_str = acc_match.group(2).strip()
                    if acc_idx_str.isdigit():
                        attempted_index = int(acc_idx_str)
                    elif ".length" in acc_idx_str:
                        attempted_index = length
                return {
                    "visual_type": "array_bounds",
                    "array_name": arr_name,
                    "elements": items[:10],
                    "length": length,
                    "valid_min": 0,
                    "valid_max": length - 1,
                    "attempted_index": attempted_index,
                    "is_out_of_bounds": attempted_index >= length or attempted_index < 0,
                    "note": f"Java arrays are fixed-length with valid indices [0 .. {length - 1}]."
                }
    except Exception:
        pass
    return None

def build_loop_trace(items: list, condition_op: str = "<=") -> Dict[str, Any]:
    """Generates step-by-step loop trace states"""
    steps = []
    length = len(items)
    # Simulate iterations up to length + 1 (the error point)
    limit = length if condition_op == "<=" else length - 1
    total = 0
    for i in range(length + 1):
        cond_eval = (i <= length) if condition_op == "<=" else (i < length)
        is_crash = i >= length and cond_eval
        
        val = items[i] if i < length else "CRASH 💥"
        if isinstance(val, (int, float)):
            total += val
            
        steps.append({
            "step": i + 1,
            "index_i": i,
            "condition": f"i {condition_op} {length} -> {str(cond_eval).upper()}",
            "accessed_value": str(val),
            "state_snapshot": {"i": i, "running_total": total if not is_crash else "ABORTED"},
            "is_error_step": is_crash,
            "explanation": (
                f"Loop executed because {i} {condition_op} {length} was TRUE. Trying to read index {i} failed!"
                if is_crash else
                f"Iteration {i}: condition holds. Successfully accessed index {i}."
            )
        })
        if is_crash:
            break
            
    return {
        "visual_type": "loop_trace",
        "loop_variable": "i",
        "boundary_limit": length,
        "condition_used": f"i {condition_op} {length}",
        "correct_condition": f"i < {length}",
        "steps": steps
    }

def get_visual_data_for_error(
    error_type: str,
    code: str,
    language: str,
    curriculum_visual: Optional[Dict[str, Any]] = None
) -> Optional[VisualData]:
    """Return structured visual state for the Visual Bug Explorer"""
    if curriculum_visual:
        v_type = curriculum_visual.get("visual_type", "array_bounds")
        title = curriculum_visual.get("title", "Visual Bug Explorer")
        return VisualData(visual_type=v_type, title=title, data=curriculum_visual)

    err_lower = error_type.lower()
    
    # 1. Array Index / Out of bounds
    if "index" in err_lower or "outofbounds" in err_lower:
        arr_data = extract_array_data_from_code(code, language)
        if arr_data:
            return VisualData(
                visual_type="array_bounds",
                title="Array Memory & Index Explorer",
                data=arr_data
            )
        # Default sample visualizer if couldn't parse
        return VisualData(
            visual_type="array_bounds",
            title="Array Memory & Index Explorer",
            data={
                "visual_type": "array_bounds",
                "array_name": "dataList",
                "elements": [10, 20, 30, 40, 50],
                "length": 5,
                "valid_min": 0,
                "valid_max": 4,
                "attempted_index": 5,
                "is_out_of_bounds": True,
                "note": "Attempted index 5 does not exist in a 5-element collection."
            }
        )

    # 2. Loop / Off-by-one trace
    if "loop" in err_lower or "offbyone" in err_lower or "<=" in code:
        trace = build_loop_trace([15, 25, 35, 45, 55], condition_op="<=")
        return VisualData(
            visual_type="loop_trace",
            title="Loop Iteration & Boundary Stepper",
            data=trace
        )

    # 3. Null / None pointer
    if "null" in err_lower or "none" in err_lower or "attributeerror" in err_lower:
        return VisualData(
            visual_type="tree",
            title="Object Reference & Tree Explorer",
            data={
                "root": {
                    "val": "Head / Root (id=0x1A)",
                    "left": {"val": "Left Child (id=0x2B)", "left": None, "right": None},
                    "right": None,
                    "target_null_access": "right.value"
                },
                "crash_node": "right",
                "reason": "Variable points to null/None. Accessing fields on a non-existent object throws a runtime fault."
            }
        )

    # 4. Stack underflow / recursion
    if "stack" in err_lower or "recursion" in err_lower:
        return VisualData(
            visual_type="stack",
            title="Call Stack & Frame Tracker",
            data={
                "frames": [
                    {"depth": 1, "func": "traverse(node=10)", "status": "active"},
                    {"depth": 2, "func": "traverse(node=5)", "status": "active"},
                    {"depth": 3, "func": "traverse(node=2)", "status": "active"},
                    {"depth": 4, "func": "traverse(node=0)", "status": "missing base case!"},
                    {"depth": "...", "func": "traverse(node=-1000)", "status": "OVERFLOW 💥"}
                ],
                "reason": "Missing termination base condition caused unbounded stack growth."
            }
        )

    # 5. Default variable state table
    return VisualData(
        visual_type="variable_state",
        title="Runtime Variable Inspector",
        data={
            "variables": [
                {"name": "status", "type": "str", "value": "'ERROR'"},
                {"name": "line", "type": "int", "value": "Refer to traceback"}
            ],
            "reason": "Inspect variable values at point of crash."
        }
    )
