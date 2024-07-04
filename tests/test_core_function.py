"""
    Unit tests for the detect_programming_language function.

    None is used for the expected_language where the result
    is unknown or it is an edge case
"""


from pypacter.language_detector import detect_programming_language

def test_valid_python_code():
    """
    Test a valid Python code.
    """
    code = "print('Hello World!')"
    expected_language = "python"
    actual_language = detect_programming_language(code)
    assert actual_language == expected_language


def test_java_code():
    """
    Test a valid Java code.
    """
    code = """
    public class MyClass {
        public static void main(String[] args) {
          System.out.println("Hello World!");
        }
      }
      """
    expected_language = "java"
    actual_language = detect_programming_language(code)
    assert actual_language == expected_language


def test_c_code():
    """
    Test a valid C code.
    """
    code = """
    #include <stdio.h>

    int main() {
        printf("Hello World!\n");
        return 0;
      }
      """
    expected_language = "c"
    actual_language = detect_programming_language(code)
    assert actual_language == expected_language


def test_cpp_code():
    """
    Test a valid C++ code.
    """
    code = """
    #include <iostream>

    int main() {
        std::cout << "Hello World!" << std::endl;
        return 0;
      }
      """
    expected_language = "cpp"
    actual_language = detect_programming_language(code)
    assert actual_language == expected_language


def test_html_code():
    """
    Test a valid HTML code/Non programming language.
    """
    code = """
    <!DOCTYPE html>
    <html>
        <body>
          <h1>Hello World!</h1>
        </body>
      </html>
      """
    expected_language = None
    actual_language = detect_programming_language(code)
    assert actual_language == expected_language


def test_empty_code():
    """
    Test an empty string code.
    """
    code = ""
    expected_language = None
    actual_language = detect_programming_language(code)
    assert actual_language == expected_language


def test_non_code_content():
    """
    Test a non-code content like, Natural language etc.
    """
    content = "This is not code!"
    expected_language = None
    actual_language = detect_programming_language(content)
    assert actual_language == expected_language


def test_multi_language_code():
    """
    Test string with mutliple programming languages.
    """
    code = """
    # This is a comment in Python
    print("Hello World!")  # Python statement
    function greet(name) {  # JavaScript function syntax
        console.log("Hello, " + name);
      }
      """

    expected_language = None
    actual_language = detect_programming_language(code)
    assert actual_language == expected_language


def test_unsupported_language():
    """
    Test string with unsupported programming language.
    """
    code = ";; This is a comment in Lisp"
    expected_language = None
    actual_language = detect_programming_language(code)
    assert actual_language == expected_language


def test_leading_whitespace():
    """
    Test string with leading whitespace.
    """
    code = "  print('Hello World!')"
    expected_language = "python"
    actual_language = detect_programming_language(code)
    assert actual_language == expected_language


def test_trailing_whitespace():
    """
    Test string with trailing whitespace.
    """
    code = "print('Hello World!') "
    expected_language = "python"
    actual_language = detect_programming_language(code)
    assert actual_language == expected_language


def test_case_sensitivity():
    """
    Test string with case sensitivity.
    """
    code = "PRINT('Hello World!')"  # Uppercase keywords
    expected_language = "python"
    actual_language = detect_programming_language(code)
    assert actual_language == expected_language


def test_comments_only():
    """
    Test string with only comments.
    """
    code = "# This is a comment in Python"
    expected_language = "python"  # Might be language-specific depending on implementation
    actual_language = detect_programming_language(code)
    assert actual_language == expected_language


def test_invalid_syntax():
    """
    Test string with invalid syntax.
    """
    code = "invalid_syntax("  # Missing closing parenthesis
    expected_language = None
    actual_language = detect_programming_language(code)
    assert actual_language == expected_language


def test_large_code_snippet():
    """
    Test a large code snippet.
    """
    # Simulate a large code snippet to test handling long inputs
    code = """
    function largeFunction(x, y) {
        // This is a large function with many lines of code
        for (let i = 0; i < 100; i++) {
          console.log("Iteration", i);
        }
        return x + y;
      }

      const result = largeFunction(5, 3);
      console.log("Result:", result);
      """
    expected_language = "javascript"  # Or based on dominant language in the snippet
    actual_language = detect_programming_language(code)
    assert actual_language == expected_language
