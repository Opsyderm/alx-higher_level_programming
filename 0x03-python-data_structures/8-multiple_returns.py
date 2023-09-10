#!/usr/bin/python3
# 8-multiple_returns.py


def multiple_returns(sentence):
    """will Return the length of a string and its first char."""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])

