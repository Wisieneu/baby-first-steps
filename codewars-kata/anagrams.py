#   -   Write a function that will find all the anagrams of a word from a list. 
#   -   You will be given two inputs a word and an array with words. 
#   -   You should return an array of all the anagrams or an empty array if there are none.



def anagrams(word, words):
    print(word)
    letters = []
    anagrams = []
    for i in word:
            
        if i not in letters:
            letters.append(i)
    
    letters.sort()
    print('main word letters:', letters)
    
    for wordz in words:
        letters1 = []
        if len(wordz) != len(word):
            continue
            
        for i in wordz:
            if i not in letters1:
                letters1.append(i)
        
        print('for', wordz, 'letters are:', letters1)
        letters1.sort()
        if letters1 == letters:
            anagrams.append(wordz)
            print('adding', wordz)
            print(anagrams)
            print()
    
    return anagrams



anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])
anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])
anagrams('laser', ['lazing', 'lazy',  'lacer']))