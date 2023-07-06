#!/usr/bin/python3
"""Define a say name

    Functions:
        say_my_name
"""


def say_my_name(first_name, last_name=""):
    """Prints out first name & last name with a massage

        Args:
            first_name(string): first name
            last_name(string): last name

        Raises:
            TypeError: when first name is not string
            TypeError: when last name is not string

        Return: Nothing
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
