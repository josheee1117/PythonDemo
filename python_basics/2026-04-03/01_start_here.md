# Day 1 入口：先把 VS Code 真正用起来

今天不先读长文，直接按顺序做两个实验：

1. 打开项目并绑定正确解释器
2. 跑通第一个脚本
3. 用一个断点完成一次最小调试

## 你今天只需要产出两个结果

- `python_basics/2026-04-03/04_vscode_quickstart.py` 可以正常运行
- `python_basics/2026-04-03/05_vscode_debug_demo.py` 里的故意错误被你自己定位并修好

## 学习顺序

1. 先做 `02_lab_vscode_workspace_setup.md`
2. 再做 `03_lab_vscode_run_and_debug.md`
3. 两个实验都完成后，再结束今天学习

## 开始前只确认一件事

当前项目已经有虚拟环境：

```powershell
.\.venv\Scripts\python.exe --version
```

你当前项目里的实际版本是 `Python 3.12.11`。

## 自检标准

- VS Code 左下角或右下角能看到当前解释器已经切到 `.venv`
- 你至少亲手运行过 2 次 Python 文件
- 你至少亲手打过 1 个断点
