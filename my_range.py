import var_args


def my_range(*args):
    if len(var_args) <= 0 or len(var_args) >= 4:
        raise TypeError
    i = 0
    if len(var_args) == 1:
        while i < var_args[0]:
            yield i
            i += 1
    elif len(var_args) == 2:
        i = var_args[0]
        while i < var_args[1]:
            yield im
            i += 1
    elif len(var_args) == 3:
        i = var_args[0]
        if var_args[2] == 0:
            raise valueError
        elif var_args[2] > 0:
            while i < var_args[1]:
                yield i

                i += var_args[2]
                


        
