# rnd

**`rnd`** is an advanced, customizable random string generator written in Python.  
It avoids using the `random` or `string` modules and gives you complete control over character sets and generation behavior.

---

## Features

- No `random` or `string` module dependency
- Customizable character sets (lowercase, uppercase, digits, symbols, emojis, custom)
- Emoji and symbol support
- Presets for common use cases (alphanumeric, emoji-only, password-safe, etc.)
- Unique character enforcement
- Prefix and suffix support
- Command-line interface (CLI)

---

## Installation

```bash
pip install rnd
```

---

## Usage

### Python

```python
from rnd import rnd

print(rnd(length=16))  # default
print(rnd(length=12, mode="emoji-only"))
print(rnd(length=10, upper=True, digits=False, emojis=True))
```

### CLI

```bash
rnd -l 20 --mode password-safe
rnd -l 16 --prefix "ID_" --emojis --symbols
```

---

## Preset Modes

| Mode          | Description                        |
|---------------|------------------------------------|
| alphanumeric  | Letters (lower/upper) and numbers  |
| emoji-only    | Emojis only                        |
| password-safe | Strong password with symbols       |
| symbols-only  | Only symbols                       |
| uppercase     | Uppercase letters only             |
| numeric       | Digits only                        |

---
