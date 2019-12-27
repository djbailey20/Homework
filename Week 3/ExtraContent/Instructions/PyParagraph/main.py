import os
import re

filepath = os.path.join("raw_data", "paragraph_1.txt")
totalWords = 0
totalLetters = 0
totalSentences = 0
with open(filepath, 'r') as textfile:

    for line in textfile:
        words = line.split()
        # print(len(words))
        totalWords = totalWords + len(words)
        totalLetters = totalLetters+len(line)
        for sentence in re.split("(?<=[.!?]) +", line):
            wordsInSentence = sentence.split()
            totalSentences += 1
print(f"Total Words = {totalWords}")
print(f"Total Sentences = {totalSentences}")
print(f"Average Letter Count Per Word = {totalLetters/totalWords}")
print(f"Average Words Per Sentence = {totalWords/totalSentences}")
