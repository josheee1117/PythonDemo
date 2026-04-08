# Day 1 入口：先把 VS Code + Python 跑起来

今天做三件事：

1. 把 VS Code 和 Python 解释器真正跑通
2. 独立定位并修复一段有 bug 的代码
3. 初识 Python 的代码审美标准

## 你今天要产出三个结果

- `03_vscode_lab.py` 运行通过，所有断言没有报错
- `05_debug_challenge.py` 的 3 个 bug 被你独立修复
- 能用自己的话说出 Python 之禅中 3 条箴言的含义

## 学习顺序

1. 先做 Lab — `02_lab_vscode_setup.md`
2. 再做 Challenge — `04_challenge_debug.md`
3. 最后做 Code Taste — `06_taste_zen_and_pep8.md`

## 开始前确认一件事

在项目根目录运行：

```powershell
.\.venv\Scripts\python.exe --version
```

如果能输出版本号（应该是 `Python 3.12.11`），直接进入 Lab。

## 自检标准

- VS Code 左下角/右下角能看到解释器已切到 `.venv`
- 你至少亲手运行过 3 次 Python 文件
- 你至少亲手打过 2 个断点
- 你能解释 Python 之禅里"明确胜于隐晦"在代码中的含义
