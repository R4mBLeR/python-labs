import re

def analyze(text):
    print(f'Количество слов: {len(text)}')
    
    word_count = {}
    for word in text:
        word_count[word] = word_count.get(word, 0) + 1
    
    most_common_word = ""
    shortest_words = []
    longest_words = []
    shortest_word_len = 10e9
    longest_word_len = 0
    for word in word_count:
        print(f'Количество повторения слова {word}: {word_count[word]}')
        
        if word_count[word] > word_count.get(most_common_word, 0):
            most_common_word = word
        if len(word) > longest_word_len:
            longest_word_len = len(word)
        if len(word) < shortest_word_len:
            shortest_word_len = len(word)
    for word in word_count:
        if len(word) == longest_word_len:
            longest_words.append(word)
        if len(word) == shortest_word_len:
            shortest_words.append(word)
    print(f'Самое частое слово: {most_common_word}')
    print(f'Самые длинные слова: {longest_words}')
    print(f'Самые короткие слова: {shortest_words}')
    
text = input("Введите текст: ")
words = re.split(r"[, .:;]",text.lower())
analyze(words)
words = list(filter(lambda word: len(word) >= 3, words))
print()
# print('Повторный анализ: ')
# print()
# analyze(words)

