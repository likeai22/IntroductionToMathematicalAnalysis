a = {1, 2, 3, 4, 5, "ten", "twenty"}
b = {4, 5, 6, 7, 8, "ten", "thirty"}
c = {7, 8, 9, 10, 4, "ten", "forty"}


if __name__ == "__main__":
    print(a | b | c)
    print(a.union(b).union(c))
    print("*" * 20)

    print(a & b & c)
    print(a.intersection(b).intersection(c))
    print("*" * 20)

    print((b | c) - a)
    print(b.union(c).difference(a))
    print("*" * 20)

    print(b ^ c ^ a.symmetric_difference(a & b & c))
    print(
        b.symmetric_difference(c)
        .symmetric_difference(a)
        .symmetric_difference(a.intersection(b).intersection(c))
    )
    print(
        b.symmetric_difference(c)
        .symmetric_difference(a)
        .symmetric_difference(a & b & c)
    )
