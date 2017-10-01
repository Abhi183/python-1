# -*- coding: cp1252 -*-
"""
Author:Abhishek Shekhar
HW5
"""
a = open("myhomework.txt", "r")
for i in a:
    wordlist = i.split()

wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))

print("String\n" + wordstring +"\n")
print("List\n" + str(wordlist) + "\n")
print("Frequencies\n" + str(wordfreq) + "\n")
print("Pairs\n" + str(zip(wordlist, wordfreq)))

a.close
