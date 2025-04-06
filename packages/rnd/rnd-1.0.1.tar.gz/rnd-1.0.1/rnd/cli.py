import argparse
from . import rnd

def main():
    parser = argparse.ArgumentParser(description="Generate a secure, customizable random string.")
    
    parser.add_argument('-l', '--length', type=int, default=16, help="Length of the random string.")
    parser.add_argument('--mode', type=str, default="custom", choices=["custom", "hex", "base64", "ascii"], help="Preset mode.")
    
    # Charset flags
    parser.add_argument('--lower', action='store_true', help="Include lowercase letters.")
    parser.add_argument('--upper', action='store_true', help="Include uppercase letters.")
    parser.add_argument('--digits', action='store_true', help="Include digits.")
    parser.add_argument('--symbols', action='store_true', help="Include symbols.")
    parser.add_argument('--emojis', action='store_true', help="Include emojis.")

    # Extra features (not passed to Charset)
    parser.add_argument('--prefix', type=str, default="", help="Prefix for the string.")
    parser.add_argument('--suffix', type=str, default="", help="Suffix for the string.")
    parser.add_argument('--ensure-unique', action='store_true', help="Ensure characters are unique (if possible).")
    
    args = parser.parse_args()

    # Only Charset-related args go here
    charset_kwargs = {
        "lower": args.lower,
        "upper": args.upper,
        "digits": args.digits,
        "symbols": args.symbols,
        "emojis": args.emojis,
    }

    result = rnd(
        length=args.length,
        mode=args.mode,
        prefix=args.prefix,
        suffix=args.suffix,
        ensure_unique=args.ensure_unique,
        **charset_kwargs
    )

    print(result)
