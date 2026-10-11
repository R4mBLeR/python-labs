import re

def analyze(text):
    print(f'Количество слов: {len(text)}')
    
    word_count = {}
    for word in text:
        word_count[word] = word_count.get(word, 0) + 1
    
    most_common_word = ""
    shortest_word = text[0]
    longest_word = text[0]
    for word in word_count:
        print(f'Количество повторения слова {word}: {word_count[word]}')
        
        if word_count[word] > word_count.get(most_common_word, 0):
            most_common_word = word
        if len(word) > len(longest_word):
            longest_word = word
        if len(word) < len(shortest_word):
            shortest_word = word
    print(f'Самое частое слово: {most_common_word}')
    print(f'Самое длинное слово: {longest_word}')
    print(f'Самое короткое слово: {shortest_word}')
    
text = input("Введите текст: ")
words = re.split(r"[, .:;]",text.lower())
analyze(words)
words = list(filter(lambda word: len(word) >= 3, words))
print()
print('Повторный анализ: ')
print()
analyze(words)

