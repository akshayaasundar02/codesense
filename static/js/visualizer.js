/**
 * Visual Bug Explorer - CodeSense
 * Renders interactive state representations: Array Bounds, Loop Stepper, Call Stack, Tree Pointer
 */

const VisualizerEngine = {
  currentLoopStep: 0,
  loopStepsData: null,
  loopTimer: null,

  render(visualData, containerElement) {
    if (!containerElement) return;
    containerElement.innerHTML = "";

    if (!visualData || !visualData.data) {
      containerElement.innerHTML = `
        <div style="text-align: center; padding: 30px; color: var(--text-dim);">
          <i class="fa-solid fa-microchip" style="font-size: 2rem; margin-bottom: 10px; opacity: 0.5;"></i>
          <p>Run code to inspect runtime memory states and visual invariants.</p>
        </div>
      `;
      return;
    }

    const { visual_type, data } = visualData;

    switch (visual_type) {
      case "array_bounds":
        this.renderArrayBounds(data, containerElement);
        break;
      case "loop_trace":
        this.renderLoopStepper(data, containerElement);
        break;
      case "stack":
        this.renderStackFrames(data, containerElement);
        break;
      case "tree":
        this.renderTreePointers(data, containerElement);
        break;
      case "variable_state":
      default:
        this.renderVariableState(data, containerElement);
        break;
    }
  },

  renderArrayBounds(data, container) {
    const arrName = data.array_name || "collection";
    const elements = data.elements || [1, 2, 3, 4, 5];
    const length = data.length || elements.length;
    const attemptedIndex = data.attempted_index !== undefined ? data.attempted_index : length;
    const isOutOfBounds = data.is_out_of_bounds ?? true;

    let cellsHtml = "";
    // Display elements
    elements.forEach((val, idx) => {
      cellsHtml += `
        <div class="array-cell-wrapper">
          <div class="array-cell valid">${val}</div>
          <span class="array-idx-label">[${idx}]</span>
        </div>
      `;
    });

    // If attempted index is beyond array, render the crash cell!
    if (isOutOfBounds && attemptedIndex >= elements.length) {
      cellsHtml += `
        <div class="array-cell-wrapper">
          <i class="fa-solid fa-arrow-down pointer-arrow"></i>
          <div class="array-cell out-of-bounds-target">💥</div>
          <span class="array-idx-label target">[${attemptedIndex}] (INVALID)</span>
        </div>
      `;
    }

    container.innerHTML = `
      <div class="visualizer-card">
        <div class="visualizer-header">
          <span class="vis-title"><i class="fa-solid fa-table-cells"></i> Array Memory & Boundary Explorer</span>
          <span class="vis-type-pill">Index Bounds</span>
        </div>

        <div class="array-container">
          <span class="array-name-badge">Variable: <code>${arrName}</code> (Allocated Size: ${length})</span>
          <div class="array-cells-track">
            ${cellsHtml}
          </div>
        </div>

        <div class="bounds-summary-bar">
          <span class="bounds-valid-range"><i class="fa-solid fa-shield-halved"></i> Valid Range: 0 to ${length - 1}</span>
          <span class="bounds-invalid-attempt"><i class="fa-solid fa-triangle-exclamation"></i> Attempted Index: ${attemptedIndex}</span>
        </div>

        <div style="font-size: 0.82rem; color: var(--text-muted); line-height: 1.4; padding: 0 4px;">
          ${data.note || "Array indices are 0-based. Accessing index equal to or greater than array length triggers a boundary violation."}
        </div>
      </div>
    `;
  },

  renderLoopStepper(data, container) {
    this.loopStepsData = data.steps || [];
    this.currentLoopStep = 0;

    container.innerHTML = `
      <div class="visualizer-card">
        <div class="visualizer-header">
          <span class="vis-title"><i class="fa-solid fa-rotate"></i> Loop Iteration & Boundary Stepper</span>
          <span class="vis-type-pill">Trace Timeline</span>
        </div>

        <div class="loop-stepper-box">
          <div class="stepper-controls">
            <span class="step-indicator" id="loopStepIndicator">Step 1 of ${this.loopStepsData.length}</span>
            <div class="step-btn-group">
              <button class="step-btn" id="btnPrevStep"><i class="fa-solid fa-backward-step"></i> Prev</button>
              <button class="step-btn" id="btnPlayStep"><i class="fa-solid fa-play"></i> Auto</button>
              <button class="step-btn" id="btnNextStep">Next <i class="fa-solid fa-forward-step"></i></button>
            </div>
          </div>

          <div class="loop-step-details" id="loopStepDetails">
            <!-- Dynamic step contents rendered below -->
          </div>

          <div style="font-size: 0.8rem; color: var(--text-dim); display: flex; justify-content: space-between;">
            <span>Condition used: <code>${data.condition_used || 'i <= len'}</code></span>
            <span style="color: #34d399;">Safe condition: <code>${data.correct_condition || 'i < len'}</code></span>
          </div>
        </div>
      </div>
    `;

    document.getElementById("btnPrevStep").onclick = () => this.stepLoop(-1);
    document.getElementById("btnNextStep").onclick = () => this.stepLoop(1);
    document.getElementById("btnPlayStep").onclick = () => this.toggleAutoPlay();

    this.updateLoopStepView();
  },

  stepLoop(delta) {
    if (!this.loopStepsData || this.loopStepsData.length === 0) return;
    this.currentLoopStep = Math.max(0, Math.min(this.loopStepsData.length - 1, this.currentLoopStep + delta));
    this.updateLoopStepView();
  },

  toggleAutoPlay() {
    const playBtn = document.getElementById("btnPlayStep");
    if (this.loopTimer) {
      clearInterval(this.loopTimer);
      this.loopTimer = null;
      if (playBtn) playBtn.innerHTML = '<i class="fa-solid fa-play"></i> Auto';
    } else {
      if (this.currentLoopStep >= this.loopStepsData.length - 1) {
        this.currentLoopStep = 0;
      }
      if (playBtn) playBtn.innerHTML = '<i class="fa-solid fa-pause"></i> Pause';
      this.loopTimer = setInterval(() => {
        if (this.currentLoopStep < this.loopStepsData.length - 1) {
          this.stepLoop(1);
        } else {
          this.toggleAutoPlay();
        }
      }, 1200);
    }
  },

  updateLoopStepView() {
    const step = this.loopStepsData[this.currentLoopStep];
    const details = document.getElementById("loopStepDetails");
    const indicator = document.getElementById("loopStepIndicator");
    if (!step || !details) return;

    if (indicator) {
      indicator.textContent = `Step ${step.step} of ${this.loopStepsData.length}`;
    }

    const isCrash = step.is_error_step;
    details.innerHTML = `
      <div class="loop-step-condition">
        <span>Iteration Index: <strong>i = ${step.index_i}</strong></span>
        <span class="${isCrash ? 'cond-false' : 'cond-true'}">
          <i class="fa-solid ${isCrash ? 'fa-triangle-exclamation' : 'fa-circle-check'}"></i> ${step.condition}
        </span>
      </div>
      <div style="font-family: var(--font-mono); font-size: 0.85rem; color: ${isCrash ? '#f87171' : '#38bdf8'};">
        Accessed value: <strong>${step.accessed_value}</strong>
      </div>
      <div class="loop-step-explanation">
        ${step.explanation}
      </div>
    `;
  },

  renderStackFrames(data, container) {
    const frames = data.frames || [];
    let framesHtml = "";
    frames.forEach((f) => {
      const isOver = f.status && f.status.includes("OVERFLOW");
      framesHtml += `
        <div class="stack-frame ${isOver ? 'overflow-warn' : ''}">
          <span>Depth ${f.depth}: <strong>${f.func}</strong></span>
          <span style="font-size: 0.72rem; color: ${isOver ? '#f87171' : '#a78bfa'};">${f.status}</span>
        </div>
      `;
    });

    container.innerHTML = `
      <div class="visualizer-card">
        <div class="visualizer-header">
          <span class="vis-title"><i class="fa-solid fa-layer-group"></i> Call Stack & Memory Frame Tracker</span>
          <span class="vis-type-pill">LIFO Stack</span>
        </div>

        <div class="stack-tube-container">
          ${framesHtml}
        </div>

        <div style="font-size: 0.82rem; color: var(--text-muted); line-height: 1.4;">
          ${data.reason || "Recursion stack allocates a new memory frame per call until the termination condition is met."}
        </div>
      </div>
    `;
  },

  renderTreePointers(data, container) {
    const root = data.root || { val: "Root", left: null, right: null };
    container.innerHTML = `
      <div class="visualizer-card">
        <div class="visualizer-header">
          <span class="vis-title"><i class="fa-solid fa-network-wired"></i> Object Reference & Node Explorer</span>
          <span class="vis-type-pill">Tree Pointers</span>
        </div>

        <div class="tree-visual-wrapper">
          <div class="tree-node-circle">${root.val || 'Node'}</div>
          <div style="color: var(--text-dim); font-size: 0.75rem;"><i class="fa-solid fa-arrow-down-left"></i> Left &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Right <i class="fa-solid fa-arrow-down-right"></i></div>
          <div class="tree-branches">
            <div class="tree-branch-item">
              <div class="tree-node-circle" style="border-color: #10b981;">Left</div>
              <span style="font-size: 0.7rem; color: #34d399;">Valid Object</span>
            </div>
            <div class="tree-branch-item">
              <div class="tree-null-node">null</div>
              <span style="font-size: 0.7rem; color: #f87171;">Dereference Crash 💥</span>
            </div>
          </div>
        </div>

        <div style="font-size: 0.82rem; color: var(--text-muted); line-height: 1.4;">
          ${data.reason || "Dereferencing fields or methods on null/None throws a runtime exception."}
        </div>
      </div>
    `;
  },

  renderVariableState(data, container) {
    const variables = data.variables || [];
    let rowsHtml = "";
    variables.forEach((v) => {
      rowsHtml += `
        <tr>
          <td class="var-name">${v.name}</td>
          <td class="var-type">${v.type}</td>
          <td class="var-val">${v.value}</td>
        </tr>
      `;
    });

    container.innerHTML = `
      <div class="visualizer-card">
        <div class="visualizer-header">
          <span class="vis-title"><i class="fa-solid fa-table"></i> Runtime Variable Watch</span>
          <span class="vis-type-pill">Variables</span>
        </div>

        <table class="var-watch-table">
          <thead>
            <tr>
              <th>Variable</th>
              <th>Type</th>
              <th>Value at Crash</th>
            </tr>
          </thead>
          <tbody>
            ${rowsHtml}
          </tbody>
        </table>

        <div style="font-size: 0.82rem; color: var(--text-muted); line-height: 1.4;">
          ${data.reason || "State snapshot captured at point of failure."}
        </div>
      </div>
    `;
  }
};
