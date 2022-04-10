#   -   Write a function that will find all the anagrams of a word from a list. 
#   -   You will be given two inputs a word and an array with words. 
#   -   You should return an array of all the anagrams or an empty array if there are none.



def anagrams(word, words_list):
    print('main word:', word)
    letters = []
    anagrams = []
    for i in word:
        if i not in letters: letters.append(i)
    
    letters.sort()
    print('main word letters:', letters)
    
    for next_word in words_list:
        letters1 = []
        if len(next_word) < len(word): 
            print(next_word, 'is not an anagram')
            continue
        for i in next_word:
            if i not in letters1: letters1.append(i)
        
        print('for {} letters are: {}'.format(next_word, letters1))
        letters1.sort()
        if letters1 == letters:
            print('adding', next_word, 'to the anagrams list')
            anagrams.append(next_word)
        else:
            print(next_word, 'is not an anagram')
        print()
    
    print('anagrams list:', anagrams)
    print('--------------------------------------------')
    return anagrams



anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])
anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])
anagrams('laser', ['lazing', 'lazy',  'lacer'])