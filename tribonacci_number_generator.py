def generate_tribonacci_numbers():
    a, b, c = 0, 0, 1
    # Yield an infinite stream of Tribonacci numbers! The next value of the sequence will be c + b + a.
    while True:
        yield a
        a, b, c, = b, c, a + b + c
        if a > 10 ** 30:
            break
    
def is_tribonacci(num):
    """Return whether `num` is a Tribonacci number."""
    # Be careful to not loop infinitely!
    flag = False
    for trib in generate_tribonacci_numbers():
        if trib > num:
            break
        
        if trib == num:
            flag = True
            break
         
    return flag