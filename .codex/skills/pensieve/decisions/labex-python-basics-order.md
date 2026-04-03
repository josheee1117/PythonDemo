# 决策：Python 基础阶段按用户提供的 LabEx 顺序教学

## 背景

用户明确给出一组来自 LabEx 的教学顺序，并要求后续教学按该顺序推进。
当前项目尚未正式开始，因此可以在真实 Day 1 之前直接把该顺序固化为正式路线。

## 决策

- Python 基础阶段默认严格按以下顺序教学：
  1. 使用 VS Code 进行 Python 开发
  2. Python 基础
  3. Python 内置函数
  4. Python 控制流
  5. Python 函数
  6. Python 列表与元组
  7. Python 字典
  8. Python 集合
  9. Python 推导式
  10. Python 字符串操作
  11. Python 字符串格式化
  12. Python 正则表达式
  13. Python 文件和目录路径操作
  14. Python 文件读写
  15. Python JSON 和 YAML 处理
  16. Python 异常处理
  17. Python 调试技术
  18. Python Args 和 Kwargs
  19. Python 装饰器
  20. Python 上下文管理器
  21. Python 面向对象编程（OOP）基础
  22. Python 数据类
  23. Python 打包
  24. Python 主函数
  25. Python 虚拟环境管理
- 该顺序覆盖原来阶段 A 中较概括的“语法差异速通/标准库基础/闭包装饰器”等表达，后续应以这个具体顺序生成学习任务。
- 仍然保留“Java 开发者迁移到 Python”的教学方式，不回退到零基础铺垫。
- 若某一课需要最小化环境准备，可以辅助完成，但不视为后续主题已经正式讲解。

## 直接影响

- 用户说 `开始学习` 时，应从上面顺序的第 1 节开始生成真实 Day 1 材料。
- `LEARNING_SYSTEM.md` 中阶段 A 的描述应与该顺序保持一致。
- 后续每日任务、实验页、练习文件都应围绕这个顺序组织，不再使用其他模板默认顺序。
