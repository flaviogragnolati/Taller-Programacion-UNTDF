from pathlib import Path
import sys


def main():
    """Print the contents of the local README.md (taller/README.md).

    If the README is not found, print a short fallback message.
    """
    readme_path = Path(__file__).resolve().parent / "README.md"
    if readme_path.exists():
        try:
            text = readme_path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as e:
            print("No se pudo leer README.md:", e, file=sys.stderr)
            text = (
                "Taller de programación UNTDF 2025\n"
                "(No se pudo leer el README.md del disco.)\n"
            )
    else:
        text = (
            "Taller de programación UNTDF 2025\n"
            "README.md no encontrado en la carpeta del taller.\n"
        )

    print(text)


if __name__ == "__main__":
    main()
