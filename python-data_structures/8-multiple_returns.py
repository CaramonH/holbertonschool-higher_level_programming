#!/usr/bin/python3
# Write a dunction that returns a tuple with the
# length of a string and its first character
# Prototype: def multiple_returns(sentence):


def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    else:
        return (len(sentence), sentence[0])
