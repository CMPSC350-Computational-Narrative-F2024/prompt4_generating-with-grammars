import nltk
nltk.download('cmudict')
from nltk.corpus import cmudict
import re
import random

def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    return text

def remove_stress(phoneme):
    return re.sub(r'\d', '', phoneme)

def load_phones(text):
    phones = []
    words = re.findall(r'\b\w+\b', text.lower())
    entries = cmudict.dict()
    for word in words:
        if word in entries:
            pronunciations = entries[word]
            # Choose the first pronunciation and remove stress markers
            phone_list = [remove_stress(p) for p in pronunciations[0]]
            phones.append(' '.join(phone_list))
        else:
            pass  # Word not found in cmudict
    return phones

def build_markov_chain(nemes, order=3):
    markov_chain = {}
    for i in range(len(nemes) - order):
        key = tuple(nemes[i:i+order])
        next_item = nemes[i+order]
        if key not in markov_chain:
            markov_chain[key] = []
        markov_chain[key].append(next_item)
    return markov_chain

def generate(markov_chain, num_phonemes=14):
    order = len(next(iter(markov_chain)))
    start = random.choice(list(markov_chain.keys()))
    generated = list(start)
    for _ in range(num_phonemes - order):
        key = tuple(generated[-order:])
        if key in markov_chain:
            next_item = random.choice(markov_chain[key])
            generated.append(next_item)
        else:
            break
    return generated

def main():
    text = load_file('data/shakespeare.txt')
    phones = load_phones(text)
    nemes = []
    for phone in phones:
        sounds = phone.split()
        nemes.extend(sounds)
    markov_chain = build_markov_chain(nemes, order=3)
    sentences = generate(markov_chain, num_phonemes=14)
    print(' '.join(sentences))

if __name__ == '__main__':
    main()
