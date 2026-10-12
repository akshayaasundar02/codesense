import os
import subprocess
import time

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>CodeSense — Comprehensive Project & Technical Architecture Documentation</title>
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
  <script>
    mermaid.initialize({ startOnLoad: true, theme: 'neutral', themeVariables: { primaryColor: '#e0ecfb', edgeLabelBackground: '#ffffff', fontFamily: 'Inter, sans-serif' } });
  </script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

    :root {
      --primary: #102c57;
      --primary-light: #1679ab;
      --accent: #f39c12;
      --success: #10b981;
      --danger: #ef4444;
      --bg: #f8fafc;
      --surface: #ffffff;
      --text: #1e293b;
      --text-muted: #64748b;
      --border: #e2e8f0;
      --radius: 10px;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Inter', system-ui, -apple-system, sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.65;
      padding: 40px 20px;
    }

    .container {
      max-width: 1000px;
      margin: 0 auto;
      background: var(--surface);
      padding: 60px 80px;
      border-radius: var(--radius);
      box-shadow: 0 4px 25px rgba(0,0,0,0.06);
      border: 1px solid var(--border);
    }

    /* Header & Title */
    .header {
      text-align: center;
      border-bottom: 2px solid var(--border);
      padding-bottom: 30px;
      margin-bottom: 40px;
    }
    .badge-pill {
      display: inline-block;
      background: #eff6ff;
      color: var(--primary-light);
      font-weight: 600;
      font-size: 0.85rem;
      padding: 6px 16px;
      border-radius: 999px;
      border: 1px solid #bfdbfe;
      margin-bottom: 15px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    h1 {
      font-size: 2.6rem;
      font-weight: 800;
      color: var(--primary);
      margin-bottom: 12px;
      line-height: 1.2;
    }
    .subtitle {
      font-size: 1.2rem;
      color: var(--text-muted);
      margin-bottom: 16px;
      font-weight: 400;
    }
    .meta-bar {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 15px;
      font-size: 0.88rem;
      color: var(--text-muted);
      margin-top: 15px;
    }
    .meta-item {
      background: #f1f5f9;
      padding: 4px 12px;
      border-radius: 6px;
      border: 1px solid #e2e8f0;
    }

    /* Headings */
    h2 {
      font-size: 1.65rem;
      color: var(--primary);
      margin: 45px 0 18px 0;
      padding-bottom: 8px;
      border-bottom: 2px solid #e2e8f0;
      font-weight: 700;
    }
    h3 {
      font-size: 1.25rem;
      color: var(--primary-light);
      margin: 25px 0 12px 0;
      font-weight: 600;
    }
    p { margin-bottom: 14px; font-size: 1rem; color: #334155; }
    ul, ol { margin-bottom: 16px; padding-left: 24px; color: #334155; }
    li { margin-bottom: 6px; }

    /* Callouts & Highlights */
    .callout {
      background: #f0f7ff;
      border-left: 5px solid var(--primary-light);
      padding: 20px 24px;
      border-radius: 6px;
      margin: 24px 0;
    }
    .callout.statement {
      background: #faf5ff;
      border-left-color: #9333ea;
    }
    .callout h4 {
      font-size: 1.05rem;
      margin-bottom: 8px;
      color: var(--primary);
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .callout p { margin-bottom: 0; font-size: 0.98rem; line-height: 1.6; }

    /* Tables */
    table {
      width: 100%;
      border-collapse: collapse;
      margin: 25px 0;
      font-size: 0.95rem;
    }
    th, td {
      padding: 12px 16px;
      text-align: left;
      border: 1px solid var(--border);
    }
    th {
      background: #102c57;
      color: #ffffff;
      font-weight: 600;
    }
    tr:nth-child(even) td { background: #f8fafc; }

    /* Code blocks */
    pre, code {
      font-family: 'JetBrains Mono', monospace;
    }
    code {
      background: #f1f5f9;
      color: #0f172a;
      padding: 2px 6px;
      border-radius: 4px;
      font-size: 0.9em;
    }
    pre {
      background: #0f172a;
      color: #f8fafc;
      padding: 18px 22px;
      border-radius: 8px;
      overflow-x: auto;
      margin: 18px 0;
      font-size: 0.92rem;
      line-height: 1.5;
    }
    pre code { background: none; color: inherit; padding: 0; }

    /* Feature Grid */
    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 20px;
      margin: 25px 0;
    }
    .card {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 20px 22px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.03);
      transition: transform 0.2s ease;
    }
    .card h4 {
      color: var(--primary);
      font-size: 1.1rem;
      margin-bottom: 8px;
    }
    .card p { font-size: 0.92rem; color: #475569; margin-bottom: 0; }

    /* Diagrams */
    .diagram-box {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 24px;
      margin: 30px 0;
      text-align: center;
      overflow-x: auto;
    }
    .diagram-caption {
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-top: 10px;
      font-style: italic;
    }

    /* Print styles */
    @media print {
      body { background: #ffffff; padding: 0; }
      .container { box-shadow: none; border: none; padding: 20px 30px; max-width: 100%; }
      h2 { page-break-before: auto; }
      .diagram-box { page-break-inside: avoid; }
      table { page-break-inside: avoid; }
      pre { page-break-inside: avoid; }
    }
  </style>
</head>
<body>

<div class="container">

  <!-- Header -->
  <div class="header">
    <span class="badge-pill">AI-Powered Student Automation · Project Technical Documentation</span>
    <h1>CodeSense</h1>
    <div class="subtitle">An AI-Powered, Hint-First Intelligent Debugging & Programming Learning Platform</div>
    <div class="meta-bar">
      <span class="meta-item"><strong>Repository:</strong> akshayaasundar02/codesense</span>
      <span class="meta-item"><strong>Backend:</strong> FastAPI + Python 3.11</span>
      <span class="meta-item"><strong>Runtimes:</strong> Python 3.11 & OpenJDK 17</span>
      <span class="meta-item"><strong>Intelligence:</strong> Groq Llama-3.3-70b</span>
      <span class="meta-item"><strong>Database:</strong> SQLite</span>
      <span class="meta-item"><strong>Automation:</strong> n8n Workflow Engine</span>
    </div>
  </div>

  <!-- Section 1 -->
  <h2>1. Executive Summary & Problem Formulation</h2>

  <h3>1.1 What is the Actual Problem?</h3>
  <p>When students and junior programmers begin learning programming (in Python and Java), they frequently encounter runtime exceptions and algorithmic bugs:</p>
  <ul>
    <li><strong><code>IndexError</code>:</strong> Attempting to access an index beyond the boundaries of an array or list.</li>
    <li><strong><code>TypeError</code>:</strong> Performing operations on incompatible types (e.g., concatenating an integer and a string).</li>
    <li><strong><code>NameError</code>:</strong> Referencing identifiers, functions, or variables before declaration or initialization.</li>
    <li><strong><code>ValueError</code>:</strong> Supplying arguments with an invalid value to functions (e.g., <code>int("abc")</code>).</li>
    <li><strong><code>IndentationError</code> / <code>SyntaxError</code>:</strong> Violating lexical nesting or structural language grammar.</li>
  </ul>

  <p>Knowing that an error exists is only the starting point. Students also need to understand:</p>
  <ol>
    <li><strong>Understanding the Root Cause:</strong> Why did the program fail at this specific step?</li>
    <li><strong>Mental Model Divergence:</strong> Where did the programmer's intent diverge from the computer's actual runtime execution?</li>
    <li><strong>Prevention:</strong> How can the student internalize the logic pattern to avoid repeating the mistake in future programs?</li>
  </ol>

  <p>Consider this canonical Python off-by-one bug:</p>
  <pre><code>numbers = [10, 20, 30, 40]
for i in range(len(numbers) + 1):
    print(numbers[i])</code></pre>
  <p>The student expects all four numbers to be printed. However, the loop executes with <code>i &isin; {0, 1, 2, 3, 4}</code>. At <code>i = 4</code>, it attempts to access <code>numbers[4]</code>. Because zero-indexed lists of length 4 only have valid indices <code>0, 1, 2, 3</code>, Python halts with an <code>IndexError: list index out of range</code>.</p>

  <h3>1.2 Why Existing Approaches Fail Learners</h3>
  <table>
    <thead>
      <tr>
        <th style="width:25%;">Approach</th>
        <th style="width:38%;">Typical Workflow</th>
        <th style="width:37%;">Critical Educational Flaw</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Traditional Compilers & Debugging</strong></td>
        <td>Cryptic terminal tracebacks &rarr; Manual Web Search &rarr; Trial-and-error edits</td>
        <td>High barrier to entry; beginners get overwhelmed by traceback jargon and lack guidance on where to start.</td>
      </tr>
      <tr>
        <td><strong>Conventional AI Coding Assistants</strong></td>
        <td>Student pastes broken code &rarr; LLM spits out fully corrected replacement code</td>
        <td><strong>Premature Spoiler Syndrome:</strong> Bypasses the student's cognitive struggle. The code runs, but the student never internalizes the algorithmic reasoning.</td>
      </tr>
      <tr>
        <td><strong>CodeSense Platform</strong></td>
        <td>Identify error &rarr; 3-Way Cause Breakdown &rarr; Progressive Clues (Tier 1 &rarr; 2 &rarr; 3) &rarr; Interactive State Visualization &rarr; Transfer Mastery</td>
        <td><strong>Guided Cognitive Apprenticeship:</strong> Protects student reasoning, explains the divergence gap in plain language, visualizes invisible runtime memory, and proves mastery via isomorphic challenges.</td>
      </tr>
    </tbody>
  </table>

  <h3>1.3 Competition-Ready Problem Statement</h3>
  <div class="callout statement">
    <h4>🏆 Official Problem Statement</h4>
    <p><strong>CodeSense — An AI-Powered, Hint-First Intelligent Debugging and Programming Learning Platform</strong><br><br>
    Beginner programmers often struggle to understand, diagnose, and resolve errors in their code. Although conventional debugging tools identify errors and AI coding assistants can generate corrected programs, learners may remain dependent on ready-made solutions without developing strong debugging and problem-solving skills.<br><br>
    CodeSense aims to bridge this gap by providing an interactive, AI-powered debugging tutor that explains programming errors in simple language, identifies the underlying cause, and delivers progressive hints instead of immediately revealing the corrected code. Learners are encouraged to predict program behaviour, reason about the bug, attempt their own corrections, and validate their solutions through execution and feedback.<br><br>
    The platform further strengthens learning by generating similar practice problems, adapting hints to the learner's progress, and tracking recurring error patterns. Its goal is to transform debugging from a frustrating trial-and-error activity into a guided, measurable, and engaging learning experience that builds independent programming ability.</p>
  </div>

  <!-- Section 2 -->
  <h2>2. System Architecture</h2>
  <p>CodeSense is engineered with a modular, decoupled client-server architecture designed for sub-second execution speed, deterministic sandbox security, and pedagogical guidance.</p>

  <div class="diagram-box">
    <pre class="mermaid">
flowchart TD
    subgraph Client ["Client Tier (Browser / Frontend SPA)"]
        UI_AUTH["Screen 0: Auth Landing\n(Log In / Register / Guest)"]
        UI_TOPICS["Screen 1: Topics Hub\n(10 Progressive Domains)"]
        UI_QUESTIONS["Screen 2: Questions Track\n(10 Progressive Difficulty Tiers)"]
        UI_WORKBENCH["Screen 3: Debugging Workbench\n(Code Editor & Dual Diagnostics)"]
        UI_STUDIO["Custom Question Studio\n(Free Practice Mode)"]
        UI_ANALYTICS["Learner Analytics Modal\n(Radar Scores & Streaks)"]
    end

    subgraph API_Gateway ["API Gateway & Routing Tier (FastAPI)"]
        ENDPOINT_AUTH["/api/auth (Login & Register)"]
        ENDPOINT_EXEC["/api/execute (Run & Sandbox)"]
        ENDPOINT_CURR["/api/topics & /api/problems"]
        ENDPOINT_HINT["/api/hint (3-Tier Clues)"]
        ENDPOINT_CAUSE["/api/explain-cause (3-Way Breakdown)"]
        ENDPOINT_TRANSFER["/api/transfer-challenge (Mastery Check)"]
        ENDPOINT_PROFILE["/api/profile & /api/record-attempt"]
    end

    subgraph Engine_Tier ["Core Intelligence & Execution Tier"]
        RUNNER["Subprocess Execution Engine\n(Python 3.11 & OpenJDK 17 Sandbox)"]
        MATCHER["Resilient Output Matcher\n(Label-Agnostic Normalizer)"]
        AI_TUTOR["AI Pedagogical Tutor Engine\n(Groq Llama-3.3-70b + Heuristics)"]
        VISUALIZER["Visual State Explorer Engine\n(7 Interactive SVG/DOM Canvases)"]
    end

    subgraph Persistence_Tier ["Data & Persistence Tier"]
        DB[("SQLite Database\n(users, attempts, streaks)")]
        JSON_CURR[("Curriculum Knowledge Base\n(100 Python + 100 Java Problems)")]
    end

    subgraph Automation_Tier ["Automation & Reporting Tier"]
        N8N["n8n Automated Workflow\n(Daily Challenge Delivery & Reports)"]
    end

    UI_AUTH --> ENDPOINT_AUTH
    UI_TOPICS --> ENDPOINT_CURR
    UI_QUESTIONS --> ENDPOINT_CURR
    UI_WORKBENCH --> ENDPOINT_EXEC
    UI_WORKBENCH --> ENDPOINT_HINT
    UI_WORKBENCH --> ENDPOINT_CAUSE
    UI_WORKBENCH --> ENDPOINT_TRANSFER
    UI_STUDIO --> ENDPOINT_EXEC
    UI_ANALYTICS --> ENDPOINT_PROFILE

    ENDPOINT_AUTH --> DB
    ENDPOINT_PROFILE --> DB
    ENDPOINT_EXEC --> RUNNER
    ENDPOINT_EXEC --> MATCHER
    ENDPOINT_EXEC --> VISUALIZER
    ENDPOINT_CURR --> JSON_CURR
    ENDPOINT_HINT --> AI_TUTOR
    ENDPOINT_CAUSE --> AI_TUTOR
    ENDPOINT_TRANSFER --> AI_TUTOR

    N8N -.->|Pulls Daily Practice| ENDPOINT_CURR
    N8N -.->|Fetches Metrics| ENDPOINT_PROFILE
    </pre>
    <div class="diagram-caption">Figure 1: Full System Architecture Diagram of CodeSense</div>
  </div>

  <!-- Section 3 -->
  <h2>3. The Five Core Innovations</h2>
  <div class="grid">
    <div class="card">
      <h4>💡 1. Hint-First Debugging Engine</h4>
      <p>Prevents premature solution spoilers. Clues unlock across three distinct pedagogical stages: Line Locator, Conceptual Bridge, and Targeted Direction.</p>
    </div>
    <div class="card">
      <h4>🎨 2. Visual Bug Explorer</h4>
      <p>Interactive DOM/SVG representations for 7 runtime failure types: list memory index bounds, type collisions, variable scoping, and loop steps.</p>
    </div>
    <div class="card">
      <h4>🔍 3. 3-Way Cause Breakdown</h4>
      <p>Deconstructs the complete cognitive chain: Programmer's Intent, Actual Machine Execution, and the Divergence Gap with a memorable Golden Prevention Rule.</p>
    </div>
    <div class="card">
      <h4>🔥 4. Strict Solve-Only Streak Engine</h4>
      <p>Streaks never increment on login or failed tests. Increments strictly upon verified algorithmic success on the first solve of that calendar day.</p>
    </div>
    <div class="card">
      <h4>🚀 5. Isomorphic Transfer Challenges</h4>
      <p>Once a bug is repaired, the AI tutor generates a brand new problem with different variables but identical underlying algorithmic structure to prove true mastery.</p>
    </div>
  </div>

  <!-- Section 4 -->
  <h2>4. Key Implemented Modules & Features</h2>

  <h3>4.1 Screen 0: Dedicated Authentication Portal</h3>
  <p>A focused entry portal before the curriculum catalog. Features clean tabs for <strong>Log In</strong> and <strong>Create Account</strong>, plus a <strong>"Continue as Guest &rarr;"</strong> shortcut. User passwords are encrypted with SHA-256 salted hashes, and daily problem streaks are persisted in SQLite.</p>

  <h3>4.2 Pure Algorithmic 10-Tier Curriculum</h3>
  <p>200 hand-crafted algorithmic challenges (100 Python + 100 Java) spanning 10 topics and 10 difficulty tiers:</p>
  <ul>
    <li><strong>🟢 Beginner (Levels 1–3):</strong> List bounds, string reversals, palindrome checks, min/max scanning.</li>
    <li><strong>🟡 Intermediate (Levels 4–7):</strong> Two sum hash complements, duplicate removal, zero partitioning, array rotation.</li>
    <li><strong>🔴 Advanced (Levels 8–10):</strong> Stock profit tracking, Kadane's maximum subarray sum, trapping rain water.</li>
  </ul>
  <p>The catalog includes an active difficulty filter (All 10 Levels, Beginner, Intermediate, Advanced) and workbench header controls with an instant <code>[ 🚀 Advance to Level X ➔ ]</code> action banner.</p>

  <h3>4.3 Resilient Label-Agnostic Test Evaluator</h3>
  <p>Eliminates the frustration of traditional judges that fail correct code due to label differences (e.g. printing <code>[5, 4, 3, 2, 1]</code> instead of <code>Reversed: [5, 4, 3, 2, 1]</code>). The engine performs label stripping, whitespace normalization, and multi-line inspection to evaluate genuine logic.</p>

  <h3>4.4 Target Expected vs Actual Output Display</h3>
  <p>Dual output panels display side-by-side diagnostic feedback:</p>
  <ul>
    <li><strong>Your Output:</strong> Raw stdout/stderr produced by the student's program execution.</li>
    <li><strong>Expected Goal:</strong> Canonical target algorithmic result.</li>
  </ul>

  <h3>4.5 Review Solved Questions Mode</h3>
  <p>Students can freely reopen and review any previously solved question without resetting their progress, allowing them to experiment with alternative algorithmic solutions.</p>

  <!-- Section 5 -->
  <h2>5. End-to-End User Learning Journey</h2>
  <div class="diagram-box">
    <pre class="mermaid">
sequenceDiagram
    autonumber
    actor Student
    participant UI as CodeSense Frontend
    participant Server as FastAPI Server
    participant Sandbox as Subprocess Sandbox
    participant AI as AI Pedagogical Engine
    participant DB as SQLite DB

    Student->>UI: Visits Platform
    alt Not Logged In
        UI->>Student: Displays Screen 0 (Login / Register Portal)
        Student->>UI: Logs in or Clicks 'Continue as Guest'
    end
    UI->>Student: Displays Screen 1 (Topics Catalog)
    Student->>UI: Selects Topic (e.g., Arrays & Lists)
    UI->>Student: Displays Screen 2 (Levels 1–10 Track)
    Student->>UI: Selects Level 1 (Reverse Array)
    UI->>Student: Loads Screen 3 (Workbench)
    
    Student->>UI: Runs Broken Starter Code
    UI->>Server: POST /api/execute
    Server->>Sandbox: Execute in isolated subprocess (3.5s timeout)
    Sandbox-->>Server: stdout, stderr
    Server->>Server: Evaluate output via check_outputs_match()
    
    alt Test Failed / Runtime Error
        Server-->>UI: Output Mismatch / Parsed Exception
        UI->>Student: Shows Expected vs Actual (MISMATCH ❌)
        UI->>Server: POST /api/explain-cause
        Server->>AI: Generate 3-Way Intent/Execution Breakdown
        AI-->>Server: Structured Cause
        Server-->>UI: Cause Breakdown + Visual State Explorer
        Student->>UI: Requests Clue &rarr; Receives Tier 1 Clue
        Student->>UI: Edits Code & Runs Again
    end

    Server-->>UI: all_tests_passed == True (MATCH ✅)
    UI->>Student: Confetti Celebration 🎉 + Success Banner
    UI->>Server: POST /api/record-attempt {solved: true}
    Server->>DB: Record attempt & increment Daily Streak
    UI->>Student: Displays [Advance to Level 2 ➔]
    Student->>UI: Clicks Advance &rarr; Workbench seamlessly loads Level 2!
    </pre>
    <div class="diagram-caption">Figure 2: End-to-End User Journey Sequence Diagram</div>
  </div>

  <!-- Section 6 -->
  <h2>6. Automated Student Workflow (n8n Integration)</h2>
  <p>Packaged in <code>codesense_student_automation_workflow.json</code>, the 9-node automation workflow manages scheduled practice delivery:</p>
  <ul>
    <li><strong>Node 1: Daily Schedule Trigger</strong> &mdash; Fires every morning at 08:00 AM.</li>
    <li><strong>Node 2: Fetch Student Streak & Profile</strong> &mdash; Queries <code>/api/profile</code>.</li>
    <li><strong>Node 3: Retrieve Daily Curated Challenge</strong> &mdash; Queries <code>/api/problems</code>.</li>
    <li><strong>Node 4: AI Personalized Clue Generator</strong> &mdash; Generates targeted encouragement via Groq LLM.</li>
    <li><strong>Node 5: Conditional Branching</strong> &mdash; Detects at-risk students who missed their streak.</li>
    <li><strong>Nodes 6 & 7: Morning Challenge Dispatch</strong> &mdash; Delivers challenge via Email / Webhook.</li>
    <li><strong>Nodes 8 & 9: Progress Sync</strong> &mdash; Updates student automation metrics.</li>
  </ul>

  <!-- Section 7 -->
  <h2>7. Security & Sandbox Isolation Architecture</h2>
  <p>To safely execute untrusted student Python and Java programs without risking server integrity, CodeSense implements multi-layered isolation:</p>
  <ul>
    <li><strong>Subprocess Isolation:</strong> Code runs in standalone Python/Java sub-processes with restricted environment variables, completely stripping API keys.</li>
    <li><strong>Execution Timeouts:</strong> Hard wall-clock limit of 3.5 seconds terminates infinite loops (<code>while True</code>) and resource deadlocks.</li>
    <li><strong>Memory Safeguards:</strong> Resource limits prevent heap exhaustion and memory attacks.</li>
    <li><strong>Salted Credential Hashing:</strong> User passwords stored with SHA-256 cryptographic salts.</li>
  </ul>

  <!-- Section 8 -->
  <h2>8. Project Directory Structure</h2>
  <pre><code>codesense/
├── app/
│   ├── config.py              # Application settings, ports, and model parameters
│   ├── curriculum_data.json   # 200 progressive algorithmic challenges (10x10x2)
│   ├── curriculum_data.py     # In-memory accessors and filtering utilities
│   ├── database.py            # SQLite schema, streak calculator, user auth & analytics
│   ├── main.py                # FastAPI endpoints, output matching & error handling
│   ├── models.py              # Pydantic validation schemas
│   ├── runner.py              # Sandboxed Python & Java execution engine
│   ├── tutor_engine.py        # 3-tier hints, 3-way cause breakdown & transfer challenges
│   └── visualizer_engine.py   # State visualizer schemas (bounds, types, scope, loops)
├── static/
│   ├── css/
│   │   ├── style.css          # Glassmorphism design system & responsive styling
│   │   └── visualizer.css     # Memory cell, pointer, and flowchart styling
│   ├── js/
│   │   ├── app.js             # Main SPA coordinator, view routing & auth handlers
│   │   ├── editor.js          # Code editor manager, tab handler & run triggers
│   │   ├── hints.js           # Tiered hints drawer coordinator
│   │   └── visualizer.js      # Dynamic SVG/HTML visual memory renderer
│   └── index.html             # Single-page application root (Screens 0, 1, 2, 3)
├── n8n_workflows/
│   ├── codesense_student_automation_workflow.json # 9-node student automation workflow
│   └── AI_STUDENT_AUTOMATION_PROJECT_REPORT.md    # Domain & automation project report
├── DOCUMENTATION.md           # Markdown comprehensive documentation
├── Dockerfile                 # Debian Bookworm container with OpenJDK 17 + Python 3.11
├── requirements.txt           # FastAPI, Uvicorn, Pydantic & Groq dependencies
├── codesense.db               # SQLite persistent database
└── run.py                     # Local development launcher</code></pre>

</div>

</body>
</html>
"""

with open("CodeSense_Project_Documentation.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Generated CodeSense_Project_Documentation.html successfully.")
