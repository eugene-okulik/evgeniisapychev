text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer'
'urna nisl, facilisis vitae semper at, dignissim vitae libero')
words = text.split()
fin_word = []
for word in words:
    if word.isalpha():
        word  = word + 'ing'
        fin_word.append(word)
    else:
        word = word[:-1] + 'ing' + word[-1]
fin_word.append(word)
print(' '.join(fin_word))
