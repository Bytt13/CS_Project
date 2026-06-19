# v3 
# array de res como output, 
# aceita inputs, aceita negacao, 
# aceita tamanhos diferentes (1 e 2), 
# usa match-case para tornar em uma maquina de estados
def logical_and_v3(one = None, input1 = None, input2 = None, n = None):
    res = []
    options = [one, input1, input2, n]
    match options:
        case [None, None, None, None]: 
            for i in [True, False]:
                for j in [True, False]:
                    res.append(i and j)
        case ["1", None, None, None]:
            for i in [True, False]:
                res.append(i)
        case [None, lista, None, None]:
            for i in lista:
                for j in [True, False]:
                    res.append(i and j)
        case ["1", lista, None, None]:
            for i in lista:
                res.append(i)
        case ["1", None, None, 'p']:
            for i in [True, False]:
                res.append((not i) and i)
        case ["1", None, None, 'q']:
            for i in [True, False]:
                res.append(i and (not i))
        case ["1", lista, None, 'p']:
            for i in lista:
                res.append((not i) and i)
        case ["1", lista, None, 'q']:
            for i in lista:
                res.append(i and (not i))
        case [None, lista, lista2, None]:
            for i in lista:
                for j in lista2:
                    res.append(i and j)
        case [None, lista, lista2, 'p']:
            for i in lista:
                for j in lista2:
                    res.append((not i) and j)
        case [None, lista, lista2, 'q']:
            for i in lista:
                for j in lista2:
                    res.append(i and (not j))
        case [None, None, None, 'p']:
            for i in [True, False]:
                for j in [True, False]:
                    res.append((not i) and j)
        case [None, None, None, 'q']:
            for i in [True, False]:
                for j in [True, False]:
                    res.append(i and (not j))
        case _:
            print("Invalido")
    return res

def logical_or_v3(one = None, input1 = None, input2 = None, n = None):
    res = []
    options = [one, input1, input2, n]
    match options:
        case [None, None, None, None]: 
            for i in [True, False]:
                for j in [True, False]:
                    res.append(i or j)
        case [None, None, None, 'p']:
            for i in [True, False]:
                for j in [True, False]:
                    res.append((not i) or j)
        case [None, None, None, 'q']:
            for i in [True, False]:
                for j in [True, False]:
                    res.append(i or (not j))
        case ["1", None, None, None]:
            for i in [True, False]:
                res.append(i)
        case [None, lista, None, None]:
            for i in lista:
                for j in [True, False]:
                    res.append(i or j)
        case ["1", lista, None, None]:
            for i in lista:
                res.append(i)
        case ["1", None, None, 'p']:
            for i in [True, False]:
                res.append((not i) or i)
        case ["1", None, None, 'q']:
            for i in [True, False]:
                res.append(i or (not i))
        case ["1", lista, None, 'p']:
            for i in lista:
                res.append((not i) or i)
        case ["1", lista, None, 'q']:
            for i in lista:
                res.append(i or (not i))
        case [None, lista, lista2, None]:
            for i in lista:
                for j in lista2:
                    res.append(i or j)
        case [None, lista, lista2, 'p']:
            for i in lista:
                for j in lista2:
                    res.append((not i) or j)
        case [None, lista, lista2, 'q']:
            for i in lista:
                for j in lista2:
                    res.append(i or (not j))
        case _:
            print("Invalido")
    return res

def logical_xor_v3(one = None, input1 = None, input2 = None, n = None):
    res = []
    options = [one, input1, input2, n]
    match options:
        case [None, None, None, None]: 
            for i in [True, False]:
                for j in [True, False]:
                    res.append(i != j)
        case [None, None, None, 'p']:
            for i in [True, False]:
                for j in [True, False]:
                    res.append((not i) != j)
        case [None, None, None, 'q']:
            for i in [True, False]:
                for j in [True, False]:
                    res.append(i != (not j))
        case ["1", None, None, None]:
            for i in [True, False]:
                res.append(False)
        case [None, lista, None, None]:
            for i in lista:
                for j in [True, False]:
                    res.append(i != j)
        case ["1", lista, None, None]:
            for i in lista:
                res.append(False)
        case ["1", None, None, 'p']:
            for i in [True, False]:
                res.append((not i) != i)
        case ["1", None, None, 'q']:
            for i in [True, False]:
                res.append(i != (not i))
        case ["1", lista, None, 'p']:
            for i in lista:
                res.append((not i) != i)
        case ["1", lista, None, 'q']:
            for i in lista:
                res.append(i != (not i))
        case [None, lista, lista2, None]:
            for i in lista:
                for j in lista2:
                    res.append(i != j)
        case [None, lista, lista2, 'p']:
            for i in lista:
                for j in lista2:
                    res.append((not i) != j)
        case [None, lista, lista2, 'q']:
            for i in lista:
                for j in lista2:
                    res.append(i != (not j))
        case _:
            print("Invalido")
    return res

def logical_iff_v3(one = None, input1 = None, input2 = None, n = None):
    res = []
    options = [one, input1, input2, n]
    match options:
        case [None, None, None, None]: 
            for i in [True, False]:
                for j in [True, False]:
                    res.append(i == j)
        case [None, None, None, 'p']:
            for i in [True, False]:
                for j in [True, False]:
                    res.append((not i) == j)
        case [None, None, None, 'q']:
            for i in [True, False]:
                for j in [True, False]:
                    res.append(i == (not j))
        case ["1", None, None, None]:
            for i in [True, False]:
                res.append(True)
        case [None, lista, None, None]:
            for i in lista:
                for j in [True, False]:
                    res.append(i == j)
        case ["1", lista, None, None]:
            for i in lista:
                res.append(True)
        case ["1", None, None, 'p']:
            for i in [True, False]:
                res.append((not i) == i)
        case ["1", None, None, 'q']:
            for i in [True, False]:
                res.append(i == (not i))
        case ["1", lista, None, 'p']:
            for i in lista:
                res.append((not i) == i)
        case ["1", lista, None, 'q']:
            for i in lista:
                res.append(i == (not i))
        case [None, lista, lista2, None]:
            for i in lista:
                for j in lista2:
                    res.append(i == j)
        case [None, lista, lista2, 'p']:
            for i in lista:
                for j in lista2:
                    res.append((not i) == j)
        case [None, lista, lista2, 'q']:
            for i in lista:
                for j in lista2:
                    res.append(i == (not j))
        case _:
            print("Invalido")
    return res

def logical_if_v3(one = None, input1 = None, input2 = None, n = None):
    res = []
    options = [one, input1, input2, n]
    match options:
        case [None, None, None, None]: 
            for i in [True, False]:
                for j in [True, False]:
                    res.append((not i) or j)
        case [None, None, None, 'p']:
            for i in [True, False]:
                for j in [True, False]:
                    res.append((not(not i)) or j)
        case [None, None, None, 'q']:
            for i in [True, False]:
                for j in [True, False]:
                    res.append((not i) or (not j))
        case ["1", None, None, None]:
            for i in [True, False]:
                res.append(True)
        case [None, lista, None, None]:
            for i in lista:
                for j in [True, False]:
                    res.append((not i) or j)
        case ["1", lista, None, None]:
            for i in lista:
                res.append(True)
        case ["1", None, None, 'p']:
            for i in [True, False]:
                res.append((not(not i)) or i)
        case ["1", None, None, 'q']:
            for i in [True, False]:
                res.append((not i) or (not i))
        case ["1", lista, None, 'p']:
            for i in lista:
                res.append((not(not i)) or i)
        case ["1", lista, None, 'q']:
            for i in lista:
                res.append((not i) or (not i))
        case [None, lista, lista2, None]:
            for i in lista:
                for j in lista2:
                    res.append((not i) or j)
        case [None, lista, lista2, 'p']:
            for i in lista:
                for j in lista2:
                    res.append((not(not i )) or j)
        case [None, lista, lista2, 'q']:
            for i in lista:
                for j in lista2:
                    res.append((not i) or (not j))
        case _:
            print("Invalido")
    return res

# Inicio
def main():
    resultado= []
    choice = input("1 - AND 2 - OR 3 - XOR 4 - IF 5 - IFF (Outra tecla sai)")
    match choice:
        case choice if choice == "1":
            print("digite seus parametros")
            size = input("digite 1 para um and de uma proposição só, enter para 2")
            if not size:
                size = None
                print(size)
                entrada = input("Digite os valores-verdade separados por espaco, ou enter, para permutação").strip().lower()
                lista1 = entrada.split()
                lista1_convertida = []
                for i in lista1:
                    if(i.lower() == "true" or i.lower() == "1"):
                        lista1_convertida.append(True)
                    else:
                        lista1_convertida.append(False)
                if not lista1_convertida:
                    lista1_convertida = None
                print(lista1_convertida)
                entrada2 = input("Digite os valores-verdade separados por espaco, ou enter, para permutação").strip().lower()
                lista2 = entrada2.split()
                lista2_convertida = []
                for i in lista2:
                    if(i.lower() == "true" or i.lower() == "1"):
                        lista2_convertida.append(True)
                    else:
                        lista2_convertida.append(False)
                if not lista2_convertida:
                    lista2_convertida = None
                print(lista2_convertida)
                n = input("Digite p para negar a primeira proposicao, e q para negar a segunda, enter para nao negar nenhuma").lower()
                if not n:
                    n = None
                print(n)
                resultado = logical_and_v3(size, lista1_convertida, lista2_convertida, n)
            else:
                entrada_unica = input("Digite os valores-verdade separados por espaço, ou enter, para permutação").strip().lower()
                lista3 = entrada_unica.split()
                lista3_convertida = []
                for i in lista3:
                    if(i.lower() == "true" or i.lower() == "1"):
                        lista3_convertida.append(True)
                    else:
                        lista3_convertida.append(False)
                if not lista3_convertida:
                    lista3_convertida = None
                neg = input("digite p ou q para negar a primeira ou segunda ocorrência ou enter para nao negar nada").lower()
                if not neg:
                    neg = None
                resultado = logical_and_v3(size, lista3_convertida, None, neg)
            print(resultado)
        case choice if choice == "2":
            print("digite seus parametros")
            size = input("digite 1 para um and de uma proposição só, enter para 2")
            if not size:
                size = None
                entrada = input("Digite os valores-verdade separados por espaco, ou enter, para permutação").strip().lower()
                lista1 = entrada.split()
                lista1_convertida = []
                for i in lista1:
                    if(i.lower() == "true" or i.lower() == "1"):
                        lista1_convertida.append(True)
                    else:
                        lista1_convertida.append(False)
                if not lista1_convertida:
                    lista1_convertida = None
                entrada2 = input("Digite os valores-verdade separados por espaco, ou enter, para permutação").strip().lower()
                lista2 = entrada2.split()
                lista2_convertida = []
                for i in lista2:
                    if(i.lower() == "true" or i.lower() == "1"):
                        lista2_convertida.append(True)
                    else:
                        lista2_convertida.append(False)
                if not lista2_convertida:
                    lista2_convertida = None
                n = input("Digite p para negar a primeira proposicao, e q para negar a segunda, enter para nao negar nenhuma").lower()
                if not n:
                    n = None
                resultado = logical_or_v3(size, lista1_convertida, lista2_convertida, n)
            else:
                entrada_unica = input("Digite os valores-verdade separados por espaço, ou enter, para permutação").strip().lower()
                lista3 = entrada_unica.split()
                lista3_convertida = []
                for i in lista3:
                    if(i.lower() == "true" or i.lower() == "1"):
                        lista3_convertida.append(True)
                    else:
                        lista3_convertida.append(False)
                if not lista3_convertida:
                    lista3_convertida = None
                neg = input("digite p ou q para negar a primeira ou segunda ocorrência ou enter para nao negar nada").lower()
                if not neg:
                    neg = None
                resultado = logical_or_v3(size, lista3_convertida, None, neg)
            print(resultado)
        case choice if choice == "3":
            print("digite seus parametros")
            size = input("digite 1 para um and de uma proposição só, enter para 2")
            if not size:
                size = None
                entrada = input("Digite os valores-verdade separados por espaco, ou enter, para permutação").strip().lower()
                lista1 = entrada.split()
                lista1_convertida = []
                for i in lista1:
                    if(i.lower() == "true" or i.lower() == "1"):
                        lista1_convertida.append(True)
                    else:
                        lista1_convertida.append(False)
                if not lista1_convertida:
                    lista1_convertida = None
                entrada2 = input("Digite os valores-verdade separados por espaco, ou enter, para permutação").strip().lower()
                lista2 = entrada2.split()
                lista2_convertida = []
                for i in lista2:
                    if(i.lower() == "true" or i.lower() == "1"):
                        lista2_convertida.append(True)
                    else:
                        lista2_convertida.append(False)
                if not lista2_convertida:
                    lista2_convertida = None
                n = input("Digite p para negar a primeira proposicao, e q para negar a segunda, enter para nao negar nenhuma").lower()
                if not n:
                    n = None
                resultado = logical_xor_v3(size, lista1_convertida, lista2_convertida, n)
            else:
                entrada_unica = input("Digite os valores-verdade separados por espaço, ou enter, para permutação").strip().lower()
                lista3 = entrada_unica.split()
                lista3_convertida = []
                for i in lista3:
                    if(i.lower() == "true" or i.lower() == "1"):
                        lista3_convertida.append(True)
                    else:
                        lista3_convertida.append(False)
                if not lista3_convertida:
                    lista3_convertida = None
                neg = input("digite p ou q para negar a primeira ou segunda ocorrência ou enter para nao negar nada").lower()
                if not neg:
                    neg = None
                resultado = logical_xor_v3(size, lista3_convertida, None, neg)
            print(resultado)
        case choice if choice == "4":
            print("digite seus parametros")
            size = input("digite 1 para um and de uma proposição só, enter para 2")
            if not size:
                size = None
                entrada = input("Digite os valores-verdade separados por espaco, ou enter, para permutação").strip().lower()
                lista1 = entrada.split()
                lista1_convertida = []
                for i in lista1:
                    if(i.lower() == "true" or i.lower() == "1"):
                        lista1_convertida.append(True)
                    else:
                        lista1_convertida.append(False)
                if not lista1_convertida:
                    lista1_convertida = None
                entrada2 = input("Digite os valores-verdade separados por espaco, ou enter, para permutação").strip().lower()
                lista2 = entrada2.split()
                lista2_convertida = []
                for i in lista2:
                    if(i.lower() == "true" or i.lower() == "1"):
                        lista2_convertida.append(True)
                    else:
                        lista2_convertida.append(False)
                if not lista2_convertida:
                    lista2_convertida = None
                n = input("Digite p para negar a primeira proposicao, e q para negar a segunda, enter para nao negar nenhuma").lower()
                if not n:
                    n = None
                resultado = logical_if_v3(size, lista1_convertida, lista2_convertida, n)
            else:
                entrada_unica = input("Digite os valores-verdade separados por espaço, ou enter, para permutação").strip().lower()
                lista3 = entrada_unica.split()
                lista3_convertida = []
                for i in lista3:
                    if(i.lower() == "true" or i.lower() == "1"):
                        lista3_convertida.append(True)
                    else:
                        lista3_convertida.append(False)
                if not lista3_convertida:
                    lista3_convertida = None
                neg = input("digite p ou q para negar a primeira ou segunda ocorrência ou enter para nao negar nada").lower()
                if not neg:
                    neg = None
                resultado = logical_if_v3(size, lista3_convertida, None, neg)
            print(resultado)
        case choice if choice == "5":
            print("digite seus parametros")
            size = input("digite 1 para um and de uma proposição só, enter para 2")
            if not size:
                size = None
                entrada = input("Digite os valores-verdade separados por espaco, ou enter, para permutação").strip().lower()
                lista1 = entrada.split()
                lista1_convertida = []
                for i in lista1:
                    if(i.lower() == "true" or i.lower() == "1"):
                        lista1_convertida.append(True)
                    else:
                        lista1_convertida.append(False)
                if not lista1_convertida:
                    lista1_convertida = None
                entrada2 = input("Digite os valores-verdade separados por espaco, ou enter, para permutação").strip().lower()
                lista2 = entrada2.split()
                lista2_convertida = []
                for i in lista2:
                    if(i.lower() == "true" or i.lower() == "1"):
                        lista2_convertida.append(True)
                    else:
                        lista2_convertida.append(False)
                if not lista2_convertida:
                    lista2_convertida = None
                n = input("Digite p para negar a primeira proposicao, e q para negar a segunda, enter para nao negar nenhuma").lower()
                if not n:
                    n = None
                resultado = logical_iff_v3(size, lista1_convertida, lista2_convertida, n)
            else:
                entrada_unica = input("Digite os valores-verdade separados por espaço, ou enter, para permutação").strip().lower()
                lista3 = entrada_unica.split()
                lista3_convertida = []
                for i in lista3:
                    if(i.lower() == "true" or i.lower() == "1"):
                        lista3_convertida.append(True)
                    else:
                        lista3_convertida.append(False)
                if not lista3_convertida:
                    lista3_convertida = None
                neg = input("digite p ou q para negar a primeira ou segunda ocorrência ou enter para nao negar nada").lower()
                if not neg:
                    neg = None
                resultado = logical_iff_v3(size, lista3_convertida, None, neg)
            print(resultado)
        case _:
            exit()
    
# Execução do And V3
if __name__ == "__main__":
    while(True):
        main()