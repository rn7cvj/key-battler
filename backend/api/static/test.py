import random
import re
from collections import Counter, defaultdict


def build_markov_chain(text):
    words = re.findall(r'\w+', text)
    markov_chain = defaultdict(Counter)

    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]
        markov_chain[current_word].update([next_word])

    return markov_chain


def generate_text(markov_chain, seed_word, length=50):
    current_word = seed_word
    generated_text = [current_word]

    for _ in range(length - 1):
        next_word = random.choices(list(markov_chain[current_word].keys()),
                                   weights=list(markov_chain[current_word].values()))[0]
        generated_text.append(next_word)
        current_word = next_word

    return ' '.join(generated_text)


input_text = open('/Users/deniskirienko4/Downloads/programms/study/key-battler/backend/api/static/text.txt').readlines()

markov_chain = build_markov_chain(input_text)
generated_text = generate_text(markov_chain, "The", 20)
print(generated_text)
