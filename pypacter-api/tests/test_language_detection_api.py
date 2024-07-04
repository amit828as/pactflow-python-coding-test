"""
This file tests the language detection API.
"""

import json
import requests

API_URL = "http://localhost:8000/detect-language"


def test_detect_language_success() -> None:
    """
    This test checks if the API detects the language correctly.
    """
    # Sample code snippet
    code_snippet = """
    def my_function(x):
        return x * 2
    """

    # Send a POST request with the code snippet
    response = requests.post(API_URL, json={"code_snippet": code_snippet}, timeout=30)

    # Check for successful response (200 status code)
    assert response.status_code == 200

    # Parse the JSON response
    data = json.loads(response.text)

    # Check if the detected language is present and is lowercase
    assert "detected_language" in data
    assert data["detected_language"].islower()


def test_detect_language_missing_snippet() -> None:
    """
    This test checks if the API returns an error for missing code snippet.
    """
    # Send a POST request without the code snippet
    response = requests.post(API_URL, timeout=30)

    # Check for bad request (400 status code)
    assert response.status_code == 400

    # Check if the error message is present
    data = json.loads(response.text)
    assert "detail" in data


if __name__ == "__main__":
    test_detect_language_success()
    test_detect_language_missing_snippet()
