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
    i = 0
    while (i < len(text)):
        print(text[i], end="")
        if text[i] in ".?:":
            if text[i + 1] == " ":
                i += 1
            print("\n")
        i += 1
