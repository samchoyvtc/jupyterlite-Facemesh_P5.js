"""Let p5 sketch frames use the camera.

The p5 kernel draws each sketch in an iframe and does not set
allow="camera". The browser will not show the permission prompt until it does.
"""

from pathlib import Path

NEEDLE = 'frameborder="0" srcdoc='
REPLACEMENT = 'frameborder="0" allow="camera; microphone" srcdoc='


def main() -> None:
    dist = Path(__file__).resolve().parents[1] / "dist"
    changed = 0
    for path in dist.rglob("*.js"):
        text = path.read_text(encoding="utf-8")
        if NEEDLE not in text:
            continue
        path.write_text(text.replace(NEEDLE, REPLACEMENT), encoding="utf-8")
        changed += 1
        print(f"patched {path.relative_to(dist)}")
    if changed == 0:
        raise SystemExit("p5 sketch iframe was not found in dist/")


if __name__ == "__main__":
    main()
