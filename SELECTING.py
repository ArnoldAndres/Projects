def only_lower(s):
    lower_chars = ""
    for char in s:
        if char.islower():
            lower_chars += char
    return lower_chars

print (only_lower("I neEd To cOmpLy ThIs eXErCises tO pasS thIs SubjeCt"))
