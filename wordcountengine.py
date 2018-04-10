import string

"""
1) use hash to count instances of word
    a. process each word to lower-case and remove punctuation
2) convert from hash to array of arrays
3) sort array of arrays
"""

def get_freq(item):
    return item[1]

def sentence_to_hash(sentence):
    sentence = sentence.translate(None, string.punctuation)

    word_freq = {}
    array_sentence = sentence.split(' ')
    for word in array_sentence:
        word = word.lower()
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    array_freq = []
    for word in word_freq:
        array_freq = array_freq + [[word, str(word_freq[word])]]
    print(sorted(array_freq, key=get_freq, reverse=True))



## driver code
sent = "Practice makes perfect. you'll only get Perfect by practice. just practice!"
sentence_to_hash(sent)
