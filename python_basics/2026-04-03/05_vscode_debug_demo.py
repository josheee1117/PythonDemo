workspace_name = "PythonDemo"
lesson_name = "Day 1 VS Code"

progress = {
    "extensions_ready": True,
    "interpreter_ready": True,
    "terminal_ready": True,
}

completed_steps = sum(progress.values())
total_steps = 4
completion_rate = completed_steps / total_steps

print("=== Debug Demo ===")
print(f"workspace_name = {workspace_name}")
print(f"lesson_name = {lesson_name}")
print(f"completed_steps = {completed_steps}")
print(f"total_steps = {total_steps}")
print(f"completion_rate = {completion_rate:.0%}")

assert completion_rate == 1.0, (
    "先不要直接猜答案，请先在 VS Code 里打断点，看变量值后再修复。"
)

print("自检通过：你已经完成了一次最小调试闭环。")
