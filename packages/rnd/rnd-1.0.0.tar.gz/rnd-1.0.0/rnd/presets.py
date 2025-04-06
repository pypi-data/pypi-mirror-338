from .core import Charset

PRESETS = {
    "alphanumeric": Charset(lower=True, upper=True, digits=True),
    "emoji-only": Charset(emojis=True, lower=False, upper=False, digits=False),
    "password-safe": Charset(lower=True, upper=True, digits=True, symbols=True, avoid_confusing=True),
    "symbols-only": Charset(symbols=True, lower=False, upper=False, digits=False),
    "uppercase": Charset(upper=True, lower=False, digits=False),
    "numeric": Charset(digits=True, lower=False, upper=False),
}
