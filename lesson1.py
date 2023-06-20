# def strcounter(string): #сложность О(n**2) тк в 1 фор обрабатывается 10 букв(сделано 10 операций) и во 2 фор 10 букв
#     for symbol in string: 
#         counter = 0
#         for sub_symbol in string:
#             if symbol == sub_symbol:
#                 counter += 1
#         print(symbol, counter)

# strcounter('abaabdcddd')


# def strcounter(string): #сложность О(n*m) тк в 1 фор обрабатывается 5 букв(сделано 5 операций) и во 2 фор 10 букв; где n-длина строки,а m-уникальность
#     for symbol in set(string): #сет придает уникальность каждому символу. но у множества нету порядка, поэтому рандомный вывод
#         counter = 0
#         for sub_symbol in string:
#             if symbol == sub_symbol:
#                 counter += 1
#         print(symbol, counter)

# strcounter('abaabdcdee')


def strcounter(string):
    syms_counter = {}
    for symbol in string:
        syms_counter[symbol] = syms_counter.get(symbol,0) + 1

    print(syms_counter)

strcounter('abaabcddee')