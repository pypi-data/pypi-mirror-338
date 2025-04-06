from . import rnd

def run_tests():
    print("Running RND Tests...\n")

    tests = [
        {"desc": "Lower + Upper", "kwargs": {"length": 16, "use_lower": True, "use_upper": True}},
        {"desc": "Lower + Digits", "kwargs": {"length": 16, "use_lower": True, "use_digits": True}},
        {"desc": "Symbols Only", "kwargs": {"length": 16, "use_symbols": True}},
        {"desc": "Emojis Only", "kwargs": {"length": 16, "use_emojis": True}},
        {"desc": "All Types", "kwargs": {
            "length": 32, "use_lower": True, "use_upper": True, "use_digits": True,
            "use_symbols": True, "use_emojis": True
        }},
        {"desc": "Hex Mode", "kwargs": {"length": 16, "mode": "hex"}},
        {"desc": "Base64 Mode", "kwargs": {"length": 22, "mode": "base64"}},
        {"desc": "Ascii Mode", "kwargs": {"length": 20, "mode": "ascii"}},
        {"desc": "Prefix & Suffix", "kwargs": {
            "length": 16, "use_lower": True, "prefix": "pre_", "suffix": "_end"
        }},
    ]

    for i, test in enumerate(tests, 1):
        try:
            result = rnd(**test["kwargs"])
            print(f"[✓] Test {i}: {test['desc']}\n{result}\n")
        except Exception as e:
            print(f"[!] Test {i} FAILED: {test['desc']}\n{e}\n")

    print("All tests completed.")

if __name__ == "__main__":
    run_tests()
