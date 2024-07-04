"""
This module contains the detect_programming_language function.
"""

from pypacter import models


def detect_programming_language(code_snippet: str) -> str:
    """
    Detects the most likely programming language for a given code snippet.
    This function uses the DEFAULT_MODEL set in the models module to prompt the LLM.

    Args:
        code_snippet (str): The input code snippet.

    Returns:
        str: The detected programming language (lowercase).
    """

    response = models.DEFAULT_MODEL.predict(
            f"Given the following code snippet: '{code_snippet}'\n "\
            "What programming language is it written in? It sometimes"\
            "could be the case that it is not written in any programming"\
            "language and also, that the code has comment or invalid syntax"\
            "your response should only be the programming language name and no explanation.")
    return response
