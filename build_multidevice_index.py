import json
import sys

# 1. Load modules
with open('clean_modules_with_priority.json', encoding='utf-8') as f:
    modules = json.load(f)

modules_js = json.dumps(modules)

# 2. Read snippets
with open('terminal_styles.css', encoding='utf-8') as f:
    terminal_css = f.read()

with open('terminal_markup.html', encoding='utf-8') as f:
    terminal_html = f.read()

with open('terminal_script.js', encoding='utf-8') as f:
    terminal_js = f.read()

# 3. Read build_index_html.py to get base template
with open('build_index_html.py', encoding='utf-8') as f:
    base_script = f.read()

css_marker_start = "    /* CLI SIMULATOR */"
css_marker_end = "    /* SUBNET DRILL */"

html_marker_start = "    <!-- TAB 2: INTERACTIVE CISCO CLI TERMINAL SIMULATOR -->"
html_marker_end = "    <!-- TAB 3: SUBNETTING SPEED TRAINER -->"

js_marker_start = "    // Cisco CLI Terminal Outputs Database\n    const terminalDatabase = {"
js_marker_end = "    // Subnetting Drill\n    let currentDrill = {"

if css_marker_start not in base_script:
    print("Error: CSS marker start not found in build_index_html.py")
    sys.exit(1)
if html_marker_start not in base_script:
    print("Error: HTML marker start not found in build_index_html.py")
    sys.exit(1)
if js_marker_start not in base_script:
    print("Error: JS marker start not found in build_index_html.py")
    sys.exit(1)

# Perform replacement
idx1 = base_script.find(css_marker_start)
idx2 = base_script.find(css_marker_end)
step1 = base_script[:idx1] + terminal_css + "\n" + base_script[idx2:]

idx3 = step1.find(html_marker_start)
idx4 = step1.find(html_marker_end)
step2 = step1[:idx3] + terminal_html + "\n" + step1[idx4:]

idx5 = step2.find(js_marker_start)
idx6 = step2.find(js_marker_end)
step3 = step2[:idx5] + terminal_js + "\n\n    " + step2[idx6:]

if "initTerminalUI();" not in step3:
    step4 = step3.replace("renderCommands();\n      renderQA();\n      loadState();", "renderCommands();\n      renderQA();\n      loadState();\n      initTerminalUI();")
else:
    step4 = step3

# Save updated build_index_html.py
with open('build_index_html.py', 'w', encoding='utf-8') as f:
    f.write(step4)

print("build_index_html.py updated successfully!")
