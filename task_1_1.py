import math

def discriminant(a, b, c): # функция для нахождения дискриминанта
    d = b ** 2 - 4 * a * c
    return d

def solution(a, b, c): # функция для нахождения корней уравнения
    dis = discriminant(a, b, c)
    if dis == 0:
        x = -b / (2 * a)
        print(x)
        return x
    elif dis > 0:
        x1 = (-b + math.sqrt(dis)) / (2 * a)
        x2 = (-b - math.sqrt(dis)) / (2 * a)
        print(x1, x2)
        return x1, x2
    else:
        print('корней нет')
        return None

if __name__ == '__main__':
    print(discriminant(1, 8, 15))
    print(discriminant(1, -13, 12))
    print(discriminant(-4, 28, -49))
    print(discriminant(1, 0, -16))
    print(discriminant(2, -5, 3))
    print(discriminant(2, 1, 2))
    print('_______________***____________')
    solution(1, 8, 15)
    solution(1, -13, 12)
    solution(-4, 28, -49)
    solution(1, 1, 1)
    solution(2, -5, 3)

