# T9

The T9 input system was developed to make typing faster when cell phones only had a number pad and typing on them, requiring multiple taps on the same key to reach the desired letter, by having a dictionary of the most used words in the English dictionary and guessing which word the user meant by just a single tap on the key where the letters of the word were.

This script performs that same search using the dictionary `words.csv`.

## Usage

Call search with the words encoded in numbers (a -> 2, b -> 2...) and get the corresponding words ranked from most frequent to less frequent in the provided dictionary.

Searching for `word`, `test`, and `mirror`:

```
$ python search.py 9673 8378 647767
('9673', ['WORD', 'WORE', 'YORE', 'ZNSE'])
('8378', ['TEST', 'VEST', 'VERT', 'VERV'])
('647767', ['MIRROR'])
```

Also, for matters of testing, you can provide a word in regular text with the parameter `reverse` and the script will convert the word to numbers and perform the search. This is interesting to check which ambiguous words a search term might have.

```
$ python search.py word test mirror --reverse
('word', '9673', ['WORD', 'WORE', 'YORE', 'ZNSE'])
('test', '8378', ['TEST', 'VEST', 'VERT', 'VERV'])
('mirror', '647767', ['MIRROR'])
```

Note that the script prints back the searched word, the number encoded word, and the search results.
