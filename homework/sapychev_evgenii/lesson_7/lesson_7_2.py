words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
numb = dict.values(words)
for word, numb in words.items():
        print(f'{word}'* numb)