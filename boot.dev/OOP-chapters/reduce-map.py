import functools


def join(doc_so_far, sentence):
    return doc_so_far + ". " + sentence


def join_first_sentences(sentences, n):
    if n == 0:
        return ""

    first_sentence = sentences[:n]

    joined = functools.reduce(join, first_sentence)
    return joined + "."
