# 实验 1：工作区、解释器、第一次运行

目标：让 VS Code 真正接管这个项目里的 Python 运行环境。

## 步骤 1：打开项目

如果你已经在 VS Code 里打开了 `D:\code\PythonDemo`，直接进入下一步。  
如果还没有打开：

- 方式 1：在 VS Code 里选择 `File -> Open Folder`
- 方式 2：如果你的机器上 `code` 命令可用，运行：

```powershell
code D:\code\PythonDemo
```

## 步骤 2：确认扩展

只检查两个扩展是否可用：

- `Python`
- `Pylance`

如果缺少，就先安装。今天不研究更多插件。

## 步骤 3：选择解释器

打开命令面板：

```text
Ctrl + Shift + P
```

执行：

```text
Python: Select Interpreter
```

然后选择当前项目的虚拟环境：

```text
D:\code\PythonDemo\.venv\Scripts\python.exe
```

如果列表里没有，就手动浏览到这个路径。

## 步骤 4：完成第一个小练习

打开文件：

```text
python_basics/2026-04-03/04_vscode_quickstart.py
```

把里面的 3 个 `TODO` 改成当前项目的真实值，然后先在 VS Code 终端里运行：

```powershell
.\.venv\Scripts\python.exe python_basics\2026-04-03\04_vscode_quickstart.py
```

跑通后，再用编辑器右上角的 `Run Python File` 按钮再运行一次。

## 你要观察什么

- 终端里用的是不是当前项目的 `.venv`
- 两种运行方式的输出是否一致
- `assert` 是否全部通过

## Java 对照

- 这里的“选择解释器”，可以类比成在 IDEA 里给项目指定正确的 JDK
- 区别在于 Python 项目更常见的是“每个项目一个虚拟环境”，而不是全局只用一个运行时

## 常见错误

- 运行时误用了系统 Python，而不是项目里的 `.venv`
- 只点了运行按钮，没有先确认解释器路径
- 改了代码但没保存，就直接运行

## 完成标准

- 你能在终端里看到脚本正常输出
- 你能在 VS Code 里用按钮再次运行成功
- `04_vscode_quickstart.py` 不再触发断言错误
