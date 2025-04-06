import argparse
from . import rnd

def main():
    parser = argparse.ArgumentParser(description="rnd - Advanced Random String Generator")
    parser.add_argument("-l", "--length", type=int, default=16, help="Length of string")
    parser.add_argument("-m", "--mode", type=str, help="Preset mode")
    parser.add_argument("--unique", action="store_true", help="Ensure all characters are unique")
    parser.add_argument("--prefix", type=str, default="", help="Prefix to add to result")
    parser.add_argument("--suffix", type=str, default="", help="Suffix to add to result")
    parser.add_argument("--custom", type=str, default="", help="Add custom characters")
    parser.add_argument("--no-lower", action="store_true", help="Disable lowercase letters")
    parser.add_argument("--no-upper", action="store_true", help="Disable uppercase letters")
    parser.add_argument("--no-digits", action="store_true", help="Disable digits")
    parser.add_argument("--symbols", action="store_true", help="Enable symbols")
    parser.add_argument("--emojis", action="store_true", help="Enable emojis")
    parser.add_argument("--avoid-confusing", action="store_true", help="Avoid confusing characters")

    args = parser.parse_args()
    charset_args = {
        "lower": not args.no_lower,
        "upper": not args.no_upper,
        "digits": not args.no_digits,
        "symbols": args.symbols,
        "emojis": args.emojis,
        "custom": args.custom,
        "avoid_confusing": args.avoid_confusing
    }

    print(rnd(
        length=args.length,
        mode=args.mode,
        ensure_unique=args.unique,
        prefix=args.prefix,
        suffix=args.suffix,
        **charset_args
    ))
