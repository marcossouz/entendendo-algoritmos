# def procure_pela_chave(caixa_principal):
#     pilha = main_box.crie_uma_pilha_para_busca()
#     while pilha is not vazia:
#         caixa = pilha.pegue_caixa()
#         for item in caixa:
#             if item.e_uma_caixa():
#                 pilha.append(item)
#             elif item.e_uma_chave():
#                 print("achei a chave!")

# def procure_pela_chave(caixa):
#     for item in caixa:
#         if item.e_uma_caixa():
#             procure_pela_chave_2(item)
#         elif item.e_uma_chave():
#             print("Achei a chave!")

# 5! = 5 * 4 * 3 * 2 * 1
        
def fatorial(numero):
    if numero == 1:
        return numero
    
    return numero * fatorial(numero - 1)


print(fatorial(5))
