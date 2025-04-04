
# 🎨 termfx

> Powerful and beautiful terminal output/input utilities for Python CLI tools.  
> Make your command-line tools look professional, readable and sexy 💅

---

## 🚀 Installation

You can install `termfx` via pip:

```bash
pip install termfx
```

Or clone manually and install from source:

```bash
git clone https://github.com/MyArchiveProjects/termfx
cd termfx
pip install .
```

---

## 💡 What is termfx?

`termfx` is a lightweight, modern, and flexible terminal UI helper —  
ideal for hacking tools, CLI apps, devtools, fancy banners, dashboards and everything terminal-related.

- ✅ Clean and colored terminal outputs
- ✅ Centered input/output
- ✅ Built-in prompts: `[+]`, `[!]`, `[>]`, `[-]` style
- ✅ Password/hidden input
- ✅ Yes/No confirmation prompts
- ✅ JSON pretty-printing
- ✅ Tables, dividers and even progress bars
- ✅ Works on **Windows**, **Linux**, **MacOS**

---

## 📦 Basic Usage

```python
from termfx import *

printSuccess("Welcome to termfx!")
name = inputCentered("Enter your name:", mode="line")
printInfo(f"Hello, {name}!")
```

---

## 🧱 Functions Overview

### ✅ Print Functions

| Function           | Description                          |
|--------------------|--------------------------------------|
| `printInfo(text)`       | Light blue `[>]` prefix           |
| `printSuccess(text)`    | Green `[+]` prefix               |
| `printError(text)`      | Red `[!]` prefix                 |
| `printWarning(text)`    | Yellow `[-]` prefix              |
| `printBanner(text)`     | Cyan banner text (no prefix)     |
| `printDivider(char="-", length=50)` | Horizontal line divider |

---

### 🔤 Input Functions

| Function             | Description                      |
|----------------------|----------------------------------|
| `inputInfo(text)`        | Input with `[>]` prompt        |
| `inputSuccess(text)`     | Input with `[+]` prompt        |
| `inputError(text)`       | Input with `[!]` prompt        |
| `inputWarning(text)`     | Input with `[-]` prompt        |
| `inputCentered(text, mode="banner")` | Centered input         |
| `inputHidden(prompt)`     | Hidden input (e.g. password)   |
| `askYesNo(question)`      | Prompt for y/n confirmation    |

---

### 🧰 Utilities

#### JSON Pretty-Print

```python
data = {"name": "Alice", "age": 30}
printJsonPretty(data)
```

#### Tables

```python
printTable(
    headers=["User", "Score"],
    rows=[["Alice", 100], ["Bob", 85]]
)
```

#### Progress Bar

```python
import time
total = 50
for i in range(total + 1):
    progressBar(i, total, prefix='Progress', suffix='Complete', length=40)
    time.sleep(0.05)
```

---
