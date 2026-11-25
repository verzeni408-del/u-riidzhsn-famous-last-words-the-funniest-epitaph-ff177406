"""Write one funny epitaph to /output/entry.txt (stdlib only)."""

import os

ENTRY = "Here lies a man who outlived all his enemies. His debts outlived him."


def main():
    text = ENTRY
    if not text or not text.strip():
        raise SystemExit("entry is empty")
    if len(text) > 150:
        raise SystemExit("entry exceeds 150 characters")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
