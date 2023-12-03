#!/usr/bin/env python3

def return_evens(num_list):
    # Using list comprehension to filter even elements
    even_numbers = [num for num in num_list if num % 2 == 0]
    return even_numbers


def make_exclamation(sentence_list):
    # Using list comprehension to add exclamation marks
    exclaimed_sentences = [sentence + '!' for sentence in sentence_list]
    return exclaimed_sentences
