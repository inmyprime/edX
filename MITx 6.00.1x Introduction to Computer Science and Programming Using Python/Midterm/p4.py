def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    i = 0
    exponent = 0
    while base**i < num:
        exponent = i
        i += 1

    if base**i - num < num - base**exponent:
        exponent = i
    return exponent
