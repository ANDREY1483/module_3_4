def single_root_words(root_word, *other_words):
    same_words = []
    for str_ in other_words:
        if root_word in str_:
            same_words.append(str_)
        elif str_.lower() in root_word.lower():
            same_words.append(str_)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
