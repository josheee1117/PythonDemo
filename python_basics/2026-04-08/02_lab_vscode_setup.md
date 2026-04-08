# Lab：VS Code 工作区搭建、运行与调试

目标：把 VS Code 从"能打开文件"变成"能跑代码、能调试"，建立完整开发闭环。

---

## 步骤 1：确认工作区解释器（5 分钟）

1. 用 VS Code 打开 `D:\code\PythonDemo` 文件夹
2. 按 `Ctrl+Shift+P`，输入 `Python: Select Interpreter`
3. 选择 `.\.venv\Scripts\python.exe`

**验证**：看 VS Code 右下角状态栏，应该显示类似 `3.12.11 ('.venv')`

**Java 对照**：这一步相当于在 IntelliJ 里设置 Project SDK。区别是 Python 没有编译步骤，选好解释器就能直接运行。

---

## 步骤 2：从终端运行第一个脚本（5 分钟）

打开 VS Code 内置终端（`Ctrl+`` `），运行：

```powershell
.\.venv\Scripts\python.exe python_basics\2026-04-08\03_vscode_lab.py
```

你会看到断言失败，输出类似：

```
AssertionError: TODO: 请把这里改成你的名字
```

这是正常的，先不改，继续下一步。

---

## 步骤 3：从运行按钮执行（5 分钟）

1. 在 VS Code 中打开 `03_vscode_lab.py`
2. 点击右上角的 **▶ 运行** 按钮（或按 `Ctrl+F5`）
3. 观察底部终端输出，同样会看到断言失败

**两种运行方式的区别**：
- 终端运行：你手动指定解释器路径，更明确
- 运行按钮：VS Code 自动使用工作区解释器，更方便

**Java 对照**：相当于 IntelliJ 里的 `Run` 按钮 vs 命令行 `java -jar`。

---

## 步骤 4：补完 3 个 TODO（10 分钟）

打开 `03_vscode_lab.py`，找到 3 处 `TODO` 注释，按要求填写。

改完后再次运行，直到看到：

```
========================================
所有检查通过！VS Code 基础环境已就绪。
========================================
```

**重点观察**：运行成功后，仔细看控制台输出的每一行，特别是 `type(...)` 的结果。

---

## 步骤 5：设置断点并调试（15 分钟）

1. 在 `03_vscode_lab.py` 的 `greet` 函数第一行点击行号左侧，设置一个红色断点
2. 按 `F5` 启动调试（首次可能需要选择 "Python File" 配置）
3. 程序会停在断点处

**调试面板操作**：
- 左侧 **变量** 面板：查看 `name` 参数的值
- 按 `F10`（Step Over）：单步执行，观察变量变化
- 按 `F11`（Step Into）：进入函数内部
- 按 `F5`（Continue）：继续运行到下一个断点或结束

**练习**：
1. 在 `calculate_year` 函数也设置一个断点
2. 运行调试，观察 `birth_year` 和 `current_year` 的值
3. 用 **调试控制台**（Debug Console）输入 `type(birth_year)` 查看类型

**Java 对照**：操作方式和 IntelliJ 几乎一致。唯一区别是 Python 没有编译步骤，断点直接在源码上生效。

---

## 步骤 6：理解 launch.json（5 分钟）

按 `F5` 调试后，VS Code 会在 `.vscode/launch.json` 生成调试配置。打开这个文件看一下结构：

```json
{
    "name": "Python: 当前文件",
    "type": "debugpy",
    "request": "launch",
    "program": "${file}"
}
```

**Java 对照**：相当于 IntelliJ 的 Run/Debug Configuration。`program` 对应 Main Class。

---

## 完成标准

- `03_vscode_lab.py` 运行通过，所有断言不报错
- 你用过终端运行和运行按钮两种方式
- 你至少调试过一次，在变量面板看过变量值
- 你知道 `launch.json` 是干什么的

## 常见错误

- **解释器没选对**：运行时报 `ModuleNotFoundError` 或用了系统 Python → 重新 `Ctrl+Shift+P` 选择 `.venv`
- **终端路径不对**：确保终端当前目录是项目根目录 `D:\code\PythonDemo`
- **断点不生效**：确保用 `F5`（调试）而不是 `Ctrl+F5`（运行），后者不会停在断点
