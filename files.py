# Прочитайте файл и подсчитайте количество слов в тексте


# 1 вариант. Подсчет количества слов во всем тексте
with open('referat.txt', 'r', encoding='utf-8') as f:
    count_words = 0
    for line in f:
        line.strip()
        words_in_line = line.split()
        for word in words_in_line:
            count_words += 1
    print('Количество слов в документе: {}'.format(count_words))


# 2 вариант. Подсчет количества слов в сочинении
with open('referat.txt', 'r', encoding='utf-8') as f:
    count_words = 0
    count_after = False
    for line in f:
        line.strip()
        if line.startswith('Тема'):
            count_after = True
            continue
        words_in_line = line.split()
        for word in words_in_line:
            if count_after is True:
                count_words += 1

    print('Количество слов в сочинении: {}'.format(count_words))