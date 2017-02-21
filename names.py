#!/usr/bin/env python3
import string
import random


def name_generator():
    c1 = random.choice(string.ascii_lowercase)
    c2 = random.choice(string.ascii_lowercase)
    c3 = random.choice(string.ascii_lowercase)
    return c1 + c2 + c3


print(name_generator())
