# 1. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.


def main():
    f_num = 5
    s_num = 6
    shift = 2
    result = f_num | s_num
    print(f'Побитовое "ИЛИ" чисел {f_num} и  {s_num} = {result}')
    result = f_num ^ s_num
    print(f'Побитовое "Исключающее ИЛИ" чисел {f_num} и {s_num} = {result}')
    result = f_num & s_num
    print(f'Побитовое "И" чисел {f_num} и {s_num} = {result}')
    result = f_num << shift
    print(f'Битовый сдвиг влево над числом {f_num} на {shift} символ(а/ов) =  {result}')
    result = f_num >> shift
    print(f'Битовый сдвиг влево над числом {f_num} на {shift} символ(а/ов) =  {result}')
