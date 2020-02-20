from .decolator import *

def get_arguments(args: dict):
    ret = {}
    for ky in args:
        if ky == "self":
            continue
        if args[ky] is not None:
            ret[ky] = args[ky]
    return ret
