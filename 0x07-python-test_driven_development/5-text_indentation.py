#!/usr/bin/python3
"""Define text indent

    Functions:
        text_indentation(string)
"""


def text_indentation(text):
    """prints out text splited by chars each in line

        Args:
            text(string): given string

        Raises:
            TypeError: if text is not string

        Return: Nothing
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
