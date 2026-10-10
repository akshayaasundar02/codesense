/**
 * Code Editor Manager - CodeSense
 * Handles code editing, line numbers, execution sandbox requests, and test validations
 */

const EditorManager = {
  currentLanguage: "python", // "python" or "java"
  initialCode: "",
  attemptsCount: 0,
  errorLine: null,

  init() {
    const textarea = document.getElementById("codeEditor");
    const gutter = document.getElementById("editorGutter");

    if (textarea && gutter) {
      textarea.addEventListener("input", () => this.updateLineNumbers());
      textarea.addEventListener("scroll", () => {
        gutter.scrollTop = textarea.scrollTop;
      });

      // STRICT NO COPY-PASTE POLICY: Students must type code manually to learn!
      textarea.addEventListener("paste", (e) => {
        e.preventDefault();
        App.showToast("🚫 Copy-paste is disabled! Type code manually to build true problem-solving mastery.");
      });

      textarea.addEventListener("drop", (e) => {
        e.preventDefault();
        App.showToast("🚫 Drag & drop is disabled! Type code manually.");
      });

      textarea.addEventListener("contextmenu", (e) => {
        // Optional: Let them know paste is blocked even if context menu opens
      });

      // Support Tab key indentation & intercept Ctrl+V / Cmd+V
      textarea.addEventListener("keydown", (e) => {
        if ((e.ctrlKey || e.metaKey) && (e.key === "v" || e.key === "V")) {
          e.preventDefault();
          App.showToast("🚫 Paste shortcut is disabled! Practice typing the code manually.");
          return;
        }

        if (e.key === "Tab") {
          e.preventDefault();
          const start = textarea.selectionStart;
          const end = textarea.selectionEnd;
          textarea.value = textarea.value.substring(0, start) + "    " + textarea.value.substring(end);
          textarea.selectionStart = textarea.selectionEnd = start + 4;
          this.updateLineNumbers();
        }
      });
    }

    this.updateLineNumbers();
  },

  updateLineNumbers() {
    const textarea = document.getElementById("codeEditor");
    const gutter = document.getElementById("editorGutter");
    if (!textarea || !gutter) return;

    const lines = textarea.value.split("\n").length;
    let gutterHtml = "";
    for (let i = 1; i <= lines; i++) {
      const isErr = this.errorLine === i;
      gutterHtml += `<div style="${isErr ? 'color: #f87171; font-weight: bold; background: rgba(239, 68, 68, 0.2); border-radius: 3px;' : ''}">${i}</div>`;
    }
    gutter.innerHTML = gutterHtml;
  },

  setCode(code, language = "python") {
    const textarea = document.getElementById("codeEditor");
    if (!textarea) return;
    this.currentLanguage = language;
    this.initialCode = code;
    textarea.value = code;
    this.errorLine = null;
    this.attemptsCount = 0;
    this.updateLineNumbers();
  },

  getCode() {
    const textarea = document.getElementById("codeEditor");
    return textarea ? textarea.value : "";
  },

  resetCode() {
    const codeToLoad = this.starterTemplate || this.initialCode;
    this.setCode(codeToLoad, this.currentLanguage);
    App.showToast("Reset to clean starter template. Code it from scratch!");
  },

  clearCode() {
    const blankPrompt = this.currentLanguage === "python" 
      ? "# Write your solution from scratch below:\n\n" 
      : "public class Main {\n    public static void main(String[] args) {\n        // Write your solution from scratch below:\n        \n    }\n}\n";
    this.setCode(blankPrompt, this.currentLanguage);
    App.showToast("Cleared canvas. Write your solution from scratch!");
  },

  async runAndDiagnose() {
    const runBtn = document.getElementById("btnRunCode");
    const code = this.getCode();
    let qId = App.currentProblem ? App.currentProblem.id : null;
    this.attemptsCount += 1;

    // Smart auto-detection: If student wrote Java code while Python is selected, auto-switch to Java!
    const isJavaCode = code.includes("public class") || code.includes("public static void") || code.includes("System.out") || code.includes("int[]") || code.includes("String[]");
    const isPythonCode = code.includes("def ") || code.includes("elif ") || (code.includes("print(") && !code.includes("System.out"));

    if (this.currentLanguage === "python" && isJavaCode) {
      this.currentLanguage = "java";
      App.activeLanguage = "java";
      const btnPy = document.getElementById("langTogglePy");
      const btnJava = document.getElementById("langToggleJava");
      if (btnPy && btnJava) {
        btnPy.classList.remove("active");
        btnJava.classList.add("active");
      }
      if (qId && qId.startsWith("py-")) {
        qId = qId.replace("py-", "java-");
      }
      App.showToast("⚡ Auto-detected Java code! Running with Java ☕");
    } else if (this.currentLanguage === "java" && isPythonCode) {
      this.currentLanguage = "python";
      App.activeLanguage = "python";
      const btnPy = document.getElementById("langTogglePy");
      const btnJava = document.getElementById("langToggleJava");
      if (btnPy && btnJava) {
        btnJava.classList.remove("active");
        btnPy.classList.add("active");
      }
      if (qId && qId.startsWith("java-")) {
        qId = qId.replace("java-", "py-");
      }
      App.showToast("⚡ Auto-detected Python code! Running with Python 🐍");
    }

    if (runBtn) {
      runBtn.disabled = true;
      runBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Running...';
    }

    try {
      const customTitle = App.isCustomMode ? (document.getElementById("customInputTitle")?.value || "") : "";
      const customDesc = App.isCustomMode ? (document.getElementById("customInputDesc")?.value || "") : "";
      const customExpected = App.isCustomMode ? (document.getElementById("customInputExpected")?.value || "") : "";

      const res = await fetch("/api/execute", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          code: code,
          language: this.currentLanguage,
          question_id: qId,
          custom_title: customTitle,
          custom_description: customDesc,
          expected_output: customExpected
        })
      });

      const data = await res.json();
      this.handleExecutionResult(data);
    } catch (e) {
      console.error(e);
      App.showToast("Execution request failed.");
    } finally {
      if (runBtn) {
        runBtn.disabled = false;
        runBtn.innerHTML = '<i class="fa-solid fa-play"></i> Run & Diagnose';
      }
    }
  },

  async handleExecutionResult(res) {
    const term = document.getElementById("consoleOutput");
    if (term) {
      term.textContent = (res.output || "") + (res.error ? `\n--- ERROR LOG ---\n${res.error}` : "");
    }

    // 1. Success case: All tests passed & no error
    if (res.success && res.all_tests_passed) {
      this.errorLine = null;
      this.updateLineNumbers();
      App.onProblemSolved(res);
      return;
    }

    // 2. Error case or partial output mismatch
    const parsed = res.parsed_error || {
      error_type: "LogicalOutputMismatch",
      message: "Output did not match expected solution result.",
      line_number: null
    };

    this.errorLine = parsed.line_number;
    this.updateLineNumbers();

    // Render visual data
    VisualizerEngine.render(res.visual_data, document.getElementById("visualizerContainer"));

    // Render Error Banner
    App.renderErrorBanner(parsed, res.execution_time_ms);

    // Fetch 3-Way Cause Breakdown
    App.fetchCauseBreakdown(parsed);

    // Record attempt in background DB
    if (App.currentProblem) {
      fetch("/api/record-attempt", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          question_id: App.currentProblem.id,
          language: this.currentLanguage,
          solved: false,
          hints_used: HintManager.currentTier,
          attempts_count: this.attemptsCount,
          error_type: parsed.error_type,
          code: this.getCode()
        })
      }).catch(console.error);
    }

    // Switch to diagnostic tab
    App.switchSuiteTab("diagnostic");
    App.showToast(`Error caught: ${parsed.error_type}`);
  }
};
