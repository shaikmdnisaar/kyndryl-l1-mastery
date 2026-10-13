import json

with open('clean_modules_with_priority.json', encoding='utf-8') as f:
    modules = json.load(f)

modules_js = json.dumps(modules)

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Kyndryl L1 Network Operations Center — CCNA v1.1 Mastery Platform</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-dark: #070b14;
      --bg-card: #0d1424;
      --bg-card-hover: #141d33;
      --border: #1e293d;
      --border-focus: #38bdf8;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --cyan: #38bdf8;
      --cyan-glow: rgba(56, 189, 248, 0.25);
      --indigo: #6366f1;
      --emerald: #10b981;
      --emerald-glow: rgba(16, 185, 129, 0.25);
      --amber: #f59e0b;
      --amber-glow: rgba(245, 158, 11, 0.25);
      --rose: #f43f5e;
      --rose-glow: rgba(244, 63, 94, 0.3);
      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 20px;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Plus Jakarta Sans', sans-serif;
      background-color: var(--bg-dark);
      color: var(--text-main);
      line-height: 1.6;
      padding-bottom: 90px;
      background-image: 
        radial-gradient(at 0% 0%, rgba(56, 189, 248, 0.08) 0px, transparent 50%),
        radial-gradient(at 100% 100%, rgba(99, 102, 241, 0.08) 0px, transparent 50%);
      background-attachment: fixed;
    }

    code, pre, .mono { font-family: 'JetBrains Mono', monospace; }

    .container {
      max-width: 1320px;
      margin: 0 auto;
      padding: 0 24px;
    }

    /* Top Sticky Header */
    header {
      padding: 24px 0 20px;
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      background: rgba(7, 11, 20, 0.9);
      backdrop-filter: blur(16px);
      z-index: 100;
    }

    .header-content {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 20px;
      flex-wrap: wrap;
    }

    .brand-group {
      display: flex;
      align-items: center;
      gap: 16px;
    }

    .badge-kyndryl {
      background: linear-gradient(135deg, #f43f5e, #be123c);
      color: white;
      font-weight: 800;
      font-size: 0.75rem;
      letter-spacing: 1.5px;
      padding: 5px 12px;
      border-radius: var(--radius-sm);
      text-transform: uppercase;
      box-shadow: 0 0 20px var(--rose-glow);
    }

    .header-title h1 {
      font-size: 1.45rem;
      font-weight: 800;
      background: linear-gradient(to right, #ffffff, #94a3b8);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .header-title p {
      font-size: 0.85rem;
      color: var(--text-muted);
    }

    /* Saved Credentials Strip */
    .portal-quick-strip {
      background: linear-gradient(90deg, rgba(244, 63, 94, 0.12), rgba(56, 189, 248, 0.08));
      border: 1px solid rgba(244, 63, 94, 0.3);
      border-radius: var(--radius-md);
      padding: 14px 20px;
      margin: 20px 0;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
    }

    .portal-info {
      display: flex;
      align-items: center;
      gap: 14px;
      flex-wrap: wrap;
    }

    .portal-tag {
      font-size: 0.75rem;
      font-weight: 800;
      color: #fb7185;
      text-transform: uppercase;
      letter-spacing: 1px;
    }

    .portal-val {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.88rem;
      background: rgba(0, 0, 0, 0.4);
      padding: 4px 10px;
      border-radius: 6px;
      border: 1px solid var(--border);
      color: var(--cyan);
    }

    .portal-actions { display: flex; gap: 10px; }

    .btn-sm {
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid var(--border);
      color: var(--text-main);
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      font-family: inherit;
      transition: all 0.2s;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }

    .btn-sm:hover {
      background: var(--cyan);
      color: #070b14;
      border-color: var(--cyan);
    }

    .btn-sm.primary {
      background: var(--cyan);
      color: #070b14;
      border-color: var(--cyan);
      font-weight: 700;
    }

    .btn-sm.primary:hover { background: #7dd3fc; }

    .btn-sm.priority-toggle {
      background: rgba(245, 158, 11, 0.15);
      border-color: var(--amber);
      color: #fbbf24;
      font-weight: 700;
    }

    .btn-sm.priority-toggle.active {
      background: var(--amber);
      color: #070b14;
      box-shadow: 0 0 15px var(--amber-glow);
    }

    .watch-btn {
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.3);
      color: var(--cyan);
      font-size: 0.75rem;
      padding: 4px 10px;
      border-radius: 6px;
      flex-shrink: 0;
    }

    .watch-btn:hover {
      background: var(--cyan);
      color: #070b14;
    }

    /* KPI Metric Cards */
    .metrics-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
      gap: 16px;
      margin-bottom: 24px;
    }

    .metric-card {
      background: var(--bg-card);
      border: 1px solid var(--border);
      padding: 20px;
      border-radius: var(--radius-md);
      position: relative;
      overflow: hidden;
      transition: transform 0.2s, border-color 0.2s;
    }

    .metric-card:hover {
      transform: translateY(-2px);
      border-color: var(--border-focus);
    }

    .metric-card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 4px;
      height: 100%;
      background: var(--cyan);
    }

    .metric-card.emerald::before { background: var(--emerald); }
    .metric-card.indigo::before { background: var(--indigo); }
    .metric-card.amber::before { background: var(--amber); }

    .metric-label {
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: var(--text-dim);
      margin-bottom: 6px;
    }

    .metric-val {
      font-size: 1.8rem;
      font-weight: 800;
      color: var(--text-main);
      display: flex;
      align-items: baseline;
      gap: 6px;
    }

    .metric-val span {
      font-size: 0.88rem;
      font-weight: 500;
      color: var(--text-muted);
    }

    .progress-bar-container {
      width: 100%;
      height: 8px;
      background: var(--border);
      border-radius: 99px;
      margin-top: 12px;
      overflow: hidden;
    }

    .progress-bar-fill {
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, var(--cyan), var(--emerald));
      border-radius: 99px;
      transition: width 0.4s ease;
    }

    /* Nav Tabs */
    .nav-tabs {
      display: flex;
      gap: 8px;
      border-bottom: 1px solid var(--border);
      margin-bottom: 28px;
      overflow-x: auto;
      padding-bottom: 2px;
    }

    .tab-btn {
      background: transparent;
      border: none;
      color: var(--text-muted);
      font-family: inherit;
      font-size: 0.95rem;
      font-weight: 600;
      padding: 12px 18px;
      cursor: pointer;
      border-radius: var(--radius-sm) var(--radius-sm) 0 0;
      position: relative;
      transition: all 0.2s;
      white-space: nowrap;
    }

    .tab-btn:hover {
      color: var(--text-main);
      background: rgba(255, 255, 255, 0.03);
    }

    .tab-btn.active {
      color: var(--cyan);
      background: rgba(56, 189, 248, 0.08);
    }

    .tab-btn.active::after {
      content: '';
      position: absolute;
      bottom: -2px;
      left: 0;
      width: 100%;
      height: 3px;
      background: var(--cyan);
      box-shadow: 0 0 12px var(--cyan);
    }

    .tab-pane { display: none; animation: fadeIn 0.3s ease; }
    .tab-pane.active { display: block; }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* COURSE TRACKER ACCORDION & LESSONS */
    .tracker-toolbar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
      margin-bottom: 20px;
      flex-wrap: wrap;
    }

    .search-input {
      flex: 1;
      min-width: 280px;
      padding: 12px 18px;
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      color: white;
      font-family: inherit;
      font-size: 0.95rem;
      outline: none;
    }

    .search-input:focus {
      border-color: var(--cyan);
      box-shadow: 0 0 12px var(--cyan-glow);
    }

    .filter-actions {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
    }

    .module-card {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      margin-bottom: 20px;
      overflow: hidden;
      transition: border-color 0.2s;
    }

    .module-card:hover { border-color: rgba(56, 189, 248, 0.3); }

    .module-header {
      padding: 18px 24px;
      background: rgba(255, 255, 255, 0.02);
      border-bottom: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      align-items: center;
      cursor: pointer;
      user-select: none;
      flex-wrap: wrap;
      gap: 12px;
    }

    .module-title-wrap {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .module-badge {
      font-size: 0.78rem;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: var(--radius-sm);
      background: rgba(56, 189, 248, 0.12);
      color: var(--cyan);
      border: 1px solid rgba(56, 189, 248, 0.3);
      white-space: nowrap;
    }

    .module-title {
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--text-main);
    }

    .module-stats {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .module-counter {
      font-size: 0.8rem;
      font-weight: 600;
      padding: 3px 10px;
      border-radius: 99px;
      background: rgba(255, 255, 255, 0.05);
      color: var(--text-muted);
    }

    .module-arrow { font-size: 0.85rem; color: var(--cyan); transition: transform 0.2s; }

    .lessons-container {
      padding: 14px 20px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .lesson-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 14px;
      padding: 12px 16px;
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid rgba(255, 255, 255, 0.04);
      border-radius: var(--radius-md);
      transition: all 0.2s;
    }

    .lesson-row:hover {
      background: rgba(255, 255, 255, 0.04);
      border-color: rgba(56, 189, 248, 0.2);
    }

    .lesson-row.completed {
      background: rgba(16, 185, 129, 0.04);
      border-color: rgba(16, 185, 129, 0.2);
    }

    .lesson-left {
      display: flex;
      align-items: center;
      gap: 14px;
      flex: 1;
      min-width: 0;
    }

    .lesson-checkbox {
      appearance: none;
      -webkit-appearance: none;
      width: 20px;
      height: 20px;
      border: 2px solid var(--text-dim);
      border-radius: 6px;
      background: transparent;
      cursor: pointer;
      display: grid;
      place-content: center;
      flex-shrink: 0;
      transition: all 0.2s;
    }

    .lesson-checkbox:checked {
      background: var(--emerald);
      border-color: var(--emerald);
      box-shadow: 0 0 10px var(--emerald-glow);
    }

    .lesson-checkbox:checked::before {
      content: '✔';
      font-size: 12px;
      color: white;
      font-weight: 800;
    }

    .lesson-link {
      font-size: 0.94rem;
      font-weight: 600;
      color: var(--text-main);
      text-decoration: none;
      transition: color 0.2s;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .lesson-link:hover {
      color: var(--cyan);
      text-decoration: underline;
    }

    .lesson-row.completed .lesson-link {
      color: var(--text-muted);
      text-decoration: line-through;
    }

    .badge-priority {
      background: rgba(245, 158, 11, 0.15);
      border: 1px solid rgba(245, 158, 11, 0.35);
      color: #fbbf24;
      font-size: 0.72rem;
      font-weight: 800;
      padding: 2px 7px;
      border-radius: 4px;
      white-space: nowrap;
    }

    .lesson-right {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-shrink: 0;
    }

    .lesson-duration {
      font-size: 0.78rem;
      font-weight: 600;
      color: var(--cyan);
      background: rgba(56, 189, 248, 0.08);
      padding: 3px 8px;
      border-radius: 4px;
      white-space: nowrap;
    }

    /* CLI SIMULATOR */
    .terminal-window {
      background: #040711;
      border: 1px solid #1e293d;
      border-radius: var(--radius-lg);
      overflow: hidden;
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6);
      margin-bottom: 30px;
    }

    .terminal-bar {
      background: #0b1120;
      padding: 12px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #1e293d;
      flex-wrap: wrap;
      gap: 12px;
    }

    .terminal-dots { display: flex; gap: 8px; }
    .dot { width: 12px; height: 12px; border-radius: 50%; }
    .dot.red { background: #ef4444; }
    .dot.yellow { background: #f59e0b; }
    .dot.green { background: #10b981; }

    .terminal-title {
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--text-muted);
      font-family: 'JetBrains Mono', monospace;
    }

    .terminal-presets { display: flex; gap: 8px; flex-wrap: wrap; }

    .terminal-body {
      padding: 20px;
      min-height: 380px;
      max-height: 520px;
      overflow-y: auto;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.9rem;
      color: #38bdf8;
      line-height: 1.5;
    }

    .terminal-output {
      color: #94a3b8;
      white-space: pre-wrap;
      margin-bottom: 12px;
    }

    .terminal-input-row {
      display: flex;
      align-items: center;
      gap: 8px;
      background: rgba(255, 255, 255, 0.02);
      padding: 12px 20px;
      border-top: 1px solid #1e293d;
    }

    .terminal-prompt {
      color: #10b981;
      font-weight: 700;
      font-family: 'JetBrains Mono', monospace;
      white-space: nowrap;
    }

    .terminal-input {
      flex: 1;
      background: transparent;
      border: none;
      outline: none;
      color: #ffffff;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.95rem;
    }

    /* SUBNET DRILL */
    .subnet-card {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 28px;
      margin-bottom: 24px;
    }

    .subnet-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 24px;
      flex-wrap: wrap;
      gap: 16px;
    }

    .target-ip-display {
      font-family: 'JetBrains Mono', monospace;
      font-size: 2rem;
      font-weight: 800;
      color: var(--cyan);
      background: rgba(0, 0, 0, 0.4);
      padding: 8px 20px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border);
      display: inline-block;
    }

    .subnet-form-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 16px;
      margin-bottom: 20px;
    }

    .subnet-field { display: flex; flex-direction: column; gap: 6px; }
    .subnet-field label { font-size: 0.8rem; font-weight: 700; text-transform: uppercase; color: var(--text-muted); }
    .subnet-field input {
      padding: 12px 16px;
      background: rgba(0, 0, 0, 0.3);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      color: white;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.95rem;
      outline: none;
    }
    .subnet-field input:focus { border-color: var(--cyan); }

    .result-banner {
      margin-top: 20px;
      padding: 14px 18px;
      border-radius: var(--radius-sm);
      display: none;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.9rem;
    }
    .result-banner.correct { background: rgba(16, 185, 129, 0.15); border: 1px solid var(--emerald); color: #34d399; display: block; }
    .result-banner.wrong { background: rgba(244, 63, 94, 0.15); border: 1px solid var(--rose); color: #fb7185; display: block; }

    /* INCIDENT WAR ROOM */
    .incident-ticket {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 24px;
      margin-bottom: 20px;
    }

    .incident-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
      flex-wrap: wrap;
      gap: 10px;
    }

    .badge-sev1 { background: rgba(239, 68, 68, 0.15); color: #f87171; border: 1px solid #ef4444; padding: 4px 10px; border-radius: 6px; font-weight: 800; font-size: 0.75rem; }
    .badge-sev2 { background: rgba(245, 158, 11, 0.15); color: #fbbf24; border: 1px solid #f59e0b; padding: 4px 10px; border-radius: 6px; font-weight: 800; font-size: 0.75rem; }
    .badge-sev3 { background: rgba(56, 189, 248, 0.15); color: #38bdf8; border: 1px solid #38bdf8; padding: 4px 10px; border-radius: 6px; font-weight: 800; font-size: 0.75rem; }

    .ticket-log-template {
      background: rgba(0, 0, 0, 0.4);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: var(--radius-sm);
      padding: 14px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.82rem;
      color: #cbd5e1;
      margin-top: 14px;
      white-space: pre-wrap;
    }

    /* CLI GRID */
    .cmd-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
      gap: 16px;
    }

    .cmd-card {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 16px 20px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.2s;
    }

    .cmd-card:hover { border-color: var(--indigo); transform: translateY(-2px); }

    .cmd-syntax {
      font-size: 0.88rem;
      background: rgba(0, 0, 0, 0.4);
      padding: 8px 12px;
      border-radius: 6px;
      color: #38bdf8;
      margin: 8px 0;
      border: 1px solid rgba(255, 255, 255, 0.05);
    }

    /* Q&A FLASHCARDS */
    .qa-card {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      margin-bottom: 16px;
      overflow: hidden;
    }

    .qa-question {
      padding: 18px 24px;
      font-size: 1rem;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: rgba(255, 255, 255, 0.02);
    }

    .qa-answer {
      display: none;
      padding: 20px 24px;
      background: rgba(0, 0, 0, 0.3);
      border-top: 1px solid var(--border);
      font-size: 0.9rem;
      color: #cbd5e1;
      line-height: 1.6;
    }

    .qa-answer.open { display: block; }
  </style>
</head>
<body>

  <!-- Sticky Top Header -->
  <header>
    <div class="container header-content">
      <div class="brand-group">
        <span class="badge-kyndryl">Kyndryl</span>
        <div class="header-title">
          <h1>L1 Network Operations & CCNA v1.1 Mastery Platform</h1>
          <p>Curated Kyndryl L1 Priority Path • 201 Direct Lesson Links • Terminal Simulator • Subnet Drills</p>
        </div>
      </div>
      <div>
        <button class="btn-sm" onclick="resetAllProgress()">↺ Reset Storage</button>
      </div>
    </div>
  </header>

  <main class="container">

    <!-- Stored Credentials & Portal Quick Launch Bar -->
    <section class="portal-quick-strip">
      <div class="portal-info">
        <span class="portal-tag">🔑 Saved Library Access</span>
        <span class="portal-val">Card: 29100701939436</span>
        <span class="portal-val">PIN: 1234</span>
        <span class="portal-val">Toronto Public Library (TPL)</span>
      </div>
      <div class="portal-actions">
        <button class="btn-sm" onclick="copyCardAndPin()">📋 Copy Card & PIN</button>
        <a class="btn-sm primary" href="https://www.linkedin.com/checkpoint/enterprise/login/76281980?pathWildcard=76281980&application=learning" target="_blank">🚀 Open LinkedIn Login</a>
        <a class="btn-sm" href="https://www.linkedin.com/learning/cisco-certified-network-associate-ccna-v1-1-200-301-cert-prep/diving-into-the-course?u=76281980" target="_blank">🎬 Main CCNA Page</a>
      </div>
    </section>

    <!-- KPI Metric Strip -->
    <section class="metrics-grid">
      <div class="metric-card">
        <div class="metric-label">Course Progress</div>
        <div class="metric-val" id="progressPercentage">0% <span>Done</span></div>
        <div class="progress-bar-container">
          <div class="progress-bar-fill" id="progressBar"></div>
        </div>
      </div>
      <div class="metric-card emerald">
        <div class="metric-label">Lessons Completed</div>
        <div class="metric-val" id="lessonsCounter">0 <span>/ 201</span></div>
        <p style="font-size: 0.75rem; color: var(--text-dim); margin-top: 8px;">Direct clickable lesson links saved in browser</p>
      </div>
      <div class="metric-card indigo">
        <div class="metric-label">Subnetting Score</div>
        <div class="metric-val" id="subnetStreak">0 <span>Streak</span></div>
        <p style="font-size: 0.75rem; color: var(--text-dim); margin-top: 8px;">Mental speed calculation accuracy</p>
      </div>
      <div class="metric-card amber">
        <div class="metric-label">Kyndryl L1 Readiness</div>
        <div class="metric-val" id="readinessScore">0 <span>/ 100</span></div>
        <p style="font-size: 0.75rem; color: var(--text-dim); margin-top: 8px;">Calculated across CCNA & NOC skills</p>
      </div>
    </section>

    <!-- Navigation Tabs -->
    <nav class="nav-tabs">
      <button class="tab-btn active" onclick="switchTab('trackerTab')">🎬 Course Tracker & Priority Path</button>
      <button class="tab-btn" onclick="switchTab('terminalTab')">💻 Interactive Cisco Terminal</button>
      <button class="tab-btn" onclick="switchTab('subnetTab')">⚡ Subnetting Speed Trainer</button>
      <button class="tab-btn" onclick="switchTab('warRoomTab')">🚨 Kyndryl Incident War Room</button>
      <button class="tab-btn" onclick="switchTab('cliTab')">📖 Top 25 Cisco CLI Reference</button>
      <button class="tab-btn" onclick="switchTab('interviewTab')">🎯 Interview & Technical Q&A</button>
    </nav>

    <!-- TAB 1: CCNA COURSE & LESSON TRACKER WITH DIRECT LINKS -->
    <div id="trackerTab" class="tab-pane active">
      <div class="tracker-toolbar">
        <input type="text" id="lessonSearchInput" class="search-input" placeholder="🔍 Search across lessons (e.g. OSPF, VLAN, Subnetting, EtherChannel, ACL, HSRP)..." oninput="filterLessons()">
        <div class="filter-actions">
          <button class="btn-sm priority-toggle active" id="priorityToggleBtn" onclick="togglePriorityFilter()">⭐ Kyndryl L1 Priority Only (66 Lessons)</button>
          <button class="btn-sm" onclick="expandAllModules()">Expand All</button>
          <button class="btn-sm" onclick="collapseAllModules()">Collapse All</button>
        </div>
      </div>

      <div id="modulesContainer">
        <!-- Rendered dynamically by JavaScript with all 201 lesson links -->
      </div>
    </div>

    <!-- TAB 2: INTERACTIVE CISCO CLI TERMINAL SIMULATOR -->
    <div id="terminalTab" class="tab-pane">
      <div class="terminal-window">
        <div class="terminal-bar">
          <div class="terminal-dots">
            <span class="dot red"></span>
            <span class="dot yellow"></span>
            <span class="dot green"></span>
          </div>
          <div class="terminal-title">KYNDRYL-CORE-SW01# (Cisco Catalyst 9300 IOS-XE 17.9)</div>
          <div class="terminal-presets">
            <button class="btn-sm" onclick="runPreset('show ip interface brief')">show ip int br</button>
            <button class="btn-sm" onclick="runPreset('show vlan brief')">show vlan br</button>
            <button class="btn-sm" onclick="runPreset('show interfaces trunk')">show int trunk</button>
            <button class="btn-sm" onclick="runPreset('show ip ospf neighbor')">show ip ospf neigh</button>
            <button class="btn-sm" onclick="runPreset('show interface status err-disabled')">show errdisabled</button>
            <button class="btn-sm" onclick="runPreset('clear')">Clear</button>
          </div>
        </div>
        <div class="terminal-body" id="termBody">
          <div class="terminal-output">Kyndryl Global Managed Network Infrastructure - Node: KYNDRYL-CORE-SW01
Cisco IOS XE Software, Version 17.09.04a [Amsterdam]
Type 'help' to see available commands or click the quick presets above.
================================================================================
</div>
        </div>
        <div class="terminal-input-row">
          <span class="terminal-prompt">KYNDRYL-CORE-SW01#</span>
          <input type="text" id="termInput" class="terminal-input" placeholder="Type a Cisco command (e.g. show ip int br, show ip route, show standby brief)..." onkeydown="handleTerminalKey(event)">
          <button class="btn-sm primary" onclick="executeCurrentInput()">Run</button>
        </div>
      </div>
    </div>

    <!-- TAB 3: SUBNETTING SPEED TRAINER -->
    <div id="subnetTab" class="tab-pane">
      <div class="subnet-card">
        <div class="subnet-header">
          <div>
            <h3>Mental Subnetting Speed Drill</h3>
            <p style="color: var(--text-muted); font-size: 0.88rem;">An L1 engineer at Kyndryl must verify client subnets and gateways within 10 seconds.</p>
          </div>
          <div class="target-ip-display" id="drillTarget">192.168.10.74 /27</div>
        </div>

        <div class="subnet-form-grid">
          <div class="subnet-field">
            <label>Subnet Network ID</label>
            <input type="text" id="ansNetId" placeholder="e.g. 192.168.10.64">
          </div>
          <div class="subnet-field">
            <label>First Usable Host IP</label>
            <input type="text" id="ansFirstHost" placeholder="e.g. 192.168.10.65">
          </div>
          <div class="subnet-field">
            <label>Last Usable Host IP</label>
            <input type="text" id="ansLastHost" placeholder="e.g. 192.168.10.94">
          </div>
          <div class="subnet-field">
            <label>Broadcast Address</label>
            <input type="text" id="ansBcast" placeholder="e.g. 192.168.10.95">
          </div>
          <div class="subnet-field">
            <label>Total Usable Hosts</label>
            <input type="text" id="ansHosts" placeholder="e.g. 30">
          </div>
        </div>

        <div style="display:flex; gap:12px; align-items:center;">
          <button class="btn-sm primary" onclick="checkSubnetAnswer()">Verify Answer</button>
          <button class="btn-sm" onclick="generateNewSubnetQuestion()">Next Random IP</button>
        </div>

        <div id="subnetResultBanner" class="result-banner"></div>
      </div>
    </div>

    <!-- TAB 4: KYNDRYL INCIDENT WAR ROOM -->
    <div id="warRoomTab" class="tab-pane">

      <div class="incident-ticket">
        <div class="incident-header">
          <div>
            <span class="badge-sev1">INC098231 • P1 CRITICAL</span>
            <strong style="margin-left: 10px; font-size: 1.05rem;">Branch Office Core Switch Flapping & High CPU Loop</strong>
          </div>
          <span style="font-size: 0.8rem; color: var(--text-muted);">SLA: 15-min War Room Update</span>
        </div>
        <p style="font-size: 0.88rem; color: var(--text-muted); margin-bottom: 10px;"><strong>Client Symptom:</strong> Entire Dallas branch cannot access cloud apps. Pings have 80% loss. Core switch console reporting spanning-tree topology change storm.</p>
        <div style="font-size: 0.85rem; color: #cbd5e1; margin-bottom: 10px;">
          <strong>L1 Triage Steps:</strong>
          <ol style="margin-left: 20px; margin-top: 4px;">
            <li>Run <code>show spanning-tree detail | include is the root|from</code> to find which port is receiving frequent TCNs (Topology Change Notifications).</li>
            <li>Run <code>show mac address-table count</code> to see if MAC table is thrashing/flapping between ports.</li>
            <li>Identify the rogue switch or unmanaged hub on that port and execute <code>shutdown</code> on the offending access port.</li>
          </ol>
        </div>
        <div class="ticket-log-template">
[KYNDRYL L1 SERVICENOW WORKLOG TEMPLATE]
Incident: INC098231 (P1 Spanning Tree Broadcast Storm)
Root Cause: Unmanaged switch connected to Gi1/0/22 caused switching loop without BPDU Guard.
Action Taken: Shut down interface Gi1/0/22. Spanning-tree stabilized on CORE-SW01. CPU returned to 4%.
Status: Service restored. Recommended site technician inspect floor drop before port re-enablement.
        </div>
      </div>

      <div class="incident-ticket">
        <div class="incident-header">
          <div>
            <span class="badge-sev2">INC098402 • P2 HIGH</span>
            <strong style="margin-left: 10px; font-size: 1.05rem;">Finance VLAN 30 Workstations Assigning 169.254.x.x APIPA Addresses</strong>
          </div>
          <span style="font-size: 0.8rem; color: var(--text-muted);">SLA: 1-hour resolution</span>
        </div>
        <p style="font-size: 0.88rem; color: var(--text-muted); margin-bottom: 10px;"><strong>Client Symptom:</strong> 25 users in Finance department reporting yellow warning icon on Windows network status with zero LAN connectivity.</p>
        <div style="font-size: 0.85rem; color: #cbd5e1; margin-bottom: 10px;">
          <strong>L1 Triage Steps:</strong>
          <ol style="margin-left: 20px; margin-top: 4px;">
            <li>Run <code>show ip interface vlan 30</code> on the Layer 3 core switch to verify SVI is Up/Up.</li>
            <li>Check if <code>ip helper-address 10.100.1.50</code> is configured under <code>interface Vlan30</code>.</li>
            <li>Ping DHCP server IP from core switch. If reachable, check DHCP scope pool exhaustion on Windows/Infoblox server.</li>
          </ol>
        </div>
        <div class="ticket-log-template">
[KYNDRYL L1 SERVICENOW WORKLOG TEMPLATE]
Incident: INC098402 (P2 DHCP Lease Failure)
Root Cause: DHCP Helper address missing on newly provisioned VLAN 30 SVI following overnight maintenance.
Action Taken: Configured 'ip helper-address 10.100.1.50' under SVI Vlan30. Tested client IP renewal (10.30.0.102/24 received).
Status: Resolved. All 25 clients confirmed online.
        </div>
      </div>

      <div class="incident-ticket">
        <div class="incident-header">
          <div>
            <span class="badge-sev3">INC098555 • P3 MEDIUM</span>
            <strong style="margin-left: 10px; font-size: 1.05rem;">Executive Conference Room Port In Err-Disabled State</strong>
          </div>
          <span style="font-size: 0.8rem; color: var(--text-muted);">SLA: 4-hour resolution</span>
        </div>
        <p style="font-size: 0.88rem; color: var(--text-muted); margin-bottom: 10px;"><strong>Client Symptom:</strong> Wall jack Gi1/0/14 has no link light after conference video endpoint was moved.</p>
        <div style="font-size: 0.85rem; color: #cbd5e1; margin-bottom: 10px;">
          <strong>L1 Triage Steps:</strong>
          <ol style="margin-left: 20px; margin-top: 4px;">
            <li>Run <code>show interface status err-disabled</code>. Found reason: <code>psecure-violation</code> (Port Security).</li>
            <li>Run <code>show port-security interface Gi1/0/14</code>. Max allowed MACs: 1. Last violating MAC logged.</li>
            <li>Clear old MAC address: <code>clear port-security dynamic interface Gi1/0/14</code> then bounce interface (<code>shutdown</code> / <code>no shutdown</code>).</li>
          </ol>
        </div>
        <div class="ticket-log-template">
[KYNDRYL L1 SERVICENOW WORKLOG TEMPLATE]
Incident: INC098555 (P3 Port Security Err-Disable)
Root Cause: Port Security violation triggered when new video codec MAC address was plugged into wall jack Gi1/0/14.
Action Taken: Verified authorized hardware with local contact. Cleared sticky MAC table and un-shut interface.
Status: Resolved. Link up at 1000Mbps Full Duplex.
        </div>
      </div>

    </div>

    <!-- TAB 5: TOP 25 CISCO CLI REFERENCE -->
    <div id="cliTab" class="tab-pane">
      <input type="text" id="cliSearch" class="search-input" placeholder="🔍 Search commands by keyword (e.g. trunk, ospf, mac, err-disabled, nat)..." oninput="filterCommands()" style="width:100%; margin-bottom:20px;">
      <div class="cmd-grid" id="cmdGridContainer"></div>
    </div>

    <!-- TAB 6: INTERVIEW Q&A FLASHCARDS -->
    <div id="interviewTab" class="tab-pane">
      <div id="qaContainer"></div>
    </div>

  </main>

  <script>
    // Full 201-Lesson Curriculum Database with Direct Links and Priority Flagging
    const courseModules = MODULES_PLACEHOLDER;

    let priorityOnlyFilter = true; // Default to Kyndryl Priority track

    // Cisco CLI Terminal Outputs Database
    const terminalDatabase = {
      "help": `Available commands:
  show ip interface brief       - Display IP and interface status
  show vlan brief               - Display active VLANs and assigned ports
  show interfaces trunk         - Display active 802.1Q trunk links
  show mac address-table        - Display dynamically learned MAC addresses
  show spanning-tree            - Display STP topology and port roles
  show ip route                 - Display router forwarding table
  show ip ospf neighbor         - Display dynamic OSPF neighbor adjacencies
  show standby brief            - Display HSRP gateway redundancy state
  show interface status err-disabled - Display ports shutdown by security/STP
  show tech-support             - Dump standard Kyndryl escalation logs
  clear                         - Clear terminal window`,

      "show ip interface brief": `Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1/0/1   unassigned      YES unset  up                    up      
GigabitEthernet1/0/2   unassigned      YES unset  up                    up      
GigabitEthernet1/0/3   unassigned      YES unset  down                  down    
GigabitEthernet1/0/4   unassigned      YES unset  down                  down    
GigabitEthernet1/0/24  10.10.1.2       YES manual up                    up      
TenGigabitEthernet1/1/1 unassigned     YES unset  up                    up      
Vlan1                  unassigned      YES unset  administratively down down    
Vlan10                 10.10.10.1      YES manual up                    up      
Vlan20                 10.10.20.1      YES manual up                    up      
Vlan99                 10.10.99.1      YES manual up                    up      `,

      "show vlan brief": `VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Gi1/0/5, Gi1/0/6, Gi1/0/7
10   DATA_USERS                       active    Gi1/0/8, Gi1/0/9, Gi1/0/10
20   VOICE_PHONES                     active    Gi1/0/11, Gi1/0/12, Gi1/0/13
30   SERVERS_DC                       active    Gi1/0/14, Gi1/0/15
99   MANAGEMENT                       active    Gi1/0/24
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup `,

      "show interfaces trunk": `Port        Mode             Encapsulation  Status        Native vlan
Te1/1/1     on               802.1q         trunking      99
Te1/1/2     on               802.1q         trunking      99

Port        Vlans allowed on trunk
Te1/1/1     1-4094
Te1/1/2     1-4094

Port        Vlans in spanning tree forwarding state and not pruned
Te1/1/1     1,10,20,30,99
Te1/1/2     1,10,20,30,99`,

      "show mac address-table": `          Mac Address Table
-------------------------------------------
Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  10    0050.56a1.2b3c    DYNAMIC     Gi1/0/8
  10    0050.56a1.9f12    DYNAMIC     Gi1/0/9
  20    0004.f211.bb44    DYNAMIC     Gi1/0/11
  30    d46d.50e1.77aa    DYNAMIC     Gi1/0/14
  99    0000.0c07.ac01    DYNAMIC     Te1/1/1
Total Mac Addresses for this criterion: 5`,

      "show spanning-tree": `VLAN0010
  Spanning tree enabled protocol rstp
  Root ID    Priority    24586
             Address     0019.06e7.6480
             Cost        4
             Port        Te1/1/1 (TenGigabitEthernet1/1/1)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32778  (priority 32768 sys-id-ext 10)
             Address     70ea.1ae4.3300
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Te1/1/1             Root FWD 4         128.53   P2p 
Te1/1/2             Altn BLK 4         128.54   P2p 
Gi1/0/8             Desg FWD 19        128.8    P2p Edge `,

      "show ip route": `Gateway of last resort is 10.10.1.1 to network 0.0.0.0

S*    0.0.0.0/0 [1/0] via 10.10.1.1, GigabitEthernet1/0/24
C     10.10.10.0/24 is directly connected, Vlan10
L     10.10.10.1/32 is directly connected, Vlan10
C     10.10.20.0/24 is directly connected, Vlan20
L     10.10.20.1/32 is directly connected, Vlan20
O     10.50.0.0/16 [110/11] via 10.10.1.1, 04:12:33, GigabitEthernet1/0/24
O     192.168.100.0/24 [110/20] via 10.10.1.1, 04:12:33, GigabitEthernet1/0/24`,

      "show ip ospf neighbor": `Neighbor ID     Pri   State           Dead Time   Address         Interface
192.168.1.1       1   FULL/BDR        00:00:36    10.10.1.1       GigabitEthernet1/0/24
192.168.1.2       1   FULL/DR         00:00:33    10.10.1.3       GigabitEthernet1/0/24`,

      "show standby brief": `Interface   Grp  Pri P State   Active          Standby         Virtual IP
Vl10        10   110 P Active  local           10.10.10.2      10.10.10.254
Vl20        20   90    Standby 10.10.20.2      local           10.10.20.254`,

      "show interface status err-disabled": `Port      Name               Status       Reason               Err-disabled Vlans
Gi1/0/14  CONF_ROOM_JACK     err-disabled psecure-violation
Gi1/0/22  FLOOR_3_DROP       err-disabled bpduguard`,

      "show tech-support": `------------------ show version ------------------
Cisco IOS XE Software, Version 17.09.04a
System image file is "bootflash:packages.conf"
cisco C9300-24T (X86) processor with 1813437K/6147K bytes of memory.
Uptime for this switch is 18 weeks, 4 days, 12 hours, 14 minutes.
Configuration register is 0x102
[LOG BUFFER ATTACHED FOR KYNDRYL L2/L3 ESCALATION TICKET]`
    };

    function executeCurrentInput() {
      const input = document.getElementById('termInput');
      const cmd = input.value.trim().toLowerCase();
      if (!cmd) return;
      printTerminalCommand(input.value.trim());
      input.value = "";
    }

    function handleTerminalKey(e) {
      if (e.key === 'Enter') executeCurrentInput();
    }

    function runPreset(cmd) { printTerminalCommand(cmd); }

    function printTerminalCommand(cmd) {
      const term = document.getElementById('termBody');
      const lower = cmd.toLowerCase();

      if (lower === 'clear') {
        term.innerHTML = "";
        return;
      }

      let response = terminalDatabase[lower];
      if (!response) {
        for (let key in terminalDatabase) {
          if (key.includes(lower) || lower.includes(key)) {
            response = terminalDatabase[key];
            break;
          }
        }
      }

      if (!response) {
        response = `% Invalid command: "${cmd}". Type 'help' to see valid Cisco commands.`;
      }

      const block = document.createElement('div');
      block.innerHTML = `
        <div style="color: #ffffff; margin-top: 10px;">KYNDRYL-CORE-SW01# <span style="color: #38bdf8;">${cmd}</span></div>
        <div class="terminal-output">${response}</div>
      `;
      term.appendChild(block);
      term.scrollTop = term.scrollHeight;
    }

    // Subnetting Drill
    let currentDrill = {
      ip: "192.168.10.74", cidr: 27,
      netId: "192.168.10.64", firstHost: "192.168.10.65", lastHost: "192.168.10.94", bcast: "192.168.10.95", hosts: 30
    };
    let streak = 0;

    function generateNewSubnetQuestion() {
      const octet1 = [10, 172, 192][Math.floor(Math.random() * 3)];
      const octet2 = Math.floor(Math.random() * 254) + 1;
      const octet3 = Math.floor(Math.random() * 254) + 1;
      const octet4 = Math.floor(Math.random() * 254) + 1;
      const cidr = [25, 26, 27, 28, 29, 30][Math.floor(Math.random() * 6)];
      const blockSize = Math.pow(2, 32 - cidr);
      const netOctet4 = Math.floor(octet4 / blockSize) * blockSize;
      const bcastOctet4 = netOctet4 + blockSize - 1;

      currentDrill = {
        ip: `${octet1}.${octet2}.${octet3}.${octet4}`,
        cidr: cidr,
        netId: `${octet1}.${octet2}.${octet3}.${netOctet4}`,
        firstHost: `${octet1}.${octet2}.${octet3}.${netOctet4 + 1}`,
        lastHost: `${octet1}.${octet2}.${octet3}.${bcastOctet4 - 1}`,
        bcast: `${octet1}.${octet2}.${octet3}.${bcastOctet4}`,
        hosts: blockSize - 2
      };

      document.getElementById('drillTarget').innerText = `${currentDrill.ip} /${currentDrill.cidr}`;
      document.getElementById('ansNetId').value = "";
      document.getElementById('ansFirstHost').value = "";
      document.getElementById('ansLastHost').value = "";
      document.getElementById('ansBcast').value = "";
      document.getElementById('ansHosts').value = "";
      document.getElementById('subnetResultBanner').className = "result-banner";
      document.getElementById('subnetResultBanner').innerText = "";
    }

    function checkSubnetAnswer() {
      const netId = document.getElementById('ansNetId').value.trim();
      const first = document.getElementById('ansFirstHost').value.trim();
      const last = document.getElementById('ansLastHost').value.trim();
      const bcast = document.getElementById('ansBcast').value.trim();
      const hosts = parseInt(document.getElementById('ansHosts').value.trim());
      const banner = document.getElementById('subnetResultBanner');

      if (netId === currentDrill.netId && first === currentDrill.firstHost && last === currentDrill.lastHost && bcast === currentDrill.bcast && hosts === currentDrill.hosts) {
        streak++;
        document.getElementById('subnetStreak').innerHTML = `${streak} <span>Streak</span>`;
        banner.className = "result-banner correct";
        banner.innerText = `✔ SPOT ON! Block size was ${Math.pow(2, 32 - currentDrill.cidr)}. Streak increased to ${streak}!`;
      } else {
        streak = 0;
        document.getElementById('subnetStreak').innerHTML = `0 <span>Streak</span>`;
        banner.className = "result-banner wrong";
        banner.innerText = `❌ Incorrect. Correct Answers:\\nNetwork ID: ${currentDrill.netId}\\nFirst Usable Host: ${currentDrill.firstHost}\\nLast Usable Host: ${currentDrill.lastHost}\\nBroadcast Address: ${currentDrill.bcast}\\nTotal Usable Hosts: ${currentDrill.hosts}`;
      }
    }

    function copyCardAndPin() {
      navigator.clipboard.writeText("Card: 29100701939436 | PIN: 1234").then(() => {
        alert("Copied to clipboard!\\nCard Number: 29100701939436\\nPIN: 1234");
      });
    }

    // Top 25 Commands & Q&A
    const commandsData = [
      { cmd: "show ip interface brief", cat: "Interface", desc: "Displays one-line summary of all interfaces, assigned IP addresses, and Layer 1/2 status (Status / Protocol)." },
      { cmd: "show interfaces status", cat: "Switching", desc: "Lists all switchports, their connected state, VLAN assignment, duplex, speed, and media type." },
      { cmd: "show vlan brief", cat: "Switching", desc: "Displays all active VLANs on the switch and which physical ports are currently mapped to each VLAN." },
      { cmd: "show interfaces trunk", cat: "Switching", desc: "Reveals all active 802.1Q trunk ports, native VLANs, trunk encapsulation, and allowed VLAN lists." },
      { cmd: "show mac address-table dynamic", cat: "Switching", desc: "Displays dynamically learned MAC addresses, associated VLANs, and outgoing switchports." },
      { cmd: "show spanning-tree summary", cat: "Spanning Tree", desc: "Summarizes STP state, root bridge flags, and PortFast/BPDU Guard default status across VLANs." },
      { cmd: "show spanning-tree vlan <id>", cat: "Spanning Tree", desc: "Detailed breakdown of port roles (Root, Designated, Alternate) and states (Forwarding, Blocking) for a VLAN." },
      { cmd: "show etherchannel summary", cat: "Link Aggregation", desc: "Shows port-channel status flags (SU = Layer2 In-Use) and member bundled ports (P = Bundled in Port-Channel)." },
      { cmd: "show cdp neighbors detail", cat: "Discovery", desc: "Provides rich information about directly connected Cisco devices: IP addresses, software version, and remote port ID." },
      { cmd: "show lldp info remote-device", cat: "Discovery", desc: "Industry-standard neighbor discovery showing multi-vendor devices, IP phones, and server NICs." },
      { cmd: "show ip route", cat: "Routing", desc: "Prints the entire routing table: directly connected (C), local (L), static (S), and OSPF (O) routes." },
      { cmd: "show ip route <destination-ip>", cat: "Routing", desc: "Performs Longest Prefix Match to show exactly which route entry and next-hop router handles that destination IP." },
      { cmd: "show ip ospf neighbor", cat: "Routing", desc: "Shows active OSPF neighbors, their state (Full, 2-Way, Init), Router ID, Dead Timer, and interface." },
      { cmd: "show ip ospf interface brief", cat: "Routing", desc: "Lists all OSPF-enabled interfaces, Area IDs, costs, and DR/BDR roles." },
      { cmd: "show standby brief", cat: "HSRP", desc: "Displays HSRP group status: Group number, Priority, State (Active / Standby), Virtual IP, and Active Router IP." },
      { cmd: "show ip arp", cat: "ARP", desc: "Shows IP-to-MAC resolution table with interface mappings and age timers." },
      { cmd: "show ip nat translations", cat: "NAT", desc: "Lists current active NAT/PAT translation sessions (Inside Local:Port to Inside Global:Port)." },
      { cmd: "show access-lists", cat: "Security", desc: "Displays all Standard and Extended Access Control Lists along with packet match (hit) counters." },
      { cmd: "show port-security interface <id>", cat: "Security", desc: "Shows max allowed MACs, current MAC count, violation mode, and whether the port is operational or shutdown." },
      { cmd: "show interface status err-disabled", cat: "Security", desc: "Lists every port currently in an err-disabled state and the specific violation reason." },
      { cmd: "show logging", cat: "Diagnostics", desc: "Displays the internal Syslog buffer, timestamped interface flaps, duplex mismatches, and security events." },
      { cmd: "show ntp status", cat: "Services", desc: "Verifies whether the switch/router clock is synchronized with the master enterprise NTP server." },
      { cmd: "traceroute <ip> source <source-ip>", cat: "Diagnostics", desc: "Traces each router hop to a destination using a specific source interface or loopback." },
      { cmd: "show running-config | include <regex>", cat: "Config", desc: "Quickly filters the running config to find specific keywords without scrolling through thousands of lines." },
      { cmd: "show tech-support", cat: "Kyndryl SOP", desc: "Standard Kyndryl escalation dump: gathers version, running-config, logs, and controller states for L2/L3 ticket handover." }
    ];

    const qaData = [
      { q: "1. What is the difference between Half Duplex and Full Duplex, and what happens if there is a mismatch?", a: "Half Duplex permits transmission in only one direction at a time using CSMA/CD. Full Duplex allows simultaneous two-way transmission. A mismatch (e.g. one side Full, other side Half) causes late collisions, severe throughput drop, and rapidly incrementing CRC errors." },
      { q: "2. Walk me through the DORA process in DHCP and explain why 'ip helper-address' is required.", a: "DORA: Discover (broadcast), Offer (unicast), Request (broadcast), Acknowledge (unicast). Because routers drop broadcast packets by default, 'ip helper-address' converts client broadcast DHCP Discovers into unicast UDP packets forwarded to the central DHCP server across subnets." },
      { q: "3. What is Spanning Tree Protocol (STP), and why are PortFast and BPDU Guard critical?", a: "STP prevents Layer 2 switching loops and broadcast storms. PortFast immediately moves access ports into forwarding mode (skipping listening/learning). BPDU Guard immediately err-disables a PortFast port if a BPDU is received, preventing rogue switches from forming loops." },
      { q: "4. How does a router determine which path to choose when multiple routes exist for the same destination?", a: "Hierarchical criteria: 1) Longest Prefix Match (most specific mask wins, /28 beats /24); 2) Lowest Administrative Distance (Connected=0, Static=1, eBGP=20, OSPF=110); 3) Lowest Metric (cost) if prefix and AD match." },
      { q: "5. What are the common states of OSPF neighbor adjacency, and what causes an adjacency to be stuck in 'ExStart'?", a: "States: Down, Init, 2-Way, ExStart, Exchange, Loading, Full. Neighbors stuck in 'ExStart' is almost always caused by an MTU mismatch between connected interfaces, which prevents Database Descriptor (DBD) packet exchange." }
    ];

    // LocalStorage State Management
    const STORAGE_KEY = "kyndryl_ccna_v11_tracker";
    let appState = { completedLessons: [] };

    function loadState() {
      const saved = localStorage.getItem(STORAGE_KEY);
      if (saved) {
        try { appState = JSON.parse(saved); } catch (e) {}
      }
      renderModules();
      updateProgressUI();
    }

    function saveState() {
      const checkedIds = [];
      document.querySelectorAll('.lesson-checkbox:checked').forEach(box => checkedIds.push(box.id));
      appState.completedLessons = checkedIds;
      localStorage.setItem(STORAGE_KEY, JSON.stringify(appState));
    }

    function updateProgress() {
      document.querySelectorAll('.lesson-checkbox').forEach(box => {
        const row = box.closest('.lesson-row');
        if (box.checked) {
          row.classList.add('completed');
        } else {
          row.classList.remove('completed');
        }
      });
      saveState();
      updateProgressUI();
    }

    function updateProgressUI() {
      const allCheckboxes = document.querySelectorAll('.lesson-checkbox');
      const totalLessons = allCheckboxes.length || 201;
      const count = appState.completedLessons ? appState.completedLessons.length : 0;
      const pct = Math.round((count / totalLessons) * 100);

      document.getElementById('progressPercentage').innerHTML = `${pct}% <span>Done</span>`;
      document.getElementById('progressBar').style.width = `${pct}%`;
      document.getElementById('lessonsCounter').innerHTML = `${count} <span>/ ${totalLessons}</span>`;
      document.getElementById('readinessScore').innerHTML = `${pct} <span>/ 100</span>`;

      // Update module badge counts
      courseModules.forEach((mod, idx) => {
        const modEl = document.getElementById(`module-${idx}`);
        if (!modEl) return;
        const total = mod.lessons.length;
        const checked = modEl.querySelectorAll('.lesson-checkbox:checked').length;
        const pill = document.getElementById(`mod-pill-${idx}`);
        if (pill) pill.innerText = `${checked}/${total} Done`;
      });
    }

    function togglePriorityFilter() {
      priorityOnlyFilter = !priorityOnlyFilter;
      const btn = document.getElementById('priorityToggleBtn');
      if (priorityOnlyFilter) {
        btn.classList.add('active');
        btn.innerText = "⭐ Kyndryl L1 Priority Only (66 Lessons)";
      } else {
        btn.classList.remove('active');
        btn.innerText = "🌐 Show All Lessons (201 Lessons)";
      }
      filterLessons();
    }

    // Render Modules and Lessons with Direct Links & Priority Flagging
    function renderModules(filter = "") {
      const container = document.getElementById('modulesContainer');
      container.innerHTML = "";
      const lowerFilter = filter.toLowerCase().trim();

      let visibleLessonCount = 0;

      courseModules.forEach((mod, modIdx) => {
        const filteredLessons = mod.lessons.filter(l => {
          if (priorityOnlyFilter && !l.isPriority) return false;
          if (!lowerFilter) return true;
          return l.name.toLowerCase().includes(lowerFilter) || mod.title.toLowerCase().includes(lowerFilter);
        });

        if (filteredLessons.length === 0) return;
        visibleLessonCount += filteredLessons.length;

        const card = document.createElement('div');
        card.className = "module-card";
        card.id = `module-${modIdx}`;

        card.innerHTML = `
          <div class="module-header" onclick="toggleModule(${modIdx})">
            <div class="module-title-wrap">
              <span class="module-badge">Module ${modIdx}</span>
              <span class="module-title">${mod.title}</span>
            </div>
            <div class="module-stats">
              <span class="module-counter" id="mod-pill-${modIdx}">0/${mod.lessons.length} Done</span>
              <span class="module-arrow" id="mod-arrow-${modIdx}">▼</span>
            </div>
          </div>
          <div class="lessons-container" id="lessons-${modIdx}" style="${(lowerFilter || priorityOnlyFilter) ? 'display:flex;' : (modIdx <= 1 ? 'display:flex;' : 'display:none;')}">
            ${filteredLessons.map(l => {
              const isDone = appState.completedLessons.includes(l.slug);
              return `
                <div class="lesson-row ${isDone ? 'completed' : ''}">
                  <div class="lesson-left">
                    <input type="checkbox" class="lesson-checkbox" id="${l.slug}" ${isDone ? 'checked' : ''} onchange="updateProgress()">
                    <a href="${l.url}" target="_blank" class="lesson-link" title="Click to open lesson on LinkedIn Learning">${l.name}</a>
                    ${l.isPriority ? `<span class="badge-priority">⭐ Kyndryl L1 Core</span>` : ''}
                  </div>
                  <div class="lesson-right">
                    ${l.duration ? `<span class="lesson-duration">${l.duration}</span>` : ''}
                    <a href="${l.url}" target="_blank" class="btn-sm watch-btn" title="Open lesson in new tab">▶ Watch</a>
                  </div>
                </div>
              `;
            }).join('')}
          </div>
        `;
        container.appendChild(card);
      });
    }

    function toggleModule(idx) {
      const list = document.getElementById(`lessons-${idx}`);
      const arrow = document.getElementById(`mod-arrow-${idx}`);
      if (list.style.display === "none") {
        list.style.display = "flex";
        arrow.innerText = "▲";
      } else {
        list.style.display = "none";
        arrow.innerText = "▼";
      }
    }

    function expandAllModules() {
      courseModules.forEach((_, idx) => {
        const list = document.getElementById(`lessons-${idx}`);
        const arrow = document.getElementById(`mod-arrow-${idx}`);
        if (list) list.style.display = "flex";
        if (arrow) arrow.innerText = "▲";
      });
    }

    function collapseAllModules() {
      courseModules.forEach((_, idx) => {
        const list = document.getElementById(`lessons-${idx}`);
        const arrow = document.getElementById(`mod-arrow-${idx}`);
        if (list) list.style.display = "none";
        if (arrow) arrow.innerText = "▼";
      });
    }

    function filterLessons() {
      const query = document.getElementById('lessonSearchInput').value;
      renderModules(query);
      updateProgressUI();
    }

    function switchTab(tabId) {
      document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
      document.querySelectorAll('.tab-pane').forEach(pane => pane.classList.remove('active'));
      event.target.classList.add('active');
      document.getElementById(tabId).classList.add('active');
    }

    function renderCommands(filter = "") {
      const container = document.getElementById('cmdGridContainer');
      container.innerHTML = "";
      const lower = filter.toLowerCase();
      commandsData.forEach(item => {
        if (!filter || item.cmd.toLowerCase().includes(lower) || item.desc.toLowerCase().includes(lower) || item.cat.toLowerCase().includes(lower)) {
          const card = document.createElement('div');
          card.className = "cmd-card";
          card.innerHTML = `
            <div>
              <div style="display:flex; justify-content:space-between; align-items:center;">
                <span style="font-size:0.75rem; font-weight:700; color:var(--cyan); text-transform:uppercase;">${item.cat}</span>
                <button class="btn-sm" onclick="copyText('${item.cmd}')">Copy</button>
              </div>
              <div class="cmd-syntax mono">${item.cmd}</div>
            </div>
            <p style="font-size:0.83rem; color:var(--text-muted);">${item.desc}</p>
          `;
          container.appendChild(card);
        }
      });
    }

    function filterCommands() {
      renderCommands(document.getElementById('cliSearch').value);
    }

    function copyText(txt) {
      navigator.clipboard.writeText(txt).then(() => {
        event.target.innerText = "Copied!";
        setTimeout(() => event.target.innerText = "Copy", 1200);
      });
    }

    function renderQA() {
      const container = document.getElementById('qaContainer');
      container.innerHTML = "";
      qaData.forEach((item, idx) => {
        const div = document.createElement('div');
        div.className = "qa-card";
        div.innerHTML = `
          <div class="qa-question" onclick="toggleQA(${idx})">
            <span>${item.q}</span>
            <span id="qaArrow${idx}" style="font-size:0.85rem; color:var(--cyan);">▼</span>
          </div>
          <div class="qa-answer" id="qaAns${idx}">${item.a}</div>
        `;
        container.appendChild(div);
      });
    }

    function toggleQA(idx) {
      const ans = document.getElementById(`qaAns${idx}`);
      const arrow = document.getElementById(`qaArrow${idx}`);
      if (ans.classList.contains('open')) {
        ans.classList.remove('open');
        arrow.innerText = "▼";
      } else {
        ans.classList.add('open');
        arrow.innerText = "▲";
      }
    }

    function resetAllProgress() {
      if (confirm("Reset all lesson checkboxes and progress metrics?")) {
        localStorage.removeItem(STORAGE_KEY);
        appState.completedLessons = [];
        loadState();
      }
    }

    window.addEventListener('DOMContentLoaded', () => {
      renderCommands();
      renderQA();
      loadState();
    });
  </script>
</body>
</html>
"""

full_html = html_template.replace('MODULES_PLACEHOLDER', modules_js)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print("Updated index.html with priority tagging and toggle button!")
