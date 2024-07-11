import subprocess
import os
import locale

def test_ccwc():
    # Set the locale to the user's default setting
    locale.setlocale(locale.LC_ALL, '')

    # Create a text file
    with open('test.txt', 'w') as f:
        f.write("Hello World!\nThis is a test file.\nIt has 3 lines, 12 words, and 54 characters including newlines.")
    
    expected_bytes = os.path.getsize('test.txt')
    expected_lines = 2
    expected_words = 18
    expected_chars = 99

    # Test with file input
    result = subprocess.run(['python', 'ccwc.py', '-c', 'test.txt'], capture_output=True, text=True)
    assert f"{expected_bytes:8d} test.txt" in result.stdout, f"Byte count failed. Expected {expected_bytes}, got {result.stdout}"

    result = subprocess.run(['python', 'ccwc.py', '-l', 'test.txt'], capture_output=True, text=True)
    assert f"{expected_lines:8d} test.txt" in result.stdout, f"Line count failed. Expected {expected_lines}, got {result.stdout}"

    result = subprocess.run(['python', 'ccwc.py', '-w', 'test.txt'], capture_output=True, text=True)
    assert f"{expected_words:8d} test.txt" in result.stdout, f"Word count failed. Expected {expected_words}, got {result.stdout}"

    result = subprocess.run(['python', 'ccwc.py', '-m', 'test.txt'], capture_output=True, text=True)
    assert f"{expected_chars:8d} test.txt" in result.stdout, f"Character count failed. Expected {expected_chars}, got {result.stdout}"

    result = subprocess.run(['python', 'ccwc.py', 'test.txt'], capture_output=True, text=True)
    expected_output = f"{expected_lines:8d}{expected_words:8d}{expected_bytes:8d} test.txt"
    assert expected_output in result.stdout, f"Default option failed. Expected {expected_output}, got {result.stdout}"

    # Test with standard input
    result = subprocess.run('cat test.txt | python ccwc.py -l', shell=True, capture_output=True, text=True)
    assert f"{expected_lines:8d}" in result.stdout, f"Standard input line count failed. Expected {expected_lines}, got {result.stdout}"

    result = subprocess.run('cat test.txt | python ccwc.py -w', shell=True, capture_output=True, text=True)
    assert f"{expected_words:8d}" in result.stdout, f"Standard input word count failed. Expected {expected_words}, got {result.stdout}"

    result = subprocess.run('cat test.txt | python ccwc.py -c', shell=True, capture_output=True, text=True)
    assert f"{expected_bytes:8d}" in result.stdout, f"Standard input byte count failed. Expected {expected_bytes}, got {result.stdout}"

    result = subprocess.run('cat test.txt | python ccwc.py -m', shell=True, capture_output=True, text=True)
    assert f"{expected_chars:8d}" in result.stdout, f"Standard input character count failed. Expected {expected_chars}, got {result.stdout}"

    result = subprocess.run('cat test.txt | python ccwc.py', shell=True, capture_output=True, text=True)
    expected_output = f"{expected_lines:8d}{expected_words:8d}{expected_bytes:8d}"
    assert expected_output in result.stdout, f"Standard input default option failed. Expected {expected_output}, got {result.stdout}"

    print("All tests passed!")

    # Clean up
    os.remove('test.txt')

if __name__ == "__main__":
    test_ccwc()