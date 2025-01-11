import pyfiglet
import argparse

def ink(text, font_name=None):
    """Generates ASCII art from the given text.

    Args:
        text: The text to convert.
        font_name: The name of the font to use (optional).
    """
    try:
        if font_name:
            font = pyfiglet.Figlet(font=font_name)
        else:
            font = pyfiglet.Figlet()  # Use default font

        result = font.renderText(text)
        print(result)
        return result

    except pyfiglet.FontNotFound:
        print(f"Error: Font '{font_name}' not found.")
        return None

def list_fonts():
    """Lists available font names."""
    fonts = pyfiglet.FigletFont.getFonts()
    print("Available fonts:")
    for font in fonts:
        print(font)

def main():
    parser = argparse.ArgumentParser(description="Generate ASCII art from text.",
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("text_and_font", nargs="*", help="The text to convert and optional font name.")
    parser.add_argument("--fonts", action="store_true", help="List available fonts.")

    parser.epilog = (
        "Examples:\n"
        "  Generate ASCII art with default font:\n"
        "    ink \"Hello world\"\n\n"
        "  Generate ASCII art with a specific font:\n"
        "    ink \"Hello world\" slant\n\n"
        "  List available fonts:\n"
        "    ink --fonts\n"
    )

    args = parser.parse_args()

    if args.fonts:
        list_fonts()
    elif args.text_and_font:
        # Intenta encontrar un nombre de fuente conocido entre los argumentos
        font_name = None
        known_fonts = pyfiglet.FigletFont.getFonts()
        for i, arg in enumerate(args.text_and_font):
            if arg in known_fonts:
                font_name = arg
                text = " ".join(args.text_and_font[:i])
                break
        else:  # Si no se encuentra una fuente conocida, usa todos los argumentos como texto
            text = " ".join(args.text_and_font)

        ink(text, font_name)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()