"""
Author:Abhishek Shekhar
hw 8
"""
f= open('paragraph.txt')
words = f.read()
wordfreq = {}
for word in words.split():
    wordfreq[word] = wordfreq.setdefault(word, 0) + 1
print wordfreq
a = open("word_counts.txt", "w")
a.write(str(wordfreq))
print a
a.close
