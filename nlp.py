# -*- coding: utf-8 -*-
def make_range_ngram(text: str, range_n: int, sort_mode=True) -> list:
    """
    1 ~ n gram 단어 list 반환

    output:
        - range_ngram_words: 1 ~ n gram 단어 list
    """
    range_ngram_words = set()

    '''main logic'''
    for i in range(1, range_n + 1):
        range_ngram_words.update(make_ngram(text, i, sort_mode=False))
    range_ngram_words = list(range_ngram_words)

    '''postprocess'''
    if sort_mode:
        range_ngram_words = sorted(range_ngram_words, key=len, reverse=True)

    return range_ngram_words


def make_ngram(text: str, ngram: int, sort_mode=True) -> list:
    """
    n gram 단어 list 반환.

    output:
        - ngram_words: n gram 단어 list. (n이 입력의 어절 갯수보다 크다면 빈 리스트 반환)
    """
    text = text.split()
    start_idx, end_idx = 0, ngram

    '''main logic'''
    ngram_words = set()
    while end_idx <= len(text):
        ngram_words.add("".join(text[start_idx:end_idx]))
        start_idx += 1
        end_idx += 1
    ngram_words = list(ngram_words)

    '''postprocess'''
    if sort_mode:
        ngram_words = sorted(ngram_words, key=len, reverse=True)

    return ngram_words


if __name__ == '__main__':
    ngrams = make_ngram("안녕 반가워 나는 너의 친구란다.", 1, True)
    print(ngrams)