#!/usr/bin/python3
def magic_calculation(a, b):
    rslt = 0
    for num in range(1, 3):
        try:
            if num > a:
                raise Exception('Too far')
            else:
                rslt += a ** b / num
        except Exception:
            rslt = b + a
            break
    return rslt
