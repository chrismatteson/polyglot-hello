from __future__ import annotations

from polyglot_hello import (
    list_languages,
    say_hello_world,
)


def main() -> None:
    # Print hello world in five random languages
    print("Five random 'Hello World':")
    for _ in range(5):
        print(" -", say_hello_world())

    # Print specific languages by code and name
    print("\nSpecific selections:")
    print("English (en):", say_hello_world("en"))
    print("Spanish (name):", say_hello_world("Spanish"))

    # Show list usage
    langs = list_languages()
    print(f"\nThere are {len(langs)} languages available. The first 10:")
    for i, name in enumerate(langs[:10]):
        print(f" {i}: {name}")

    # Pick by index
    print("\nBy index 0 (first entry):", say_hello_world(0))


if __name__ == "__main__":
    main()


