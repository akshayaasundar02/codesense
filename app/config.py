import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR / "static"
DB_PATH = BASE_DIR / "codesense.db"

# Groq API configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

# Java executable resolution
def get_java_executable() -> str:
    # 1. Check custom environment variable
    custom_java = os.getenv("JAVA_PATH")
    if custom_java and os.path.exists(custom_java):
        return custom_java
    
    # 2. Check Tableau bundled OpenJDK 17 which was verified on this system
    tableau_java = r"C:\Program Files\Tableau\Tableau 2026.1\bin\jre\bin\java.exe"
    if os.path.exists(tableau_java):
        return tableau_java
        
    # 3. Check common Java paths
    common_paths = [
        r"C:\Program Files\Java\jdk-17\bin\java.exe",
        r"C:\Program Files\Java\jdk-21\bin\java.exe",
        r"C:\Program Files\Eclipse Adoptium\jdk-17\bin\java.exe",
        r"C:\Program Files\Zulu\zulu-17\bin\java.exe"
    ]
    for p in common_paths:
        if os.path.exists(p):
            return p
            
    # 4. Fallback to 'java' in system PATH
    return "java"

JAVA_EXEC = get_java_executable()
PYTHON_EXEC = sys.executable or "python"
