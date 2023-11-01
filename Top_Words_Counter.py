# -*- coding: utf-8 -*-

import sys
from collections import Counter

# Get the filename as an argument from the command line
if len(sys.argv) != 2:
    sys.exit(1)

file_name = sys.argv[1]

# Open the file for reading
try:
    with open(file_name, 'r', encoding='utf-8') as file:
        text = file.read()
    # Break the text into words and count the frequency of each word
    words = text.split()
    word_counts = Counter(words)

    # Get the value N from the user
    N = int(input("Enter the value of N: "))

    # Show the N most common words
    most_common_words = word_counts.most_common(N)
    for i, (word, count) in enumerate(most_common_words, 1):
        print(f"{i} - word \"{word}\" {count} times")    
except FileNotFoundError:
    print(f"File {file_name} not found.")
    sys.exit(1)

