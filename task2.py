def dot_between(word):
    list_of_dots = [bin(i)[2:] for i in range(2 ** (len(word)-1))]
    full_list = []
    for i in list_of_dots:
        new_word = word
        for j in range(len(str(i))):
            if str(i[::-1])[-j] == '1':
                new_word = word[:(len(list_of_dots[-1])-j)] + '.' + new_word[(len(list_of_dots[-1])-j):]
        full_list.append(new_word)
    return full_list


word = 'abcd'
print(dot_between(word))
print(len(dot_between(word)))
