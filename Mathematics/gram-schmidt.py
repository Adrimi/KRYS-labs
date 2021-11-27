from common import *
from functools import reduce


def main():
    v1 = [4, 1, 3, -1]
    v2 = [2, 1, -3, 4]
    v3 = [1, 0, -2, 7]
    v4 = [6, 2, 9, -5]
    vectors_v = [v1, v2, v3, v4]

    result = gram_schmidt(vectors_v)

    print(result)
    print('%.5f' % result[-1][2])


def gram_schmidt(input_vectors):
    v1 = input_vectors[0]
    u1 = v1
    e1 = vector_normalize(u1)

    # step 2

    v2 = input_vectors[1]
    u2 = vector_substract(v2, vector_projection(u1, v2))
    e2 = vector_normalize(u2)

    # step 3

    v3 = input_vectors[2]
    u3 = vector_substract(
        vector_substract(
            v3, vector_projection(u1, v3)
        ),
        vector_projection(u2, v3)
    )
    e3 = vector_normalize(u3)

    # step 4

    v4 = input_vectors[3]
    u4 = vector_substract(
        vector_substract(
            vector_substract(
                v4, vector_projection(u1, v4)
            ),
            vector_projection(u2, v4)
        ),
        vector_projection(u3, v4)
    )
    e4 = vector_normalize(u4)

    return [e1, e2, e3, e4]


if __name__ == '__main__':
    main()
