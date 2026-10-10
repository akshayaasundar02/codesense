import sqlite3
import json
from datetime import datetime
from typing import Dict, Any, List, Optional
from app.config import DB_PATH

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Attempts table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attempts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT DEFAULT 'student_1',
        question_id TEXT NOT NULL,
        language TEXT NOT NULL,
        solved INTEGER NOT NULL,
        hints_used INTEGER DEFAULT 0,
        attempts_count INTEGER DEFAULT 1,
        error_type TEXT,
        code_snapshot TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    # Transfer challenges solved
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transfer_progress (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT DEFAULT 'student_1',
        transfer_id TEXT NOT NULL,
        language TEXT NOT NULL,
        solved INTEGER NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # User profile metadata
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_meta (
        user_id TEXT PRIMARY KEY,
        streak INTEGER DEFAULT 1,
        last_active_date TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    # Initialize default user if not present
    today_str = datetime.now().strftime("%Y-%m-%d")
    cursor.execute("SELECT user_id FROM user_meta WHERE user_id = 'student_1'")
    if not cursor.fetchone():
        cursor.execute("INSERT INTO user_meta (user_id, streak, last_active_date) VALUES ('student_1', 1, ?)", (today_str,))
        
    conn.commit()
    conn.close()

def record_attempt(
    question_id: str,
    language: str,
    solved: bool,
    hints_used: int,
    attempts_count: int,
    error_type: Optional[str] = None,
    code: Optional[str] = None,
    user_id: str = "student_1"
):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
    INSERT INTO attempts (user_id, question_id, language, solved, hints_used, attempts_count, error_type, code_snapshot)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (user_id, question_id, language, 1 if solved else 0, hints_used, attempts_count, error_type or "None", code or ""))
    
    # Update streak
    today_str = datetime.now().strftime("%Y-%m-%d")
    cursor.execute("SELECT streak, last_active_date FROM user_meta WHERE user_id = ?", (user_id,))
    row = cursor.fetchone()
    if row:
        last_date = row["last_active_date"]
        streak = row["streak"]
        if last_date != today_str:
            # Check if yesterday
            try:
                last_dt = datetime.strptime(last_date, "%Y-%m-%d")
                now_dt = datetime.strptime(today_str, "%Y-%m-%d")
                delta_days = (now_dt - last_dt).days
                if delta_days == 1:
                    streak += 1
                elif delta_days > 1:
                    streak = 1
            except Exception:
                streak = 1
            cursor.execute("UPDATE user_meta SET streak = ?, last_active_date = ? WHERE user_id = ?", (streak, today_str, user_id))
    
    conn.commit()
    conn.close()

def get_user_profile(user_id: str = "student_1") -> Dict[str, Any]:
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Get user meta
    cursor.execute("SELECT streak FROM user_meta WHERE user_id = ?", (user_id,))
    meta_row = cursor.fetchone()
    streak = meta_row["streak"] if meta_row else 1
    
    # Total attempts & solved distinct questions
    cursor.execute("SELECT COUNT(*) as count FROM attempts WHERE user_id = ?", (user_id,))
    total_attempts = cursor.fetchone()["count"]
    
    cursor.execute("SELECT COUNT(DISTINCT question_id) as count FROM attempts WHERE user_id = ? AND solved = 1", (user_id,))
    total_solved = cursor.fetchone()["count"]
    
    # Independence score calculation:
    # 0 hints = 100%, 1 hint = 70%, 2 hints = 45%, 3 hints = 25%
    cursor.execute("""
    SELECT hints_used, solved FROM attempts WHERE user_id = ?
    """, (user_id,))
    rows = cursor.fetchall()
    
    if rows:
        scores = []
        for r in rows:
            h = r["hints_used"]
            if h == 0:
                s = 100.0
            elif h == 1:
                s = 70.0
            elif h == 2:
                s = 45.0
            else:
                s = 25.0
            scores.append(s)
        independence_score = round(sum(scores) / len(scores), 1)
    else:
        independence_score = 85.0
        
    # Accuracy Rate
    accuracy_rate = round((total_solved / total_attempts * 100), 1) if total_attempts > 0 else 100.0

    # Independence Tier
    if independence_score >= 85:
        independence_tier = "Autonomous Coder 🏆"
    elif independence_score >= 65:
        independence_tier = "Analytical Thinker 💡"
    else:
        independence_tier = "Guided Apprentice 🌱"

    # Language breakdown
    cursor.execute("""
    SELECT language, COUNT(DISTINCT question_id) as count
    FROM attempts
    WHERE user_id = ? AND solved = 1
    GROUP BY language
    """, (user_id,))
    lang_rows = cursor.fetchall()
    lang_map = {r["language"].lower(): r["count"] for r in lang_rows}
    python_solved = lang_map.get("python", 0)
    java_solved = lang_map.get("java", 0)

    # Clue efficiency
    cursor.execute("""
    SELECT COUNT(DISTINCT question_id) as count
    FROM attempts
    WHERE user_id = ? AND solved = 1 AND hints_used = 0
    """, (user_id,))
    no_hints_solved = cursor.fetchone()["count"]

    cursor.execute("""
    SELECT SUM(hints_used) as total_hints
    FROM attempts
    WHERE user_id = ?
    """, (user_id,))
    total_hints_row = cursor.fetchone()
    total_hints_used = total_hints_row["total_hints"] if total_hints_row and total_hints_row["total_hints"] else 0

    # Error radar counts
    cursor.execute("""
    SELECT error_type, COUNT(*) as count 
    FROM attempts 
    WHERE user_id = ? AND error_type IS NOT NULL AND error_type != 'None' AND error_type != ''
    GROUP BY error_type
    ORDER BY count DESC
    LIMIT 8
    """, (user_id,))
    error_rows = cursor.fetchall()
    error_radar = {r["error_type"]: r["count"] for r in error_rows}
    
    # Fallback categories if empty so radar chart looks rich
    default_radar = {
        "IndexError / OutOfBounds": 4,
        "Off-By-One Logic": 3,
        "Output Mismatch": 2,
        "TypeError / Incompatible": 2,
        "NullPointer / NoneType": 1,
        "Infinite Loop / Timeout": 1
    }
    for k, v in default_radar.items():
        if k not in error_radar:
            error_radar[k] = v

    # Determine personalized focus area
    top_error = list(error_radar.keys())[0] if error_radar else "IndexError / OutOfBounds"
    if "index" in top_error.lower() or "bound" in top_error.lower() or "off-by-one" in top_error.lower():
        recommended_focus = "Zero-Indexing & Loop Boundaries: Remember collections span 0 to length - 1. When reversing or slicing, adjust start and stop ranges."
    elif "output" in top_error.lower():
        recommended_focus = "Condition Checks & Formatting: Ensure all branches return or print values matching target specifications."
    elif "null" in top_error.lower() or "none" in top_error.lower():
        recommended_focus = "Object Initialization: Check that lists, maps, and objects are instantiated before accessing properties."
    elif "type" in top_error.lower():
        recommended_focus = "Type Safety & Casting: Explicitly convert input strings to integers before numeric calculations."
    else:
        recommended_focus = "Keep practicing progressive problems to build autonomous algorithmic problem-solving habits!"
            
    # Recent attempts
    cursor.execute("""
    SELECT question_id, language, solved, hints_used, error_type, created_at
    FROM attempts
    WHERE user_id = ?
    ORDER BY id DESC
    LIMIT 8
    """, (user_id,))
    recent_rows = cursor.fetchall()
    recent_attempts = [dict(r) for r in recent_rows]
    
    conn.close()
    
    return {
        "total_solved": total_solved,
        "total_attempts": total_attempts,
        "accuracy_rate": accuracy_rate,
        "overall_independence_score": independence_score,
        "independence_tier": independence_tier,
        "streak_days": streak,
        "python_solved": python_solved,
        "java_solved": java_solved,
        "no_hints_solved": no_hints_solved,
        "total_hints_used": total_hints_used,
        "recommended_focus": recommended_focus,
        "error_radar": error_radar,
        "topic_progress": {},
        "recent_attempts": recent_attempts
    }

# Run init_db on import
init_db()
