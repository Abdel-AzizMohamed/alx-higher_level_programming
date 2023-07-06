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

text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")
