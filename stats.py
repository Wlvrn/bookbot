import sys

def get_book_text(path):
    if not path.endswith('.txt'):
        print("Error: Only .txt files are supported.")
        sys.exit(1)
    try:
        with open(path, encoding='utf-8', errors='ignore') as f:
            file_contents = f.read()
            return file_contents
    except Exception as e:
        print("Error: An error occurred while reading the file: %s" % str(e))
        sys.exit(1)

def get_num_words(text):
    if not isinstance(text, str):
        print("Error: Input must be a string.")
        sys.exit(1)
    words = text.split()
    return len(words)

def get_char_counts(text):
    if not isinstance(text, str):
        print("Error: Input must be a string.")
        sys.exit(1)
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def get_char_report(char_counts):
    if not isinstance(char_counts, dict):
        print("Error: Input must be a dictionary.")
        sys.exit(1)
    char_report = []
    for char, count in char_counts.items():
        if char.isalpha():
            char_report.append({'char': char, 'count': count})
    char_report.sort(key=lambda x: x['count'], reverse=True)
    return char_report