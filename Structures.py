letters = ['A','R','N','O','L','D','A','N',
                'D','R','E','S','B','U','S','T',
                'A','R','D','E','C','O','M',
                'P','U','T','E','R','E','N','G',
                'I','N','E','E','R','I','N','G']


from collections import Counter
letters_counts = Counter(letters)
repeat = letters_counts.most_common(3)
print ("letters repeated")
print(repeat)