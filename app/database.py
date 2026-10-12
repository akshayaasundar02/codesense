import sqlite3
import json
import hashlib
from datetime import datetime
from typing import Dict, Any, List, Optional
from app.config import DB_PATH

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def hash_password(password: str, salt: str = "codesense_salt_2026") -> str:
    return hashlib.sha256(f"{salt}_{password}".encode("utf-8")).hexdigest()

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Registered users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        streak INTEGER DEFAULT 0,
        last_solve_date TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

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

    # User profile metadata (for guest / default fallback)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_meta (
        user_id TEXT PRIMARY KEY,
        streak INTEGER DEFAULT 0,
        last_active_date TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    conn.commit()
    conn.close()

# ----------------- AUTHENTICATION -----------------

def create_user(username: str, email: str, password: str) -> Dict[str, Any]:
    username = username.strip()
    email = email.strip().lower()
    
    if len(username) < 3:
        return {"success": False, "message": "Username must be at least 3 characters."}
    if "@" not in email or "." not in email:
        return {"success": False, "message": "Please enter a valid email address."}
    if len(password) < 4:
        return {"success": False, "message": "Password must be at least 4 characters."}

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM users WHERE LOWER(username) = LOWER(?)", (username,))
    if cursor.fetchone():
        conn.close()
        return {"success": False, "message": "Username already taken. Please choose another."}

    cursor.execute("SELECT id FROM users WHERE LOWER(email) = LOWER(?)", (email,))
    if cursor.fetchone():
        conn.close()
        return {"success": False, "message": "An account with this email already exists."}

    pwd_hash = hash_password(password)
    cursor.execute("""
    INSERT INTO users (username, email, password_hash, streak, last_solve_date)
    VALUES (?, ?, ?, 0, NULL)
    """, (username, email, pwd_hash))
    user_id = cursor.lastrowid
    conn.commit()
    conn.close()

    return {
        "success": True,
        "message": "Account created successfully!",
        "user": {
            "id": user_id,
            "username": username,
            "email": email,
            "streak": 0
        }
    }

def authenticate_user(identifier: str, password: str) -> Dict[str, Any]:
    identifier = identifier.strip()
    pwd_hash = hash_password(password)

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT id, username, email, password_hash, streak, last_solve_date
    FROM users
    WHERE LOWER(username) = LOWER(?) OR LOWER(email) = LOWER(?)
    """, (identifier, identifier))
    row = cursor.fetchone()
    conn.close()

    if not row:
        return {"success": False, "message": "No account found with this username or email."}

    if row["password_hash"] != pwd_hash:
        return {"success": False, "message": "Incorrect password. Please try again."}

    # Streak stays as-is; never increase on login!
    return {
        "success": True,
        "message": "Logged in successfully!",
        "user": {
            "id": row["id"],
            "username": row["username"],
            "email": row["email"],
            "streak": row["streak"] or 0
        }
    }

# ----------------- STREAK & ATTEMPTS -----------------

def update_streak_on_solve(user_id: str) -> int:
    """
    INCREASE STREAK ONLY WHEN SOLVING A QUESTION (all_tests_passed == True).
    Never increases on login, page refresh, or failed runs.
    """
    today_str = datetime.now().strftime("%Y-%m-%d")
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, streak, last_solve_date FROM users WHERE id = ? OR username = ?", (str(user_id), str(user_id)))
    user_row = cursor.fetchone()

    if user_row:
        last_date = user_row["last_solve_date"]
        current_streak = user_row["streak"] or 0

        if not last_date:
            new_streak = 1
        elif last_date == today_str:
            new_streak = max(1, current_streak)  # Solved multiple today -> keeps today's streak
        else:
            try:
                last_dt = datetime.strptime(last_date, "%Y-%m-%d")
                now_dt = datetime.strptime(today_str, "%Y-%m-%d")
                delta_days = (now_dt - last_dt).days
                if delta_days == 1:
                    new_streak = current_streak + 1  # Continuous day -> increment
                else:
                    new_streak = 1  # Missed days -> reset to 1
            except Exception:
                new_streak = 1

        cursor.execute("UPDATE users SET streak = ?, last_solve_date = ? WHERE id = ?", (new_streak, today_str, user_row["id"]))
        conn.commit()
        conn.close()
        return new_streak
    else:
        cursor.execute("SELECT streak, last_active_date FROM user_meta WHERE user_id = ?", (str(user_id),))
        meta_row = cursor.fetchone()
        current_streak = meta_row["streak"] if meta_row else 0
        last_date = meta_row["last_active_date"] if meta_row else None

        if not last_date:
            new_streak = 1
        elif last_date == today_str:
            new_streak = max(1, current_streak)
        else:
            try:
                last_dt = datetime.strptime(last_date, "%Y-%m-%d")
                now_dt = datetime.strptime(today_str, "%Y-%m-%d")
                delta_days = (now_dt - last_dt).days
                new_streak = current_streak + 1 if delta_days == 1 else 1
            except Exception:
                new_streak = 1

        cursor.execute("INSERT OR REPLACE INTO user_meta (user_id, streak, last_active_date) VALUES (?, ?, ?)", (str(user_id), new_streak, today_str))
        conn.commit()
        conn.close()
        return new_streak

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
    """, (str(user_id), question_id, language, 1 if solved else 0, hints_used, attempts_count, error_type or "None", code or ""))
    
    conn.commit()
    conn.close()

    # CRITICAL: ONLY update streak when solved is True!
    if solved:
        update_streak_on_solve(str(user_id))

def get_user_solved_status(user_id: str, language: Optional[str] = None) -> Dict[str, Any]:
    """
    Returns a map of question_id -> {solved: True, last_code: str, solved_at: str}
    Allows students to review and re-practice questions even after solving them.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
    SELECT question_id, code_snapshot, created_at
    FROM attempts
    WHERE (user_id = ? OR user_id = 'student_1') AND solved = 1
    """
    params = [str(user_id)]
    if language:
        query += " AND LOWER(language) = LOWER(?)"
        params.append(language)
    query += " ORDER BY id ASC"

    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()

    solved_map = {}
    for r in rows:
        solved_map[r["question_id"]] = {
            "solved": True,
            "last_code": r["code_snapshot"] or "",
            "solved_at": r["created_at"]
        }
    return solved_map

def get_user_profile(user_id: str = "student_1") -> Dict[str, Any]:
    conn = get_db_connection()
    cursor = conn.cursor()
    
    today_str = datetime.now().strftime("%Y-%m-%d")
    streak = 0

    # 1. Fetch user streak
    cursor.execute("SELECT streak, last_solve_date FROM users WHERE id = ? OR username = ?", (str(user_id), str(user_id)))
    user_row = cursor.fetchone()

    if user_row:
        raw_streak = user_row["streak"] or 0
        last_date = user_row["last_solve_date"]
        if last_date:
            try:
                last_dt = datetime.strptime(last_date, "%Y-%m-%d")
                now_dt = datetime.strptime(today_str, "%Y-%m-%d")
                delta_days = (now_dt - last_dt).days
                # Streak is active only if solved today (0) or yesterday (1)
                streak = raw_streak if delta_days <= 1 else 0
            except Exception:
                streak = 0
        else:
            streak = 0
    else:
        cursor.execute("SELECT streak, last_active_date FROM user_meta WHERE user_id = ?", (str(user_id),))
        meta_row = cursor.fetchone()
        if meta_row and meta_row["last_active_date"]:
            try:
                last_dt = datetime.strptime(meta_row["last_active_date"], "%Y-%m-%d")
                now_dt = datetime.strptime(today_str, "%Y-%m-%d")
                delta_days = (now_dt - last_dt).days
                streak = meta_row["streak"] if delta_days <= 1 else 0
            except Exception:
                streak = 0
        else:
            streak = 0
    
    # 2. Total attempts & solved distinct questions
    cursor.execute("SELECT COUNT(*) as count FROM attempts WHERE user_id = ? OR user_id = 'student_1'", (str(user_id),))
    total_attempts = cursor.fetchone()["count"]
    
    cursor.execute("SELECT COUNT(DISTINCT question_id) as count FROM attempts WHERE (user_id = ? OR user_id = 'student_1') AND solved = 1", (str(user_id),))
    total_solved = cursor.fetchone()["count"]
    
    # 3. Independence score calculation
    cursor.execute("""
    SELECT hints_used, solved FROM attempts WHERE user_id = ? OR user_id = 'student_1'
    """, (str(user_id),))
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
        independence_score = 95.0
        
    accuracy_rate = round((total_solved / total_attempts * 100), 1) if total_attempts > 0 else 100.0

    if independence_score >= 85:
        independence_tier = "Autonomous Coder 🏆"
    elif independence_score >= 65:
        independence_tier = "Analytical Thinker 💡"
    else:
        independence_tier = "Guided Apprentice 🌱"

    # 4. Language breakdown
    cursor.execute("""
    SELECT language, COUNT(DISTINCT question_id) as count
    FROM attempts
    WHERE (user_id = ? OR user_id = 'student_1') AND solved = 1
    GROUP BY language
    """, (str(user_id),))
    lang_rows = cursor.fetchall()
    lang_map = {r["language"].lower(): r["count"] for r in lang_rows}
    python_solved = lang_map.get("python", 0)
    java_solved = lang_map.get("java", 0)

    # 5. Clue efficiency
    cursor.execute("""
    SELECT COUNT(DISTINCT question_id) as count
    FROM attempts
    WHERE (user_id = ? OR user_id = 'student_1') AND solved = 1 AND hints_used = 0
    """, (str(user_id),))
    no_hints_solved = cursor.fetchone()["count"]

    cursor.execute("""
    SELECT SUM(hints_used) as total_hints
    FROM attempts
    WHERE user_id = ? OR user_id = 'student_1'
    """, (str(user_id),))
    total_hints_row = cursor.fetchone()
    total_hints_used = total_hints_row["total_hints"] if total_hints_row and total_hints_row["total_hints"] else 0

    # 6. Error radar counts
    cursor.execute("""
    SELECT error_type, COUNT(*) as count 
    FROM attempts 
    WHERE (user_id = ? OR user_id = 'student_1') AND error_type IS NOT NULL AND error_type != 'None' AND error_type != ''
    GROUP BY error_type
    ORDER BY count DESC
    LIMIT 8
    """, (str(user_id),))
    error_rows = cursor.fetchall()
    error_radar = {r["error_type"]: r["count"] for r in error_rows}
    
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
            
    # 7. Recent attempts
    cursor.execute("""
    SELECT question_id, language, solved, hints_used, error_type, created_at
    FROM attempts
    WHERE user_id = ? OR user_id = 'student_1'
    ORDER BY id DESC
    LIMIT 8
    """, (str(user_id),))
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
