from .core import Generator, Charset
from .presets import PRESETS

def rnd(length: int = 16, mode: str = None, **kwargs) -> str:
    charset = PRESETS.get(mode, Charset(**kwargs))
    return Generator(
        length=length,
        charset=charset,
        prefix=kwargs.get("prefix", ""),
        suffix=kwargs.get("suffix", ""),
        ensure_unique=kwargs.get("ensure_unique", False)
    ).generate()
