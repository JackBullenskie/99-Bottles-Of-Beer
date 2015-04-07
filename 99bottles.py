#!/usr/bin/env python

words = [" bottles of beer on the wall, ", \
" bottles of beer. ",  "You take one down, \
you pass it around, ",  " bottles of beer on the wall."]

words_last = [" bottle of beer on the wall, ", \
" bottle of beer. ",  "You take it down, you \
pass it around, ",  " bottle of beer on the wall."]

def num():
     numbers = []
     for i in range (1,  100):
         numbers.append(i)
     new_num = numbers[::-1]
     return new_num
n = num()

def lyrics():
    x = 0
    while x < 98:
        print str(n[x]) + str(words[0]) +str(n[x]) + \
        str(words[1]) + str(words[2]) + str(n[x]) + str(words[3])
        x = x + 1
    else:
        print str(n[x]) + str(words_last[0]) + str(n[x]) + \
        str(words_last[1]) + str(words_last[2]) + str(n[x]) + str(words_last[3])
        
    
lyrics()
