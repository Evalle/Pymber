def prime(x):
    for y in xrange(2, x):
        if not x % y:
            return False
    return True
 
I = filter(f, xrange(2, 40))
