import json

with open('clean_modules_with_priority.json', encoding='utf-8') as f:
    modules = json.load(f)

with open('engineer_topics.json', encoding='utf-8') as f:
    engineer_topics = json.load(f)

with open('kevin_wallace_15_courses.json', encoding='utf-8') as f:
    kw_courses = json.load(f)

modules_js = json.dumps(modules)
engineer_topics_js = json.dumps(engineer_topics)
kw_courses_js = json.dumps(kw_courses)

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

    /* MULTI-DEVICE CLI SIMULATOR */
    .device-selector-wrap {
      margin-bottom: 20px;
    }

    .device-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
      gap: 12px;
      margin-bottom: 16px;
    }

    .device-btn {
      background: var(--bg-card);
      border: 1px solid var(--border);
      padding: 12px 14px;
      border-radius: var(--radius-md);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 12px;
      transition: all 0.2s ease;
      text-align: left;
      font-family: inherit;
      color: var(--text-main);
      position: relative;
      overflow: hidden;
    }

    .device-btn:hover {
      border-color: var(--cyan);
      background: var(--bg-card-hover);
      transform: translateY(-2px);
    }

    .device-btn.active {
      background: rgba(56, 189, 248, 0.12);
      border-color: var(--cyan);
      box-shadow: 0 0 16px var(--cyan-glow);
    }

    .device-btn.active::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 4px;
      height: 100%;
      background: var(--cyan);
    }

    .dev-icon {
      font-size: 1.5rem;
      flex-shrink: 0;
    }

    .dev-meta {
      display: flex;
      flex-direction: column;
      gap: 2px;
      overflow: hidden;
    }

    .dev-name {
      font-size: 0.85rem;
      font-weight: 800;
      font-family: 'JetBrains Mono', monospace;
      color: var(--text-main);
      white-space: nowrap;
      text-overflow: ellipsis;
      overflow: hidden;
    }

    .device-btn.active .dev-name {
      color: var(--cyan);
    }

    .dev-role {
      font-size: 0.72rem;
      color: var(--text-muted);
      white-space: nowrap;
      text-overflow: ellipsis;
      overflow: hidden;
    }

    .dev-status {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      font-size: 0.68rem;
      font-weight: 700;
      color: #34d399;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .dev-status-dot {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: #10b981;
      box-shadow: 0 0 6px #10b981;
    }

    /* Interactive Topology Strip */
    .topology-strip {
      background: rgba(13, 20, 36, 0.85);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 12px 18px;
      margin-bottom: 20px;
      display: flex;
      align-items: center;
      gap: 8px;
      overflow-x: auto;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.78rem;
    }

    .topo-label {
      font-size: 0.72rem;
      font-weight: 800;
      color: var(--cyan);
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-right: 6px;
      white-space: nowrap;
    }

    .topo-node {
      padding: 6px 12px;
      border-radius: 6px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border);
      cursor: pointer;
      transition: all 0.2s;
      white-space: nowrap;
      display: flex;
      align-items: center;
      gap: 6px;
      color: var(--text-muted);
    }

    .topo-node:hover {
      border-color: var(--cyan);
      color: white;
    }

    .topo-node.active {
      background: rgba(56, 189, 248, 0.16);
      border-color: var(--cyan);
      color: var(--cyan);
      font-weight: 700;
      box-shadow: 0 0 12px var(--cyan-glow);
    }

    .topo-link {
      color: var(--text-dim);
      font-size: 0.82rem;
      user-select: none;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      white-space: nowrap;
    }

    .topo-link span {
      font-size: 0.65rem;
      color: #475569;
    }

    /* Terminal Window Styles */
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

    .terminal-title-group {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }

    .terminal-title {
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--text-muted);
      font-family: 'JetBrains Mono', monospace;
    }

    .terminal-dev-badge {
      font-size: 0.7rem;
      font-weight: 700;
      background: rgba(56, 189, 248, 0.15);
      color: var(--cyan);
      border: 1px solid rgba(56, 189, 248, 0.3);
      padding: 2px 8px;
      border-radius: 4px;
      font-family: 'JetBrains Mono', monospace;
    }

    .terminal-presets { display: flex; gap: 6px; flex-wrap: wrap; }

    .terminal-body {
      padding: 20px;
      min-height: 400px;
      max-height: 540px;
      overflow-y: auto;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.88rem;
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
      gap: 10px;
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

    /* NETWORK ENGINEER TOPICS & LESSONS TAB STYLING */
    .engineer-header-card {
      background: linear-gradient(135deg, rgba(13, 20, 36, 0.95), rgba(20, 29, 51, 0.85));
      border: 1px solid rgba(56, 189, 248, 0.25);
      border-radius: var(--radius-lg);
      padding: 26px 30px;
      margin-bottom: 24px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
      position: relative;
      overflow: hidden;
    }
    .engineer-header-card::before {
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0; height: 3px;
      background: linear-gradient(90deg, #38bdf8, #6366f1, #10b981);
    }
    .engineer-header-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 20px;
      flex-wrap: wrap;
      margin-bottom: 18px;
    }
    .engineer-header-title h2 {
      font-size: 1.45rem;
      font-weight: 800;
      color: #ffffff;
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .engineer-header-title p {
      color: var(--text-muted);
      font-size: 0.9rem;
      margin-top: 4px;
    }
    .engineer-stats-strip {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
      gap: 12px;
      margin-top: 16px;
      padding-top: 16px;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
    }
    .eng-stat-box {
      background: rgba(0, 0, 0, 0.35);
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-radius: var(--radius-sm);
      padding: 10px 14px;
      text-align: center;
    }
    .eng-stat-num {
      font-family: 'JetBrains Mono', monospace;
      font-size: 1.35rem;
      font-weight: 800;
      color: var(--cyan);
    }
    .eng-stat-label {
      font-size: 0.72rem;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-top: 2px;
    }
    .engineer-progress-wrap {
      margin-top: 16px;
    }
    .eng-prog-meta {
      display: flex;
      justify-content: space-between;
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--text-muted);
      margin-bottom: 6px;
    }

    /* SPRINT FILTER TABS */
    .sprint-filters-wrap {
      display: flex;
      gap: 10px;
      overflow-x: auto;
      padding-bottom: 12px;
      margin-bottom: 20px;
      scrollbar-width: thin;
    }
    .sprint-chip {
      background: var(--bg-card);
      border: 1px solid var(--border);
      color: var(--text-muted);
      padding: 8px 16px;
      border-radius: 99px;
      font-size: 0.82rem;
      font-weight: 700;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .sprint-chip:hover {
      border-color: var(--cyan);
      color: var(--text-main);
      background: var(--bg-card-hover);
    }
    .sprint-chip.active {
      background: rgba(56, 189, 248, 0.14);
      border-color: var(--cyan);
      color: var(--cyan);
      box-shadow: 0 0 14px var(--cyan-glow);
    }

    /* TOPIC CARD */
    .eng-topic-card {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      margin-bottom: 22px;
      overflow: hidden;
      transition: border-color 0.25s, box-shadow 0.25s;
    }
    .eng-topic-card:hover {
      border-color: rgba(56, 189, 248, 0.35);
    }
    .eng-topic-header {
      padding: 20px 24px;
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
      background: rgba(255, 255, 255, 0.015);
      border-bottom: 1px solid transparent;
      user-select: none;
    }
    .eng-topic-header.open {
      border-bottom-color: var(--border);
      background: rgba(56, 189, 248, 0.03);
    }
    .eng-topic-info {
      display: flex;
      align-items: center;
      gap: 16px;
      flex: 1;
      min-width: 0;
    }
    .eng-topic-icon {
      font-size: 1.8rem;
      flex-shrink: 0;
      background: rgba(0, 0, 0, 0.3);
      width: 48px;
      height: 48px;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: var(--radius-sm);
      border: 1px solid rgba(255, 255, 255, 0.06);
    }
    .eng-topic-meta {
      flex: 1;
      min-width: 0;
    }
    .eng-topic-badges {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 4px;
      flex-wrap: wrap;
    }
    .badge-sprint {
      background: rgba(99, 102, 241, 0.15);
      color: #818cf8;
      border: 1px solid rgba(99, 102, 241, 0.3);
      padding: 2px 8px;
      border-radius: 4px;
      font-size: 0.72rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .badge-device-target {
      background: rgba(16, 185, 129, 0.12);
      color: #34d399;
      border: 1px solid rgba(16, 185, 129, 0.3);
      padding: 2px 8px;
      border-radius: 4px;
      font-size: 0.72rem;
      font-weight: 700;
    }
    .eng-topic-title {
      font-size: 1.05rem;
      font-weight: 800;
      color: #ffffff;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .eng-topic-actions-right {
      display: flex;
      align-items: center;
      gap: 14px;
      flex-shrink: 0;
    }
    .eng-topic-counter-pill {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--cyan);
      background: rgba(56, 189, 248, 0.1);
      border: 1px solid rgba(56, 189, 248, 0.25);
      padding: 4px 10px;
      border-radius: 99px;
    }
    .eng-topic-arrow {
      color: var(--text-muted);
      font-size: 0.85rem;
      transition: transform 0.2s;
    }

    /* TOPIC BODY */
    .eng-topic-body {
      padding: 22px 24px;
      display: flex;
      flex-direction: column;
      gap: 18px;
      background: rgba(0, 0, 0, 0.15);
    }

    /* NOC CALLOUT */
    .eng-noc-callout {
      background: rgba(56, 189, 248, 0.05);
      border-left: 3px solid var(--cyan);
      border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
      padding: 12px 16px;
      font-size: 0.86rem;
      color: #e2e8f0;
      line-height: 1.5;
    }
    .eng-noc-callout strong {
      color: var(--cyan);
    }

    /* COMMANDS SHOWCASE */
    .eng-cmds-wrap {
      background: rgba(0, 0, 0, 0.35);
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-radius: var(--radius-sm);
      padding: 16px;
    }
    .eng-cmds-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
      flex-wrap: wrap;
      gap: 10px;
    }
    .eng-cmds-header span {
      font-size: 0.78rem;
      font-weight: 800;
      color: var(--emerald);
      text-transform: uppercase;
      letter-spacing: 0.8px;
    }
    .eng-cmds-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 10px;
    }
    .eng-cmd-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid rgba(255, 255, 255, 0.04);
      border-radius: 6px;
      padding: 8px 12px;
      gap: 10px;
    }
    .eng-cmd-text {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.82rem;
      color: #38bdf8;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }
    .eng-cmd-desc {
      font-size: 0.74rem;
      color: var(--text-dim);
      margin-top: 2px;
    }

    /* TOPIC LESSONS WRAPPER */
    .eng-lessons-wrap {
      display: flex;
      flex-direction: column;
      gap: 8px;
    }


    /* CAREER ROADMAP & BANGALORE SALARY PROGRESSION STYLES */
    .roadmap-hero {
      background: linear-gradient(135deg, rgba(15, 23, 42, 0.95), rgba(30, 41, 59, 0.9));
      border: 1px solid rgba(56, 189, 248, 0.3);
      border-radius: var(--radius-lg);
      padding: 28px 32px;
      margin-bottom: 24px;
      position: relative;
      overflow: hidden;
      box-shadow: 0 12px 32px rgba(0, 0, 0, 0.4);
    }
    .roadmap-hero::before {
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0; height: 3px;
      background: linear-gradient(90deg, #10b981, #38bdf8, #6366f1, #f59e0b);
    }
    .roadmap-hero-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 20px;
      flex-wrap: wrap;
      margin-bottom: 20px;
    }
    .roadmap-hero-title h2 {
      font-size: 1.5rem;
      font-weight: 800;
      color: #ffffff;
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .roadmap-hero-title p {
      color: var(--text-muted);
      font-size: 0.92rem;
      margin-top: 4px;
    }

    /* CTC PROGRESSION LADDER */
    .ctc-ladder-wrap {
      margin-top: 20px;
      padding-top: 20px;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
    }
    .ctc-ladder-title {
      font-size: 0.85rem;
      font-weight: 800;
      color: var(--cyan);
      text-transform: uppercase;
      letter-spacing: 0.8px;
      margin-bottom: 14px;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .ctc-ladder-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 12px;
    }
    .ctc-node {
      background: rgba(0, 0, 0, 0.4);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: var(--radius-md);
      padding: 14px 16px;
      display: flex;
      flex-direction: column;
      gap: 6px;
      position: relative;
      transition: all 0.25s ease;
    }
    .ctc-node:hover {
      border-color: rgba(56, 189, 248, 0.4);
      transform: translateY(-2px);
    }
    .ctc-node.current {
      border-color: #f43f5e;
      background: rgba(244, 63, 94, 0.08);
    }
    .ctc-node.target {
      border-color: #10b981;
      background: rgba(16, 185, 129, 0.1);
      box-shadow: 0 0 20px rgba(16, 185, 129, 0.2);
    }
    .ctc-node-tag {
      font-size: 0.68rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      display: inline-block;
    }
    .ctc-node.current .ctc-node-tag { color: #fb7185; }
    .ctc-node.target .ctc-node-tag { color: #34d399; }
    .ctc-node-salary {
      font-family: 'JetBrains Mono', monospace;
      font-size: 1.3rem;
      font-weight: 800;
      color: #ffffff;
    }
    .ctc-node.current .ctc-node-salary { color: #fda4af; }
    .ctc-node.target .ctc-node-salary { color: #34d399; }
    .ctc-node-role {
      font-size: 0.8rem;
      font-weight: 700;
      color: #e2e8f0;
      line-height: 1.3;
    }
    .ctc-node-skills {
      font-size: 0.72rem;
      color: var(--text-dim);
      margin-top: 4px;
    }

    /* PHASES CONTAINER & CARDS */
    .roadmap-section-title {
      font-size: 1.18rem;
      font-weight: 800;
      color: #ffffff;
      margin: 28px 0 16px;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .phases-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
      gap: 18px;
      margin-bottom: 28px;
    }
    .phase-card {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 22px 24px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 16px;
      transition: all 0.2s ease;
      position: relative;
    }
    .phase-card:hover {
      border-color: rgba(56, 189, 248, 0.35);
      background: var(--bg-card-hover);
    }
    .phase-card.priority-high {
      border-color: rgba(16, 185, 129, 0.4);
    }
    .phase-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 12px;
    }
    .phase-tag-wrap {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
      margin-bottom: 6px;
    }
    .phase-number-badge {
      font-size: 0.72rem;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: 4px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .phase-number-badge.p1 { background: rgba(56, 189, 248, 0.15); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.3); }
    .phase-number-badge.p2 { background: rgba(16, 185, 129, 0.18); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.4); }
    .phase-number-badge.p3 { background: rgba(245, 158, 11, 0.15); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.3); }
    .phase-number-badge.p4 { background: rgba(99, 102, 241, 0.15); color: #818cf8; border: 1px solid rgba(99, 102, 241, 0.3); }
    .phase-number-badge.p5 { background: rgba(236, 72, 153, 0.15); color: #f472b6; border: 1px solid rgba(236, 72, 153, 0.3); }
    
    .phase-timeline {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--text-muted);
      background: rgba(0, 0, 0, 0.35);
      padding: 3px 8px;
      border-radius: 4px;
    }
    .phase-title {
      font-size: 1.1rem;
      font-weight: 800;
      color: #ffffff;
    }
    .phase-skills-pill-wrap {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-top: 8px;
    }
    .skill-pill {
      font-size: 0.72rem;
      font-weight: 600;
      color: var(--text-muted);
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.07);
      padding: 2px 8px;
      border-radius: 4px;
    }
    .phase-courses-list {
      display: flex;
      flex-direction: column;
      gap: 8px;
      background: rgba(0, 0, 0, 0.25);
      border: 1px solid rgba(255, 255, 255, 0.04);
      border-radius: var(--radius-sm);
      padding: 12px;
    }
    .phase-course-item {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 10px;
      font-size: 0.85rem;
    }
    .phase-course-item label {
      display: flex;
      align-items: center;
      gap: 10px;
      color: var(--text-main);
      cursor: pointer;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
      flex: 1;
    }
    .phase-course-item a {
      color: var(--cyan);
      text-decoration: none;
      font-size: 0.74rem;
      font-weight: 700;
      background: rgba(56, 189, 248, 0.1);
      border: 1px solid rgba(56, 189, 248, 0.25);
      padding: 3px 8px;
      border-radius: 4px;
      white-space: nowrap;
      flex-shrink: 0;
      transition: all 0.2s;
    }
    .phase-course-item a:hover {
      background: rgba(56, 189, 248, 0.2);
      border-color: var(--cyan);
    }
    .phase-goal-note {
      font-size: 0.8rem;
      color: #cbd5e1;
      border-left: 2px solid var(--indigo);
      padding-left: 10px;
      line-height: 1.4;
    }

    /* PRIORITIES & SCHEDULE DUAL GRID */
    .dual-roadmap-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(420px, 1fr));
      gap: 20px;
      margin-bottom: 28px;
    }
    .roadmap-subcard {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 24px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }
    .priority-list {
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    .priority-row {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 8px 12px;
      background: rgba(0, 0, 0, 0.25);
      border: 1px solid rgba(255, 255, 255, 0.04);
      border-radius: 6px;
    }
    .priority-rank {
      width: 24px;
      height: 24px;
      border-radius: 50%;
      background: rgba(56, 189, 248, 0.15);
      color: var(--cyan);
      font-weight: 800;
      font-size: 0.78rem;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }
    .priority-row:nth-child(1) .priority-rank { background: #ef4444; color: white; }
    .priority-row:nth-child(2) .priority-rank { background: #10b981; color: white; }
    .priority-row:nth-child(3) .priority-rank { background: #38bdf8; color: white; }
    .priority-name {
      font-weight: 700;
      font-size: 0.85rem;
      color: #ffffff;
      flex: 1;
    }
    .priority-reason {
      font-size: 0.75rem;
      color: var(--text-dim);
    }

    /* WEEKLY SCHEDULE GRID */
    .schedule-day-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 9px 12px;
      border-radius: 6px;
      background: rgba(0, 0, 0, 0.25);
      border: 1px solid rgba(255, 255, 255, 0.04);
      font-size: 0.85rem;
    }
    .schedule-day-row.is-today {
      border-color: var(--cyan);
      background: rgba(56, 189, 248, 0.08);
      box-shadow: 0 0 12px var(--cyan-glow);
    }
    .day-badge {
      font-family: 'JetBrains Mono', monospace;
      font-weight: 800;
      font-size: 0.75rem;
      width: 85px;
      color: var(--text-muted);
    }
    .schedule-day-row.is-today .day-badge { color: var(--cyan); }
    .day-activity {
      font-weight: 600;
      color: var(--text-main);
      flex: 1;
    }
    .today-pill {
      font-size: 0.65rem;
      font-weight: 800;
      text-transform: uppercase;
      background: var(--cyan);
      color: #070b14;
      padding: 2px 6px;
      border-radius: 99px;
    }

    /* ACTION PLAN CARD */
    .action-checklist {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .action-step-item {
      display: flex;
      align-items: flex-start;
      gap: 12px;
      padding: 12px 14px;
      background: rgba(0, 0, 0, 0.3);
      border: 1px solid rgba(255, 255, 255, 0.05);
      border-radius: 8px;
      transition: all 0.2s;
    }
    .action-step-item.checked {
      background: rgba(16, 185, 129, 0.06);
      border-color: rgba(16, 185, 129, 0.3);
    }
    .action-step-item.checked .action-text {
      color: var(--text-muted);
      text-decoration: line-through;
    }
    .action-text strong { color: #ffffff; }
    .action-text {
      font-size: 0.86rem;
      color: #cbd5e1;
      line-height: 1.45;
    }


    /* KEVIN WALLACE 15-COURSE CATALOG STYLES */
    .kw-package-box {
      background: rgba(16, 185, 129, 0.08);
      border: 1px solid rgba(16, 185, 129, 0.25);
      border-radius: var(--radius-sm);
      padding: 10px 14px;
      margin-top: 10px;
    }
    .kw-package-tag {
      font-size: 0.82rem;
      color: #34d399;
      font-weight: 800;
    }
    .kw-package-role {
      font-size: 0.72rem;
      color: #94a3b8;
      background: rgba(0, 0, 0, 0.4);
      padding: 2px 8px;
      border-radius: 4px;
      border: 1px solid var(--border);
    }
    .phase-package-banner {
      background: rgba(16, 185, 129, 0.12);
      border: 1px solid rgba(16, 185, 129, 0.3);
      color: #34d399;
      padding: 7px 12px;
      border-radius: var(--radius-sm);
      font-size: 0.78rem;
      font-weight: 700;
      margin: 10px 0;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .kw-catalog-wrap {
      margin-top: 36px;
      margin-bottom: 30px;
    }
    .kw-catalog-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
      margin-bottom: 18px;
    }
    .kw-catalog-title {
      font-size: 1.25rem;
      font-weight: 800;
      color: #ffffff;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .kw-filter-chips {
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 8px;
      scrollbar-width: thin;
      margin-bottom: 16px;
    }
    .kw-filter-chip {
      background: var(--bg-card);
      border: 1px solid var(--border);
      color: var(--text-muted);
      padding: 6px 14px;
      border-radius: 99px;
      font-size: 0.78rem;
      font-weight: 700;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s;
    }
    .kw-filter-chip:hover {
      border-color: var(--cyan);
      color: var(--text-main);
    }
    .kw-filter-chip.active {
      background: rgba(56, 189, 248, 0.14);
      border-color: var(--cyan);
      color: var(--cyan);
      box-shadow: 0 0 12px var(--cyan-glow);
    }
    .kw-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
      gap: 16px;
    }
    .kw-card {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 20px 22px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 14px;
      transition: all 0.2s ease;
    }
    .kw-card:hover {
      border-color: rgba(56, 189, 248, 0.35);
      transform: translateY(-2px);
      background: var(--bg-card-hover);
    }
    .kw-card-top {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 10px;
    }
    .kw-card-badges {
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
      margin-bottom: 6px;
    }
    .kw-badge-tier {
      font-size: 0.68rem;
      font-weight: 800;
      padding: 2px 7px;
      border-radius: 4px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .kw-badge-tier.tier-foundations { background: rgba(56, 189, 248, 0.12); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.3); }
    .kw-badge-tier.tier-ccna { background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.35); }
    .kw-badge-tier.tier-support { background: rgba(245, 158, 11, 0.12); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.3); }
    .kw-badge-tier.tier-ccnp { background: rgba(99, 102, 241, 0.15); color: #818cf8; border: 1px solid rgba(99, 102, 241, 0.35); }

    .kw-badge-cert {
      font-size: 0.68rem;
      font-weight: 700;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.08);
      color: #e2e8f0;
      padding: 2px 7px;
      border-radius: 4px;
    }
    .kw-duration-pill {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--cyan);
      background: rgba(0, 0, 0, 0.35);
      padding: 3px 8px;
      border-radius: 4px;
      white-space: nowrap;
    }
    .kw-course-title {
      font-size: 1.02rem;
      font-weight: 800;
      color: #ffffff;
      line-height: 1.35;
    }
    .kw-course-desc {
      font-size: 0.8rem;
      color: var(--text-muted);
      line-height: 1.45;
    }
    .kw-modules-box {
      background: rgba(0, 0, 0, 0.3);
      border: 1px solid rgba(255, 255, 255, 0.05);
      border-radius: var(--radius-sm);
      padding: 10px 12px;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }
    .kw-modules-header {
      font-size: 0.72rem;
      font-weight: 800;
      color: var(--text-dim);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .kw-modules-list {
      display: flex;
      flex-direction: column;
      gap: 3px;
      margin-top: 6px;
    }
    .kw-mod-item {
      font-size: 0.75rem;
      color: #cbd5e1;
      display: flex;
      align-items: baseline;
      gap: 6px;
    }
    .kw-skills-strip {
      display: flex;
      flex-wrap: wrap;
      gap: 5px;
    }
    .kw-skill-tag {
      font-size: 0.68rem;
      color: var(--text-dim);
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.06);
      padding: 1px 6px;
      border-radius: 4px;
    }

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
      <button class="tab-btn" onclick="switchTab('engineerTab')">🎓 Network Engineer Topics & Lessons</button>
      <button class="tab-btn" onclick="switchTab('roadmapTab')">🚀 Career Roadmap & Bangalore Salary Path</button>
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

    <!-- TAB: CAREER ROADMAP & BANGALORE SALARY PROGRESSION (₹3.6L TO ₹16L+) -->
    <div id="roadmapTab" class="tab-pane">
      
      <!-- Executive Roadmap Hero Banner -->
      <div class="roadmap-hero">
        <div class="roadmap-hero-top">
          <div class="roadmap-hero-title">
            <h2><span>🚀</span> Network Engineer Career Roadmap — Bangalore Market Path</h2>
            <p>From Kyndryl L1 NOC (₹3.6 LPA) to High-Paying Network Engineering in Bangalore (₹4.5–7L Next Switch ➔ ₹16L+ Specialist)</p>
          </div>
          <div style="display:flex; gap:10px; flex-wrap:wrap;">
            <a href="https://shaikmdnisaar.github.io/kyndryl-l1-mastery/" target="_blank" class="btn-sm primary">🌐 Live Deployment</a>
            <button class="btn-sm" onclick="resetRoadmapProgress()">↺ Reset Action Plan</button>
          </div>
        </div>

        <!-- Bangalore CTC Ladder -->
        <div class="ctc-ladder-wrap">
          <div class="ctc-ladder-title">
            <span>📈 Bangalore Annual CTC Progression Ladder</span>
          </div>
          <div class="ctc-ladder-grid">
            <div class="ctc-node current">
              <span class="ctc-node-tag">Current Role</span>
              <div class="ctc-node-salary">₹3.6 LPA</div>
              <div class="ctc-node-role">L1 Network Support</div>
              <div class="ctc-node-skills">Kyndryl NOC, ticket dispatch, basic show commands</div>
            </div>
            <div class="ctc-node target">
              <span class="ctc-node-tag">⭐ Next Switch (Target)</span>
              <div class="ctc-node-salary">₹4.5–7.0 LPA</div>
              <div class="ctc-node-role">L1/L2 Network Engineer</div>
              <div class="ctc-node-skills">CCNA 200-301, VLANs, OSPF, Packet Tracer & Wireshark triage</div>
            </div>
            <div class="ctc-node">
              <span class="ctc-node-tag">Intermediate</span>
              <div class="ctc-node-salary">₹6.0–10.0 LPA</div>
              <div class="ctc-node-role">L2 Enterprise R&S</div>
              <div class="ctc-node-skills">HSRP, EtherChannel, multi-vendor enterprise NOC</div>
            </div>
            <div class="ctc-node">
              <span class="ctc-node-tag">Specialization</span>
              <div class="ctc-node-salary">₹7.0–12.0 LPA</div>
              <div class="ctc-node-role">Network Security</div>
              <div class="ctc-node-skills">Palo Alto, Fortinet, ASA firewalls, IPsec VPNs, ZTNA</div>
            </div>
            <div class="ctc-node">
              <span class="ctc-node-tag">Advanced</span>
              <div class="ctc-node-salary">₹9.0–16.0+ LPA</div>
              <div class="ctc-node-role">CCNP Enterprise</div>
              <div class="ctc-node-skills">ENCOR/ENARSI, BGP multi-homing, SD-WAN, architecture</div>
            </div>
            <div class="ctc-node">
              <span class="ctc-node-tag">Automation</span>
              <div class="ctc-node-salary">₹8.0–16.0+ LPA</div>
              <div class="ctc-node-role">Network Automation</div>
              <div class="ctc-node-skills">Python (Netmiko), REST APIs, Ansible, Cisco DevNet</div>
            </div>
          </div>
        </div>
      </div>

      <!-- 5-Phase Structured Learning Path Grid -->
      <div class="roadmap-section-title">
        <span>📚 The 5-Phase Curriculum (Direct One-Click LinkedIn Learning Links)</span>
      </div>

      <div class="phases-grid">

        <!-- Phase 1 -->
        <div class="phase-card">
          <div>
            <div class="phase-header">
              <div class="phase-tag-wrap">
                <span class="phase-number-badge p1">Phase 1</span>
                <span style="font-size:0.75rem; color:#38bdf8; font-weight:700;">Start Here</span>
              </div>
              <span class="phase-timeline">Weeks 1–3</span>
            </div>
            <div class="phase-title">Networking Fundamentals</div>
            <div class="phase-skills-pill-wrap">
              <span class="skill-pill">OSI 7 Layers</span>
              <span class="skill-pill">TCP/IP</span>
              <span class="skill-pill">IPv4 Subnetting</span>
              <span class="skill-pill">DNS / DHCP</span>
              <span class="skill-pill">TCP vs UDP</span>
            </div>
          </div>

          <div class="phase-courses-list">
            <div class="phase-course-item">
              <label><input type="checkbox" class="roadmap-checkbox" id="rc_p1_1" onchange="saveRoadmapCheckboxes()"> Networking Basics</label>
              <a href="https://www.linkedin.com/learning/search?keywords=Networking+Foundations+Networking+Basics&u=76281980" target="_blank">▶ Watch</a>
            </div>
            <div class="phase-course-item">
              <label><input type="checkbox" class="roadmap-checkbox" id="rc_p1_2" onchange="saveRoadmapCheckboxes()"> Learning IP Addressing</label>
              <a href="https://www.linkedin.com/learning/search?keywords=Learning+IP+Addressing&u=76281980" target="_blank">▶ Watch</a>
            </div>
            <div class="phase-course-item">
              <label><input type="checkbox" class="roadmap-checkbox" id="rc_p1_3" onchange="saveRoadmapCheckboxes()"> Learning Subnetting</label>
              <a href="https://www.linkedin.com/learning/search?keywords=Learning+Subnetting&u=76281980" target="_blank">▶ Watch</a>
            </div>
            <div class="phase-course-item">
              <label><input type="checkbox" class="roadmap-checkbox" id="rc_p1_4" onchange="saveRoadmapCheckboxes()"> Cisco Foundations: IP Addressing</label>
              <a href="https://www.linkedin.com/learning/search?keywords=Cisco+Networking+Foundations+IP+Addressing&u=76281980" target="_blank">▶ Watch</a>
            </div>
          </div>

          <div class="phase-goal-note">
            <strong>Practical Goal:</strong> Master mental CIDR calculation (/24 to /30) under 10 seconds and packet headers.
          </div>
        </div>

        <!-- Phase 2 -->
        <div class="phase-card priority-high">
          <div>
            <div class="phase-header">
              <div class="phase-tag-wrap">
                <span class="phase-number-badge p2">Phase 2</span>
                <span style="font-size:0.75rem; color:#34d399; font-weight:800;">⭐ Highest Priority</span>
              </div>
              <span class="phase-timeline">Weeks 4–10</span>
            </div>
            <div class="phase-title">Cisco Networking & CCNA</div>
            <div class="phase-package-banner">
              <span>💰</span> <strong>CTC Target:</strong> ₹5.5–8.0 LPA · <em>Network Engineer L2 / Cisco Specialist</em>
            </div>
            <div class="phase-skills-pill-wrap">
              <span class="skill-pill">VLANs & Trunks</span>
              <span class="skill-pill">STP / RSTP</span>
              <span class="skill-pill">Inter-VLAN SVI</span>
              <span class="skill-pill">OSPFv2</span>
              <span class="skill-pill">ACLs & NAT</span>
              <span class="skill-pill">Packet Tracer</span>
            </div>
          </div>

          <div class="phase-courses-list">
            <div class="phase-course-item">
              <label><input type="checkbox" class="roadmap-checkbox" id="rc_p2_1" onchange="saveRoadmapCheckboxes()"> Cisco Foundations: Fundamentals</label>
              <a href="https://www.linkedin.com/learning/search?keywords=Cisco+Networking+Foundations+Fundamentals+of+Cisco+Networking&u=76281980" target="_blank">▶ Watch</a>
            </div>
            <div class="phase-course-item">
              <label><input type="checkbox" class="roadmap-checkbox" id="rc_p2_2" onchange="saveRoadmapCheckboxes()"> Switching & Routing Foundations</label>
              <a href="https://www.linkedin.com/learning/search?keywords=Cisco+Networking+Foundations+Switching+and+Routing&u=76281980" target="_blank">▶ Watch</a>
            </div>
            <div class="phase-course-item">
              <label><input type="checkbox" class="roadmap-checkbox" id="rc_p2_3" onchange="saveRoadmapCheckboxes()"> Wireless, Services, Security</label>
              <a href="https://www.linkedin.com/learning/search?keywords=Cisco+Networking+Foundations+Wireless+Networks+Services+Security+Virtualization&u=76281980" target="_blank">▶ Watch</a>
            </div>
            <div class="phase-course-item">
              <label><input type="checkbox" class="roadmap-checkbox" id="rc_p2_4" onchange="saveRoadmapCheckboxes()"> Wireless Networking Training</label>
              <a href="https://www.linkedin.com/learning/search?keywords=Wireless+Networking+Essential+Training&u=76281980" target="_blank">▶ Watch</a>
            </div>
            <div class="phase-course-item">
              <label><input type="checkbox" class="roadmap-checkbox" id="rc_p2_5" onchange="saveRoadmapCheckboxes()"> Kevin Wallace CCNA (201 Lessons)</label>
              <a href="https://www.linkedin.com/learning/cisco-certified-network-associate-ccna-v1-1-200-301-cert-prep/diving-into-the-course?u=76281980" target="_blank">▶ Watch</a>
            </div>
          </div>

          <div class="phase-goal-note">
            <strong>Practical Goal:</strong> Clear CCNA 200-301 and build 3 showcase enterprise topologies in Cisco Packet Tracer.
          </div>
        </div>

        <!-- Phase 3 -->
        <div class="phase-card">
          <div>
            <div class="phase-header">
              <div class="phase-tag-wrap">
                <span class="phase-number-badge p3">Phase 3</span>
                <span style="font-size:0.75rem; color:#fbbf24; font-weight:700;">Specialization</span>
              </div>
              <span class="phase-timeline">Months 3–4</span>
            </div>
            <div class="phase-title">Network Security & Firewalls</div>
            <div class="phase-package-banner">
              <span>💰</span> <strong>CTC Target:</strong> ₹5.0–7.5 LPA · <em>SOC Tier 1 / Security Support Specialist</em>
            </div>
            <div class="phase-skills-pill-wrap">
              <span class="skill-pill">Extended ACLs</span>
              <span class="skill-pill">Firewalls (ASA/Palo)</span>
              <span class="skill-pill">IPsec VPNs</span>
              <span class="skill-pill">Port Security</span>
              <span class="skill-pill">DAI & Snooping</span>
            </div>
          </div>

          <div class="phase-courses-list">
            <div class="phase-course-item">
              <label><input type="checkbox" class="roadmap-checkbox" id="rc_p3_1" onchange="saveRoadmapCheckboxes()"> Cisco CCST Cybersecurity Cert Prep</label>
              <a href="https://www.linkedin.com/learning/search?keywords=Cisco+Certified+Support+Technician+CCST+Cybersecurity+Cert+Prep&u=76281980" target="_blank">▶ Watch</a>
            </div>
            <div class="phase-course-item">
              <label><input type="checkbox" class="roadmap-checkbox" id="rc_p3_2" onchange="saveRoadmapCheckboxes()"> CCNA Cybersecurity / CyberOps</label>
              <a href="https://www.linkedin.com/learning/search?keywords=CCNA+Cybersecurity+Cert+Prep&u=76281980" target="_blank">▶ Watch</a>
            </div>
          </div>

          <div class="phase-goal-note">
            <strong>Practical Goal:</strong> Build foundation for Security Operations (SOC/NOC), Next-Gen Firewalls, and IPsec site tunnels.
          </div>
        </div>

        <!-- Phase 4 -->
        <div class="phase-card">
          <div>
            <div class="phase-header">
              <div class="phase-tag-wrap">
                <span class="phase-number-badge p4">Phase 4</span>
                <span style="font-size:0.75rem; color:#818cf8; font-weight:700;">Enterprise Tier</span>
              </div>
              <span class="phase-timeline">Months 5–8+</span>
            </div>
            <div class="phase-title">Advanced Networking (CCNP)</div>
            <div class="phase-package-banner">
              <span>💰</span> <strong>CTC Target:</strong> ₹7.0–13.0 LPA · <em>Senior Network Engineer / L3 Escalations</em>
            </div>
            <div class="phase-skills-pill-wrap">
              <span class="skill-pill">BGP Peering</span>
              <span class="skill-pill">Multi-Area OSPF</span>
              <span class="skill-pill">SD-WAN</span>
              <span class="skill-pill">QoS & VRFs</span>
              <span class="skill-pill">L3 Escalations</span>
            </div>
          </div>

          <div class="phase-courses-list">
            <div class="phase-course-item">
              <label><input type="checkbox" class="roadmap-checkbox" id="rc_p4_1" onchange="saveRoadmapCheckboxes()"> Cisco CCNP Enterprise: ENCOR (350-401)</label>
              <a href="https://www.linkedin.com/learning/search?keywords=Cisco+CCNP+Enterprise+ENCOR+350-401+Cert+Prep&u=76281980" target="_blank">▶ Watch</a>
            </div>
            <div class="phase-course-item">
              <label><input type="checkbox" class="roadmap-checkbox" id="rc_p4_2" onchange="saveRoadmapCheckboxes()"> Cisco CCNP Enterprise: ENARSI (300-410)</label>
              <a href="https://www.linkedin.com/learning/search?keywords=Cisco+CCNP+Enterprise+ENARSI+300-410+Cert+Prep&u=76281980" target="_blank">▶ Watch</a>
            </div>
          </div>

          <div class="phase-goal-note">
            <strong>Practical Goal:</strong> Target ₹9–16+ LPA Senior Enterprise roles at Cisco, Juniper, Akamai, or Fortune 500 banks.
          </div>
        </div>

        <!-- Phase 5 -->
        <div class="phase-card">
          <div>
            <div class="phase-header">
              <div class="phase-tag-wrap">
                <span class="phase-number-badge p5">Phase 5</span>
                <span style="font-size:0.75rem; color:#f472b6; font-weight:700;">Future-Ready</span>
              </div>
              <span class="phase-timeline">Months 6–10+</span>
            </div>
            <div class="phase-title">Network Automation (DevNet)</div>
            <div class="phase-package-banner">
              <span>💰</span> <strong>CTC Target:</strong> ₹10.0–16.0+ LPA · <em>Network Automation Engineer / NetDevOps</em>
            </div>
            <div class="phase-skills-pill-wrap">
              <span class="skill-pill">Python Netmiko</span>
              <span class="skill-pill">REST APIs</span>
              <span class="skill-pill">JSON / YAML</span>
              <span class="skill-pill">Git</span>
              <span class="skill-pill">Ansible Playbooks</span>
            </div>
          </div>

          <div class="phase-courses-list">
            <div class="phase-course-item">
              <label><input type="checkbox" class="roadmap-checkbox" id="rc_p5_1" onchange="saveRoadmapCheckboxes()"> Cisco DevNet Associate (200-901 DEVASC)</label>
              <a href="https://www.linkedin.com/learning/search?keywords=Cisco+Certified+DevNet+Associate+DEVASC+200-901+Cert+Prep&u=76281980" target="_blank">▶ Watch</a>
            </div>
          </div>

          <div class="phase-goal-note">
            <strong>Practical Goal:</strong> Automate configuration audits, backup routines, and telemetry to transition into NetDevOps.
          </div>
        </div>

      </div>


      <!-- Kevin Wallace 15-Course LinkedIn Learning Master Library -->
      <div class="kw-catalog-wrap">
        <div class="kw-catalog-header">
          <div>
            <div class="kw-catalog-title">
              <span>📚</span> Kevin Wallace 15-Course Master Library (LinkedIn Learning)
            </div>
            <p style="font-size:0.82rem; color:var(--text-muted); margin-top:3px;">
              Complete catalog with course syllabi, module breakdowns, durations, and direct Toronto Public Library SSO links.
            </p>
          </div>
          <div style="display:flex; gap:8px;">
            <button class="btn-sm" onclick="expandAllKWModules()">Expand Modules</button>
            <button class="btn-sm" onclick="collapseAllKWModules()">Collapse</button>
          </div>
        </div>

        <div class="tracker-toolbar" style="margin-bottom:14px;">
          <input type="text" id="kwSearchInput" class="search-input" placeholder="🔍 Search across 15 Kevin Wallace courses (e.g. Subnetting, BGP, ENCOR, Switching, Wireless, CCST)..." oninput="renderKWCatalogUI()">
        </div>

        <div class="kw-filter-chips" id="kwFilterChips">
          <button class="kw-filter-chip active" onclick="setKWTierFilter('all')">🌟 All 15 Courses</button>
          <button class="kw-filter-chip" onclick="setKWTierFilter('tier-foundations')">🟢 Foundations (Courses 1–5)</button>
          <button class="kw-filter-chip" onclick="setKWTierFilter('tier-ccna')">🟡 Cisco CCNA Track (Courses 6–9)</button>
          <button class="kw-filter-chip" onclick="setKWTierFilter('tier-support')">🛡️ Support & Security (Courses 10–11)</button>
          <button class="kw-filter-chip" onclick="setKWTierFilter('tier-ccnp')">🟣 Enterprise CCNP Tier (Courses 12–15)</button>
        </div>

        <div class="kw-grid" id="kwCoursesContainer">
          <!-- Rendered dynamically by JavaScript -->
        </div>
      </div>


            <!-- Dual Grid: What to Prioritize & Weekly Study Routine -->
      <div class="dual-roadmap-grid">

        <!-- Priority Matrix -->
        <div class="roadmap-subcard">
          <h3 style="font-size:1.1rem; font-weight:800; color:#ffffff; display:flex; align-items:center; gap:8px;">
            <span>🎯</span> Ranked Skill Prioritization Matrix
          </h3>
          <p style="font-size:0.8rem; color:var(--text-muted);">
            Focus your energy where the return on investment (ROI) for Bangalore job offers is highest:
          </p>

          <div class="priority-list">
            <div class="priority-row">
              <span class="priority-rank">1</span>
              <div>
                <div class="priority-name">IP Addressing & Subnetting</div>
                <div class="priority-reason">The gatekeeper question in 95% of L1/L2 technical rounds. Zero hesitation allowed.</div>
              </div>
            </div>
            <div class="priority-row">
              <span class="priority-rank">2</span>
              <div>
                <div class="priority-name">CCNA 200-301 Certification Baseline</div>
                <div class="priority-reason">Validates full stack understanding above basic service-desk operators.</div>
              </div>
            </div>
            <div class="priority-row">
              <span class="priority-rank">3</span>
              <div>
                <div class="priority-name">Wireshark & Packet Triage</div>
                <div class="priority-reason">Demonstrates real-world problem-solving (TCP resets, ARP drops, DNS failures).</div>
              </div>
            </div>
            <div class="priority-row">
              <span class="priority-rank">4</span>
              <div>
                <div class="priority-name">Routing & Switching Labs (Packet Tracer)</div>
                <div class="priority-reason">Builds concrete confidence to narrate troubleshooting stories in interviews.</div>
              </div>
            </div>
            <div class="priority-row">
              <span class="priority-rank">5</span>
              <div>
                <div class="priority-name">Firewalls, VPNs & Security Specialization</div>
                <div class="priority-reason">Adds an instant ₹1.5–2.5 LPA premium over generic network support profiles.</div>
              </div>
            </div>
            <div class="priority-row">
              <span class="priority-rank">6</span>
              <div>
                <div class="priority-name">CCNP Enterprise (ENCOR / ENARSI)</div>
                <div class="priority-reason">Key to breaking into ₹10–16+ LPA enterprise architecture after 2-3 years.</div>
              </div>
            </div>
            <div class="priority-row">
              <span class="priority-rank">7</span>
              <div>
                <div class="priority-name">Python & Network Automation</div>
                <div class="priority-reason">High-leverage differentiator that future-proofs your engineering career.</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Weekly Study Routine -->
        <div class="roadmap-subcard">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <h3 style="font-size:1.1rem; font-weight:800; color:#ffffff; display:flex; align-items:center; gap:8px;">
              <span>📅</span> Weekly 1.5–2 Hour Daily Study Routine
            </h3>
            <span style="font-size:0.72rem; color:var(--cyan); font-weight:700;">Consistent Daily Habit</span>
          </div>
          <p style="font-size:0.8rem; color:var(--text-muted);">
            Suggested routine tailored to work alongside your Kyndryl NOC shift schedule:
          </p>

          <div style="display:flex; flex-direction:column; gap:8px;" id="weeklyScheduleWrap">
            <div class="schedule-day-row" id="day-row-1">
              <span class="day-badge">Monday</span>
              <span class="day-activity">Networking Theory & Architecture</span>
            </div>
            <div class="schedule-day-row" id="day-row-2">
              <span class="day-badge">Tuesday</span>
              <span class="day-activity">IP Addressing & Mental Subnetting Drills</span>
            </div>
            <div class="schedule-day-row" id="day-row-3">
              <span class="day-badge">Wednesday</span>
              <span class="day-activity">CCNA Course Modules & Note Taking</span>
            </div>
            <div class="schedule-day-row" id="day-row-4">
              <span class="day-badge">Thursday</span>
              <span class="day-activity">Packet Tracer Hands-on Lab Practice</span>
            </div>
            <div class="schedule-day-row" id="day-row-5">
              <span class="day-badge">Friday</span>
              <span class="day-activity">Wireshark Packet Capture & Protocol Triage</span>
            </div>
            <div class="schedule-day-row" id="day-row-6">
              <span class="day-badge">Saturday</span>
              <span class="day-activity">Hands-on Lab Projects & Interview Q&A Drills</span>
            </div>
            <div class="schedule-day-row" id="day-row-0">
              <span class="day-badge">Sunday</span>
              <span class="day-activity">Revision, Mock Testing & Ticket Worklogs</span>
            </div>
          </div>

          <!-- Quick Navigation Actions -->
          <div style="display:flex; gap:10px; margin-top:8px; flex-wrap:wrap;">
            <button class="btn-sm" onclick="switchTab('subnetTab')">⚡ Launch Subnet Trainer</button>
            <button class="btn-sm" onclick="switchTab('terminalTab')">💻 Practice in Terminal</button>
            <button class="btn-sm" onclick="switchTab('warRoomTab')">🚨 Review War Room</button>
          </div>
        </div>

      </div>

      <!-- Immediate 7-Step Action Plan -->
      <div class="roadmap-subcard" style="margin-bottom:28px;">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
          <div>
            <h3 style="font-size:1.15rem; font-weight:800; color:#ffffff; display:flex; align-items:center; gap:8px;">
              <span>✅</span> Immediate 7-Step Action Plan for Bangalore Job Switch
            </h3>
            <p style="font-size:0.82rem; color:var(--text-muted);">
              Track your execution milestones from current ₹3.6 LPA role to your next offer letter:
            </p>
          </div>
          <span style="font-family:'JetBrains Mono', monospace; font-size:0.85rem; font-weight:800; color:var(--emerald); background:rgba(16,185,129,0.12); border:1px solid rgba(16,185,129,0.3); padding:4px 12px; border-radius:99px;" id="actionPlanCounter">
            0 / 7 Steps Completed
          </span>
        </div>

        <div class="action-checklist" style="margin-top:14px;">
          <div class="action-step-item" id="step-row-1">
            <input type="checkbox" class="action-checkbox" id="act_step_1" onchange="handleActionPlanCheck(this)">
            <div class="action-text">
              <strong>Step 1: Finish Networking Fundamentals (Weeks 1–3)</strong> — Lock in OSI model, TCP vs UDP differences, and mental subnetting calculations without calculator.
            </div>
          </div>
          <div class="action-step-item" id="step-row-2">
            <input type="checkbox" class="action-checkbox" id="act_step_2" onchange="handleActionPlanCheck(this)">
            <div class="action-text">
              <strong>Step 2: Complete CCNA 200-301 Preparation (Weeks 4–10)</strong> — Work through the 66 Kyndryl Core Priority lessons and master VLANs, 802.1Q, OSPF, and NAT.
            </div>
          </div>
          <div class="action-step-item" id="step-row-3">
            <input type="checkbox" class="action-checkbox" id="act_step_3" onchange="handleActionPlanCheck(this)">
            <div class="action-text">
              <strong>Step 3: Build 3 Showcase Cisco Packet Tracer Topologies</strong> — Create a multi-VLAN campus with SVI routing, OSPF dynamic routing, and an HSRP redundant gateway.
            </div>
          </div>
          <div class="action-step-item" id="step-row-4">
            <input type="checkbox" class="action-checkbox" id="act_step_4" onchange="handleActionPlanCheck(this)">
            <div class="action-text">
              <strong>Step 4: Learn Packet Capture Analysis in Wireshark</strong> — Inspect TCP 3-way handshakes, SYN-ACK, RST flags, DHCP DORA packets, and ARP request/reply cycles.
            </div>
          </div>
          <div class="action-step-item" id="step-row-5">
            <input type="checkbox" class="action-checkbox" id="act_step_5" onchange="handleActionPlanCheck(this)">
            <div class="action-text">
              <strong>Step 5: Document 3 Technical Incident Scenarios for Interviews</strong> — Prepare concise stories describing a switching loop, DHCP lease failure, and OSPF MTU mismatch resolution.
            </div>
          </div>
          <div class="action-step-item" id="step-row-6">
            <input type="checkbox" class="action-checkbox" id="act_step_6" onchange="handleActionPlanCheck(this)">
            <div class="action-text">
              <strong>Step 6: Update Naukri, LinkedIn & Begin Targeted Bangalore Applications</strong> — Target ₹4.5–7.0 LPA L1/L2 network engineer openings across Bangalore tech parks.
            </div>
          </div>
          <div class="action-step-item" id="step-row-7">
            <input type="checkbox" class="action-checkbox" id="act_step_7" onchange="handleActionPlanCheck(this)">
            <div class="action-text">
              <strong>Step 7: Specialize in Security, CCNP, or DevNet Automation</strong> — Once secured in your new role, pursue CCNP Enterprise or Python automation for the ₹9–16+ LPA tier.
            </div>
          </div>
        </div>
      </div>

    </div>


    <!-- TAB: NETWORK ENGINEER TOPICS & LESSONS (KYNDRYL L1/L2 NOC MASTER PATH) -->
    <div id="engineerTab" class="tab-pane">
      
      <!-- Executive Overview Banner -->
      <div class="engineer-header-card">
        <div class="engineer-header-top">
          <div class="engineer-header-title">
            <h2><span>🎓</span> Kyndryl Network Engineer Core Curriculum</h2>
            <p>7 Mission-Critical Topics • 73 High-Yield Lessons • Cisco IOS-XE CLI Diagnostic Sequences • Day-1 NOC Readiness</p>
          </div>
          <div style="display:flex; gap:10px; flex-wrap:wrap;">
            <button class="btn-sm" onclick="expandAllEngineerTopics()">Expand All Topics</button>
            <button class="btn-sm" onclick="collapseAllEngineerTopics()">Collapse All</button>
          </div>
        </div>

        <div class="engineer-stats-strip">
          <div class="eng-stat-box">
            <div class="eng-stat-num" id="engStatTopics">7 / 7</div>
            <div class="eng-stat-label">Core Topics</div>
          </div>
          <div class="eng-stat-box">
            <div class="eng-stat-num" id="engStatLessonsDone">0 / 73</div>
            <div class="eng-stat-label">Lessons Done</div>
          </div>
          <div class="eng-stat-box">
            <div class="eng-stat-num" id="engStatPct">0%</div>
            <div class="eng-stat-label">Role Track Progress</div>
          </div>
          <div class="eng-stat-box">
            <div class="eng-stat-num">6</div>
            <div class="eng-stat-label">Simulated Devices</div>
          </div>
          <div class="eng-stat-box">
            <div class="eng-stat-num">100%</div>
            <div class="eng-stat-label">NOC Aligned</div>
          </div>
        </div>

        <div class="engineer-progress-wrap">
          <div class="eng-prog-meta">
            <span>Overall Network Engineer Curriculum Completion</span>
            <span id="engProgressLabel">0% Done (0 of 73 Lessons)</span>
          </div>
          <div class="progress-bar-container">
            <div class="progress-bar-fill" id="engProgressBar" style="width: 0%;"></div>
          </div>
        </div>
      </div>

      <!-- Sprint / Domain Filter Chips & Search -->
      <div class="tracker-toolbar" style="margin-bottom: 18px;">
        <input type="text" id="engSearchInput" class="search-input" placeholder="🔍 Filter lessons across Network Engineer topics (e.g. VLAN, OSPF, HSRP, BPDU, ACL, NAT)..." oninput="filterEngineerTopicsUI()">
      </div>

      <div class="sprint-filters-wrap" id="sprintFilterWrap">
        <button class="sprint-chip active" onclick="setSprintFilter('all')">🌟 All 7 Topics (73 Lessons)</button>
        <button class="sprint-chip" onclick="setSprintFilter('week-1')">🔌 Week 1: LAN Switching & Layer 2 (18 Lessons)</button>
        <button class="sprint-chip" onclick="setSprintFilter('week-2')">⚡ Week 2: Subnetting & Routing (16 Lessons)</button>
        <button class="sprint-chip" onclick="setSprintFilter('week-3')">🌐 Week 3: OSPF & IP Services (17 Lessons)</button>
        <button class="sprint-chip" onclick="setSprintFilter('week-4')">🛡️ Week 4: Security & NOC Operations (15 Lessons)</button>
        <button class="sprint-chip" onclick="setSprintFilter('week-modern')">🤖 Modern: Automation & Cloud (7 Lessons)</button>
      </div>

      <!-- Container where JavaScript renders the 7 Topics -->
      <div id="engineerTopicsContainer">
        <!-- Rendered dynamically by JavaScript -->
      </div>
    </div>


    <!-- TAB 2: INTERACTIVE MULTI-DEVICE CISCO CLI TERMINAL SIMULATOR -->
    <div id="terminalTab" class="tab-pane">
      
      <!-- Multi-Device Selection Bar -->
      <div class="device-selector-wrap">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:10px;">
          <div>
            <h3 style="font-size:1.15rem; font-weight:800; color:white; display:flex; align-items:center; gap:8px;">
              <span>🌐</span> Multi-Device Enterprise Network Simulation
            </h3>
            <p style="font-size:0.85rem; color:var(--text-muted);">
              Interactive console across Core Switches, Access Switches, Routers, Firewalls, Wireless Controllers, and Host PCs with real CLI responses.
            </p>
          </div>
          <span style="font-size:0.75rem; background:rgba(16,185,129,0.12); color:#34d399; border:1px solid rgba(16,185,129,0.3); padding:4px 10px; border-radius:99px; font-weight:700;">
            ● 6 NODES ONLINE
          </span>
        </div>

        <div class="device-grid" id="deviceGrid">
          <button class="device-btn active" id="devBtn-core-sw" onclick="switchDevice('core-sw')">
            <span class="dev-icon">🔀</span>
            <div class="dev-meta">
              <span class="dev-name">KYNDRYL-CORE-SW01</span>
              <span class="dev-role">Catalyst 9300 (L3 Core/Dist)</span>
              <span class="dev-status"><span class="dev-status-dot"></span>10.10.1.2</span>
            </div>
          </button>

          <button class="device-btn" id="devBtn-acc-sw" onclick="switchDevice('acc-sw')">
            <span class="dev-icon">🔌</span>
            <div class="dev-meta">
              <span class="dev-name">KYNDRYL-ACC-SW02</span>
              <span class="dev-role">Catalyst 9200 (L2 Floor-3)</span>
              <span class="dev-status"><span class="dev-status-dot"></span>10.10.99.2</span>
            </div>
          </button>

          <button class="device-btn" id="devBtn-edge-rtr" onclick="switchDevice('edge-rtr')">
            <span class="dev-icon">🌐</span>
            <div class="dev-meta">
              <span class="dev-name">KYNDRYL-EDGE-RTR01</span>
              <span class="dev-role">Cisco ISR 4451 (WAN/BGP)</span>
              <span class="dev-status"><span class="dev-status-dot"></span>10.10.1.1</span>
            </div>
          </button>

          <button class="device-btn" id="devBtn-fw" onclick="switchDevice('fw')">
            <span class="dev-icon">🛡️</span>
            <div class="dev-meta">
              <span class="dev-name">KYNDRYL-FW01</span>
              <span class="dev-role">Cisco ASA 5516 (Perimeter)</span>
              <span class="dev-status"><span class="dev-status-dot"></span>198.51.100.1</span>
            </div>
          </button>

          <button class="device-btn" id="devBtn-wlc" onclick="switchDevice('wlc')">
            <span class="dev-icon">📶</span>
            <div class="dev-meta">
              <span class="dev-name">KYNDRYL-WLC01</span>
              <span class="dev-role">Catalyst 9800-CL (Wi-Fi)</span>
              <span class="dev-status"><span class="dev-status-dot"></span>10.10.50.10</span>
            </div>
          </button>

          <button class="device-btn" id="devBtn-host-pc" onclick="switchDevice('host-pc')">
            <span class="dev-icon">💻</span>
            <div class="dev-meta">
              <span class="dev-name">NOC-ADMIN-PC</span>
              <span class="dev-role">Admin Host (Win11 / PS)</span>
              <span class="dev-status"><span class="dev-status-dot"></span>10.10.10.85</span>
            </div>
          </button>
        </div>

        <!-- Interactive End-to-End Topology Map -->
        <div class="topology-strip">
          <span class="topo-label">Data Path:</span>
          <div class="topo-node" id="topoNode-host-pc" onclick="switchDevice('host-pc')">💻 NOC-PC (10.10.10.85)</div>
          <div class="topo-link">──<span>[Access]</span>──▶</div>
          <div class="topo-node" id="topoNode-acc-sw" onclick="switchDevice('acc-sw')">🔌 ACC-SW02 (Floor 3)</div>
          <div class="topo-link">──<span>[802.1Q Trunk]</span>──▶</div>
          <div class="topo-node active" id="topoNode-core-sw" onclick="switchDevice('core-sw')">🔀 CORE-SW01 (L3 Core)</div>
          <div class="topo-link">──<span>[OSPF Area 0]</span>──▶</div>
          <div class="topo-node" id="topoNode-edge-rtr" onclick="switchDevice('edge-rtr')">🌐 EDGE-RTR01 (WAN)</div>
          <div class="topo-link">──<span>[Inside/Out]</span>──▶</div>
          <div class="topo-node" id="topoNode-fw" onclick="switchDevice('fw')">🛡️ FW01 (ASA)</div>
          <div class="topo-link">──▶</div>
          <span style="color:#38bdf8; font-weight:700;">☁️ Cloud/Internet</span>
          <div style="margin-left:auto; display:flex; align-items:center; gap:6px;">
            <div class="topo-link"><span>[CAPWAP]</span>◀──</div>
            <div class="topo-node" id="topoNode-wlc" onclick="switchDevice('wlc')">📶 WLC01 (9800 Wi-Fi)</div>
          </div>
        </div>
      </div>

      <!-- Live Terminal Window -->
      <div class="terminal-window">
        <div class="terminal-bar">
          <div class="terminal-dots">
            <span class="dot red"></span>
            <span class="dot yellow"></span>
            <span class="dot green"></span>
          </div>
          <div class="terminal-title-group">
            <div class="terminal-title" id="terminalTitle">KYNDRYL-CORE-SW01# (Cisco Catalyst 9300 IOS-XE 17.9.4a)</div>
            <span class="terminal-dev-badge" id="terminalBadge">Active Node: CORE-SW01</span>
          </div>
          <div class="terminal-presets" id="terminalPresets">
            <!-- Rendered dynamically for active device -->
          </div>
        </div>
        <div class="terminal-body" id="termBody">
          <!-- Terminal session stream -->
        </div>
        <div class="terminal-input-row">
          <span class="terminal-prompt" id="terminalPrompt">KYNDRYL-CORE-SW01#</span>
          <input type="text" id="termInput" class="terminal-input" placeholder="Type a command (or click presets above)..." onkeydown="handleTerminalKey(event)">
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

    // Multi-Device Terminal Simulation Database
    const deviceConfigs = {
      "core-sw": {
        name: "KYNDRYL-CORE-SW01",
        title: "KYNDRYL-CORE-SW01# (Cisco Catalyst 9300-24T IOS-XE 17.09.04a)",
        badge: "Layer 3 Distribution & Core Gateway",
        prompt: "KYNDRYL-CORE-SW01#",
        promptColor: "#10b981",
        banner: `Kyndryl Global Managed Network Infrastructure - Node: KYNDRYL-CORE-SW01
Cisco IOS XE Software, Version 17.09.04a [Amsterdam] - Catalyst 9300-24T
IP Address: 10.10.1.2/24 (Uplink), 10.10.10.1/24 (VLAN 10 Default Gateway)
Type 'help' to see valid commands or click the quick presets above.
================================================================================`,
        presets: [
          { label: "show ip int br", cmd: "show ip interface brief" },
          { label: "show vlan br", cmd: "show vlan brief" },
          { label: "show int trunk", cmd: "show interfaces trunk" },
          { label: "show spanning-tree", cmd: "show spanning-tree" },
          { label: "show standby br", cmd: "show standby brief" },
          { label: "show ip route", cmd: "show ip route" },
          { label: "show errdisabled", cmd: "show interface status err-disabled" },
          { label: "Clear", cmd: "clear" }
        ],
        commands: {
          "help": `Available commands on KYNDRYL-CORE-SW01:
  show ip interface brief       - Display IP addresses and status on all ports & SVIs
  show vlan brief               - Display active VLANs and assigned physical ports
  show interfaces trunk         - Display active 802.1Q trunk links, allowed VLANs
  show mac address-table        - Display dynamically learned Layer 2 MAC addresses
  show spanning-tree            - Display STP RSTP topology, root bridge, port roles
  show standby brief            - Display HSRP First Hop Redundancy gateway state
  show ip route                 - Display core Layer 3 routing table
  show ip ospf neighbor         - Display OSPF neighbor adjacencies with Edge Router
  show etherchannel summary     - Display bundled port-channels and member ports
  show interface status err-disabled - Display ports shutdown by STP or port security
  show cdp neighbors            - Display directly connected Cisco neighbors
  show version                  - Display IOS-XE version and uptime
  show logging                  - Display syslog buffer and interface flap alerts
  show tech-support             - Dump standard Kyndryl escalation diagnostic logs
  ping 10.10.1.1                - Test ICMP reachability to Edge Router
  traceroute 10.50.0.1          - Trace route to wireless gateway
  clear                         - Clear terminal window`,

          "show ip interface brief": `Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1/0/1   unassigned      YES unset  up                    up      
GigabitEthernet1/0/2   unassigned      YES unset  up                    up      
GigabitEthernet1/0/3   unassigned      YES unset  down                  down    
GigabitEthernet1/0/4   unassigned      YES unset  down                  down    
GigabitEthernet1/0/23  unassigned      YES unset  up                    up      
GigabitEthernet1/0/24  10.10.1.2       YES manual up                    up      
TenGigabitEthernet1/1/1 unassigned     YES unset  up                    up      
TenGigabitEthernet1/1/2 unassigned     YES unset  up                    up      
Vlan1                  unassigned      YES unset  administratively down down    
Vlan10                 10.10.10.1      YES manual up                    up      
Vlan20                 10.10.20.1      YES manual up                    up      
Vlan30                 10.10.30.1      YES manual up                    up      
Vlan50                 10.10.50.1      YES manual up                    up      
Vlan99                 10.10.99.1      YES manual up                    up      `,

          "show vlan brief": `VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Gi1/0/5, Gi1/0/6, Gi1/0/7
10   DATA_USERS                       active    Gi1/0/8, Gi1/0/9, Gi1/0/10
20   VOICE_PHONES                     active    Gi1/0/11, Gi1/0/12, Gi1/0/13
30   SERVERS_DC                       active    Gi1/0/14, Gi1/0/15
50   WIRELESS_USERS                   active    Gi1/0/16, Gi1/0/17
99   MANAGEMENT                       active    Gi1/0/24`,

          "show interfaces trunk": `Port        Mode             Encapsulation  Status        Native vlan
Te1/1/1     on               802.1q         trunking      99
Te1/1/2     on               802.1q         trunking      99
Gi1/0/23    on               802.1q         trunking      99

Port        Vlans allowed on trunk
Te1/1/1     1-4094
Te1/1/2     1-4094
Gi1/0/23    10,20,30,50,99

Port        Vlans in spanning tree forwarding state and not pruned
Te1/1/1     1,10,20,30,50,99
Te1/1/2     1,10,20,30,50,99
Gi1/0/23    10,20,99`,

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
Gi1/0/23            Desg FWD 19        128.23   P2p `,

          "show standby brief": `Interface   Grp  Pri P State   Active          Standby         Virtual IP
Vl10        10   110 P Active  local           10.10.10.2      10.10.10.254
Vl20        20   90    Standby 10.10.20.2      local           10.10.20.254
Vl50        50   110 P Active  local           10.10.50.2      10.10.50.254`,

          "show ip route": `Gateway of last resort is 10.10.1.1 to network 0.0.0.0

S*    0.0.0.0/0 [1/0] via 10.10.1.1, GigabitEthernet1/0/24
C     10.10.10.0/24 is directly connected, Vlan10
L     10.10.10.1/32 is directly connected, Vlan10
C     10.10.20.0/24 is directly connected, Vlan20
L     10.10.20.1/32 is directly connected, Vlan20
C     10.10.30.0/24 is directly connected, Vlan30
L     10.10.30.1/32 is directly connected, Vlan30
C     10.10.50.0/24 is directly connected, Vlan50
O     172.16.0.0/16 [110/11] via 10.10.1.1, 05:22:18, GigabitEthernet1/0/24
O     192.168.100.0/24 [110/20] via 10.10.1.1, 05:22:18, GigabitEthernet1/0/24`,

          "show ip ospf neighbor": `Neighbor ID     Pri   State           Dead Time   Address         Interface
198.51.100.2      1   FULL/BDR        00:00:36    10.10.1.1       GigabitEthernet1/0/24`,

          "show mac address-table": `          Mac Address Table
-------------------------------------------
Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  10    0050.56a1.2b3c    DYNAMIC     Gi1/0/23
  10    0050.56a1.9f12    DYNAMIC     Gi1/0/23
  20    0004.f211.bb44    DYNAMIC     Gi1/0/23
  30    d46d.50e1.77aa    DYNAMIC     Gi1/0/14
  99    0000.0c07.ac01    DYNAMIC     Te1/1/1
Total Mac Addresses for this criterion: 5`,

          "show etherchannel summary": `Group  Port-channel  Protocol    Ports
------+-------------+-----------+-----------------------------------------------
1      Po1(SU)         LACP      Te1/1/1(P)    Te1/1/2(P)`,

          "show interface status err-disabled": `Port      Name               Status       Reason               Err-disabled Vlans
Gi1/0/14  CONF_ROOM_JACK     err-disabled psecure-violation
Gi1/0/22  FLOOR_3_DROP       err-disabled bpduguard`,

          "show cdp neighbors": `Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
KYNDRYL-EDGE-RTR01 Gi 1/0/24       162        R B         ISR4451   Gi 0/0/2
KYNDRYL-ACC-SW02   Gi 1/0/23       148        S I         C9200L    Gi 1/0/23`,

          "show version": `Cisco IOS XE Software, Version 17.09.04a [Amsterdam]
cisco C9300-24T (X86) processor with 1813437K/6147K bytes of memory.
Processor board ID FOC2419L1AB
Switch Ports Model              SW Version        SW Image              Mode   
*    1 28    C9300-24T          17.09.04a         CAT9K_IOSXE           INSTALL
Configuration register is 0x102`,

          "show logging": `Syslog logging: enabled (0 messages dropped, 3 flushes, 0 overruns)
    Console logging: level debugging, 1823 messages logged
*Oct 13 18:22:10.412: %LINK-3-UPDOWN: Interface GigabitEthernet1/0/24, changed state to up
*Oct 13 18:22:11.413: %LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet1/0/24, changed state to up
*Oct 13 18:22:15.981: %OSPF-5-ADJCHG: Process 1, Nbr 198.51.100.2 on GigabitEthernet1/0/24 from LOADING to FULL, Loading Done`,

          "show tech-support": `------------------ show version ------------------
Cisco IOS XE Software, Version 17.09.04a
System image file is "bootflash:packages.conf"
cisco C9300-24T (X86) processor with 1813437K/6147K bytes of memory.
Uptime for this switch is 18 weeks, 4 days, 12 hours, 14 minutes.
Configuration register is 0x102
[LOG BUFFER ATTACHED FOR KYNDRYL L2/L3 ESCALATION TICKET]`,

          "ping 10.10.1.1": `Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.10.1.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/2/4 ms`,

          "traceroute 10.50.0.1": `Type escape sequence to abort.
Tracing the route to 10.50.0.1
VRF info: (default VRF)
  1 10.10.1.1 1 msec 1 msec 2 msec
  2 10.50.0.1 2 msec 2 msec 3 msec`
        }
      },

      "acc-sw": {
        name: "KYNDRYL-ACC-SW02",
        title: "KYNDRYL-ACC-SW02# (Cisco Catalyst 9200L-48P-4G IOS-XE 17.09.03)",
        badge: "Floor 3 Access Switch / PoE+ & 802.1X",
        prompt: "KYNDRYL-ACC-SW02#",
        promptColor: "#38bdf8",
        banner: `Kyndryl Global Managed Network Infrastructure - Node: KYNDRYL-ACC-SW02
Cisco IOS XE Software, Version 17.09.03 [Amsterdam] - Catalyst 9200L-48P-4G
Management IP: 10.10.99.2/24 (VLAN 99), Uplink: Gi1/0/23 -> CORE-SW01
Type 'help' to see valid commands or click the quick presets above.
================================================================================`,
        presets: [
          { label: "show int status", cmd: "show interfaces status" },
          { label: "show port-sec", cmd: "show port-security interface gi1/0/14" },
          { label: "show power inline", cmd: "show power inline" },
          { label: "show vlan br", cmd: "show vlan brief" },
          { label: "show errdisabled", cmd: "show interface status err-disabled" },
          { label: "show cdp neighbors", cmd: "show cdp neighbors" },
          { label: "Clear", cmd: "clear" }
        ],
        commands: {
          "help": `Available commands on KYNDRYL-ACC-SW02:
  show interfaces status        - Display connected state, VLAN, duplex, speed of ports
  show port-security interface <id> - Check port security violations & shutdown state
  show port-security address    - Display secure sticky MAC address table
  show power inline             - Display PoE budget and power draw (IP Phones & APs)
  show vlan brief               - Display active VLANs on access switch
  show ip interface brief       - Display management SVI and port states
  show interface status err-disabled - Check errdisabled ports (e.g. psecure-violation)
  show spanning-tree vlan 10    - Display STP port state (Root, Designated, Edge)
  show mac address-table        - Display learned MAC addresses from desk drops
  show ip dhcp snooping binding - Display DHCP snooping table (IP-to-MAC leases)
  show cdp neighbors            - Display connected Core Switch, IP Phones, APs
  show version                  - Display Catalyst 9200 switch model and software
  ping 10.10.99.1               - Test reachability to Core Switch SVI gateway
  clear                         - Clear terminal window`,

          "show interfaces status": `Port      Name               Status       Vlan       Duplex  Speed Type
Gi1/0/1   PC_DESK_301        connected    10         a-full a-1000 10/100/1000BaseTX
Gi1/0/2   PC_DESK_302        connected    10         a-full a-1000 10/100/1000BaseTX
Gi1/0/3   PC_DESK_303        notconnect   10           auto   auto 10/100/1000BaseTX
Gi1/0/11  IP_PHONE_301       connected    10,20      a-full a-1000 10/100/1000BaseTX
Gi1/0/14  CONF_ROOM_JACK     err-disabled 10           auto   auto 10/100/1000BaseTX
Gi1/0/15  AP_FLOOR_3_EAST    connected    50,trunk   a-full a-1000 10/100/1000BaseTX
Gi1/0/23  UPLINK_CORE-SW01   connected    trunk      a-full a-1000 10/100/1000BaseTX`,

          "show port-security interface gi1/0/14": `Port Security              : Enabled
Port Status                : Secure-shutdown
Violation Mode             : Shutdown
Aging Time                 : 0 mins
Aging Type                 : Absolute
SecureStatic Address Aging : Disabled
Maximum MAC Addresses      : 1
Total MAC Addresses        : 0
Configured MAC Addresses   : 0
Sticky MAC Addresses       : 0
Last Source Address:Vlan   : 0050.56b2.88e1:10
Security Violation Count   : 1`,

          "show port-security address": `               Secure Mac Address Table
-------------------------------------------------------------------
Vlan    Mac Address       Type                    Ports   Remaining Age
                                                             (mins)
----    -----------       ----                    -----   -------------
  10    0050.56a1.2b3c    SecureConfigured        Gi1/0/1      -
  10    0050.56a1.9f12    SecureSticky            Gi1/0/2      -
Total Addresses: 2`,

          "show power inline": `Available: 740.0(w)  Used: 124.6(w)  Remaining: 615.4(w)

Interface Admin  Oper       Power(Watts) Device              Class Max
--------- ------ ---------- ----------- ------------------- ----- ----
Gi1/0/11  auto   on         12.0        IP Phone 8845       3     15.4
Gi1/0/12  auto   on         12.0        IP Phone 8845       3     15.4
Gi1/0/15  auto   on         25.5        C9120AXI-B Access Pt 4     30.0
Gi1/0/16  auto   on         25.5        C9120AXI-B Access Pt 4     30.0`,

          "show vlan brief": `VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Gi1/0/4, Gi1/0/5, Gi1/0/6
10   DATA_USERS                       active    Gi1/0/1, Gi1/0/2, Gi1/0/3, Gi1/0/11
20   VOICE_PHONES                     active    Gi1/0/11, Gi1/0/12
50   WIRELESS_AP                      active    Gi1/0/15, Gi1/0/16
99   MANAGEMENT                       active    `,

          "show ip interface brief": `Interface              IP-Address      OK? Method Status                Protocol
Vlan99                 10.10.99.2      YES manual up                    up      
GigabitEthernet1/0/1   unassigned      YES unset  up                    up      
GigabitEthernet1/0/2   unassigned      YES unset  up                    up      
GigabitEthernet1/0/14  unassigned      YES unset  down                  down    
GigabitEthernet1/0/23  unassigned      YES unset  up                    up      `,

          "show interface status err-disabled": `Port      Name               Status       Reason               Err-disabled Vlans
Gi1/0/14  CONF_ROOM_JACK     err-disabled psecure-violation`,

          "show spanning-tree vlan 10": `VLAN0010
  Spanning tree enabled protocol rstp
  Root ID    Priority    24586
             Address     0019.06e7.6480
             Cost        19
             Port        Gi1/0/23 (GigabitEthernet1/0/23)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32778  (priority 32768 sys-id-ext 10)
             Address     ac44.f288.1900
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Gi1/0/1             Desg FWD 19        128.1    P2p Edge 
Gi1/0/2             Desg FWD 19        128.2    P2p Edge 
Gi1/0/11            Desg FWD 19        128.11   P2p Edge 
Gi1/0/23            Root FWD 19        128.23   P2p `,

          "show mac address-table": `          Mac Address Table
-------------------------------------------
Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  10    0050.56a1.2b3c    STATIC      Gi1/0/1
  10    0050.56a1.9f12    STATIC      Gi1/0/2
  20    0004.f211.bb44    DYNAMIC     Gi1/0/11
  50    4c77.6d22.ea10    DYNAMIC     Gi1/0/15
  99    70ea.1ae4.3300    DYNAMIC     Gi1/0/23
Total Mac Addresses for this criterion: 5`,

          "show ip dhcp snooping binding": `MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
00:50:56:A1:2B:3C   10.10.10.85      86400       dhcp-snooping   10   GigabitEthernet1/0/1
00:50:56:A1:9F:12   10.10.10.86      86400       dhcp-snooping   10   GigabitEthernet1/0/2
00:04:F2:11:BB:44   10.10.20.101     86400       dhcp-snooping   20   GigabitEthernet1/0/11
Total number of bindings: 3`,

          "show cdp neighbors": `Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
KYNDRYL-CORE-SW01 Gi 1/0/23        174        S I         C9300-24T Gi 1/0/23
SEP0004F211BB44  Gi 1/0/11        132        H P         IP Phone  Port 1
AP-FL3-EAST      Gi 1/0/15        155        T           C9120AXI  Gig 0`,

          "show version": `Cisco IOS XE Software, Version 17.09.03 [Amsterdam]
cisco C9200L-48P-4G (ARM) processor with 2097152K bytes of memory.
Processor board ID JAE254807ZZ
Switch Ports Model              SW Version        SW Image              Mode   
*    1 52    C9200L-48P-4G      17.09.03          CAT9K_LITE_IOSXE      INSTALL
Configuration register is 0x102`,

          "ping 10.10.99.1": `Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.10.99.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/2 ms`
        }
      },

      "edge-rtr": {
        name: "KYNDRYL-EDGE-RTR01",
        title: "KYNDRYL-EDGE-RTR01# (Cisco ISR 4451-X/K9 IOS-XE 17.06.05)",
        badge: "Enterprise WAN Edge / BGP & IPsec Gateway",
        prompt: "KYNDRYL-EDGE-RTR01#",
        promptColor: "#6366f1",
        banner: `Kyndryl Global Managed Network Infrastructure - Node: KYNDRYL-EDGE-RTR01
Cisco IOS XE Software, Version 17.06.05 - Cisco ISR4451-X/K9
WAN Public IP: 198.51.100.2 (ISP1), LAN Gateway: 10.10.1.1/24 (Core Uplink)
Type 'help' to see valid commands or click the quick presets above.
================================================================================`,
        presets: [
          { label: "show ip int br", cmd: "show ip interface brief" },
          { label: "show ip route", cmd: "show ip route" },
          { label: "show ip ospf neighbor", cmd: "show ip ospf neighbor" },
          { label: "show ip bgp summary", cmd: "show ip bgp summary" },
          { label: "show ip nat translations", cmd: "show ip nat translations" },
          { label: "show access-lists", cmd: "show access-lists" },
          { label: "show crypto session", cmd: "show crypto session" },
          { label: "ping 8.8.8.8", cmd: "ping 8.8.8.8" },
          { label: "Clear", cmd: "clear" }
        ],
        commands: {
          "help": `Available commands on KYNDRYL-EDGE-RTR01:
  show ip interface brief       - Display WAN, LAN, and Tunnel IP interface statuses
  show ip route                 - Display entire BGP, OSPF, and Static routing table
  show ip ospf neighbor         - Display internal OSPF neighbor state with Core Switch
  show ip bgp summary           - Display ISP BGP peer status (AS 15169 / AS 209)
  show ip nat translations      - Display active dynamic NAT/PAT translation sessions
  show ip nat statistics        - Display NAT hit/miss counters and pool exhaustion
  show access-lists             - Display ACL packet match counters
  show crypto session           - Display IPsec VPN tunnel state to Microsoft Azure
  show ip arp                   - Display ARP IP-to-MAC resolution table
  show version                  - Display ISR 4451 hardware and IOS-XE version
  ping 8.8.8.8                  - Test public Internet DNS reachability
  traceroute 8.8.8.8            - Trace WAN hops across ISP Autonomous Systems
  clear                         - Clear terminal window`,

          "show ip interface brief": `Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0/0   198.51.100.2    YES manual up                    up      
GigabitEthernet0/0/1   203.0.113.2     YES manual up                    up      
GigabitEthernet0/0/2   10.10.1.1       YES manual up                    up      
Tunnel1                172.16.254.2    YES manual up                    up      
Loopback0              198.51.100.254  YES manual up                    up      `,

          "show ip route": `Gateway of last resort is 198.51.100.1 to network 0.0.0.0

B*    0.0.0.0/0 [20/0] via 198.51.100.1, 42w2d
C     10.10.1.0/24 is directly connected, GigabitEthernet0/0/2
L     10.10.1.1/32 is directly connected, GigabitEthernet0/0/2
O     10.10.10.0/24 [110/2] via 10.10.1.2, 05:42:11, GigabitEthernet0/0/2
O     10.10.20.0/24 [110/2] via 10.10.1.2, 05:42:11, GigabitEthernet0/0/2
O     10.10.50.0/24 [110/2] via 10.10.1.2, 05:42:11, GigabitEthernet0/0/2
S     172.16.0.0/16 [1/0] via 172.16.254.1, Tunnel1
C     198.51.100.0/29 is directly connected, GigabitEthernet0/0/0
L     198.51.100.2/32 is directly connected, GigabitEthernet0/0/0
C     203.0.113.0/29 is directly connected, GigabitEthernet0/0/1`,

          "show ip ospf neighbor": `Neighbor ID     Pri   State           Dead Time   Address         Interface
10.10.10.1        1   FULL/DR         00:00:32    10.10.1.2       GigabitEthernet0/0/2`,

          "show ip bgp summary": `BGP router identifier 198.51.100.2, local AS number 65000
BGP table version is 9124401, main routing table version 9124401

Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
198.51.100.1    4        15169 1240182  941209  9124401    0    0 42w2d               1
203.0.113.1     4          209  981204  782103  9124401    0    0 18w5d               1`,

          "show ip nat translations": `Pro Inside global         Inside local          Outside local         Outside global
tcp 198.51.100.2:49821    10.10.10.85:49821     52.96.166.130:443     52.96.166.130:443
tcp 198.51.100.2:51402    10.10.10.85:51402     142.250.224.46:443    142.250.224.46:443
udp 198.51.100.2:58102    10.10.20.101:5060     104.244.42.1:5060     104.244.42.1:5060
icmp 198.51.100.2:12      10.10.10.85:12        8.8.8.8:12            8.8.8.8:12`,

          "show ip nat statistics": `Total active translations: 3,428 (0 static, 3428 dynamic; 3428 extended)
Outside interfaces: GigabitEthernet0/0/0, GigabitEthernet0/0/1
Inside interfaces: GigabitEthernet0/0/2
Hits: 28914022  Misses: 3428
CEF Translated packets: 28910594, CEF Punted packets: 3428
Expired translations: 1842109
Dynamic mappings:
-- Inside Source
 [Id: 1] access-list NAT_USERS pool OVERLOAD refcount 3428`,

          "show access-lists": `Extended IP access list WAN_INSPECT
    10 permit ospf any any (142010 matches)
    20 permit tcp any any established (18442100 matches)
    30 permit udp any any eq domain (894012 matches)
    40 permit icmp any any echo-reply (31024 matches)
    50 deny ip any any log (41209 matches)
Standard IP access list NAT_USERS
    10 permit 10.10.0.0, wildcard bits 0.0.255.255 (28914022 matches)`,

          "show crypto session": `Crypto session current status

Interface: Tunnel1
Session status: UP-ACTIVE
Peer: 20.42.118.90 port 500
  Session ID: 4108
  IKEv2 SA: local 198.51.100.2/500 remote 20.42.118.90/500 Active
  IPSEC FLOW: permit ip 10.10.0.0/16 172.16.0.0/16
        Active SAs: 2, origin: crypto map
        Inbound Pkts: 7991440, Outbound Pkts: 8421902`,

          "show ip arp": `Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  10.10.1.1               -   001b.d45a.1102  ARPA   GigabitEthernet0/0/2
Internet  10.10.1.2               4   70ea.1ae4.3324  ARPA   GigabitEthernet0/0/2
Internet  198.51.100.1            1   0008.e3ff.fd90  ARPA   GigabitEthernet0/0/0
Internet  198.51.100.2            -   001b.d45a.1100  ARPA   GigabitEthernet0/0/0`,

          "show version": `Cisco IOS XE Software, Version 17.06.05
Cisco ISR4451-X/K9 (quad-core) processor with 3816567K/6147K bytes of memory.
Router operating mode: Autonomous
4 Gigabit Ethernet interfaces
System image file is "bootflash:isr4400-universalk9.17.06.05.SPA.bin"
Uptime for this router is 42 weeks, 2 days, 8 hours, 19 minutes.`,

          "ping 8.8.8.8": `Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 14/16/21 ms`,

          "traceroute 8.8.8.8": `Type escape sequence to abort.
Tracing the route to 8.8.8.8
VRF info: (default VRF)
  1 198.51.100.1 [AS 15169] 2 msec 1 msec 2 msec
  2 72.14.214.1 [AS 15169] 8 msec 7 msec 9 msec
  3 142.250.224.1 [AS 15169] 12 msec 13 msec 12 msec
  4 8.8.8.8 [AS 15169] 15 msec 16 msec 15 msec`
        }
      },

      "fw": {
        name: "KYNDRYL-FW01",
        title: "KYNDRYL-FW01# (Cisco ASA 5516-X Software Version 9.16(2))",
        badge: "Perimeter Security & Stateful Firewall",
        prompt: "KYNDRYL-FW01#",
        promptColor: "#f43f5e",
        banner: `Kyndryl Global Managed Network Infrastructure - Node: KYNDRYL-FW01
Cisco Adaptive Security Appliance Software Version 9.16(2) - ASA 5516-X
Security Context: System / Multi-Zone (Inside, Outside, DMZ)
Type 'help' to see valid commands or click the quick presets above.
================================================================================`,
        presets: [
          { label: "show int ip br", cmd: "show interface ip brief" },
          { label: "show conn count", cmd: "show conn count" },
          { label: "show access-list", cmd: "show access-list" },
          { label: "show nat", cmd: "show nat" },
          { label: "show vpn-sessiondb l2l", cmd: "show vpn-sessiondb l2l" },
          { label: "show failover", cmd: "show failover" },
          { label: "Clear", cmd: "clear" }
        ],
        commands: {
          "help": `Available commands on KYNDRYL-FW01 (Cisco ASA):
  show interface ip brief       - Display IP addresses and status of firewall zones
  show conn count               - Display current active stateful TCP/UDP connections
  show conn                     - Display active connection table details
  show access-list              - Display ASA Access Control Entries with hit counts
  show nat                      - Display Object and Manual NAT policy statistics
  show vpn-sessiondb l2l        - Display active Site-to-Site IPsec VPN tunnels
  show failover                 - Display High Availability (Active/Standby) status
  show xlate count              - Display active address translation slots
  show version                  - Display ASA software version and hardware spec
  ping 10.10.1.1                - Test reachability to Edge Router inside interface
  clear                         - Clear terminal window`,

          "show interface ip brief": `Interface                  IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0         198.51.100.1    YES manual up                    up      
GigabitEthernet0/1         10.10.1.254     YES manual up                    up      
GigabitEthernet0/2         172.16.10.1     YES manual up                    up      
Management0/0              10.10.99.254    YES manual up                    up      `,

          "show conn count": `4821 in use, 14290 most used`,

          "show conn": `TCP outside 13.107.42.16:443 inside 10.10.10.85:51221, idle 0:00:04, bytes 192842, flags UIO
TCP outside 52.96.166.130:443 inside 10.10.10.85:49821, idle 0:00:01, bytes 849102, flags UIO
UDP outside 8.8.8.8:53 inside 10.10.10.85:61204, idle 0:00:12, bytes 184, flags -
TCP dmz 172.16.10.50:443 outside 198.51.100.88:39102, idle 0:00:08, bytes 42890, flags UIO`,

          "show access-list": `access-list OUTSIDE_IN; 4 elements; name hash: 0x8a91bc12
  line 1 extended permit icmp any any echo-reply (hitcnt=14201)
  line 2 extended permit tcp any host 172.16.10.50 eq https (hitcnt=892100)
  line 3 extended permit esp any any (hitcnt=498112)
  line 4 extended deny ip any any (hitcnt=68219)
access-list INSIDE_OUT; 2 elements; name hash: 0x4f12dc88
  line 1 extended permit ip 10.10.0.0 255.255.0.0 any (hitcnt=9412081)
  line 2 extended deny ip any any (hitcnt=0)`,

          "show nat": `Manual NAT Policies (Section 1)
1 (inside,outside) to (outside,inside)
    source dynamic OBJ-CORP-LAN interface
    translate_hits = 9412081, untranslate_hits = 8912440
Auto NAT Policies (Section 2)
1 (dmz,outside) to (outside,dmz)
    source static OBJ-WEB-SERVER 198.51.100.50 service tcp 443 443
    translate_hits = 892100, untranslate_hits = 892100`,

          "show vpn-sessiondb l2l": `---------------------------------------------------------------------------
VPN Session Summary
---------------------------------------------------------------------------
Active : 2   Cumulative : 184   Peak : 6

---------------------------------------------------------------------------
Connection-specific data:
---------------------------------------------------------------------------
Connection   : Azure-East-US-Tunnel
Index        : 14                IP Addr     : 20.42.118.90
Protocol     : IKEv2 IPsec       Encryption  : AES-GCM-256
Hashing      : SHA384            Bytes Tx    : 842190204
Bytes Rx     : 799144012         Login Time  : 04:12:18 UTC Oct 01 2026
Duration     : 12d 14h 22m

Connection   : AWS-Transit-Gateway
Index        : 15                IP Addr     : 3.120.44.12
Protocol     : IKEv2 IPsec       Encryption  : AES-GCM-256
Duration     : 38d 02h 11m`,

          "show failover": `Failover On 
Failover unit Primary
Failover LAN Interface: FO-LINK GigabitEthernet0/3 (up)
Unit Poll frequency 1 seconds, holdtime 15 seconds
Interface outside (198.51.100.1): Normal (Monitored)
Interface inside (10.10.1.254): Normal (Monitored)
Interface dmz (172.16.10.1): Normal (Monitored)
  This host: Primary - Active 
             Active time: 8941200 (sec)
  Other host: Secondary - Standby Ready 
             Active time: 0 (sec)`,

          "show version": `Cisco Adaptive Security Appliance Software Version 9.16(2)
SSP Operating System Version 9.16(2)
Device Type: ASA 5516-X with FirePOWER Services
Hardware:   ASA5516, 8192 MB RAM, CPU Atom C2000 series 2400 MHz
Uptime:     103 days 11 hours 42 mins
Configuration register is 0x1`,

          "ping 10.10.1.1": `Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.10.1.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/2 ms`
        }
      },

      "wlc": {
        name: "KYNDRYL-WLC01",
        title: "KYNDRYL-WLC01# (Cisco Catalyst 9800-CL WLC IOS-XE 17.09.02)",
        badge: "Enterprise Wireless LAN Controller",
        prompt: "KYNDRYL-WLC01#",
        promptColor: "#f59e0b",
        banner: `Kyndryl Global Managed Network Infrastructure - Node: KYNDRYL-WLC01
Cisco IOS XE Software, Version 17.09.02 - Catalyst 9800-CL Wireless Controller
Management IP: 10.10.50.10/24 (VLAN 50), Active APs: 4, Associated Clients: 142
Type 'help' to see valid commands or click the quick presets above.
================================================================================`,
        presets: [
          { label: "show ap summary", cmd: "show ap summary" },
          { label: "show wlan summary", cmd: "show wlan summary" },
          { label: "show client summary", cmd: "show wireless client summary" },
          { label: "show ap 5ghz", cmd: "show ap dot11 5ghz summary" },
          { label: "show mobility summary", cmd: "show mobility summary" },
          { label: "Clear", cmd: "clear" }
        ],
        commands: {
          "help": `Available commands on KYNDRYL-WLC01:
  show ap summary               - Display all registered lightweight APs, model, IP, status
  show wlan summary             - Display broadcasted SSIDs and security profiles
  show wireless client summary  - Display active associated Wi-Fi stations & speeds
  show ap dot11 5ghz summary    - Display 5GHz RF channels, power levels, utilization
  show mobility summary         - Display mobility tunnel peering with remote controllers
  show ip interface brief       - Display controller management and CAPWAP interfaces
  show version                  - Display Catalyst 9800-CL WLC system information
  clear                         - Clear terminal window`,

          "show ap summary": `Number of APs: 4

AP Name          Slots    AP Model       Ethernet MAC    Radio MAC       Location             State
---------------------------------------------------------------------------------------------------
AP-FL3-EAST        2      C9120AXI-B     4c77.6d22.ea10  4c77.6d22.ea20  Floor-3-Wing-A       Registered
AP-FL3-WEST        2      C9120AXI-B     4c77.6d22.eb10  4c77.6d22.eb20  Floor-3-Wing-B       Registered
AP-CONF-01         2      C9130AXI-B     7069.5a11.9010  7069.5a11.9020  Exec-Boardroom       Registered
AP-EXEC-02         2      C9130AXI-B     7069.5a11.9110  7069.5a11.9120  Floor-4-Exec-Suite   Registered`,

          "show wlan summary": `Number of WLANs: 3

WLAN ID   WLAN Profile Name       SSID                    Status   Security
--------------------------------------------------------------------------------
1         Kyndryl-Corp-Profile    Kyndryl-Corporate       UP       [WPA3-Enterprise] 802.1x
2         Kyndryl-Guest-Profile   Kyndryl-Guest           UP       [Open] WebAuth-Portal
3         Kyndryl-IoT-Profile     Kyndryl-Warehouse-IoT   UP       [WPA2-PSK] AES`,

          "show wireless client summary": `Number of Local Clients: 142

MAC Address    AP Name          WLAN  State            Protocol  Method   Role
--------------------------------------------------------------------------------
0050.56a1.2b3c AP-FL3-EAST      1     Run              11ax(5G)  Dot1x    Local
0004.f211.bb44 AP-FL3-WEST      1     Run              11ac(5G)  Dot1x    Local
784f.43a2.1190 AP-CONF-01       2     Webauth Pending  11ax(2.4G)None     Guest
d46d.50e1.77aa AP-EXEC-02       1     Run              11ax(5G)  Dot1x    Local`,

          "show ap dot11 5ghz summary": `AP Name          Radio MAC       Channel       Pwr-Lvl CleanAir  Channel-Utilization
------------------------------------------------------------------------------------
AP-FL3-EAST      4c77.6d22.ea20  36, (80MHz)   2       Enabled   18%
AP-FL3-WEST      4c77.6d22.eb20  52, (80MHz)*  2       Enabled   22%
AP-CONF-01       7069.5a11.9020  100,(80MHz)*  1       Enabled   14%
AP-EXEC-02       7069.5a11.9120  149,(80MHz)   2       Enabled   12%
*DFS Channel`,

          "show mobility summary": `Mobility Protocol: 802.11r / CAPWAP
Mobility Group Name: KYNDRYL-CORP-MOBILITY
Public IP: 198.51.100.50

Peer IP          State           Data Path   Control Path
---------------------------------------------------------
10.10.50.11      Up              Encrypted   Encrypted`,

          "show ip interface brief": `Interface              IP-Address      OK? Method Status                Protocol
Vlan50                 10.10.50.10     YES manual up                    up      
GigabitEthernet1       unassigned      YES unset  up                    up      
GigabitEthernet2       unassigned      YES unset  up                    up      `,

          "show version": `Cisco IOS XE Software, Version 17.09.02 [Amsterdam]
cisco C9800-CL Software (X86_64_LINUX_IOSD-UNIVERSALK9-M)
Processor board ID 90K9W800CL1
Uptime for this controller is 64 days, 18 hours, 44 minutes.`
        }
      },

      "host-pc": {
        name: "NOC-ADMIN-PC",
        title: "NOC-ADMIN-PC (Windows 11 Enterprise PowerShell 7.4)",
        badge: "Diagnostic End-User Host / Workstation",
        prompt: "PS C:\\Users\\Kyndryl-NOC> ",
        promptColor: "#a78bfa",
        banner: `Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.
Host Name: NOC-ADMIN-PC (Kyndryl Network Operations Operations Center)
Assigned IP: 10.10.10.85/24 (VLAN 10 Data), Gateway: 10.10.10.1
Type 'help' to see valid commands or click the quick presets above.
================================================================================`,
        presets: [
          { label: "ipconfig /all", cmd: "ipconfig /all" },
          { label: "ping gateway", cmd: "ping 10.10.10.1" },
          { label: "ping internet", cmd: "ping 8.8.8.8" },
          { label: "tracert 8.8.8.8", cmd: "tracert 8.8.8.8" },
          { label: "nslookup", cmd: "nslookup portal.kyndryl.com" },
          { label: "arp -a", cmd: "arp -a" },
          { label: "netstat -ano", cmd: "netstat -ano" },
          { label: "Clear", cmd: "clear" }
        ],
        commands: {
          "help": `Available diagnostic commands on NOC-ADMIN-PC:
  ipconfig /all                 - Display full TCP/IP configuration, DHCP lease & DNS
  ping 10.10.10.1               - Test ICMP echo to Local Default Gateway (Core Switch)
  ping 8.8.8.8                  - Test ICMP echo across WAN edge to Public Internet
  tracert 8.8.8.8               - Trace complete hop path from PC to Internet
  nslookup portal.kyndryl.com   - Test internal corporate DNS record resolution
  arp -a                        - Display local ARP table and Gateway MAC address
  netstat -ano                  - Display active TCP socket connections and PIDs
  curl -I https://portal.kyndryl.com - Send HTTP HEAD request to verify Web server
  route print                   - Display local Windows IPv4 routing table
  clear                         - Clear terminal window`,

          "ipconfig /all": `Windows IP Configuration

   Host Name . . . . . . . . . . . . : NOC-ADMIN-PC
   Primary Dns Suffix  . . . . . . . : corp.kyndryl.com
   Node Type . . . . . . . . . . . . : Hybrid
   IP Routing Enabled. . . . . . . . : No
   WINS Proxy Enabled. . . . . . . . : No
   DNS Suffix Search List. . . . . . : corp.kyndryl.com

Ethernet adapter vEthernet (Corporate LAN):

   Connection-specific DNS Suffix  . : corp.kyndryl.com
   Description . . . . . . . . . . . : Intel(R) Ethernet Connection (7) I219-LM
   Physical Address. . . . . . . . . : 00-50-56-A1-2B-3C
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes
   IPv4 Address. . . . . . . . . . . : 10.10.10.85(Preferred) 
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Lease Obtained. . . . . . . . . . : Tuesday, October 13, 2026 8:00:00 AM
   Lease Expires . . . . . . . . . . : Wednesday, October 14, 2026 8:00:00 AM
   Default Gateway . . . . . . . . . : 10.10.10.1
   DHCP Server . . . . . . . . . . . : 10.100.1.50
   DNS Servers . . . . . . . . . . . : 10.100.1.10
                                       10.100.1.11`,

          "ping 10.10.10.1": `Pinging 10.10.10.1 with 32 bytes of data:
Reply from 10.10.10.1: bytes=32 time<1ms TTL=255
Reply from 10.10.10.1: bytes=32 time<1ms TTL=255
Reply from 10.10.10.1: bytes=32 time<1ms TTL=255
Reply from 10.10.10.1: bytes=32 time<1ms TTL=255

Ping statistics for 10.10.10.1:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms`,

          "ping 8.8.8.8": `Pinging 8.8.8.8 with 32 bytes of data:
Reply from 8.8.8.8: bytes=32 time=14ms TTL=117
Reply from 8.8.8.8: bytes=32 time=15ms TTL=117
Reply from 8.8.8.8: bytes=32 time=14ms TTL=117
Reply from 8.8.8.8: bytes=32 time=14ms TTL=117

Ping statistics for 8.8.8.8:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 14ms, Maximum = 15ms, Average = 14ms`,

          "tracert 8.8.8.8": `Tracing route to dns.google [8.8.8.8]
over a maximum of 30 hops:

  1    <1 ms    <1 ms    <1 ms  KYNDRYL-CORE-SW01 [10.10.10.1]
  2     1 ms     1 ms     1 ms  KYNDRYL-EDGE-RTR01 [10.10.1.1]
  3     2 ms     2 ms     2 ms  KYNDRYL-FW01 [198.51.100.1]
  4     8 ms     8 ms     9 ms  core2-chi.isp1.net [72.14.214.1]
  5    12 ms    12 ms    12 ms  142.250.224.1
  6    14 ms    14 ms    15 ms  dns.google [8.8.8.8]

Trace complete.`,

          "nslookup portal.kyndryl.com": `Server:  dc01.corp.kyndryl.com
Address:  10.100.1.10

Non-authoritative answer:
Name:    portal.kyndryl.com
Address:  10.100.25.105
Aliases:  intranet.kyndryl.com`,

          "arp -a": `Interface: 10.10.10.85 --- 0x12
  Internet Address      Physical Address      Type
  10.10.10.1            70-ea-1a-e4-33-00     dynamic (CORE-SW01 SVI)
  10.10.10.254          00-00-0c-07-ac-0a     dynamic (HSRP Virtual IP)
  10.10.10.86           00-50-56-a1-9f-12     dynamic (Peer Workstation)
  10.10.10.255          ff-ff-ff-ff-ff-ff     static`,

          "netstat -ano": `Active Connections

  Proto  Local Address          Foreign Address        State           PID
  TCP    10.10.10.85:49821      52.96.166.130:443      ESTABLISHED     4812
  TCP    10.10.10.85:51221      13.107.42.16:443       ESTABLISHED     4812
  TCP    10.10.10.85:58900      10.100.1.10:88         ESTABLISHED     824
  UDP    10.10.10.85:61204      10.100.1.10:53                         1102`,

          "curl -I https://portal.kyndryl.com": `HTTP/2 200 
content-type: text/html; charset=utf-8
server: Kyndryl-Cloud-Edge/2.4
date: Tue, 13 Oct 2026 18:25:00 GMT
strict-transport-security: max-age=31536000; includeSubDomains
x-frame-options: DENY
x-content-type-options: nosniff
content-length: 48921`,

          "route print": `===========================================================================
IPv4 Route Table
===========================================================================
Active Routes:
Network Destination        Netmask          Gateway       Interface  Metric
          0.0.0.0          0.0.0.0       10.10.10.1     10.10.10.85      25
       10.10.10.0    255.255.255.0         On-link      10.10.10.85     281
      10.10.10.85  255.255.255.255         On-link      10.10.10.85     281
     10.10.10.255  255.255.255.255         On-link      10.10.10.85     281
        127.0.0.1  255.255.255.255         On-link        127.0.0.1     331
===========================================================================`
        }
      }
    };

    let activeDeviceId = "core-sw";
    const terminalSessionBuffers = {};
    const commandHistories = { "core-sw": [], "acc-sw": [], "edge-rtr": [], "fw": [], "wlc": [], "host-pc": [] };
    const historyIndices = { "core-sw": -1, "acc-sw": -1, "edge-rtr": -1, "fw": -1, "wlc": -1, "host-pc": -1 };

    function initTerminalUI() {
      // Initialize buffers with welcome banners
      for (const devId in deviceConfigs) {
        terminalSessionBuffers[devId] = `<div class="terminal-output">${deviceConfigs[devId].banner}</div>`;
      }
      renderActiveDeviceUI();
    }

    function switchDevice(devId) {
      if (!deviceConfigs[devId]) return;
      
      // Save current terminal body
      terminalSessionBuffers[activeDeviceId] = document.getElementById('termBody').innerHTML;

      // Update active ID
      activeDeviceId = devId;
      
      renderActiveDeviceUI();
    }

    function renderActiveDeviceUI() {
      const dev = deviceConfigs[activeDeviceId];

      // Update Device buttons
      document.querySelectorAll('.device-btn').forEach(btn => btn.classList.remove('active'));
      const activeBtn = document.getElementById(`devBtn-${activeDeviceId}`);
      if (activeBtn) activeBtn.classList.add('active');

      // Update Topology Nodes
      document.querySelectorAll('.topo-node').forEach(node => node.classList.remove('active'));
      const activeTopo = document.getElementById(`topoNode-${activeDeviceId}`);
      if (activeTopo) activeTopo.classList.add('active');

      // Update Window Header
      document.getElementById('terminalTitle').innerText = dev.title;
      document.getElementById('terminalBadge').innerText = dev.badge;

      // Update Prompt
      const promptEl = document.getElementById('terminalPrompt');
      promptEl.innerText = dev.prompt;
      promptEl.style.color = dev.promptColor;

      // Update Presets
      const presetsEl = document.getElementById('terminalPresets');
      presetsEl.innerHTML = "";
      dev.presets.forEach(p => {
        const btn = document.createElement('button');
        btn.className = "btn-sm";
        btn.innerText = p.label;
        btn.onclick = () => runPreset(p.cmd);
        presetsEl.appendChild(btn);
      });

      // Restore terminal output
      const termBody = document.getElementById('termBody');
      termBody.innerHTML = terminalSessionBuffers[activeDeviceId] || `<div class="terminal-output">${dev.banner}</div>`;
      termBody.scrollTop = termBody.scrollHeight;

      // Focus input
      const inputEl = document.getElementById('termInput');
      inputEl.value = "";
      inputEl.placeholder = activeDeviceId === 'host-pc' ? "Type PowerShell command (e.g. ipconfig /all, ping, tracert)..." : "Type Cisco command (e.g. show ip int br, show ip route)...";
      inputEl.focus();
    }

    function executeCurrentInput() {
      const input = document.getElementById('termInput');
      const rawCmd = input.value.trim();
      if (!rawCmd) return;

      // Record in history
      const history = commandHistories[activeDeviceId];
      history.push(rawCmd);
      historyIndices[activeDeviceId] = history.length;

      printTerminalCommand(rawCmd);
      input.value = "";
    }

    function handleTerminalKey(e) {
      const history = commandHistories[activeDeviceId];
      if (e.key === 'Enter') {
        executeCurrentInput();
      } else if (e.key === 'ArrowUp') {
        if (history.length > 0 && historyIndices[activeDeviceId] > 0) {
          historyIndices[activeDeviceId]--;
          document.getElementById('termInput').value = history[historyIndices[activeDeviceId]];
        }
      } else if (e.key === 'ArrowDown') {
        if (historyIndices[activeDeviceId] < history.length - 1) {
          historyIndices[activeDeviceId]++;
          document.getElementById('termInput').value = history[historyIndices[activeDeviceId]];
        } else {
          historyIndices[activeDeviceId] = history.length;
          document.getElementById('termInput').value = "";
        }
      }
    }

    function runPreset(cmd) {
      printTerminalCommand(cmd);
    }

    function printTerminalCommand(cmd) {
      const term = document.getElementById('termBody');
      const dev = deviceConfigs[activeDeviceId];
      const lower = cmd.toLowerCase().trim();

      if (lower === 'clear' || lower === 'cls') {
        term.innerHTML = "";
        terminalSessionBuffers[activeDeviceId] = "";
        return;
      }

      let response = dev.commands[lower];

      // Fuzzy shortcut resolution
      if (!response) {
        for (let key in dev.commands) {
          if (key === lower) {
            response = dev.commands[key];
            break;
          }
          // Handle common Cisco abbreviations: sh -> show, int -> interface, br -> brief, neigh -> neighbor
          let normalizedKey = key.replace(/interface/g, 'int').replace(/brief/g, 'br').replace(/neighbor/g, 'neigh').replace(/show/g, 'sh');
          let normalizedInput = lower.replace(/interface/g, 'int').replace(/brief/g, 'br').replace(/neighbor/g, 'neigh').replace(/show/g, 'sh');
          if (normalizedKey === normalizedInput || key.startsWith(lower) || normalizedKey.startsWith(normalizedInput)) {
            response = dev.commands[key];
            break;
          }
        }
      }

      if (!response) {
        if (activeDeviceId === 'host-pc') {
          response = `'${cmd}' is not recognized as the name of a cmdlet, function, script file, or operable program. Type 'help' to see available commands.`;
        } else if (activeDeviceId === 'fw') {
          response = `% [ERROR] Command '${cmd}' not recognized in current context. Type 'help' for valid ASA commands.`;
        } else {
          response = `% Invalid command: "${cmd}". Type 'help' to see valid commands for ${dev.name}.`;
        }
      }

      const block = document.createElement('div');
      block.innerHTML = `
        <div style="color: #ffffff; margin-top: 10px; font-weight:600;">
          <span style="color: ${dev.promptColor};">${dev.prompt}</span> <span style="color: #38bdf8;">${cmd}</span>
        </div>
        <div class="terminal-output">${response}</div>
      `;
      term.appendChild(block);
      term.scrollTop = term.scrollHeight;
      terminalSessionBuffers[activeDeviceId] = term.innerHTML;
    }


    
    // 7 Core Network Engineer Topics Database with Direct Links & CLI Labs
    const engineerTopicsData = ENGINEER_TOPICS_PLACEHOLDER;
    let currentSprintFilter = 'all';

    function renderEngineerTopicsUI() {
      const container = document.getElementById('engineerTopicsContainer');
      if (!container) return;
      container.innerHTML = "";

      const searchQuery = (document.getElementById('engSearchInput')?.value || "").toLowerCase().trim();

      engineerTopicsData.forEach((topic, tIdx) => {
        // Sprint filter
        if (currentSprintFilter !== 'all' && topic.sprintTag !== currentSprintFilter) {
          if (!searchQuery) return;
        }

        // Filter lessons
        const visibleLessons = topic.lessons.filter(l => {
          if (!searchQuery) return true;
          return l.name.toLowerCase().includes(searchQuery) || topic.title.toLowerCase().includes(searchQuery) || topic.desc.toLowerCase().includes(searchQuery);
        });

        if (searchQuery && visibleLessons.length === 0) return;

        // Calculate progress for this topic
        const doneCount = topic.lessons.filter(l => appState.completedLessons.includes(l.slug)).length;
        const totalCount = topic.lessons.length;
        const topicPct = Math.round((doneCount / totalCount) * 100);

        const card = document.createElement('div');
        card.className = "eng-topic-card";
        card.id = `eng-topic-card-${tIdx}`;

        const isAutoOpen = searchQuery || currentSprintFilter !== 'all' || tIdx <= 1;

        card.innerHTML = `
          <div class="eng-topic-header ${isAutoOpen ? 'open' : ''}" onclick="toggleEngineerTopic(${tIdx})">
            <div class="eng-topic-info">
              <span class="eng-topic-icon">${topic.icon}</span>
              <div class="eng-topic-meta">
                <div class="eng-topic-badges">
                  <span class="badge-sprint">${topic.sprint}</span>
                  <span class="badge-priority">${topic.num}</span>
                  <span class="badge-device-target">💻 Target: ${topic.targetDeviceName}</span>
                </div>
                <div class="eng-topic-title">${topic.title}</div>
              </div>
            </div>
            <div class="eng-topic-actions-right">
              <span class="eng-topic-counter-pill" id="eng-topic-pill-${tIdx}">${doneCount}/${totalCount} Done (${topicPct}%)</span>
              <span class="eng-topic-arrow" id="eng-arrow-${tIdx}">${isAutoOpen ? '▲' : '▼'}</span>
            </div>
          </div>

          <div class="eng-topic-body" id="eng-body-${tIdx}" style="${isAutoOpen ? 'display:flex;' : 'display:none;'}">
            
            <!-- NOC Application Callout -->
            <div class="eng-noc-callout">
              <strong>🚨 Kyndryl NOC Focus:</strong> ${topic.nocFocus}
            </div>

            <!-- Key Cisco Commands Showcase -->
            <div class="eng-cmds-wrap">
              <div class="eng-cmds-header">
                <span>🛠️ Core Diagnostic Show Commands (${topic.commands.length})</span>
                <button class="btn-sm primary" onclick="event.stopPropagation(); jumpToTerminal('${topic.targetDevice}', '${topic.defaultCmd}')">
                  💻 Launch ${topic.targetDeviceName} Simulator
                </button>
              </div>
              <div class="eng-cmds-grid">
                ${topic.commands.map(c => `
                  <div class="eng-cmd-row">
                    <div style="overflow:hidden;">
                      <div class="eng-cmd-text">${c.cmd}</div>
                      <div class="eng-cmd-desc">${c.desc}</div>
                    </div>
                    <div style="display:flex; gap:6px; flex-shrink:0;">
                      <button class="btn-sm" style="font-size:0.7rem; padding:3px 8px;" onclick="event.stopPropagation(); copyText('${c.cmd}')">Copy</button>
                      <button class="btn-sm" style="font-size:0.7rem; padding:3px 8px;" onclick="event.stopPropagation(); jumpToTerminal('${topic.targetDevice}', '${c.cmd}')">Run</button>
                    </div>
                  </div>
                `).join('')}
              </div>
            </div>

            <!-- Lessons Checklist -->
            <div>
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                <span style="font-size:0.8rem; font-weight:800; color:var(--text-muted); text-transform:uppercase; letter-spacing:0.5px;">
                  Curated Lessons (${visibleLessons.length} of ${totalCount})
                </span>
                <span style="font-size:0.75rem; color:var(--cyan);">Direct SSO Watch Links Enabled</span>
              </div>
              <div class="eng-lessons-wrap">
                ${visibleLessons.map(l => {
                  const isDone = appState.completedLessons.includes(l.slug);
                  return `
                    <div class="lesson-row ${isDone ? 'completed' : ''}">
                      <div class="lesson-left">
                        <input type="checkbox" class="lesson-checkbox" id="eng-${l.slug}" data-slug="${l.slug}" ${isDone ? 'checked' : ''} onchange="handleEngineerCheckbox(this)">
                        <a href="${l.url}" target="_blank" class="lesson-link" title="Open lesson on LinkedIn Learning">${l.name}</a>
                        ${l.isPriority ? `<span class="badge-priority">⭐ Kyndryl L1 Core</span>` : ''}
                      </div>
                      <div class="lesson-right">
                        ${l.duration ? `<span class="lesson-duration">${l.duration}</span>` : ''}
                        <a href="${l.url}" target="_blank" class="btn-sm watch-btn" title="Open video lesson in new tab">▶ Watch</a>
                      </div>
                    </div>
                  `;
                }).join('')}
              </div>
            </div>

          </div>
        `;

        container.appendChild(card);
      });

      updateEngineerStatsUI();
    }

    function toggleEngineerTopic(idx) {
      const body = document.getElementById(`eng-body-${idx}`);
      const arrow = document.getElementById(`eng-arrow-${idx}`);
      const header = document.querySelector(`#eng-topic-card-${idx} .eng-topic-header`);
      if (!body) return;

      if (body.style.display === "none") {
        body.style.display = "flex";
        arrow.innerText = "▲";
        header.classList.add('open');
      } else {
        body.style.display = "none";
        arrow.innerText = "▼";
        header.classList.remove('open');
      }
    }

    function expandAllEngineerTopics() {
      engineerTopicsData.forEach((_, idx) => {
        const body = document.getElementById(`eng-body-${idx}`);
        const arrow = document.getElementById(`eng-arrow-${idx}`);
        const header = document.querySelector(`#eng-topic-card-${idx} .eng-topic-header`);
        if (body) body.style.display = "flex";
        if (arrow) arrow.innerText = "▲";
        if (header) header.classList.add('open');
      });
    }

    function collapseAllEngineerTopics() {
      engineerTopicsData.forEach((_, idx) => {
        const body = document.getElementById(`eng-body-${idx}`);
        const arrow = document.getElementById(`eng-arrow-${idx}`);
        const header = document.querySelector(`#eng-topic-card-${idx} .eng-topic-header`);
        if (body) body.style.display = "none";
        if (arrow) arrow.innerText = "▼";
        if (header) header.classList.remove('open');
      });
    }

    function setSprintFilter(sprintTag) {
      currentSprintFilter = sprintTag;
      document.querySelectorAll('.sprint-chip').forEach(btn => btn.classList.remove('active'));
      event.target.classList.add('active');
      renderEngineerTopicsUI();
    }

    function filterEngineerTopicsUI() {
      renderEngineerTopicsUI();
    }

    function handleEngineerCheckbox(box) {
      const slug = box.dataset.slug || box.id.replace('eng-', '');
      if (box.checked) {
        if (!appState.completedLessons.includes(slug)) {
          appState.completedLessons.push(slug);
        }
      } else {
        appState.completedLessons = appState.completedLessons.filter(s => s !== slug);
      }

      // Sync CCNA tracker checkbox
      const ccnaBox = document.getElementById(slug);
      if (ccnaBox) {
        ccnaBox.checked = box.checked;
        const row = ccnaBox.closest('.lesson-row');
        if (row) {
          if (box.checked) row.classList.add('completed');
          else row.classList.remove('completed');
        }
      }

      const engRow = box.closest('.lesson-row');
      if (engRow) {
        if (box.checked) engRow.classList.add('completed');
        else engRow.classList.remove('completed');
      }

      saveState();
      updateProgressUI();
      updateEngineerStatsUI();
    }

    function updateEngineerStatsUI() {
      let totalLessonsInTopics = 0;
      let totalCompletedInTopics = 0;

      engineerTopicsData.forEach((t, idx) => {
        const done = t.lessons.filter(l => appState.completedLessons.includes(l.slug)).length;
        const total = t.lessons.length;
        totalLessonsInTopics += total;
        totalCompletedInTopics += done;
        const pct = Math.round((done / total) * 100);

        const pill = document.getElementById(`eng-topic-pill-${idx}`);
        if (pill) pill.innerText = `${done}/${total} Done (${pct}%)`;
      });

      const overallPct = totalLessonsInTopics > 0 ? Math.round((totalCompletedInTopics / totalLessonsInTopics) * 100) : 0;

      const statDone = document.getElementById('engStatLessonsDone');
      if (statDone) statDone.innerText = `${totalCompletedInTopics} / ${totalLessonsInTopics}`;

      const statPct = document.getElementById('engStatPct');
      if (statPct) statPct.innerText = `${overallPct}%`;

      const progLabel = document.getElementById('engProgressLabel');
      if (progLabel) progLabel.innerText = `${overallPct}% Done (${totalCompletedInTopics} of ${totalLessonsInTopics} Lessons)`;

      const progBar = document.getElementById('engProgressBar');
      if (progBar) progBar.style.width = `${overallPct}%`;
    }

    function jumpToTerminal(deviceId, cmd) {
      document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
      document.querySelectorAll('.tab-pane').forEach(pane => pane.classList.remove('active'));
      
      const targetBtn = Array.from(document.querySelectorAll('.tab-btn')).find(b => b.getAttribute('onclick')?.includes('terminalTab'));
      if (targetBtn) targetBtn.classList.add('active');
      const termPane = document.getElementById('terminalTab');
      if (termPane) termPane.classList.add('active');

      switchDevice(deviceId);

      if (cmd) {
        setTimeout(() => {
          runPreset(cmd);
          const termEl = document.getElementById('terminalWrap');
          if (termEl) termEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }, 120);
      }
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


    // Career Roadmap & Action Plan Persistent State
    const ROADMAP_STORAGE_KEY = "kyndryl_career_roadmap_state";
    let roadmapState = {
      courses: {},
      actions: {}
    };

    function loadRoadmapState() {
      const saved = localStorage.getItem(ROADMAP_STORAGE_KEY);
      if (saved) {
        try { roadmapState = JSON.parse(saved); } catch(e) {}
      }
      
      // Restore course checkboxes
      document.querySelectorAll('.roadmap-checkbox').forEach(box => {
        box.checked = !!roadmapState.courses[box.id];
      });

      // Restore action plan checkboxes
      document.querySelectorAll('.action-checkbox').forEach(box => {
        const isDone = !!roadmapState.actions[box.id];
        box.checked = isDone;
        const row = box.closest('.action-step-item');
        if (row) {
          if (isDone) row.classList.add('checked');
          else row.classList.remove('checked');
        }
      });

      updateActionPlanUI();
      highlightTodaySchedule();
    }

    function saveRoadmapCheckboxes() {
      roadmapState.courses = {};
      document.querySelectorAll('.roadmap-checkbox:checked').forEach(box => {
        roadmapState.courses[box.id] = true;
      });
      localStorage.setItem(ROADMAP_STORAGE_KEY, JSON.stringify(roadmapState));
    }

    function handleActionPlanCheck(box) {
      roadmapState.actions[box.id] = box.checked;
      const row = box.closest('.action-step-item');
      if (row) {
        if (box.checked) row.classList.add('checked');
        else row.classList.remove('checked');
      }
      localStorage.setItem(ROADMAP_STORAGE_KEY, JSON.stringify(roadmapState));
      updateActionPlanUI();
    }

    function updateActionPlanUI() {
      const allActions = document.querySelectorAll('.action-checkbox');
      const checkedActions = document.querySelectorAll('.action-checkbox:checked');
      const counter = document.getElementById('actionPlanCounter');
      if (counter) {
        counter.innerText = `${checkedActions.length} / ${allActions.length} Steps Completed`;
      }
    }

    function highlightTodaySchedule() {
      const today = new Date().getDay(); // 0 is Sunday, 1 is Monday...
      document.querySelectorAll('.schedule-day-row').forEach(row => row.classList.remove('is-today'));
      const todayRow = document.getElementById(`day-row-${today}`);
      if (todayRow) {
        todayRow.classList.add('is-today');
        if (!todayRow.querySelector('.today-pill')) {
          const pill = document.createElement('span');
          pill.className = 'today-pill';
          pill.innerText = "Today's Focus";
          todayRow.appendChild(pill);
        }
      }
    }

    function resetRoadmapProgress() {
      if (confirm("Reset your Career Roadmap and Action Plan checkboxes?")) {
        roadmapState = { courses: {}, actions: {} };
        localStorage.removeItem(ROADMAP_STORAGE_KEY);
        loadRoadmapState();
      }
    }



    // Kevin Wallace 15-Course Master Library Database
    const kwCoursesData = KW_COURSES_PLACEHOLDER;
    let currentKWTier = 'all';

    function renderKWCatalogUI() {
      const container = document.getElementById('kwCoursesContainer');
      if (!container) return;
      container.innerHTML = "";

      const query = (document.getElementById('kwSearchInput')?.value || "").toLowerCase().trim();

      kwCoursesData.forEach((c, idx) => {
        if (currentKWTier !== 'all' && c.tierTag !== currentKWTier) {
          if (!query) return;
        }

        if (query) {
          const matchTitle = c.title.toLowerCase().includes(query);
          const matchDesc = c.desc.toLowerCase().includes(query);
          const matchSkills = c.skills.some(s => s.toLowerCase().includes(query));
          const matchMods = c.modules.some(m => m.toLowerCase().includes(query));
          if (!matchTitle && !matchDesc && !matchSkills && !matchMods) return;
        }

        const card = document.createElement('div');
        card.className = "kw-card";
        card.id = `kw-card-${idx}`;

        card.innerHTML = `
          <div>
            <div class="kw-card-top">
              <div class="kw-card-badges">
                <span class="kw-badge-tier ${c.tierTag}">${c.tier}</span>
                <span class="kw-badge-cert">${c.cert}</span>
                <span style="font-size:0.68rem; font-weight:800; color:var(--text-dim);">${c.num}</span>
              </div>
              <span class="kw-duration-pill">${c.duration}</span>
            </div>

            <div class="kw-course-title">${c.title}</div>
            <div class="kw-course-desc" style="margin-top:6px;">${c.desc}</div>

            <div class="kw-package-box">
              <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:6px;">
                <span class="kw-package-tag">💰 Target Package: <strong>${c.package || '₹4.5–6.5 LPA'}</strong></span>
                <span class="kw-package-role">${c.packageRole || 'Network Specialist'}</span>
              </div>
              <div style="font-size:0.75rem; color:var(--text-muted); margin-top:5px;">
                🏢 <strong style="color:#e2e8f0;">Hiring in BLR:</strong> ${c.companies || 'Kyndryl, Cisco, NTT Data, Wipro'}
              </div>
              <div style="font-size:0.75rem; color:var(--cyan); margin-top:3px;">
                🛠️ <strong style="color:#e2e8f0;">Lab Package:</strong> ${c.labPackage || 'Packet Tracer 8.2+, Wireshark'}
              </div>
            </div>

            <div class="kw-modules-box" style="margin-top:10px;">
              <div class="kw-modules-header" onclick="toggleKWModules(${idx})">
                <span>📚 Course Structure (${c.modules.length} Modules)</span>
                <span id="kw-arrow-${idx}" style="font-size:0.75rem; color:var(--cyan);">▼</span>
              </div>
              <div class="kw-modules-list" id="kw-mods-${idx}" style="${query ? 'display:flex;' : 'display:none;'}">
                ${c.modules.map(m => `
                  <div class="kw-mod-item">
                    <span style="color:var(--cyan); font-weight:800;">•</span>
                    <span>${m}</span>
                  </div>
                `).join('')}
                ${c.interviewDeliverable ? `
                  <div style="margin-top:8px; padding-top:8px; border-top:1px dashed rgba(255,255,255,0.12); font-size:0.74rem; color:#f59e0b;">
                    🎯 <strong>Interview Deliverable:</strong> ${c.interviewDeliverable}
                  </div>
                ` : ''}
              </div>
            </div>
          </div>

          <div style="display:flex; justify-content:space-between; align-items:flex-end; gap:10px; margin-top:8px;">
            <div class="kw-skills-strip">
              ${c.skills.slice(0, 3).map(s => `<span class="kw-skill-tag">${s}</span>`).join('')}
            </div>
            <a href="${c.url}" target="_blank" class="btn-sm primary" style="white-space:nowrap;">▶ Watch on LinkedIn</a>
          </div>
        `;

        container.appendChild(card);
      });
    }

    function toggleKWModules(idx) {
      const list = document.getElementById(`kw-mods-${idx}`);
      const arrow = document.getElementById(`kw-arrow-${idx}`);
      if (!list) return;
      if (list.style.display === "none") {
        list.style.display = "flex";
        if (arrow) arrow.innerText = "▲";
      } else {
        list.style.display = "none";
        if (arrow) arrow.innerText = "▼";
      }
    }

    function expandAllKWModules() {
      kwCoursesData.forEach((_, idx) => {
        const list = document.getElementById(`kw-mods-${idx}`);
        const arrow = document.getElementById(`kw-arrow-${idx}`);
        if (list) list.style.display = "flex";
        if (arrow) arrow.innerText = "▲";
      });
    }

    function collapseAllKWModules() {
      kwCoursesData.forEach((_, idx) => {
        const list = document.getElementById(`kw-mods-${idx}`);
        const arrow = document.getElementById(`kw-arrow-${idx}`);
        if (list) list.style.display = "none";
        if (arrow) arrow.innerText = "▼";
      });
    }

    function setKWTierFilter(tierTag) {
      currentKWTier = tierTag;
      document.querySelectorAll('.kw-filter-chip').forEach(btn => btn.classList.remove('active'));
      event.target.classList.add('active');
      renderKWCatalogUI();
    }


    function loadState() {
      const saved = localStorage.getItem(STORAGE_KEY);
      if (saved) {
        try { appState = JSON.parse(saved); } catch (e) {}
      }
      renderModules();
      renderEngineerTopicsUI();
      updateProgressUI();
      updateEngineerStatsUI();
    }

    function saveState() {
      const checkedIds = [];
      document.querySelectorAll('.lesson-checkbox:checked').forEach(box => checkedIds.push(box.id));
      appState.completedLessons = checkedIds;
      localStorage.setItem(STORAGE_KEY, JSON.stringify(appState));
    }

    function updateProgress() {
      const checkedIds = [];
      document.querySelectorAll('.lesson-checkbox').forEach(box => {
        const slug = box.dataset.slug || box.id.replace('eng-', '');
        const row = box.closest('.lesson-row');
        if (box.checked) {
          if (row) row.classList.add('completed');
          if (!checkedIds.includes(slug)) checkedIds.push(slug);
        } else {
          if (row) row.classList.remove('completed');
        }
      });
      appState.completedLessons = checkedIds;
      
      // Synchronize all checkboxes across both tabs
      document.querySelectorAll('.lesson-checkbox').forEach(box => {
        const slug = box.dataset.slug || box.id.replace('eng-', '');
        const isDone = appState.completedLessons.includes(slug);
        box.checked = isDone;
        const row = box.closest('.lesson-row');
        if (row) {
          if (isDone) row.classList.add('completed');
          else row.classList.remove('completed');
        }
      });

      saveState();
      updateProgressUI();
      updateEngineerStatsUI();
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
        renderEngineerTopicsUI();
      }
    }

    window.addEventListener('DOMContentLoaded', () => {
      renderCommands();
      renderQA();
      loadState();
      initTerminalUI();
    });
  </script>
</body>
</html>
"""

full_html = html_template.replace('MODULES_PLACEHOLDER', modules_js).replace('ENGINEER_TOPICS_PLACEHOLDER', engineer_topics_js).replace('KW_COURSES_PLACEHOLDER', kw_courses_js)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print("Updated index.html with priority tagging and toggle button!")
