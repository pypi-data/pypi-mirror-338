
# 🎨 termfx

> Powerful and beautiful terminal output/input utilities for Python CLI tools.  
> Make your command-line apps look professional, stylish, and human-friendly 💅

---

## 🚀 Installation

Install via pip:

```bash
pip install termfx
```

Or install from source:

```bash
git clone https://github.com/MyArchiveProjects/termfx
cd termfx
pip install .
```

---

## 💡 What is termfx?

`termfx` is a lightweight and flexible terminal UI helper —  
perfect for hacking tools, CLI utilities, developer dashboards, and more.

### Features:
- ✅ Beautiful colored output
- ✅ Centered input/output
- ✅ Prompt styles: `[+]`, `[!]`, `[>]`, `[-]`
- ✅ Hidden input for passwords
- ✅ Yes/No confirmation
- ✅ JSON pretty-printing
- ✅ Table rendering
- ✅ Progress bars
- ✅ Works on Windows, Linux, and macOS

---

## ⚡ Quick Example

```python
from termfx import *

printSuccess("Welcome to termfx!")
printCentered("Loading complete", mode="line")
name = inputCentered("Enter your name:", mode="line")
printInfo(f"Hello, {name}!")
```

---

## 📚 API Overview

### 📤 Output Functions

| Function                                 | Description                                      |
|------------------------------------------|--------------------------------------------------|
| `printInfo(text)`                        | Light blue `[>]` prefix                          |
| `printSuccess(text)`                     | Green `[+]` prefix                               |
| `printError(text)`                       | Red `[!]` prefix                                 |
| `printWarning(text)`                     | Yellow `[-]` prefix                              |
| `printBanner(text)`                      | Cyan banner text (no prefix)                     |
| `printCentered(text, mode='banner')`     | Centered output; `mode='banner'` or `'line'`     |
| `printDivider(char='-', length=50)`      | Horizontal divider line                          |

---

### 🧾 Input Functions

| Function                                 | Description                                      |
|------------------------------------------|--------------------------------------------------|
| `inputInfo(text)`                        | Standard `[>]` input prompt                      |
| `inputSuccess(text)`                     | Green `[+]` input                                |
| `inputError(text)`                       | Red `[!]` input                                  |
| `inputWarning(text)`                     | Yellow `[-]` input                               |
| `inputCentered(text, mode='banner')`     | Centered input; `mode='banner'` or `'line'`      |
| `inputHidden(prompt)`                    | Hidden input (e.g. for passwords)                |
| `askYesNo(question)`                     | Ask a yes/no question, returns `True`/`False`    |

---

### 🔧 Utilities

#### Pretty JSON Output

```python
data = {"name": "Alice", "score": 95}
printJsonPretty(data)
```

#### Table Rendering

```python
printTable(
    headers=["User", "Score"],
    rows=[["Alice", 90], ["Bob", 85], ["Eve", 99]]
)
```

#### Progress Bar

```python
import time
total = 100
for i in range(total + 1):
    progressBar(i, total, prefix='Progress', suffix='Complete', length=40)
    time.sleep(0.03)
```

---

## 🤝 Contributing

Want to add features or fix something? Pull requests are welcome.  
You can also submit issues on the [GitHub issues page](https://github.com/MyArchiveProjects/termfx/issues).

---

## 📄 License

MIT License – do whatever you want, just give credit.

---

## 🔗 Links

- PyPI: [https://pypi.org/project/termfx/1.0.0/](https://pypi.org/project/termfx/1.0.0/)
- GitHub: [https://github.com/MyArchiveProjects/termfx](https://github.com/MyArchiveProjects/termfx)

Enjoy building your sexy terminals 🤘
