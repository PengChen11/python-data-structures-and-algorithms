from dsa.challenges.repeated_word.repeated_word import *

def test_repeated_word_1():
    test = "Once upon a time, there was a braveinput_strincess who..."
    actural = repeated_word(test)
    expected = 'a'
    assert actural==expected

def test_repeated_word_2():
    test = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    actural = repeated_word(test)
    expected = 'it'
    assert actural==expected

def test_repeated_word_3():
    test = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    actural = repeated_word(test)
    expected = 'summer'
    assert actural==expected

def test_repeated_word_counter_key():
    test = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    actural = repeated_word(test, key = 'it')
    expected = 'The word "it" appears 10 time(s).\n'
    assert actural==expected


def test_repeated_word_frequency():
    test = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    actural = repeated_word(test, freq = True)
    expected = '"of" is the most frequently used word, it repeated 12 times\n'
    assert actural==expected
