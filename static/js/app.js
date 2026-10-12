/**
 * Main Application Coordinator - CodeSense
 * 3-View Screen Navigation:
 * View 1: Topics Hub (Home)
 * View 2: Topic Questions (10 Progressive Levels from Scratch to Advanced)
 * View 3: Debugging Workbench
 */

const App = {
  currentView: "topics", // "topics", "questions", "workbench"
  currentTopic: null,
  currentProblem: null,
  currentTopicProblems: [],
  topics: [],
  activeLanguage: "python", // "python" or "java"
  transferChallengeData: null,
  isCustomMode: false,
  currentUser: null,
  currentUserId: "student_1",
  solvedProblemsMap: {},

  async init() {
    this.currentUser = JSON.parse(localStorage.getItem("codesense_user") || "null");
    this.currentUserId = this.currentUser ? this.currentUser.username : "student_1";
    this.updateAuthUI();

    EditorManager.init();
    HintManager.reset();
    this.setupEventListeners();
    await this.loadTopics();
    await this.fetchUserProgress();
    await this.updateProfileStats();
    this.showTopicsView();
  },

  setupEventListeners() {
    // Language toggles
    const btnPy = document.getElementById("langTogglePy");
    const btnJava = document.getElementById("langToggleJava");
    if (btnPy && btnJava) {
      btnPy.onclick = () => this.setLanguage("python");
      btnJava.onclick = () => this.setLanguage("java");
    }

    // Suite tabs
    document.querySelectorAll(".suite-tab").forEach((tab) => {
      tab.addEventListener("click", () => {
        const tabId = tab.getAttribute("data-tab");
        this.switchSuiteTab(tabId);
      });
    });

    // Run Code
    const runBtn = document.getElementById("btnRunCode");
    if (runBtn) runBtn.onclick = () => EditorManager.runAndDiagnose();

    // Reset Code
    const resetBtn = document.getElementById("btnResetCode");
    if (resetBtn) resetBtn.onclick = () => EditorManager.resetCode();

    // Clear Code Canvas
    const clearBtn = document.getElementById("btnClearCode");
    if (clearBtn) clearBtn.onclick = () => EditorManager.clearCode();

    // Modals
    const btnAnalytics = document.getElementById("btnAnalytics");
    if (btnAnalytics) btnAnalytics.onclick = () => this.openAnalyticsModal();

    const btnSettings = document.getElementById("btnSettings");
    if (btnSettings) btnSettings.onclick = () => this.openSettingsModal();
  },

  setLanguage(lang) {
    this.activeLanguage = lang;
    const btnPy = document.getElementById("langTogglePy");
    const btnJava = document.getElementById("langToggleJava");

    if (lang === "python") {
      btnPy.classList.add("active");
      btnJava.classList.remove("active");
    } else {
      btnJava.classList.add("active");
      btnPy.classList.remove("active");
    }

    // If currently on questions view, reload the 10 questions in the new language
    if (this.currentView === "questions" && this.currentTopic) {
      this.showTopicQuestionsView(this.currentTopic.id);
    } else if (this.currentView === "workbench" && this.currentProblem) {
      // Find counterpart in the new language with same topic and level
      const newId = (lang === "java")
        ? this.currentProblem.id.replace("py-", "java-")
        : this.currentProblem.id.replace("java-", "py-");
      this.selectProblem(newId);
    } else if (this.currentView === "workbench" && this.isCustomMode) {
      // Keep custom fields intact, just adjust editor language
      EditorManager.currentLanguage = lang;
      const curCode = EditorManager.getCode().trim();
      if (!curCode || curCode.startsWith("#") || curCode.startsWith("public class")) {
        const titleVal = document.getElementById("customInputTitle")?.value || "";
        if (titleVal.includes("Prime")) {
          this.loadSampleCustomQuestion("prime");
        } else if (titleVal.includes("Vowel")) {
          this.loadSampleCustomQuestion("vowels");
        } else if (titleVal.includes("Second Largest")) {
          this.loadSampleCustomQuestion("second_largest");
        } else {
          const blankPy = `# Practice Your Own Question\n# Write your code from scratch below:\n\n`;
          const blankJava = `public class Main {\n    public static void main(String[] args) {\n        // Write your code from scratch below:\n        \n    }\n}\n`;
          EditorManager.setCode(lang === "java" ? blankJava : blankPy, lang);
        }
      }
    } else {
      this.showTopicsView();
    }
    this.showToast(`Switched to ${lang === 'python' ? 'Python 🐍' : 'Java ☕'}`);
  },

  async loadTopics() {
    try {
      const res = await fetch("/api/topics");
      const data = await res.json();
      this.topics = data.topics || [];
    } catch (e) {
      console.error(e);
      this.showToast("Failed to load topics catalog.");
    }
  },

  // ========================================================
  // VIEW 1: TOPIC HUB
  // ========================================================
  showTopicsView() {
    this.currentView = "topics";
    document.querySelectorAll(".app-view").forEach((v) => v.classList.remove("active"));
    document.getElementById("view-topics").classList.add("active");

    const container = document.getElementById("topicsGridContainer");
    if (!container) return;

    let html = "";
    this.topics.forEach((t) => {
      html += `
        <div class="topic-card" onclick="App.showTopicQuestionsView('${t.id}')">
          <div class="topic-card-top">
            <div class="topic-icon-box" style="color: ${t.color || 'var(--accent-cyan)'};">
              <i class="fa-solid ${t.icon || 'fa-cube'}"></i>
            </div>
            <span class="topic-badge-count">10 Levels</span>
          </div>

          <div class="topic-card-body">
            <h3>${t.name}</h3>
            <div class="topic-tagline">${t.tagline || '10 progressive challenges'}</div>
            <p class="topic-desc">${t.description}</p>
          </div>

          <div class="topic-card-footer">
            <span class="topic-diff-tag">
              <i class="fa-solid fa-graduation-cap"></i> 10 Coding Challenges
            </span>
            <span class="topic-start-btn">
              Practice Topic <i class="fa-solid fa-arrow-right"></i>
            </span>
          </div>
        </div>
      `;
    });

    container.innerHTML = html;
  },

  // ========================================================
  // VIEW 2: TOPIC QUESTIONS (10 PROGRESSIVE LEVELS)
  // ========================================================
  async showTopicQuestionsView(topicId) {
    this.currentView = "questions";
    this.currentTopic = this.topics.find((t) => t.id === topicId) || { id: topicId, name: topicId };

    document.querySelectorAll(".app-view").forEach((v) => v.classList.remove("active"));
    document.getElementById("view-questions").classList.add("active");

    // Update banner
    document.getElementById("topicBreadcrumbTitle").textContent = this.currentTopic.name;
    document.getElementById("topicBannerTitle").textContent = this.currentTopic.name;
    document.getElementById("topicBannerDesc").textContent = `${this.currentTopic.description} (${this.activeLanguage.toUpperCase()} Edition)`;
    
    const bannerIcon = document.getElementById("topicBannerIcon");
    if (bannerIcon) {
      bannerIcon.innerHTML = `<i class="fa-solid ${this.currentTopic.icon || 'fa-layer-group'}"></i>`;
    }

    const container = document.getElementById("questionsTrackContainer");
    if (!container) return;
    container.innerHTML = `<div style="text-align: center; padding: 40px;"><i class="fa-solid fa-spinner fa-spin"></i> Loading 10 Progressive Challenges...</div>`;

    try {
      const res = await fetch(`/api/problems?topic_id=${topicId}&language=${this.activeLanguage}`);
      const data = await res.json();
      this.currentTopicProblems = data.problems || [];

      await this.fetchUserProgress();
      let html = "";
      this.currentTopicProblems.forEach((p) => {
        const lvl = p.level || 1;
        const diffClass = lvl <= 3 ? "beg" : lvl <= 7 ? "mid" : "adv";
        const isSolved = Boolean(this.solvedProblemsMap && this.solvedProblemsMap[p.id]);

        html += `
          <div class="question-level-card ${isSolved ? 'is-solved' : ''}" onclick="App.selectProblem('${p.id}')">
            <div class="q-level-badge ${diffClass}">
              Level ${lvl}
            </div>

            <div class="q-info">
              <div style="display: flex; align-items: center; gap: 8px; flex-wrap: wrap;">
                <div class="q-title">${p.title}</div>
                ${isSolved ? `<span class="q-solved-badge"><i class="fa-solid fa-circle-check"></i> Solved</span>` : ''}
              </div>
              <div class="q-scenario">
                <i class="fa-solid fa-brain"></i> ${p.scenario}
              </div>
              <div class="q-desc">${p.description}</div>
            </div>

            <button class="q-action-btn ${isSolved ? 'is-solved' : ''}">
              ${isSolved ? 'Review & Practice <i class="fa-solid fa-rotate-left"></i>' : 'Solve Problem <i class="fa-solid fa-code"></i>'}
            </button>
          </div>
        `;
      });

      container.innerHTML = html;
    } catch (e) {
      console.error(e);
      container.innerHTML = `<div style="color: #f87171;">Failed to load questions.</div>`;
    }
  },

  backToCurrentTopicQuestions() {
    if (this.currentTopic) {
      this.showTopicQuestionsView(this.currentTopic.id);
    } else {
      this.showTopicsView();
    }
  },

  // ========================================================
  // VIEW 3: THE DEBUGGING WORKBENCH
  // ========================================================
  async selectProblem(problemId) {
    try {
      const res = await fetch(`/api/problems/${problemId}`);
      const data = await res.json();
      this.currentProblem = data;
      this.isCustomMode = false;
      this.currentView = "workbench";

      document.querySelectorAll(".app-view").forEach((v) => v.classList.remove("active"));
      document.getElementById("view-workbench").classList.add("active");

      // Toggle panels: show curriculum brief, hide custom question box
      const curBrief = document.getElementById("curriculumContextBrief");
      const custBox = document.getElementById("customQuestionBox");
      if (curBrief) curBrief.style.display = "block";
      if (custBox) custBox.style.display = "none";

      // Breadcrumb updates
      const topicName = data.topic_name || (this.currentTopic ? this.currentTopic.name : "Topic");
      document.getElementById("workbenchTopicBackText").textContent = `Back to ${topicName} (10 Levels)`;
      document.getElementById("workbenchBreadcrumbTitle").textContent = data.title;

      // Workbench Titles & Brief
      document.getElementById("editorTitle").textContent = data.title;
      document.getElementById("scenarioTag").textContent = data.scenario;
      document.getElementById("scenarioDescription").textContent = data.description;
      document.getElementById("expectedOutputText").textContent = data.expected_output;

      // Check if problem is already solved (Review Mode)
      const isSolved = Boolean(this.solvedProblemsMap && this.solvedProblemsMap[data.id]);
      const solvedInfo = this.solvedProblemsMap ? this.solvedProblemsMap[data.id] : null;

      let reviewBanner = document.getElementById("reviewModeBanner");
      if (isSolved) {
        if (!reviewBanner && curBrief) {
          reviewBanner = document.createElement("div");
          reviewBanner.id = "reviewModeBanner";
          reviewBanner.className = "solved-review-banner";
          curBrief.insertBefore(reviewBanner, curBrief.firstChild);
        }
        if (reviewBanner) {
          reviewBanner.style.display = "flex";
          reviewBanner.innerHTML = `
            <div>
              <i class="fa-solid fa-circle-check" style="color: #34d399; margin-right: 6px;"></i>
              <strong>Solved Problem (Review Mode):</strong> You've already solved this challenge! Review your working code below or practice alternate approaches.
            </div>
            <button class="btn-secondary" style="font-size: 0.74rem; padding: 4px 10px;" onclick="App.resetToStarterCode()">
              <i class="fa-solid fa-rotate-left"></i> Reset to Starter Code
            </button>
          `;
        }
      } else if (reviewBanner) {
        reviewBanner.style.display = "none";
      }

      // Editor code setup - if solved and saved code exists, load it; else use starter template
      EditorManager.starterTemplate = data.starter_code;
      EditorManager.sampleBuggyCode = data.buggy_code;
      if (isSolved && solvedInfo && solvedInfo.last_code && solvedInfo.last_code.trim()) {
        EditorManager.setCode(solvedInfo.last_code, data.language);
      } else {
        EditorManager.setCode(EditorManager.starterTemplate, data.language);
      }

      // Reset Hints Drawer with new simplified clues
      HintManager.reset();

      // Reset Diagnostic views
      this.resetDiagnosticView();

      this.showToast(`Loaded ${data.title}`);
    } catch (e) {
      console.error(e);
      this.showToast("Failed to load challenge details.");
    }
  },

  openCustomPracticeView(sampleKey = null) {
    this.isCustomMode = true;
    this.currentProblem = null;
    this.currentView = "workbench";

    document.querySelectorAll(".app-view").forEach((v) => v.classList.remove("active"));
    document.getElementById("view-workbench").classList.add("active");

    // Toggle panels: hide curriculum brief, show custom question specification card
    const curBrief = document.getElementById("curriculumContextBrief");
    const custBox = document.getElementById("customQuestionBox");
    if (curBrief) curBrief.style.display = "none";
    if (custBox) custBox.style.display = "block";

    document.getElementById("workbenchTopicBackText").textContent = "Back to All Topics";
    document.getElementById("workbenchBreadcrumbTitle").textContent = "Practice Your Own Question Studio";
    document.getElementById("editorTitle").textContent = "Custom Practice Workspace";
    document.getElementById("scenarioTag").textContent = "Custom Mode";

    if (sampleKey) {
      this.loadSampleCustomQuestion(sampleKey);
    } else {
      const titleInput = document.getElementById("customInputTitle");
      const expInput = document.getElementById("customInputExpected");
      const descInput = document.getElementById("customInputDesc");
      if (titleInput) titleInput.value = "";
      if (expInput) expInput.value = "";
      if (descInput) descInput.value = "";

      const blankPy = `# Practice Your Own Question\n# 1. Type your question title, expected goal & description above\n# 2. Write your code from scratch below:\n\n`;
      const blankJava = `public class Main {\n    public static void main(String[] args) {\n        // 1. Type your question title, expected goal & description above\n        // 2. Write your code from scratch below:\n        \n    }\n}\n`;
      EditorManager.starterTemplate = this.activeLanguage === "java" ? blankJava : blankPy;
      EditorManager.setCode(EditorManager.starterTemplate, this.activeLanguage);
    }

    HintManager.reset();
    this.resetDiagnosticView();
    this.showToast("Practice Your Own Question Studio Ready 🚀");
  },

  loadSampleCustomQuestion(sampleKey) {
    this.isCustomMode = true;
    const curBrief = document.getElementById("curriculumContextBrief");
    const custBox = document.getElementById("customQuestionBox");
    if (curBrief) curBrief.style.display = "none";
    if (custBox) custBox.style.display = "block";

    const samples = {
      prime: {
        title: "Check if a Number is Prime",
        desc: "Given an integer num = 29, write a program to check whether it is a prime number (divisible only by 1 and itself). Print True if prime, or False otherwise.",
        expected: "29 is Prime: True",
        py: `# Question: Check if a Number is Prime\nnum = 29\nis_prime = True\n\n# TODO: Write your loop and conditions below to check if num is prime:\n\n\nprint(f"{num} is Prime: {is_prime}")\n`,
        java: `public class Main {\n    public static void main(String[] args) {\n        int num = 29;\n        boolean isPrime = true;\n        \n        // TODO: Write your loop and conditions below to check if num is prime:\n        \n        \n        System.out.println(num + " is Prime: " + isPrime);\n    }\n}\n`
      },
      vowels: {
        title: "Count Vowels in a String",
        desc: "Given a string text = 'Interactive Problem Solving', count the total number of vowels (a, e, i, o, u, case-insensitive) in the string.",
        expected: "Vowel Count: 9",
        py: `# Question: Count Vowels in a String\ntext = "Interactive Problem Solving"\nvowels = "aeiouAEIOU"\ncount = 0\n\n# TODO: Write your code below to count vowels:\n\n\nprint(f"Vowel Count: {count}")\n`,
        java: `public class Main {\n    public static void main(String[] args) {\n        String text = "Interactive Problem Solving";\n        int count = 0;\n        \n        // TODO: Write your code below to count vowels:\n        \n        \n        System.out.println("Vowel Count: " + count);\n    }\n}\n`
      },
      second_largest: {
        title: "Find Second Largest Element in Array",
        desc: "Given an unsorted array nums = [12, 35, 1, 10, 34, 1], find the second largest distinct value without using built-in sorting.",
        expected: "Second Largest: 34",
        py: `# Question: Find Second Largest Element\nnums = [12, 35, 1, 10, 34, 1]\nsecond_largest = -1\n\n# TODO: Write your code below to find second largest:\n\n\nprint(f"Second Largest: {second_largest}")\n`,
        java: `public class Main {\n    public static void main(String[] args) {\n        int[] nums = {12, 35, 1, 10, 34, 1};\n        int secondLargest = -1;\n        \n        // TODO: Write your code below to find second largest:\n        \n        \n        System.out.println("Second Largest: " + secondLargest);\n    }\n}\n`
      }
    };

    const s = samples[sampleKey] || samples.prime;
    const titleInput = document.getElementById("customInputTitle");
    const expInput = document.getElementById("customInputExpected");
    const descInput = document.getElementById("customInputDesc");
    if (titleInput) titleInput.value = s.title;
    if (expInput) expInput.value = s.expected;
    if (descInput) descInput.value = s.desc;

    document.getElementById("editorTitle").textContent = s.title;
    const starterCode = this.activeLanguage === "java" ? s.java : s.py;
    EditorManager.starterTemplate = starterCode;
    EditorManager.setCode(starterCode, this.activeLanguage);
    HintManager.reset();
    this.resetDiagnosticView();
    this.showToast(`Loaded Sample: ${s.title}`);
  },

  clearCustomQuestionForm() {
    const titleInput = document.getElementById("customInputTitle");
    const expInput = document.getElementById("customInputExpected");
    const descInput = document.getElementById("customInputDesc");
    if (titleInput) titleInput.value = "";
    if (expInput) expInput.value = "";
    if (descInput) descInput.value = "";
    EditorManager.clearCode();
    this.showToast("Custom Question Form Cleared.");
  },

  resetDiagnosticView() {
    const errorBanner = document.getElementById("errorBannerContainer");
    if (errorBanner) {
      errorBanner.innerHTML = `
        <div class="error-banner" style="background: rgba(255,255,255,0.03); border-color: rgba(255,255,255,0.08);">
          <div class="error-icon" style="color: var(--text-dim);"><i class="fa-solid fa-code"></i></div>
          <div class="error-meta">
            <div class="error-type-title" style="color: var(--text-main);">Ready to Run</div>
            <div class="error-desc">Click 'Run & Diagnose' to execute the code and identify the bug.</div>
          </div>
        </div>
      `;
    }

    const causeContainer = document.getElementById("causeBreakdownContainer");
    if (causeContainer) causeContainer.innerHTML = "";

    VisualizerEngine.render(null, document.getElementById("visualizerContainer"));
    this.switchSuiteTab("diagnostic");
  },

  switchSuiteTab(tabId) {
    document.querySelectorAll(".suite-tab").forEach((tab) => {
      tab.classList.toggle("active", tab.getAttribute("data-tab") === tabId);
    });
    document.querySelectorAll(".tab-panel").forEach((panel) => {
      panel.classList.toggle("active", panel.id === `tab-${tabId}`);
    });
  },

  renderErrorBanner(parsedError, execTimeMs, res = null) {
    const banner = document.getElementById("errorBannerContainer");
    if (!banner) return;

    const expected = (res && res.computed_expected) 
      ? res.computed_expected 
      : (this.currentProblem ? (this.currentProblem.expected_output || "") : "");
    const actual = (res && res.computed_actual !== undefined) ? res.computed_actual : "";

    banner.innerHTML = `
      <div class="error-banner">
        <div class="error-icon"><i class="fa-solid fa-triangle-exclamation"></i></div>
        <div class="error-meta" style="width: 100%;">
          <div style="display: flex; justify-content: space-between; align-items: center;">
            <div class="error-type-title">
              ${parsedError.error_type}
              ${parsedError.line_number ? `<span class="error-line-badge"><i class="fa-solid fa-location-crosshairs"></i> Line ${parsedError.line_number}</span>` : ''}
            </div>
            <span style="font-size: 0.72rem; color: var(--text-dim);">${execTimeMs}ms</span>
          </div>
          <div class="error-desc" style="margin-bottom: 8px;">${parsedError.message || "Something went wrong on the highlighted line."}</div>

          <!-- Expected Output vs Output You Got Comparison Grid -->
          ${expected ? `
            <div class="output-comparison-grid">
              <div class="output-box-wrapper expected">
                <div class="output-box-title" style="color: #38bdf8;">
                  <span><i class="fa-solid fa-bullseye"></i> Expected Output:</span>
                </div>
                <pre class="output-box-content">${expected.trim()}</pre>
              </div>
              <div class="output-box-wrapper actual-fail">
                <div class="output-box-title" style="color: #f87171;">
                  <span><i class="fa-solid fa-terminal"></i> Output You Got:</span>
                  <span style="background: rgba(248,113,113,0.25); padding: 1px 6px; border-radius: 4px; font-size: 0.68rem; color: #fca5a5;">MISMATCH ❌</span>
                </div>
                <pre class="output-box-content" style="color: #fca5a5;">${actual.trim() ? actual.trim() : '[Empty - No output was printed]'}</pre>
              </div>
            </div>
          ` : ''}
        </div>
      </div>
    `;
  },

  // SUPER SIMPLE, NON-TECHNICAL CAUSE BREAKDOWN
  async fetchCauseBreakdown(parsedError) {
    const container = document.getElementById("causeBreakdownContainer");
    if (!container) return;

    container.innerHTML = `
      <div style="text-align: center; padding: 20px; color: var(--text-dim);">
        <i class="fa-solid fa-spinner fa-spin"></i> Breaking down the mistake in simple words...
      </div>
    `;

    try {
      const code = EditorManager.getCode();
      const lang = EditorManager.currentLanguage;
      const qId = this.currentProblem ? this.currentProblem.id : null;
      const userKey = localStorage.getItem("codesense_groq_key") || null;
      const customTitle = this.isCustomMode ? (document.getElementById("customInputTitle")?.value || "") : "";
      const customDesc = this.isCustomMode ? (document.getElementById("customInputDesc")?.value || "") : "";

      const res = await fetch("/api/explain-cause", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          code: code,
          language: lang,
          error_message: parsedError.message,
          error_type: parsedError.error_type,
          line_number: parsedError.line_number,
          question_id: qId,
          user_api_key: userKey,
          custom_title: customTitle,
          custom_description: customDesc
        })
      });

      const cause = await res.json();

      container.innerHTML = `
        <div class="comparison-grid">
          <!-- 1. What you were trying to do -->
          <div class="cause-card intent">
            <div class="cause-card-header"><i class="fa-solid fa-user"></i> What you were trying to do</div>
            <div class="cause-card-text">${cause.programmer_intent}</div>
          </div>

          <!-- 2. What the computer actually did -->
          <div class="cause-card execution">
            <div class="cause-card-header"><i class="fa-solid fa-robot"></i> What the computer actually did</div>
            <div class="cause-card-text">${cause.actual_execution}</div>
          </div>

          <!-- 3. Why it got confused / broke -->
          <div class="cause-card divergence">
            <div class="cause-card-header"><i class="fa-solid fa-bolt"></i> Why it got confused & broke</div>
            <div class="cause-card-text">${cause.divergence_gap}</div>
          </div>

          <!-- 4. Everyday Real-Life Analogy -->
          <div class="cause-card analogy">
            <div class="cause-card-header"><i class="fa-solid fa-lightbulb"></i> Real-Life Analogy</div>
            <div class="cause-card-text">${cause.mental_model_analogy}</div>
          </div>

          <!-- 5. Golden Rule to Remember -->
          <div class="cause-card prevention">
            <div class="cause-card-header"><i class="fa-solid fa-shield-halved"></i> Golden Rule for Life</div>
            <div class="cause-card-text">${cause.prevention_tip}</div>
          </div>
        </div>
      `;
    } catch (e) {
      console.error(e);
      container.innerHTML = `<div style="color: var(--text-dim);">Could not fetch simple explanation.</div>`;
    }
  },

  async onProblemSolved(res) {
    const expected = (res && res.computed_expected) 
      ? res.computed_expected 
      : (this.currentProblem ? (this.currentProblem.expected_output || "") : "");
    const actual = (res && res.computed_actual !== undefined) ? res.computed_actual : "";

    if (this.isCustomMode) {
      this.showToast("🎉 Awesome Job! Custom Question Solved!");
      this.launchConfetti();
      const banner = document.getElementById("errorBannerContainer");
      if (banner) {
        banner.innerHTML = `
          <div class="error-banner success">
            <div class="error-icon"><i class="fa-solid fa-circle-check"></i></div>
            <div class="error-meta" style="width: 100%;">
              <div class="error-type-title">Awesome Job! Custom Problem Solved! 🎉</div>
              <div class="error-desc" style="margin-bottom: 8px;">Your code executed cleanly and successfully matched your expected goal!</div>
              ${expected ? `
                <div class="output-comparison-grid">
                  <div class="output-box-wrapper expected">
                    <div class="output-box-title" style="color: #38bdf8;"><i class="fa-solid fa-bullseye"></i> Expected Output</div>
                    <pre class="output-box-content">${expected.trim()}</pre>
                  </div>
                  <div class="output-box-wrapper actual-pass">
                    <div class="output-box-title" style="color: #4ade80;"><span><i class="fa-solid fa-terminal"></i> Output You Got</span> <span style="background: rgba(74,222,128,0.25); padding: 1px 6px; border-radius: 4px; font-size: 0.68rem; color: #86efac;">MATCH ✅</span></div>
                    <pre class="output-box-content" style="color: #86efac;">${actual.trim() ? actual.trim() : '[Output matched target]'}</pre>
                  </div>
                </div>
              ` : ''}
            </div>
          </div>
        `;
      }
      return;
    }

    this.showToast("🎉 Problem Solved! All Tests Passed!");
    this.launchConfetti();

    // Render success banner with Expected and Actual output comparison
    const banner = document.getElementById("errorBannerContainer");
    if (banner) {
      banner.innerHTML = `
        <div class="error-banner success">
          <div class="error-icon"><i class="fa-solid fa-circle-check"></i></div>
          <div class="error-meta" style="width: 100%;">
            <div class="error-type-title">Awesome Job! Problem Solved!</div>
            <div class="error-desc" style="margin-bottom: 8px;">Your code executed cleanly and produced the exact expected output.</div>
            ${expected ? `
              <div class="output-comparison-grid">
                <div class="output-box-wrapper expected">
                  <div class="output-box-title" style="color: #38bdf8;"><i class="fa-solid fa-bullseye"></i> Expected Output</div>
                  <pre class="output-box-content">${expected.trim()}</pre>
                </div>
                <div class="output-box-wrapper actual-pass">
                  <div class="output-box-title" style="color: #4ade80;"><span><i class="fa-solid fa-terminal"></i> Output You Got</span> <span style="background: rgba(74,222,128,0.25); padding: 1px 6px; border-radius: 4px; font-size: 0.68rem; color: #86efac;">MATCH ✅</span></div>
                  <pre class="output-box-content" style="color: #86efac;">${actual.trim() ? actual.trim() : '[Output matched target]'}</pre>
                </div>
              </div>
            ` : ''}
          </div>
        </div>
      `;
    }

    // Record solved attempt in database for active user
    if (this.currentProblem) {
      try {
        await fetch("/api/record-attempt", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            question_id: this.currentProblem.id,
            language: EditorManager.currentLanguage,
            solved: true,
            hints_used: HintManager.currentTier,
            attempts_count: EditorManager.attemptsCount,
            error_type: "None",
            code: EditorManager.getCode(),
            user_id: this.currentUserId || "student_1"
          })
        });
        await this.fetchUserProgress();
        await this.updateProfileStats();
      } catch (err) {
        console.error(err);
      }
    }

    // Prepare Transfer Challenge
    await this.prepareTransferChallenge();
  },

  async prepareTransferChallenge() {
    const qId = this.currentProblem ? this.currentProblem.id : null;
    const bugCat = this.currentProblem ? this.currentProblem.bug_category : "OffByOne";
    const lang = EditorManager.currentLanguage;
    const userKey = localStorage.getItem("codesense_groq_key") || null;

    try {
      const res = await fetch("/api/transfer-challenge", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          question_id: qId,
          bug_category: bugCat,
          language: lang,
          user_api_key: userKey
        })
      });

      const tc = await res.json();
      this.transferChallengeData = tc;

      const container = document.getElementById("transferChallengeContainer");
      if (container) {
        // Calculate next level button
        const currLvl = this.currentProblem ? (this.currentProblem.level || 1) : 1;
        const nextLvl = currLvl + 1;
        const hasNext = nextLvl <= 10;

        container.innerHTML = `
          <div class="visualizer-card" style="border-color: rgba(16, 185, 129, 0.4);">
            <div class="visualizer-header">
              <span class="vis-title" style="color: #34d399;">
                <i class="fa-solid fa-graduation-cap"></i> Practice & Prove Mastery
              </span>
              <span class="vis-type-pill" style="background: rgba(16, 185, 129, 0.2); color: #6ee7b7;">Unlocked</span>
            </div>

            <div style="font-size: 1rem; font-weight: 700;">${tc.title}</div>
            <div style="font-size: 0.82rem; color: #38bdf8;"><i class="fa-solid fa-building"></i> ${tc.scenario}</div>
            <p style="font-size: 0.88rem; color: var(--text-main); line-height: 1.5;">${tc.description}</p>

            <div style="background: #0d111c; border-radius: 8px; padding: 12px; font-family: var(--font-mono); font-size: 0.82rem; color: #cbd5e1; white-space: pre-wrap;">
${tc.buggy_code}
            </div>

            <div style="font-size: 0.82rem; color: var(--text-dim);">
              <i class="fa-solid fa-lightbulb" style="color: var(--accent-amber);"></i> Quick Clue: ${tc.hint}
            </div>

            <div style="display: flex; gap: 10px; margin-top: 10px;">
              <button class="btn-primary" onclick="App.loadTransferChallengeToEditor()">
                <i class="fa-solid fa-pencil"></i> Try Practice Challenge
              </button>
              ${
                hasNext
                  ? `<button class="btn-secondary" onclick="App.goToNextLevel(${nextLvl})">Next Level ${nextLvl} <i class="fa-solid fa-arrow-right"></i></button>`
                  : ''
              }
            </div>
          </div>
        `;
      }

      this.switchSuiteTab("transfer");
    } catch (e) {
      console.error(e);
    }
  },

  goToNextLevel(nextLvl) {
    if (!this.currentTopic) return;
    const prefix = this.activeLanguage === "java" ? "java" : "py";
    const topicPrefix = this.currentTopic.id.substring(0, 4);
    const nextId = `${prefix}-${topicPrefix}-${String(nextLvl).padStart(2, '0')}`;
    this.selectProblem(nextId);
  },

  loadTransferChallengeToEditor() {
    if (!this.transferChallengeData) return;
    const tc = this.transferChallengeData;
    const starter = tc.language === "python"
      ? `# Practice Challenge: ${tc.title}\n# Scenario: ${tc.scenario}\n# Task: ${tc.description}\n\n# TODO: Write your solution below from scratch:\n\n`
      : `// Practice Challenge: ${tc.title}\n// Scenario: ${tc.scenario}\n// Task: ${tc.description}\n\npublic class Main {\n    public static void main(String[] args) {\n        // TODO: Write your solution below from scratch:\n        \n    }\n}\n`;
    EditorManager.setCode(starter, tc.language);
    HintManager.reset();

    document.getElementById("editorTitle").textContent = tc.title;
    document.getElementById("scenarioTag").textContent = "Practice Challenge";
    document.getElementById("scenarioDescription").textContent = tc.scenario + " — " + tc.description;
    document.getElementById("expectedOutputText").textContent = tc.expected_output;

    this.resetDiagnosticView();
    this.showToast("Practice challenge loaded into editor! Code it from scratch.");
  },

  async updateProfileStats() {
    try {
      const res = await fetch(`/api/profile?user_id=${encodeURIComponent(this.currentUserId || 'student_1')}`);
      const profile = await res.json();

      const streakEl = document.getElementById("userStreak");
      if (streakEl) streakEl.textContent = profile.streak_days;

      this.updateIndependenceBadge(profile.overall_independence_score);
    } catch (e) {
      console.error(e);
    }
  },

  updateIndependenceBadge(score) {
    const indEl = document.getElementById("independenceScore");
    if (indEl) indEl.textContent = `${Math.round(score)}%`;
  },

  async openAnalyticsModal() {
    const modal = document.getElementById("analyticsModal");
    if (!modal) return;
    modal.classList.add("open");

    try {
      const res = await fetch(`/api/profile?user_id=${encodeURIComponent(this.currentUserId || 'student_1')}`);
      const p = await res.json();

      // Top 5 Key Metrics
      const metricSolved = document.getElementById("metricSolved");
      if (metricSolved) metricSolved.textContent = p.total_solved;

      const metricAttempts = document.getElementById("metricAttempts");
      if (metricAttempts) metricAttempts.textContent = p.total_attempts;

      const metricAccuracy = document.getElementById("metricAccuracy");
      if (metricAccuracy) metricAccuracy.textContent = `${p.accuracy_rate || 100}%`;

      const metricIndependence = document.getElementById("metricIndependence");
      if (metricIndependence) metricIndependence.textContent = `${Math.round(p.overall_independence_score)}%`;

      const metricStreak = document.getElementById("metricStreak");
      if (metricStreak) metricStreak.textContent = `${p.streak_days} Days`;

      // Learner Tier Badge
      const tierBadge = document.getElementById("analyticsTierBadge");
      if (tierBadge) {
        tierBadge.textContent = p.independence_tier || "Autonomous Coder 🏆";
      }

      // Language Mastery Breakdown
      const pySolved = document.getElementById("metricPySolved");
      if (pySolved) pySolved.textContent = `${p.python_solved || 0} Challenges`;

      const javaSolved = document.getElementById("metricJavaSolved");
      if (javaSolved) javaSolved.textContent = `${p.java_solved || 0} Challenges`;

      const noHintsSolved = document.getElementById("metricNoHintsSolved");
      if (noHintsSolved) noHintsSolved.textContent = `${p.no_hints_solved || 0} Challenges`;

      // Recommended Practice Focus
      const recEl = document.getElementById("analyticsRecommendation");
      if (recEl) {
        recEl.textContent = p.recommended_focus || "Keep practicing progressive problems to build autonomous algorithmic problem-solving habits!";
      }

      // Styled Bug Vulnerability Radar Bars
      const radarList = document.getElementById("errorRadarList");
      if (radarList) {
        const errors = Object.entries(p.error_radar || {});
        const maxVal = Math.max(...errors.map(([, c]) => c), 1);
        let rows = "";
        for (const [err, count] of errors) {
          const pct = Math.round((count / maxVal) * 100);
          rows += `
            <div style="margin-bottom: 6px;">
              <div style="display: flex; justify-content: space-between; font-size: 0.76rem; margin-bottom: 3px;">
                <span style="font-family: var(--font-mono); color: #cbd5e1;">${err}</span>
                <span style="font-weight: 700; color: #f87171;">${count}</span>
              </div>
              <div style="width: 100%; height: 6px; background: rgba(255,255,255,0.08); border-radius: 4px; overflow: hidden;">
                <div style="width: ${pct}%; height: 100%; background: linear-gradient(90deg, #f43f5e, #fb7185); border-radius: 4px;"></div>
              </div>
            </div>
          `;
        }
        radarList.innerHTML = rows;
      }

      // Recent Practice Activity Table
      const activityList = document.getElementById("recentActivityList");
      if (activityList) {
        if (!p.recent_attempts || p.recent_attempts.length === 0) {
          activityList.innerHTML = `<div style="color: var(--text-dim); text-align: center; padding: 10px;">No recent runs recorded yet. Start practicing!</div>`;
        } else {
          let rows = `
            <div style="display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; font-size: 0.72rem; color: var(--text-dim); text-transform: uppercase; font-weight: 700; padding-bottom: 6px; border-bottom: 1px solid rgba(255,255,255,0.08); margin-bottom: 6px;">
              <span>Problem / Task</span>
              <span>Language</span>
              <span>Outcome</span>
              <span>Clues Used</span>
            </div>
          `;
          p.recent_attempts.forEach((a) => {
            const isSolved = a.solved === 1;
            const langIcon = a.language === "java" ? "☕ Java" : "🐍 Python";
            rows += `
              <div style="display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; align-items: center; padding: 5px 0; border-bottom: 1px solid rgba(255,255,255,0.04); font-size: 0.76rem;">
                <span style="font-family: var(--font-mono); color: #e2e8f0;">${a.question_id}</span>
                <span style="color: #94a3b8;">${langIcon}</span>
                <span style="font-weight: 600; color: ${isSolved ? '#34d399' : '#f87171'};">
                  ${isSolved ? '<i class="fa-solid fa-circle-check"></i> Solved' : `<i class="fa-solid fa-circle-xmark"></i> ${a.error_type || 'Error'}`}
                </span>
                <span style="color: var(--text-muted);">${a.hints_used || 0} clues</span>
              </div>
            `;
          });
          activityList.innerHTML = rows;
        }
      }
    } catch (e) {
      console.error(e);
    }
  },

  closeAnalyticsModal() {
    const modal = document.getElementById("analyticsModal");
    if (modal) modal.classList.remove("open");
  },

  openSettingsModal() {
    const modal = document.getElementById("settingsModal");
    if (!modal) return;
    modal.classList.add("open");

    const input = document.getElementById("inputGroqKey");
    if (input) {
      input.value = localStorage.getItem("codesense_groq_key") || "";
    }
  },

  closeSettingsModal() {
    const modal = document.getElementById("settingsModal");
    if (modal) modal.classList.remove("open");
  },

  async saveGroqKey() {
    const input = document.getElementById("inputGroqKey");
    const val = input ? input.value.trim() : "";
    localStorage.setItem("codesense_groq_key", val);

    const statusEl = document.getElementById("groqStatusMsg");
    if (!val) {
      if (statusEl) statusEl.textContent = "API key cleared. CodeSense will use built-in curriculum heuristics.";
      this.showToast("Groq Key Cleared");
      return;
    }

    if (statusEl) statusEl.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Verifying with Groq...';
    try {
      const res = await fetch("/api/settings/verify-groq", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ api_key: val })
      });
      const data = await res.json();
      if (data.valid) {
        if (statusEl) statusEl.innerHTML = `<span style="color: #34d399;"><i class="fa-solid fa-circle-check"></i> ${data.message}</span>`;
        this.showToast("Groq API Connected!");
      } else {
        if (statusEl) statusEl.innerHTML = `<span style="color: #f87171;"><i class="fa-solid fa-circle-xmark"></i> ${data.message}</span>`;
      }
    } catch (e) {
      if (statusEl) statusEl.textContent = "Verification request failed.";
    }
  },

  showToast(msg) {
    const container = document.getElementById("toastContainer");
    if (!container) return;
    const toast = document.createElement("div");
    toast.className = "toast";
    toast.innerHTML = `<i class="fa-solid fa-bell" style="color: var(--accent-cyan); margin-right: 8px;"></i> ${msg}`;
    container.appendChild(toast);
    setTimeout(() => {
      toast.style.opacity = "0";
      setTimeout(() => toast.remove(), 300);
    }, 3200);
  },

  launchConfetti() {
    const colors = ["#06b6d4", "#8b5cf6", "#10b981", "#f59e0b", "#f43f5e"];
    for (let i = 0; i < 40; i++) {
      const conf = document.createElement("div");
      conf.style.position = "fixed";
      conf.style.width = `${Math.random() * 8 + 6}px`;
      conf.style.height = `${Math.random() * 12 + 8}px`;
      conf.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
      conf.style.left = `${Math.random() * 80 + 10}vw`;
      conf.style.top = "-20px";
      conf.style.zIndex = "9999";
      conf.style.borderRadius = "2px";
      conf.style.pointerEvents = "none";
      conf.style.transform = `rotate(${Math.random() * 360}deg)`;
      document.body.appendChild(conf);

      const anim = conf.animate(
        [
          { transform: `translate(0, 0) rotate(0deg)`, opacity: 1 },
          {
            transform: `translate(${(Math.random() - 0.5) * 200}px, ${window.innerHeight + 50}px) rotate(${Math.random() * 720}deg)`,
            opacity: 0
          }
        ],
        { duration: Math.random() * 1500 + 1500, easing: "cubic-bezier(0.25, 1, 0.5, 1)" }
      );
      anim.onfinish = () => conf.remove();
    }
  },

  // ========================================================
  // USER AUTHENTICATION & SESSION MANAGEMENT
  // ========================================================
  updateAuthUI() {
    const loggedOutPill = document.getElementById("loggedOutPill");
    const loggedInPill = document.getElementById("loggedInPill");
    const navUsername = document.getElementById("navUsername");

    if (this.currentUser) {
      if (loggedOutPill) loggedOutPill.style.display = "none";
      if (loggedInPill) loggedInPill.style.display = "flex";
      if (navUsername) navUsername.textContent = this.currentUser.username;
    } else {
      if (loggedOutPill) loggedOutPill.style.display = "flex";
      if (loggedInPill) loggedInPill.style.display = "none";
    }
  },

  openAuthModal(tab = "login") {
    const modal = document.getElementById("authModal");
    if (!modal) return;
    this.switchAuthTab(tab);
    modal.classList.add("active");
  },

  closeAuthModal() {
    const modal = document.getElementById("authModal");
    if (modal) modal.classList.remove("active");
    const statusMsg = document.getElementById("authStatusMsg");
    if (statusMsg) statusMsg.style.display = "none";
  },

  switchAuthTab(tab) {
    const tabLogin = document.getElementById("authTabLogin");
    const tabRegister = document.getElementById("authTabRegister");
    const loginForm = document.getElementById("loginForm");
    const registerForm = document.getElementById("registerForm");
    const statusMsg = document.getElementById("authStatusMsg");
    const modalTitle = document.getElementById("authModalTitle");
    if (statusMsg) statusMsg.style.display = "none";

    if (tab === "login") {
      if (tabLogin) { tabLogin.style.background = "#6366f1"; tabLogin.style.color = "white"; }
      if (tabRegister) { tabRegister.style.background = "transparent"; tabRegister.style.color = "#94a3b8"; }
      if (loginForm) loginForm.style.display = "block";
      if (registerForm) registerForm.style.display = "none";
      if (modalTitle) modalTitle.textContent = "Log In to CodeSense";
    } else {
      if (tabRegister) { tabRegister.style.background = "#10b981"; tabRegister.style.color = "white"; }
      if (tabLogin) { tabLogin.style.background = "transparent"; tabLogin.style.color = "#94a3b8"; }
      if (loginForm) loginForm.style.display = "none";
      if (registerForm) registerForm.style.display = "block";
      if (modalTitle) modalTitle.textContent = "Create Free Account";
    }
  },

  async handleLogin(e) {
    e.preventDefault();
    const identifier = document.getElementById("loginIdentifier").value.trim();
    const password = document.getElementById("loginPassword").value;
    const statusMsg = document.getElementById("authStatusMsg");
    const submitBtn = document.getElementById("btnLoginSubmit");

    submitBtn.disabled = true;
    submitBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Logging in...';

    try {
      const res = await fetch("/api/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ identifier, password })
      });
      const data = await res.json();

      if (data.success && data.user) {
        this.currentUser = data.user;
        this.currentUserId = data.user.username;
        localStorage.setItem("codesense_user", JSON.stringify(data.user));
        this.updateAuthUI();
        this.closeAuthModal();
        this.showToast(`Welcome back, ${data.user.username}!`);
        await this.fetchUserProgress();
        await this.updateProfileStats();
        if (this.currentTopic) {
          this.showTopicQuestionsView(this.currentTopic.id);
        }
      } else {
        statusMsg.style.display = "block";
        statusMsg.style.background = "rgba(239, 68, 68, 0.15)";
        statusMsg.style.border = "1px solid rgba(239, 68, 68, 0.3)";
        statusMsg.style.color = "#fca5a5";
        statusMsg.textContent = data.message || "Login failed. Check your credentials.";
      }
    } catch (err) {
      statusMsg.style.display = "block";
      statusMsg.textContent = "Network error. Please try again.";
    } finally {
      submitBtn.disabled = false;
      submitBtn.innerHTML = '<i class="fa-solid fa-arrow-right-to-bracket"></i> Log In to CodeSense';
    }
  },

  async handleRegister(e) {
    e.preventDefault();
    const username = document.getElementById("regUsername").value.trim();
    const email = document.getElementById("regEmail").value.trim();
    const password = document.getElementById("regPassword").value;
    const statusMsg = document.getElementById("authStatusMsg");
    const submitBtn = document.getElementById("btnRegisterSubmit");

    submitBtn.disabled = true;
    submitBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Creating Account...';

    try {
      const res = await fetch("/api/auth/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, email, password })
      });
      const data = await res.json();

      if (data.success && data.user) {
        this.currentUser = data.user;
        this.currentUserId = data.user.username;
        localStorage.setItem("codesense_user", JSON.stringify(data.user));
        this.updateAuthUI();
        this.closeAuthModal();
        this.showToast(`Account created! Welcome, ${data.user.username}! 🎉`);
        await this.fetchUserProgress();
        await this.updateProfileStats();
      } else {
        statusMsg.style.display = "block";
        statusMsg.style.background = "rgba(239, 68, 68, 0.15)";
        statusMsg.style.border = "1px solid rgba(239, 68, 68, 0.3)";
        statusMsg.style.color = "#fca5a5";
        statusMsg.textContent = data.message || "Failed to create account.";
      }
    } catch (err) {
      statusMsg.style.display = "block";
      statusMsg.textContent = "Network error. Please try again.";
    } finally {
      submitBtn.disabled = false;
      submitBtn.innerHTML = '<i class="fa-solid fa-user-plus"></i> Create Free Account';
    }
  },

  logout() {
    this.currentUser = null;
    this.currentUserId = "student_1";
    localStorage.removeItem("codesense_user");
    this.updateAuthUI();
    this.showToast("Logged out successfully.");
    this.fetchUserProgress();
    this.updateProfileStats();
    if (this.currentTopic) {
      this.showTopicQuestionsView(this.currentTopic.id);
    }
  },

  async fetchUserProgress() {
    try {
      const res = await fetch(`/api/user-progress?user_id=${encodeURIComponent(this.currentUserId || 'student_1')}&language=${this.activeLanguage}`);
      const data = await res.json();
      this.solvedProblemsMap = data.solved_problems || {};
    } catch (e) {
      console.error("Failed to fetch progress:", e);
      this.solvedProblemsMap = {};
    }
  },

  resetToStarterCode() {
    if (this.currentProblem) {
      EditorManager.setCode(this.currentProblem.starter_code, this.currentProblem.language);
      this.showToast("Reset to starter code template.");
    }
  }
};

window.addEventListener("DOMContentLoaded", () => App.init());
