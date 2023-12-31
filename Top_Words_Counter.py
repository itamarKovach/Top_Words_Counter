# -*- coding: utf-8 -*-

import sys

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
     word_count = {}
        
     for word in words:
         if word in word_count:
            word_count[word] += 1
         else:
            word_count[word] = 1
         # sort the words by their freq
        
     most_common_words = sorted(word_count.items(), key = lambda x : x[1], reverse=True)

     # Show the N most common words
     N = int(input("Enter the value of N: "))
        
     for i, (word, count) in enumerate(most_common_words[:N], 1):
         print(f"{i} - word \"{word}\" {count} times")
     sys.exit(1)    
except FileNotFoundError:
       print(f"File {file_name} not found.")
       sys.exit(1)

