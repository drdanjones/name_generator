#!/usr/bin/env python3
import string
import random

vowels = 'aeiouy'
consonants = 'bcdfghjklmnpqrstvwxz'


ltype1 = input('Which kind of letter would you like? Type "v" for vowel, "c" for consonant, "l" for any letter:')
ltype2 = input('Which kind of letter would you like? Type "v" for vowel, "c" for consonant, "l" for any letter:')
ltype3 = input('Which kind of letter would you like? Type "v" for vowel, "c" for consonant, "l" for any letter:')


def name_generator():
    if ltype1 == 'v':
        c1 = random.choice(vowels)
    elif ltype1 == 'c':
        c1 = random.choice(consonants)
    elif ltype1 == 'l':
        c1 = random.choice(string.ascii_lowercase)

    if ltype2 == 'v':
        c2 = random.choice(vowels)
    elif ltype2 == 'c':
        c2 = random.choice(consonants)
    elif ltype2 == 'l':
        c2 = random.choice(string.ascii_lowercase)

    if ltype3 == 'v':
        c3 = random.choice(vowels)
    elif ltype3 == 'c':
        c3 = random.choice(consonants)
    elif ltype3 == 'l':
        c3 = random.choice(string.ascii_lowercase)

    return c1 + c2 + c3


for n in range(10):
    print(name_generator())
