import argparse  # noqa: D100

from pypacter.language_detector import detect_programming_language


def detect_language_from_file(file_path: str) -> str:
    """
    Detects the programming language from a code snippet in a file.

    Args:
        file_path (str): The path to the code snippet file.

    Returns:
        str: The detected programming language.
    """
    with open(file_path, "r") as file:
        code_snippet = file.read()
    return detect_programming_language(code_snippet)


def detect_language_from_stdin() -> str:
    """
    Detects the programming language from a code snippet provided through standard input.

    Returns:
        str: The detected programming language.
    """
    code_snippet = input("Enter the code snippet: ")
    return detect_programming_language(code_snippet)


def main() -> str:
    """
    Main function to parse command-line arguments and execute the appropriate action.
    """
    parser = argparse.ArgumentParser(
        description="Detect the programming language of a code snippet."
    )
    source_choices = ["file", "stdin"]  # Pre-define choices for cleaner code
    parser.add_argument(
        "source", choices=source_choices, help="Specify the source of the code snippet."
    )
    parser.add_argument(
        "--file-path",
        required=lambda args: args.source == "file",
        help="Path to the code snippet file.",
    )

    args = parser.parse_args()

    if args.source == "file":
        detected_language = detect_language_from_file(args.file_path)
    elif args.source == "stdin":
        detected_language = detect_language_from_stdin()

    print(f"Detected language: {detected_language}")


if __name__ == "__main__":
    main()
