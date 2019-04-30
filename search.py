import argparse, sys
from t9 import word_to_t9, t9_matches

def reverse_search(words):
    for word in words:
        t9_code = word_to_t9(word)
        matches = t9_matches(t9_code)
        print(word, t9_code, matches)

def search(t9_codes):
    for code in t9_codes:
        matches = t9_matches(code)
        print(code, matches)

if len(sys.argv) > 1:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'word', metavar='word', type=str,
         nargs='+', help='')
    parser.add_argument(
        '--reverse', dest='accumulate', action='store_const', const=reverse_search,
        default=search, help='')

    args = parser.parse_args()
    args.accumulate(args.word)
    sys.exit()
