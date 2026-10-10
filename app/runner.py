import os
import sys
import tempfile
import subprocess
import time
import re
from typing import Dict, Any, Optional, Tuple, List
from app.config import JAVA_EXEC, PYTHON_EXEC
from app.models import ParsedError

def parse_python_error(stderr: str, code: str) -> ParsedError:
    lines = stderr.strip().splitlines()
    error_type = "PythonRuntimeError"
    message = ""
    line_number = None
    snippet = None
    stack_trace = lines[-10:] if len(lines) > 10 else lines

    # Try to find exception line (typically the last line)
    for line in reversed(lines):
        line_clean = line.strip()
        if re.match(r"^[A-Za-z0-9_]+Error:|^[A-Za-z0-9_]+Exception:", line_clean):
            parts = line_clean.split(":", 1)
            error_type = parts[0].strip()
            message = parts[1].strip() if len(parts) > 1 else ""
            break
        elif "SyntaxError:" in line_clean or "IndentationError:" in line_clean:
            parts = line_clean.split(":", 1)
            error_type = parts[0].strip()
            message = parts[1].strip() if len(parts) > 1 else ""
            break

    # Look for line number
    for line in reversed(lines):
        match = re.search(r'File ".*?", line (\d+)', line)
        if match:
            line_number = int(match.group(1))
            break

    # Extract snippet from original code
    code_lines = code.splitlines()
    if line_number and 1 <= line_number <= len(code_lines):
        snippet = code_lines[line_number - 1].strip()

    if not message and lines:
        message = lines[-1]

    # Smart detection: Did the student write Java in Python mode?
    is_java_like = any(kw in code for kw in ["public class", "public static void main", "System.out", "int[]", "String[]", "boolean "])
    if is_java_like and (error_type == "SyntaxError" or "invalid syntax" in message):
        return ParsedError(
            error_type="LanguageMismatch (Java in Python mode)",
            line_number=line_number,
            file_name="solution.py",
            message="You wrote Java code, but the active language toggle is set to Python! Python stops on 'public class' or Java types. Simply switch to the '☕ Java' toggle at the top to run this!",
            snippet=snippet,
            stack_trace=stack_trace
        )

    return ParsedError(
        error_type=error_type,
        line_number=line_number,
        file_name="solution.py",
        message=message,
        snippet=snippet,
        stack_trace=stack_trace
    )

def parse_java_error(stderr: str, stdout: str, code: str) -> ParsedError:
    full_output = (stderr + "\n" + stdout).strip()
    lines = full_output.splitlines()
    error_type = "JavaError"
    message = ""
    line_number = None
    snippet = None
    stack_trace = lines[-10:] if len(lines) > 10 else lines

    # Check for compilation errors: e.g. "Main.java:7: error: incompatible types"
    comp_match = re.search(r'(?:[A-Za-z0-9_]+\.java):(\d+):\s*(?:error:)?\s*(.*)', full_output)
    if comp_match:
        line_number = int(comp_match.group(1))
        error_type = "JavaCompilationError"
        message = comp_match.group(2).strip()

    # Check for runtime exceptions: e.g. "Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException: Index 5 out of bounds"
    for line in lines:
        runtime_match = re.search(r'Exception in thread ".*?"\s+([a-zA-Z0-9_\.]+):\s*(.*)', line)
        if runtime_match:
            full_class = runtime_match.group(1)
            error_type = full_class.split(".")[-1]
            message = runtime_match.group(2)
            break
        elif "java.lang." in line:
            simple_match = re.search(r'java\.lang\.([A-Za-z0-9_]+):\s*(.*)', line)
            if simple_match:
                error_type = simple_match.group(1)
                message = simple_match.group(2)
                break

    # Find line number from stack trace: at Main.main(Main.java:9)
    for line in lines:
        line_match = re.search(r'\([A-Za-z0-9_]+\.java:(\d+)\)', line)
        if line_match:
            line_number = int(line_match.group(1))
            break

    # Extract snippet from original code
    code_lines = code.splitlines()
    if line_number and 1 <= line_number <= len(code_lines):
        snippet = code_lines[line_number - 1].strip()

    if not message and lines:
        message = lines[-1]

    # Smart detection: Did the student write Python in Java mode?
    is_python_like = ("def " in code or ("print(" in code and "System.out" not in code) or "elif " in code or "for i in range" in code)
    if is_python_like:
        return ParsedError(
            error_type="LanguageMismatch (Python in Java mode)",
            line_number=line_number,
            file_name="Solution.java",
            message="You wrote Python code, but the active language toggle is set to Java! Java compiler cannot parse Python indentation or 'def'. Simply switch to the '🐍 Python' toggle at the top to run this!",
            snippet=snippet,
            stack_trace=stack_trace
        )

    return ParsedError(
        error_type=error_type,
        line_number=line_number,
        file_name="Solution.java",
        message=message,
        snippet=snippet,
        stack_trace=stack_trace
    )

def execute_python(code: str, user_input: Optional[str] = None, timeout_sec: int = 4) -> Tuple[bool, str, Optional[str], int, float, Optional[ParsedError]]:
    start_time = time.time()
    
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = os.path.join(tmpdir, "solution.py")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(code)

        try:
            process = subprocess.Popen(
                [sys.executable, file_path],
                stdin=subprocess.PIPE if user_input else None,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                cwd=tmpdir
            )
            stdout, stderr = process.communicate(input=user_input, timeout=timeout_sec)
            elapsed_ms = round((time.time() - start_time) * 1000, 2)
            
            if process.returncode == 0:
                return True, stdout, None, 0, elapsed_ms, None
            else:
                parsed_err = parse_python_error(stderr, code)
                return False, stdout, stderr, process.returncode, elapsed_ms, parsed_err

        except subprocess.TimeoutExpired:
            process.kill()
            elapsed_ms = round(timeout_sec * 1000, 2)
            err_msg = f"TimeLimitExceeded: Execution timed out after {timeout_sec}s. Likely an infinite loop or unbounded recursion."
            parsed_err = ParsedError(
                error_type="TimeLimitExceeded",
                message="Program did not terminate. Check your loop exit condition or recursive base case.",
                stack_trace=[err_msg]
            )
            return False, "", err_msg, -1, elapsed_ms, parsed_err
            
        except Exception as e:
            elapsed_ms = round((time.time() - start_time) * 1000, 2)
            return False, "", str(e), -1, elapsed_ms, ParsedError(error_type="SystemError", message=str(e))

def execute_java(code: str, user_input: Optional[str] = None, timeout_sec: int = 5) -> Tuple[bool, str, Optional[str], int, float, Optional[ParsedError]]:
    start_time = time.time()
    
    # Detect public class name or default to Main
    class_match = re.search(r'public\s+class\s+([A-Za-z0-9_]+)', code)
    if class_match:
        class_name = class_match.group(1)
    else:
        # Check for regular class
        class_match = re.search(r'class\s+([A-Za-z0-9_]+)', code)
        class_name = class_match.group(1) if class_match else "Main"

    with tempfile.TemporaryDirectory() as tmpdir:
        java_file_path = os.path.join(tmpdir, f"{class_name}.java")
        with open(java_file_path, "w", encoding="utf-8") as f:
            f.write(code)

        try:
            # Java 11+ directly runs single-file source code: java ClassName.java
            process = subprocess.Popen(
                [JAVA_EXEC, f"{class_name}.java"],
                stdin=subprocess.PIPE if user_input else None,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                cwd=tmpdir
            )
            stdout, stderr = process.communicate(input=user_input, timeout=timeout_sec)
            elapsed_ms = round((time.time() - start_time) * 1000, 2)
            
            if process.returncode == 0:
                return True, stdout, None, 0, elapsed_ms, None
            else:
                parsed_err = parse_java_error(stderr, stdout, code)
                return False, stdout, stderr, process.returncode, elapsed_ms, parsed_err

        except subprocess.TimeoutExpired:
            process.kill()
            elapsed_ms = round(timeout_sec * 1000, 2)
            err_msg = f"TimeLimitExceeded: Java program timed out after {timeout_sec}s. Likely an infinite loop or unbounded recursion."
            parsed_err = ParsedError(
                error_type="TimeLimitExceeded",
                message="Java program timed out. Verify loop termination or recursion base cases.",
                stack_trace=[err_msg]
            )
            return False, "", err_msg, -1, elapsed_ms, parsed_err
            
        except Exception as e:
            elapsed_ms = round((time.time() - start_time) * 1000, 2)
            return False, "", str(e), -1, elapsed_ms, ParsedError(error_type="SystemError", message=str(e))

def run_code(code: str, language: str = "python", user_input: Optional[str] = None):
    # Auto-detect language if user submitted Java in Python mode or vice-versa
    is_java = any(kw in code for kw in ["public class", "public static void main", "System.out", "int[]", "String[]", "boolean "])
    is_python = ("def " in code or "elif " in code or ("print(" in code and "System.out" not in code))

    if language.lower() == "python" and is_java:
        return execute_java(code, user_input)
    elif language.lower() == "java" and is_python and not is_java:
        return execute_python(code, user_input)

    if language.lower() == "java":
        return execute_java(code, user_input)
    return execute_python(code, user_input)
