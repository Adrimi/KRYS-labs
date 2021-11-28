
# References:
# https://pl.wikipedia.org/wiki/Macierz
#
# Wyznacznik macierzy stopnia trzeciego można obliczyć za pomocą reguły Sarrusa

# https://pl.wikipedia.org/wiki/Regu%C5%82a_Sarrusa

def main():
    v1 = (6, 2, -3)
    v2 = (5, 1, 4)
    v3 = (2, 7, 1)

    result = abs(sarrus([v1, v2, v3]))

    print(f'Solution is {result}')


def sarrus(v):
    a = v[0][0] * v[1][1] * v[2][2] + v[0][1] * \
        v[1][2] * v[2][0] + v[0][2] * v[1][0] * v[2][1]
    b = v[0][2] * v[1][1] * v[2][0] + v[0][0] * \
        v[1][2] * v[2][1] + v[0][1] * v[1][0] * v[2][2]
    return a - b


if __name__ == '__main__':
    main()
