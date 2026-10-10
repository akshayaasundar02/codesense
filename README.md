# 🧠 CodeSense: An AI-Powered Debugging Tutor That Teaches You to Think Like a Programmer

> **Intellexa TechTober Challenge Edition**  
> *Transforming code-generating chatbots into intelligent Socratic tutors that build independent problem-solving mastery.*

---

## 🌟 The Core Problem
When students and placement aspirants learn programming, they frequently face daunting runtime failures:
- **`IndexError` / `ArrayIndexOutOfBoundsException`**: Off-by-one errors in loop boundaries and array subscripts.
- **`TypeError` / `NumberFormatException`**: Mixing incompatible data types or failing to parse API payloads safely.
- **`NullPointerException` / `AttributeError: 'NoneType'`**: Dereferencing null object pointers in data structures.
- **`RecursionError` / `StackOverflowError`**: Missing termination base conditions in recursive traversals.
- **`KeyError` / `NoSuchElementException`**: Unchecked hash table lookups and queue underflows.

Traditional AI chatbots simply spit out the corrected code. While convenient, **this deprives students of learning why their code broke and prevents them from clearing technical placement interviews.**

---

## 🚀 The 5 Core Innovations of CodeSense

### 1. 💡 Hint-First Graduated Debugging Engine
CodeSense **never dumps complete solutions**. It guides the learner through 3 progressive stages:
- **Level 1 (Subtle Observation)**: Highlights the suspicious code area and asks a guiding question (-5 Independence pts).
- **Level 2 (Conceptual Logic)**: Explains the underlying computer science mechanism (memory indexing, fail-fast iterators, call stack frames) (-15 pts).
- **Level 3 (Targeted Strategy)**: Provides structured pseudocode and actionable fixing steps (-30 pts).
- **Independence Score**: Rewarding learners who conquer bugs with fewer clues.

### 2. 🔬 Visual Bug Explorer (The Showstopper Innovation)
Makes invisible runtime state visible before the student's eyes:
- **Array Memory & Boundary Visualizer**: Renders elements with valid `[0 .. N-1]` indices and flashes a pulsing neon crash cell pointing to the out-of-bounds target index.
- **Loop State & Boundary Stepper**: Interactive step-by-step playback with Play/Pause/Prev/Next buttons, live condition evaluations, and index watches.
- **Stack & Frame Tracker**: Visual vertical tube displaying call stack frames pushing and popping with recursion overflow warnings.
- **Object Reference & Tree Explorer**: Highlights null pointers where a child node reference was dereferenced.
- **Variable Watch Table**: Real-time snapshot of runtime variables and types at the moment of failure.

### 3. 🔍 3-Way Comparative Decomposition
Breaks every failure down into:
1. **Programmer's Intention**: What you intended the logic to accomplish.
2. **Actual Runtime Execution**: What the interpreter/CPU actually executed.
3. **The Divergence Gap**: The exact root-cause invariant violation where intention and execution diverged.
4. **Placement Interview & Production Guard**: Senior engineering practices to prevent the bug in real-world systems.
5. **Mental Model Physical Analogy**: An intuitive real-world physical metaphor (e.g. "Looking for the 5th floor in a 4-story building").

### 4. 📈 Adaptive Learning Profile & Bug Vulnerability Radar
- Tracks recurring mistake patterns (Off-by-One, Null Pointers, Type Coercion, Infinite Recursion).
- Measures learner **Independence Rating** over time.
- Maintains daily debugging streak.

### 5. 🎓 Learn, Retry, and Prove Mastery (Transfer Learning)
Once a student successfully fixes a bug, CodeSense automatically unlocks a **Transfer Challenge**—a related scenario-based question testing the exact same underlying concept in a new context to prove real mastery before moving forward.

---

## 🛠️ Tech Stack & Multi-Language Support
- **Frontend**: Clean HTML5, CSS3 Glassmorphism design system (`backdrop-filter: blur(16px)`), modern dark aesthetic with glowing accents, and vanilla JavaScript.
- **Multi-Language Execution**: Natively runs and parses stack traces for **Python 3.14** and **Java 17 OpenJDK**!
- **Backend**: **FastAPI** + **Uvicorn** for low-latency asynchronous processing.
- **AI Acceleration**: **Groq Cloud** (`llama-3.3-70b-versatile` / `llama-3.1-8b-instant`) with sub-second response times, plus offline fallback heuristics.
- **Persistence**: **SQLite** (`codesense.db`) storing attempts, streak, and error radar distribution.

---

## 📚 Placement Curriculum (Basics to Advanced)
Covers 10 core technical placement interview topics across Python and Java:
1. **Variables & Type Safety** *(Fintech Invoice Total, Microservice User ID)*
2. **Conditionals & Logic Gates** *(Loan Eligibility Decision, String Reference vs Value)*
3. **Loops & Off-by-One Boundaries** *(IoT Sensor Moving Average, High-Frequency Order Book)*
4. **Arrays & Slicing** *(Two-Pointer Target Pair, Sliding Window Maximum)*
5. **Strings & HashMaps** *(URL Shortener Cache, Concurrent Session Pruning)*
6. **Stacks & Queues** *(Valid Bracket Linter, Task Dispatcher Underflow)*
7. **Recursion & Call Stacks** *(Directory Quota Calculator, Fibonacci Recursion)*
8. **Binary Trees & BSTs** *(Corporate Org Compensation Auditor, BST Validator)*
9. **Heaps & Priority Queues** *(Ride-Sharing Dispatcher, Meeting Rooms Scheduler)*
10. **Dynamic Programming & Graphs** *(ATM Cash Dispenser Min Coins, Longest Increasing Subsequence)*

---

## ⚡ Quick Start Guide

### 1. Start the Server
```bash
python run.py
```

### 2. Open in Browser
Navigate to:
```
http://localhost:8000
```

### 3. Optional: Configure Groq API Key
Click the **Sliders (⚙️)** icon in the top header and enter your Groq API key (`gsk_...`). If omitted, CodeSense seamlessly runs with its built-in curriculum heuristics.
