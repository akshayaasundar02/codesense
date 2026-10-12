import os
import re
import subprocess
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), hex_color)
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def create_docx(filename="CodeSense_Project_Documentation.docx"):
    doc = Document()
    
    # Page setup - 1 inch margins
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)
        
    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_title = p_title.add_run("CodeSense")
    run_title.font.name = "Calibri"
    run_title.font.size = Pt(28)
    run_title.font.bold = True
    run_title.font.color.rgb = RGBColor(16, 44, 87) # Deep Navy
    
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_sub = p_sub.add_run("AI-Powered Interactive Coding, Debugging & Learning Platform\nComprehensive Technical & Pedagogical Architecture Documentation")
    run_sub.font.name = "Calibri"
    run_sub.font.size = Pt(14)
    run_sub.font.italic = True
    run_sub.font.color.rgb = RGBColor(70, 80, 95)
    
    # Divider line
    p_meta = doc.add_paragraph()
    p_meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_meta = p_meta.add_run("Domain: AI-Powered Student Automation | Repository: https://github.com/akshayaasundar02/codesense\nStack: FastAPI · Python 3.11 · OpenJDK 17 · Groq Llama-3.3 · SQLite · Vanilla SPA · n8n Automation")
    run_meta.font.name = "Calibri"
    run_meta.font.size = Pt(10)
    run_meta.font.color.rgb = RGBColor(100, 110, 125)
    
    doc.add_paragraph() # spacer

    def add_h1(text):
        h = doc.add_paragraph()
        run = h.add_run(text)
        run.font.name = "Calibri"
        run.font.size = Pt(18)
        run.font.bold = True
        run.font.color.rgb = RGBColor(16, 44, 87)
        h.paragraph_format.space_before = Pt(14)
        h.paragraph_format.space_after = Pt(6)
        return h

    def add_h2(text):
        h = doc.add_paragraph()
        run = h.add_run(text)
        run.font.name = "Calibri"
        run.font.size = Pt(14)
        run.font.bold = True
        run.font.color.rgb = RGBColor(30, 70, 130)
        h.paragraph_format.space_before = Pt(10)
        h.paragraph_format.space_after = Pt(4)
        return h

    def add_h3(text):
        h = doc.add_paragraph()
        run = h.add_run(text)
        run.font.name = "Calibri"
        run.font.size = Pt(12)
        run.font.bold = True
        run.font.color.rgb = RGBColor(50, 90, 150)
        h.paragraph_format.space_before = Pt(6)
        h.paragraph_format.space_after = Pt(2)
        return h

    def add_p(text, bold_prefix="", italic=False):
        p = doc.add_paragraph()
        if bold_prefix:
            r_bold = p.add_run(bold_prefix)
            r_bold.font.name = "Calibri"
            r_bold.font.size = Pt(11)
            r_bold.font.bold = True
        run = p.add_run(text)
        run.font.name = "Calibri"
        run.font.size = Pt(11)
        run.font.italic = italic
        run.font.color.rgb = RGBColor(30, 30, 30)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        return p

    def add_bullet(text, bold_prefix=""):
        p = doc.add_paragraph(style='List Bullet')
        if bold_prefix:
            rb = p.add_run(bold_prefix)
            rb.font.name = "Calibri"
            rb.font.size = Pt(11)
            rb.font.bold = True
        run = p.add_run(text)
        run.font.name = "Calibri"
        run.font.size = Pt(11)
        run.font.color.rgb = RGBColor(30, 30, 30)
        p.paragraph_format.space_after = Pt(3)
        return p

    def add_callout(text, title="KEY PRINCIPLE"):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = tbl.cell(0, 0)
        set_cell_background(cell, "F0F4F8")
        set_cell_margins(cell, top=140, bottom=140, left=200, right=200)
        cp = cell.paragraphs[0]
        rt = cp.add_run(f"📌 {title}: ")
        rt.font.name = "Calibri"
        rt.font.size = Pt(10.5)
        rt.font.bold = True
        rt.font.color.rgb = RGBColor(16, 44, 87)
        r = cp.add_run(text)
        r.font.name = "Calibri"
        r.font.size = Pt(10.5)
        r.font.italic = True
        r.font.color.rgb = RGBColor(40, 50, 70)
        doc.add_paragraph() # space after table

    # 1. Executive Summary & Problem Formulation
    add_h1("1. Executive Summary & Problem Formulation")
    
    add_h2("1.1 What is the Actual Problem?")
    add_p("When students and junior developers begin learning Python or Java, they constantly run into common runtime exceptions:")
    add_bullet(" IndexError — Attempting to access an index beyond the boundaries of an array/list.", "•")
    add_bullet(" TypeError — Performing an operation on incompatible types (e.g. adding string and integer).", "•")
    add_bullet(" NameError — Using an identifier, variable, or function before it has been defined.", "•")
    add_bullet(" ValueError — Passing an inappropriate value or argument to a function.", "•")
    add_bullet(" IndentationError / SyntaxError — Breaking lexical indentation or structural language grammar.", "•")
    
    add_p("Simply knowing that an error occurred is only the beginning. Beginners must develop the ability to answer three essential pedagogical questions:")
    add_bullet(" What caused the error in this exact line?", "1.")
    add_bullet(" Where did the student's mental expectation diverge from the computer's actual runtime execution?", "2.")
    add_bullet(" How can the student internalize the underlying principle to avoid repeating this error?", "3.")

    add_p("Consider a canonical Python off-by-one bug:", "Example: ")
    add_p("numbers = [10, 20, 30, 40]\nfor i in range(len(numbers) + 1):\n    print(numbers[i])", italic=True)
    add_p("The student expects all four numbers to be printed. However, the loop executes with i in {0, 1, 2, 3, 4}. At index 4, the program attempts to access numbers[4]. In zero-indexed lists of length 4, valid indices are strictly 0, 1, 2, and 3. Python immediately halts with an IndexError.")

    add_h2("1.2 Why Existing Approaches Fail Learners")
    
    table_comp = doc.add_table(rows=4, cols=3)
    table_comp.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers = ["Approach", "Typical Workflow", "Critical Educational Flaw"]
    for i, h in enumerate(headers):
        cell = table_comp.cell(0, i)
        set_cell_background(cell, "102C57")
        p = cell.paragraphs[0]
        run = p.add_run(h)
        run.font.name = "Calibri"
        run.font.size = Pt(10)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)

    comp_data = [
        ("Traditional Compilers & Debugging", "Cryptic traceback messages → Manual Web/StackOverflow search → Trial-and-error edits", "Intimidating to beginners; error messages contain confusing internal engine jargon without explaining the conceptual mistake."),
        ("Ordinary AI Coding Assistants", "Student pastes broken code → Assistant immediately outputs the fully corrected code", "Premature Spoiler Syndrome: By revealing the full solution instantly, students copy-paste without critical reasoning and remain dependent."),
        ("CodeSense Learning Platform", "Identify error → 3-Way Cause Breakdown → 3-Tier Progressive Clues → Interactive Visualizer → Transfer Mastery Challenge", "Cognitive Apprenticeship: Encourages the student to reason through the bug, visualizes invisible runtime memory, and proves true mastery.")
    ]
    for row_idx, row_vals in enumerate(comp_data, start=1):
        bg = "F9FBFC" if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, val in enumerate(row_vals):
            cell = table_comp.cell(row_idx, col_idx)
            set_cell_background(cell, bg)
            p = cell.paragraphs[0]
            run = p.add_run(val)
            run.font.name = "Calibri"
            run.font.size = Pt(9.5)
            if col_idx == 0:
                run.font.bold = True

    doc.add_paragraph()

    add_h2("1.3 Competition-Ready Problem Statement")
    add_callout(
        "Beginner programmers frequently struggle to diagnose, interpret, and resolve errors in their code. "
        "While traditional compilers provide cryptic tracebacks and modern AI code generators produce instant solutions, "
        "learners remain reliant on pre-packaged answers without cultivating independent debugging ability.\n\n"
        "CodeSense bridges this learning gap by providing an interactive, pedagogical programming platform that explains "
        "programming bugs in plain language, identifies the root cause through a 3-way cognitive breakdown, and delivers "
        "tiered progressive hints without revealing spoilers. Learners are encouraged to predict runtime behaviour, explore "
        "interactive visual memory states, iteratively repair their logic, and validate comprehension through isomorphic Transfer "
        "Challenges. CodeSense transforms debugging from an intimidating trial-and-error cycle into a structured, measurable, "
        "and engaging learning journey that builds lasting programming independence.",
        title="OFFICIAL PROBLEM STATEMENT"
    )

    # 2. Five Core Innovations
    add_h1("2. Five Core Architectural Innovations")
    
    innovations = [
        ("1. Hint-First Pedagogical Debugging Engine", "Instead of blurting out the solution, CodeSense provides clues in 3 distinct progressive stages: Tier 1 identifies the suspicious construct and line; Tier 2 explains the core computer science concept; Tier 3 offers actionable direction without writing the code for the student."),
        ("2. Interactive Visual State & Bug Explorer", "Demystifies invisible runtime execution by rendering dynamic visual models for 7 error categories: array bounds with out-of-range pointers, type collision meters, variable scope frames, loop step trackers, and recursion trees."),
        ("3. 3-Way Cognitive Cause Breakdown", "Explains the complete chain of events: Programmer's Intent (what the student intended), Machine Execution (what the CPU actually did), Divergence Gap (where the two differed), and a Golden Prevention Rule for future engineering."),
        ("4. Strict Solve-Only Daily Streak Engine", "Unlike conventional platforms where streaks increment upon simply logging in, CodeSense enforces honest practice: streaks increment strictly when code passes all automated test cases on the user's first algorithmic solve of that calendar day."),
        ("5. Isomorphic Transfer Challenges (Proof of Mastery)", "Once a bug is repaired, CodeSense generates a brand-new practice problem testing the exact same conceptual pattern with different business logic. Solving the new problem proves the student truly internalized the concept rather than merely copying a fix.")
    ]
    for title, desc in innovations:
        add_h3(title)
        add_p(desc)

    # 3. System Architecture & Tech Stack
    add_h1("3. System Architecture & Technical Specifications")
    
    add_p("CodeSense is designed with a high-performance, modular 5-tier architecture:")
    add_bullet(" Client Tier: Vanilla SPA (HTML5, Glassmorphic CSS3, Vanilla JS) delivering sub-50ms render latency without framework overhead.", "1.")
    add_bullet(" API Gateway Tier: FastAPI with asynchronous ASGI request routing, strict Pydantic input validation, and SHA-256 salted authentication.", "2.")
    add_bullet(" Execution & Sandbox Tier: Isolated subprocess execution with hard 3.5s timeout limits, label-agnostic resilient output matching, and memory bounds.", "3.")
    add_bullet(" Intelligence Tier: Groq Llama-3.3-70b-versatile with temperature tuning for pedagogical coaching, backed by instant deterministic heuristics.", "4.")
    add_bullet(" Automation Tier: n8n workflow integration for scheduled morning challenge delivery, automated streak monitoring, and email digests.", "5.")

    add_h2("3.1 10-Topic Dual-Language Curriculum Matrix")
    add_p("The platform features 200 hand-crafted challenges (100 Python + 100 Java) spanning 10 progressive topics and 10 difficulty levels:")
    
    curr_topics = [
        ("1. Arrays & Lists", "Levels 1–3: Reversal, Palindromes, Min/Max | Levels 4–7: Two Sum, Duplicates, Zero Partition, Rotation | Levels 8–10: Stock Profit, Kadane's Sum, Trapping Rain Water"),
        ("2. Strings & Text", "Levels 1–3: Vowel Counting, Word Reversal | Levels 4–7: Anagrams, Longest Substring | Levels 8–10: Palindrome Partitioning, String Matching"),
        ("3. Searching & Loops", "Levels 1–3: Linear Search, First Occurrence | Levels 4–7: Binary Search, Peak Element | Levels 8–10: Rotated Array Search, Median of Arrays"),
        ("4. Math & Number Theory", "Levels 1–3: Prime Check, Factorial | Levels 4–7: GCD Euclidean, Armstrong Numbers | Levels 8–10: Modular Exponentiation, Sieve of Eratosthenes"),
        ("5. Conditionals & Branching", "Levels 1–3: Leap Year, Grade Evaluation | Levels 4–7: Roman Numerals, Version Comparison | Levels 8–10: Expression Evaluator, Interval Overlap"),
        ("6. Stacks & Queues", "Levels 1–3: Parentheses Matching, Reverse String | Levels 4–7: Min-Stack O(1), Queue via Stacks | Levels 8–10: Monotonic Stack, Sliding Window Max"),
        ("7. Recursion & Backtracking", "Levels 1–3: Exponentiation, Fibonacci | Levels 4–7: Tower of Hanoi, Power Sets | Levels 8–10: N-Queens, Word Search"),
        ("8. Binary Trees & BST", "Levels 1–3: Inorder, Max Depth | Levels 4–7: Level-Order BFS, Symmetric Tree | Levels 8–10: Lowest Common Ancestor, Max Path Sum"),
        ("9. Heaps & Priority Queues", "Levels 1–3: Min Heap Insertion, K-th Smallest | Levels 4–7: K-th Largest, Merge K Sorted | Levels 8–10: Median from Stream, Task Scheduler"),
        ("10. Dynamic Programming", "Levels 1–3: Climbing Stairs, House Robber | Levels 4–7: Coin Change, Longest Increasing Subseq | Levels 8–10: 0/1 Knapsack, Longest Common Subseq, Edit Distance")
    ]
    for topic_name, topic_levels in curr_topics:
        add_bullet(f" {topic_levels}", topic_name)

    # 4. Feature Deep Dive
    add_h1("4. Key Implemented Modules & Features")

    modules = [
        ("Screen 0: Dedicated Authentication Portal", "Presents an intuitive first-screen login and sign-up interface before accessing the curriculum. Protects student streak records, enables seamless account creation, and includes a 'Continue as Guest' mode for instant classroom demonstrations."),
        ("Resilient Label-Agnostic Test Evaluator", "Traditional coding platforms fail students if their output prints '[5, 4, 3, 2, 1]' when the test expects 'Reversed: [5, 4, 3, 2, 1]'. CodeSense implements intelligent label stripping, multi-line searching, and token whitespace normalization to reward genuine algorithmic reasoning."),
        ("Expected vs. Actual Output Visual Diff", "Workbench displays dual panels side-by-side: 'Your Output' (exact stdout/stderr produced) versus 'Expected Goal' (target algorithmic result). Clear visual status badges (MATCH / MISMATCH) clarify exactly how the program behaved."),
        ("Workbench Progressive Difficulty Switcher", "Header dropdown switcher allows immediate switching between Levels 1 to 10. Upon solving any challenge, an instant action banner '[ 🚀 Advance to Level X: Title ➔ ]' appears to seamlessly load the next tier without returning to the catalog."),
        ("Interactive Memory Visualizer Engine", "Renders rich visual representations including valid vs invalid array indices, type collision gauges, and loop step flows directly below the code editor."),
        ("Review Solved Questions Mode", "Students can revisit already solved questions at any time to review their solution, re-run test cases, or inspect alternative algorithmic approaches without disrupting their streak."),
        ("n8n Automated Student Workflow", "A 9-node scheduled automation workflow that delivers morning programming challenges, checks student streaks, branches alerts for at-risk learners, and generates automated progress digests.")
    ]
    for title, desc in modules:
        add_h2(title)
        add_p(desc)

    # 5. Security & Sandbox
    add_h1("5. Sandbox Execution & Security Architecture")
    add_p("To safely execute untrusted student Python and Java programs without risking server integrity, CodeSense implements multi-layered isolation:")
    add_bullet(" Subprocess Isolation: Code runs in standalone Python/Java sub-processes with restricted environment variables, completely stripping API keys.", "•")
    add_bullet(" Execution Timeouts: Hard wall-clock limit of 3.5 seconds terminates infinite loops (while True) and resource deadlocks.", "•")
    add_bullet(" Memory Safeguards: Resource limits prevent heap exhaustion and memory attacks.", "•")
    add_bullet(" Salted Credential Hashing: User passwords stored with SHA-256 cryptographic salts.", "•")

    # 6. Conclusion
    add_h1("6. Conclusion & Impact")
    add_p("CodeSense bridges the critical gap between frustrating trial-and-error debugging and passive copy-paste AI code generators. By integrating progressive clues, interactive visualizers, resilient test matching, and isomorphic transfer challenges, CodeSense delivers a guided, measurable, and engaging learning experience that empowers students to become confident, independent software engineers.")

    doc.save(filename)
    print(f"Successfully generated Word document: {filename}")

if __name__ == "__main__":
    create_docx()
