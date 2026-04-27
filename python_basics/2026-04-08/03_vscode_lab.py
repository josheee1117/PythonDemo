# VS Code Lab — starter 文件
# 按照 02_lab_vscode_setup.md 的指引完成下面的 TODO

# ============================================================
# 第 1 部分：基本信息
# ============================================================

# TODO 1: 把下面的 "???" 改成你的名字（字符串）
your_name = "张三"

# TODO 2: 把下面的 ??? 改成你的出生年份（整数，不要加引号）
birth_year = 1990

# TODO 3: 把下面的 ??? 改成你的 Java 开发年限（整数）
java_years = 5


# ============================================================
# 第 2 部分：自动检查（不需要修改这部分）
# ============================================================

def greet(name):
    """生成欢迎信息"""
    return f"你好，{name}！欢迎开始 Python 学习之旅。"


def calculate_year(birth_year):
    """计算年龄"""
    current_year = 2026
    return current_year - birth_year


def describe_experience(years):
    """描述经验水平"""
    if years >= 5:
        return "资深开发者"
    elif years >= 2:
        return "中级开发者"
    else:
        return "初级开发者"


# --- 运行检查 ---
print("=" * 40)
print("正在检查你的代码...")
print("=" * 40)

# 检查 1：名字
assert isinstance(your_name, str), "TODO 1: your_name 应该是字符串"
assert your_name != "???", "TODO 1: 请把 ??? 改成你的名字"
print(f"✓ 名字: {your_name}")
print(f"  类型: {type(your_name).__name__}")

# 检查 2：出生年份
assert isinstance(birth_year, int), "TODO 2: birth_year 应该是整数，不要加引号"
assert 1950 < birth_year < 2010, "TODO 2: 出生年份看起来不太对"
age = calculate_year(birth_year)
print(f"✓ 出生年份: {birth_year}，今年 {age} 岁")
print(f"  类型: {type(birth_year).__name__}")

# 检查 3：Java 年限
assert isinstance(java_years, int), "TODO 3: java_years 应该是整数"
assert java_years > 0, "TODO 3: Java 年限应该大于 0"
level = describe_experience(java_years)
print(f"✓ Java 经验: {java_years} 年 → {level}")
print(f"  类型: {type(java_years).__name__}")

# 检查 4：欢迎信息
message = greet(your_name)
print(f"\n{message}")

# 检查 5：类型总结
print(f"\n--- 类型总结 ---")
print(f"字符串 your_name 的类型: {type(your_name)}")
print(f"整数 birth_year 的类型:  {type(birth_year)}")
print(f"整数 java_years 的类型:  {type(java_years)}")
print(f"函数 greet 的类型:       {type(greet)}")

# 注意看：Python 里一切皆对象，连函数都有类型

print()
print("=" * 40)
print("所有检查通过！VS Code 基础环境已就绪。")
print("=" * 40)
