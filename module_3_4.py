

#Не совсем понятен вопрос:
# Проверяем содержимое root_word в списке other_words, и, если не содержится, проверяем обратное:

def single_root_words_1(root_word,*other_words):
    same_words = []
    for other_word in other_words:
        if root_word.upper() in other_word.upper():
            same_words.append(other_word)
    if same_words.__len__() == 0:
        for other_word in other_words:
            if other_word.upper() in root_word.upper():
                same_words.append(other_word)

    return same_words

# или проверяем оба вариант - сначала root_word в списке other_words, а затем наоборот:
def single_root_words_2(root_word, *other_words):
    same_words = []
    for other_word in other_words:
        if root_word.upper() in other_word.upper():
            same_words.append(other_word)

    for other_word in other_words:
        if other_word.upper() in root_word.upper():
            same_words.append(other_word)

    return same_words

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    result1 = single_root_words_1('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
    result2 = single_root_words_1('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
    result3 = single_root_words_1('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
    result4 = single_root_words_1('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
    print(f'Первый вариант (Либо первое слово содержится в словах элементах списка, если нет, содержать слова элемента списка в первом слове):\n\t{result1}\n\t{result2}\nВторой вариант(И первое содержится в словах элементах списка, и слова элементы списка содержат первое слов):\n\t{result3}\n\t{result4}')
