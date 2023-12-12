import math


def ofn_custom_impl(_project_path, *, param_1, param_2):
    # (not a real objective function, just for illustration)
    if param_2 is True:
        return param_1 ** 2
    return math.sqrt(param_1)
