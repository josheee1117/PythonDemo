# Code Taste：Python 之禅与 PEP 8 初识

> 素材来源：《Python编程之美》p66-68

今天是第一次 Code Taste 训练。目标不是记规则，而是建立"什么样的 Python 代码是好代码"的直觉。

---

## 第 1 部分：Python 之禅（5 分钟）

在终端里运行：

```powershell
.\.venv\Scripts\python.exe -c "import this"
```

你会看到 19 条箴言。先通读一遍，然后重点看这 3 条：

1. **明确胜于隐晦**（Explicit is better than implicit）
2. **简单胜于复杂**（Simple is better than complex）
3. **可读性很重要**（Readability counts）

**Java 对照**：Java 社区也强调可读性，但 Java 的"好代码"通常意味着更多的类型声明和分层抽象。Python 的"好代码"更倾向于直接、简洁、不过度设计。

---

## 第 2 部分：对比阅读 — 明确胜于隐晦（10 分钟）

### 例子 1：函数参数

```python
# ❌ 糟糕写法：调用者无法从函数签名看出需要什么
def make_dict(*args):
    x, y = args
    return dict(**locals())

# ✅ Pythonic 写法：参数和返回值一目了然
def make_dict(x, y):
    return {'x': x, 'y': y}
```

**判断标准**：其他开发者能否只看函数的第一行和最后一行就理解它的作用？

### 例子 2：一行多语句

```python
# ❌ 糟糕写法：紧凑但难读
print('one');print('two')
if x == 1: print('one')

# ✅ Pythonic 写法：每行一件事
print('one')
print('two')
if x == 1:
    print('one')
```

**Java 对照**：Java 开发者一般不会写 `System.out.println("one");System.out.println("two");`，Python 也一样。

### 例子 3：复杂条件拆分

```python
# ❌ 糟糕写法：长条件塞在一行
if (user.is_active and user.has_permission and
    not user.is_banned):
    do_something()

# ✅ Pythonic 写法：用有意义的变量名拆分
is_authorized = user.is_active and user.has_permission
is_allowed = is_authorized and not user.is_banned
if is_allowed:
    do_something()
```

**为什么更好**：拆分后，每个中间变量都是自文档的。调试时也能看到每一步的布尔值。

---

## 第 3 部分：PEP 8 风格识别（10 分钟）

下面这段代码有 **5 处**违反 PEP 8 的地方，找出来：

```python
import os, sys
import json

def Calculate_Total(  itemList,taxRate ):
    Total=0
    for item in itemList:
        Total+=item
    result=Total*(1+taxRate)
    return result

class   myCalculator:
    def __init__(self,name):
        self.name=name
```

**提示**：关注这几个方面：
- import 语句的组织方式
- 函数名和变量名的命名风格
- 空格的使用
- 类名的命名风格

### 参考答案（先自己找，再对照）

<details>
<summary>点击展开</summary>

1. `import os, sys` → 每个 import 独占一行：`import os` + `import sys`
2. `Calculate_Total` → 函数名用 snake_case：`calculate_total`
3. `itemList`、`taxRate` → 参数名用 snake_case：`item_list`、`tax_rate`
4. `Total` → 局部变量用 snake_case：`total`
5. `myCalculator` → 类名用 PascalCase：`MyCalculator`
6. 赋值和运算符两侧缺空格：`total = 0`、`total += item`、`result = total * (1 + tax_rate)`
7. 函数参数括号内多余空格 / 缺少空格不统一

其中最重要的 3 条：
- **命名风格**：函数和变量 snake_case，类 PascalCase（这和 Java 的 camelCase 习惯不同！）
- **import 每行一个**
- **运算符两侧加空格**

</details>

---

## Java 开发者特别注意

| Java 习惯 | Python 规范（PEP 8） |
|-----------|---------------------|
| `calculateTotal`（camelCase） | `calculate_total`（snake_case） |
| `MyClass`（PascalCase） | `MyClass`（一致） |
| `MAX_RETRY`（全大写常量） | `MAX_RETRY`（一致） |
| `private int count;`（成员变量 camelCase） | `self.count`（snake_case） |
| `getCount()` / `setCount()` | 直接用属性 `obj.count`，不写 getter/setter |

**核心差异**：Java 用 camelCase 做变量和方法名，Python 用 snake_case。这是写 Python 代码时最容易带入的 Java 习惯，从今天开始刻意纠正。

---

## 今日品味总结

- Python 之禅不是空话，它是代码审查时的判断标准
- PEP 8 是风格底线，Pythonic 是更高追求
- Java 转 Python 最先要改的习惯：命名风格从 camelCase 切到 snake_case
