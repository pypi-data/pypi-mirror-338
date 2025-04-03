import argparse

def main():
    parser = argparse.ArgumentParser(description="A simple CLI tool for yzc.")
    parser.add_argument('--hello', action='store_true', help="Print Hello, World!")
    args = parser.parse_args()

    if args.hello:
        print("Hello, World!")

if __name__ == "__main__":
    main()