import os
from typing import Optional
from dataclasses import dataclass, field

@dataclass
class Charset:
    lower: bool = True
    upper: bool = True
    digits: bool = True
    symbols: bool = False
    emojis: bool = False
    custom: str = ""
    avoid_confusing: bool = False
    whitelist: str = ""
    blacklist: str = ""

    def build(self) -> str:
        base = {
            "lower": "abcdefghijklmnopqrstuvwxyz",
            "upper": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "digits": "0123456789",
            "symbols": "!@#$%^&*()-_=+[]{}|;:',.<>?/\\`~",
            "emojis": "😀😃😄😁😆😅😂🤣😊😍😘😜😎🥳😡😱👻💀🤖🐶🐱🦄🍕🍔🍟❤️✨"
        }
        charset = ""
        if self.lower: charset += base["lower"]
        if self.upper: charset += base["upper"]
        if self.digits: charset += base["digits"]
        if self.symbols: charset += base["symbols"]
        if self.emojis: charset += base["emojis"]
        charset += self.custom

        if self.avoid_confusing:
            confusing = "0O1lI|`'\""
            charset = ''.join(c for c in charset if c not in confusing)

        if self.whitelist:
            charset = ''.join(c for c in charset if c in self.whitelist)
        if self.blacklist:
            charset = ''.join(c for c in charset if c not in self.blacklist)

        charset = ''.join(sorted(set(charset)))
        if not charset:
            raise ValueError("Character set is empty.")
        return charset

@dataclass
class Generator:
    length: int
    charset: Charset = field(default_factory=Charset)
    prefix: str = ""
    suffix: str = ""
    ensure_unique: bool = False

    def generate(self) -> str:
        chars = self.charset.build()
        core_len = self.length - len(self.prefix) - len(self.suffix)
        if core_len <= 0:
            raise ValueError("Length must be greater than prefix + suffix length")

        if self.ensure_unique and core_len > len(chars):
            raise ValueError("Not enough unique characters for the requested length.")

        used = set()
        result = []
        while len(result) < core_len:
            ch = chars[os.urandom(1)[0] % len(chars)]
            if self.ensure_unique and ch in used:
                continue
            result.append(ch)
            used.add(ch)

        return self.prefix + ''.join(result) + self.suffix
