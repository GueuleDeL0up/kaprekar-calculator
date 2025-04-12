# 🔵 Kaprekar calculator 🟡

---

## 📁 Folders & Files
Folder and file names use **snake_case**:
```
/kaprekar-calculator
    ∟ /venv
    ∟ /docs
        ∟ README.md
    ∟ /src
        ∟ /app
            ∟ main.py
        ∟ /tests
    ∟ requirements.txt
```

## 🧑‍💻 Code Style & Structure

### 🧭 Style Guide

- Documentation format: [**Sphinx**](https://www.sphinx-doc.org/en/master/index.html)  
- Variable and function names: `snake_case`  
- Class names: `PascalCase`

### 🧮 Variables
Use type annotations and snake_case naming:
```python
my_string: str = ''
my_integer: int = 0
my_float: float = 0.0
my_list: list = []
my_dict: dict = {}
my_set: set = set()
```

### 🔧 Functions
Function names in snake_case, with docstrings and return type annotations:
```python
def countdown(number: int = 3) -> str:
    """
    Simple countdown.

    :param number: Timer (seconds).
    :type number: int, optional

    :return: Message indicating the timer has ended.
    :rtype: str

    :raises TypeError: If number is not an integer.
    """
    if not isinstance(number, int):
        raise TypeError(f"number must be an integer, {type(number)} is not a valid type.")

    for i in range(number + 1):
        print(number - i)
    return "Time's over!"
```

### 🧱 Classes
Class names in PascalCase, with docstrings:
```python
class Player:
    """
    Object that represents the player.
    """
    def __init__(self) -> None:
        pass
```

## 🧪 Tests

Module status table:
| Module                                 | Status |
| :------------------------------------- | :----: |
| `generate_numbers_base`                |   ✅    |
| `soustraction_base`                    |   ✅    |
| `iteration_kaprekar`                   |   ✅    |
| `kaprekar`                             |   ✅    |
| `kaprekar_search_constants_and_cycles` |   ✅    |
