# Debug Challenge — 找出 3 个 bug 并修复
# 直接运行这个文件，根据报错信息用 VS Code 调试功能定位问题

# ============================================================
# 函数 1：计算购物车总价
# ============================================================

def calculate_total(prices, discount_rate):
    """计算折扣后的总价"""
    total = 0
    for price in prices:
        total += price
    # bug 在这附近的某个地方
    final_price = total * (1 - float(discount_rate))
    return final_price


# ============================================================
# 函数 2：格式化用户信息
# ============================================================

def format_user_info(name, age, city):
    """把用户信息格式化成一行描述"""
    # 注意每个参数的类型
    description = name + "，" + str(age) + "岁，来自" + city
    return description


# ============================================================
# 函数 3：查找最大值的索引
# ============================================================

def find_max_index(numbers):
    """返回列表中最大值的索引位置"""
    max_value = numbers[0]
    max_index = 0
    for i in range(len(numbers)):
        if numbers[i] > max_value:
            max_value = numbers[i]
            max_index=i
            # 找到更大的值了，但索引更新了吗？
    return max_index


# ============================================================
# 测试（不要修改这部分）
# ============================================================

# 测试 1：购物车总价
prices = [100, 200, 50]
discount = "0.1"  # 九折
result1 = calculate_total(prices, discount)
assert result1 == 315.0, f"测试 1 失败：期望 315.0，实际 {result1}"
print("✓ 测试 1 通过")

# 测试 2：用户信息格式化
result2 = format_user_info("张三", 28, "北京")
assert result2 == "张三，28岁，来自北京", f"测试 2 失败：实际 '{result2}'"
print("✓ 测试 2 通过")

# 测试 3：最大值索引
result3 = find_max_index([3, 7, 2, 9, 4])
assert result3 == 3, f"测试 3 失败：期望索引 3，实际 {result3}"
print("✓ 测试 3 通过")

print()
print("=" * 40)
print("全部通过！你已经能独立使用 VS Code 调试了。")
print("=" * 40)
