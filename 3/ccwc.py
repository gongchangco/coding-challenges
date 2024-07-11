import sys
import locale

def count_bytes(content):
    return len(content)

def count_lines(content):
    return content.count(b'\n')

def count_words(content):
    try:
        text = content.decode('utf-8')
    except UnicodeDecodeError:
        text = content.decode('iso-8859-1')
    return len(text.split())
        

def count_chars(content):
    try:
        return len(content.decode('utf-8'))
    except UnicodeDecodeError:
        return len(content.decode('iso-8859-1'))

def process_input(file_or_stdin):
    if hasattr(file_or_stdin, 'buffer'):
        return file_or_stdin.buffer.read()
    else:
        with open(file_or_stdin, 'rb') as f:
            return f.read()

def main():
    option = 'default'
    filename = None

    if len(sys.argv) > 1 and sys.argv[1].startswith('-'):
        option = sys.argv[1]

        if len(sys.argv) > 2:
            filename = sys.argv[2]
    elif len(sys.argv) > 1:
        filename = sys.argv[1]

    if filename:
        content = process_input(filename)
    else:
        content = process_input(sys.stdin)

    if option == '-c':
        count = count_bytes(content)
    elif option == '-l':
        count = count_lines(content)
    elif option == '-w':
        count = count_words(content)
    elif option == '-m':
        count = count_chars(content)
    elif option == 'default':
        line_count = count_lines(content)
        word_count = count_words(content)
        byte_count = count_bytes(content)
        print(f"{line_count:8d}{word_count:8d}{byte_count:8d}{' ' + filename if filename else ''}")
        return
    else:
        print(f"Unknown option: {option}")
        sys.exit(1)

    print(f"{count:8d}{' ' + filename if filename else ''}")

if __name__ == "__main__":
    # Set the locale to the user's default setting
    locale.setlocale(locale.LC_ALL, '')
    main()
