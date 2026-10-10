/**
 * Simplified Clues & Independence Engine - CodeSense
 * Friendly 3-Tier Clues:
 * Clue 1: Where to Look 🔍
 * Clue 2: The Simple Concept 💡
 * Clue 3: How to Fix It 🎯
 */

const HintManager = {
  currentTier: 0,
  hintsUnlocked: [],
  currentIndependenceScore: 100,

  reset() {
    this.currentTier = 0;
    this.hintsUnlocked = [];
    this.render();
  },

  async requestNextHint() {
    const nextTier = this.currentTier + 1;
    if (nextTier > 3) {
      App.showToast("All 3 clues are already unlocked!");
      return;
    }

    const penalties = { 1: 5, 2: 15, 3: 30 };
    const clueNames = {
      1: "Clue 1: What Went Wrong in Logic 🧩",
      2: "Clue 2: The Core Rule & Principle 💡",
      3: "Clue 3: Exact Logical Fix & What to Change 🛠️"
    };

    const confirmed = confirm(
      `Unlocking ${clueNames[nextTier]} will cost ${penalties[nextTier]} Independence Points.\n\nTake a quick look at the code logic first!\n\nDo you want to reveal this clue?`
    );
    if (!confirmed) return;

    try {
      const code = EditorManager.getCode();
      const lang = EditorManager.currentLanguage;
      const qId = App.currentProblem ? App.currentProblem.id : null;
      const userKey = localStorage.getItem("codesense_groq_key") || null;
      const customTitle = App.isCustomMode ? (document.getElementById("customInputTitle")?.value || "") : "";
      const customDesc = App.isCustomMode ? (document.getElementById("customInputDesc")?.value || "") : "";

      const res = await fetch("/api/hint", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          code: code,
          language: lang,
          hint_level: nextTier,
          question_id: qId,
          user_api_key: userKey,
          custom_title: customTitle,
          custom_description: customDesc
        })
      });

      const data = await res.json();
      this.currentTier = nextTier;
      this.hintsUnlocked.push(data);
      this.currentIndependenceScore = Math.max(10, this.currentIndependenceScore - penalties[nextTier]);
      App.updateIndependenceBadge(this.currentIndependenceScore);
      this.render();
      App.showToast(`Unlocked ${clueNames[nextTier]}`);
    } catch (e) {
      console.error(e);
      App.showToast("Failed to fetch clue.");
    }
  },

  render() {
    const container = document.getElementById("hintsContainer");
    if (!container) return;

    const tierMeta = [
      { tier: 1, name: "What Went Wrong in Logic 🧩", tag: "Clue 1", cost: "-5 pts" },
      { tier: 2, name: "The Core Rule & Principle 💡", tag: "Clue 2", cost: "-15 pts" },
      { tier: 3, name: "Exact Logical Fix & What to Change 🛠️", tag: "Clue 3", cost: "-30 pts" }
    ];

    let html = `
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
        <span style="font-size: 0.85rem; color: var(--text-muted);">
          Problem Independence: <strong style="color: var(--accent-emerald);">${this.currentIndependenceScore}%</strong>
        </span>
        <span style="font-size: 0.75rem; color: var(--text-dim);">${this.currentTier}/3 Clues Revealed</span>
      </div>
    `;

    tierMeta.forEach((meta) => {
      const isUnlocked = this.currentTier >= meta.tier;
      const hintData = this.hintsUnlocked.find((h) => h.hint_level === meta.tier);

      html += `
        <div class="hint-card ${isUnlocked ? 'unlocked' : 'locked'}">
          <div class="hint-card-header">
            <div class="hint-header-left">
              <span class="hint-tier-tag">${meta.tag}</span>
              <span class="hint-title-text">${isUnlocked && hintData ? hintData.title : meta.name}</span>
            </div>
            <span class="hint-penalty-badge">
              ${isUnlocked ? '<i class="fa-solid fa-lock-open" style="color: #a78bfa;"></i> Revealed' : `<i class="fa-solid fa-lock"></i> ${meta.cost}`}
            </span>
          </div>
          ${
            isUnlocked && hintData
              ? `<div class="hint-card-body">${hintData.hint_text.replace(/\n/g, '<br>')}</div>`
              : ''
          }
        </div>
      `;
    });

    if (this.currentTier < 3) {
      html += `
        <div class="hint-unlock-cta" style="margin-top: 14px;">
          <button class="btn-primary" style="margin: 0 auto;" onclick="HintManager.requestNextHint()">
            <i class="fa-solid fa-key"></i> Reveal Clue ${this.currentTier + 1}
          </button>
          <p style="font-size: 0.75rem; color: var(--text-dim); margin-top: 8px;">
            Hint-first rule: Read each simple clue before unlocking the next one!
          </p>
        </div>
      `;
    }

    container.innerHTML = html;
  }
};
