import sys
import stats
# from stats import get_num_words, get_char_counts, get_char_report

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]

    # book_path = "books/frankenstein.txt"
    text = stats.get_book_text(sys.argv[1])
    num_words = stats.get_num_words(text)
    print("Found %d total words" % num_words)
    char_counts = stats.get_char_counts(text)
    print("Character counts:")
    for char, count in char_counts.items():
        print("%s: %d" % (char, count))
    char_report = stats.get_char_report(char_counts)
    print("Character report:")
    for char_dict in char_report:
        print("%s: %d" % (char_dict['char'], char_dict['count']))

if __name__ == "__main__":
    main()
