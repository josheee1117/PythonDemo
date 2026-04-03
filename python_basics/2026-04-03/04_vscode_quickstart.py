project_name = "PythonDemo"
editor_name = "VS Code"

# TODO 1: 改成今天这节课的主题
today_topic = "使用 VS Code 进行 Python 开发"

# TODO 2: 改成当前项目虚拟环境解释器的相对路径
interpreter_path = ".\\.venv\\Scripts\\python.exe"

# TODO 3: 改成你在终端里准备执行的脚本命令
run_command = ".\\.venv\\Scripts\\python.exe python_basics\\2026-04-03\\04_vscode_quickstart.py"

print("=== Day 1 Quickstart ===")
print(f"project_name = {project_name}")
print(f"editor_name = {editor_name}")
print(f"today_topic = {today_topic}")
print(f"interpreter_path = {interpreter_path}")
print(f"run_command = {run_command}")

assert today_topic == "使用 VS Code 进行 Python 开发", "TODO 1 还没填对"
assert interpreter_path == ".\\.venv\\Scripts\\python.exe", "TODO 2 还没填对"
assert "04_vscode_quickstart.py" in run_command, "TODO 3 至少要指向当前脚本"

print("自检通过：你已经在这个项目里完成了第一次 VS Code + Python 运行。")
