class Charset:
    def __init__(self, lower=False, upper=False, digits=False, symbols=False, emojis=False):
        self.characters = ""

        if lower:
            self.characters += "abcdefghijklmnopqrstuvwxyz"
        if upper:
            self.characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if digits:
            self.characters += "0123456789"
        if symbols:
            self.characters += "!@#$%^&*()_-+=[]{}|;:,.<>?/\\"
        if emojis:
            # Some basic emojis
            self.characters += (
                "😀😃😄😁😆😅😂🤣😊😇🙂🙃😉😍🥰😘"
                "😜🤪🤩🥳😎🤓🧐🤯😤😱😡🥶🤧😷"
                "👻🎃👽🤖💩👾💀⚡🔥🌈⭐✨❄️"
            )

        # If no character type is selected, fallback to a default alphanumeric set
        if not self.characters:
            self.characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    def __repr__(self):
        return f"<Charset length={len(self.characters)}>"

# Predefined charset presets for convenience
PRESETS = {
    "hex": Charset(lower=True, digits=True),
    "base64": Charset(lower=True, upper=True, digits=True, symbols=True),
    "ascii": Charset(lower=True, upper=True, digits=True, symbols=True),
    "alpha": Charset(lower=True, upper=True),
    "numeric": Charset(digits=True),
    "alphanumeric": Charset(lower=True, upper=True, digits=True),
    "emoji": Charset(emojis=True),
}
