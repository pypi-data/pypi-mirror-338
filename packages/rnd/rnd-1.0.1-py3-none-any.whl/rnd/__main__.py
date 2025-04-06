import sys

if __name__ == "__main__":
    if "test" in sys.argv[0]:
        from .test import run_tests
        run_tests()
    else:
        from .cli import main
        main()
