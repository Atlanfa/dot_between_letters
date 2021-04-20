def dot_between(text):
    list_of_words = [[text]]
    while list_of_words[-1]:
        list_of_words.append([word[:i] + '.' + word[i:] for word in list_of_words[-1] for i in range(1, len(word)) if word[i] != '.' and word[i-1] != '.'])
    full_list=[]
    for lst in list_of_words:
      full_list.extend(lst)
    return list(dict.fromkeys(full_list))


word = 'acbd'
print(dot_between(word))
print(len(dot_between(word)))
print(2 ** (len(word)-1))
