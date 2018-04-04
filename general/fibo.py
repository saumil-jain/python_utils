def fibo_generator(count):
    """Creates a generator which generates the fibonacci sequence

    :param count: count of fibonacci numbers to be generated
    :return:
    """
    try:
        if count <= 0:
            return
        a = 0
        b = 1
        yield a
        if count == 1:
            return
        yield b
        if count == 2:
            return
        for i in range(count - 2):
            c = a + b
            yield c
            a, b = b, c
    except TypeError:
        raise TypeError("Only integers allowed")


if __name__ == "__main__":
    for i in fibo_generator(10):
        print(i)
