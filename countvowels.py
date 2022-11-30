def vowel_dict(word):
    vowels = {'a':0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    word = word.lower()
    
    for char in word:
        if char in vowels:
            vowels[char] += 1
        
    return vowels