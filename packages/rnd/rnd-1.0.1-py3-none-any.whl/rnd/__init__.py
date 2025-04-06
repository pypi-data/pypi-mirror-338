from .core import Charset, PRESETS
import secrets

def rnd(length=16, mode="custom", prefix="", suffix="", ensure_unique=False, **kwargs):
    # Only keep charset-specific args
    charset_args = {k: kwargs[k] for k in ['lower', 'upper', 'digits', 'symbols', 'emojis'] if k in kwargs}
    
    # Get the character set
    charset = PRESETS.get(mode, Charset(**charset_args))

    # Make sure charset isn't empty
    if not charset.characters:
        raise ValueError("Character set is empty. Enable at least one character type.")

    # Ensure uniqueness
    if ensure_unique and length > len(set(charset.characters)):
        raise ValueError("Not enough unique characters to generate a unique string of this length.")

    # Generate string
    if ensure_unique:
        result = ''.join(secrets.choice(list(set(charset.characters))) for _ in range(length))
    else:
        result = ''.join(secrets.choice(charset.characters) for _ in range(length))

    return f"{prefix}{result}{suffix}"
