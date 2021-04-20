def dot_between(word):
    list_of_dots = [bin(i)[2:].zfill(len(word)-1)[::-1] for i in range(2 ** (len(word)-1))]
    full_list = []
    for i in list_of_dots:
        new_word = word
        for j in range(len(str(i))):
            if str(i)[-j] == '1':
                new_word = word[:(len(word)-1-j)] + '.' + new_word[(len(word)-1-j):]
        full_list.append(new_word)
    return full_list


text = 'abcd'
print(dot_between(text))
print(len(dot_between(text)))
