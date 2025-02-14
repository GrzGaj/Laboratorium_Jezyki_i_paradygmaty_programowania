#analiza tekstu i transformacje funkcyjne
from collections import Counter


def analyzeText(text):
    #zliczanie akapitów, zdań i słów
    paragraphs = text.split('\n')
    sentences = [sentence for paragraph in paragraphs for sentence in paragraph.split('.')]
    words = text.split(" ")
    print(f"Liczba akapitów: {len(paragraphs)}")
    print(f"Liczba zdań: {len(sentences)}")
    print(f"Liczba słów: {len(words)}")

    #słowa występujące najczęściej z wykluczeniem stop words
    stop_words = {'a','w','z','i','o','the','or','to'}
    filtered_words = filter(lambda word: word not in stop_words, words)

    word_count = Counter(filtered_words)
    most_common = word_count.most_common(3)
    print(f"Najczęstrze słowa: {most_common}")

    #odwracanie wyrazów rozpoczynających się na a
    reversAWords = [word[::-1] if word.startswith('a'and'A') else word for word in words] #[::-1] odwracanie słowa
    print(f"Odwrócone słowo rozpocznające się na 'a': {' '.join(reversAWords)}")

text = """
    aifon
    agrafka
    ameba
    astra
    Aleksandra
"""

analyzeText(text)