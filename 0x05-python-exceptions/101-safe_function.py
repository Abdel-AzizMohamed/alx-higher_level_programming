#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        sys.stderr.write("Exception: {}\n".format(exc_value))
        res = None
    finally:
        return res
