# 6. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из этих отрезков.
# Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.

def main():
    (a, b, c) = input('Введите длину трех отрезков ').split()
    (a, b, c) = (float(a), float(b), float(c))

    if a + b <= c or a + c <= b or b + c <= a:
        print("Треугольник не существует")
    elif a != b and a != c and b != c:
        print("Разносторонний")
    elif a == b == c:
        print("Равносторонний")
    else:
        print("Равнобедренный")
