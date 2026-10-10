"""
CodeSense Server Launcher
Usage: python run.py
"""

import uvicorn
import sys
import os

# Ensure the root directory is on the python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    print("=" * 60)
    print("  CodeSense: AI-Powered Debugging Tutor")
    print("  Intellexa TechTober Challenge Edition")
    print("=" * 60)
    print("  Languages Supported: Python 3.14 & Java 17")
    print("  Server URL: http://localhost:8000")
    print("=" * 60)
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
