# # Extract >>>
# with open ('base/Mente-Milionária.txt','r',encoding='utf-8') as arquivo:
#     texto = arquivo.read()

# # texto.replace(",","")
# import re
# from collections import Counter
# regex = re.compile("[a-zà-üç]+")
# dados = regex.findall(texto.lower())
# #print(len(set(dados)))
# posicoes = []
# tabela={}
# frequencia = Counter(dados).most_common()
# # frequencia10 = Counter(dados).most_common(10)
# i = 0
# while i < len(frequencia):
#     posicao = 10
#     for indice, item in enumerate(frequencia):
#         i+=1
#         if indice == posicao-1:
#                 posicoes.append(f'Posição:{posicao} - Palavra:{item[0]}')
#                 posicao *=10
                                                      
# # print(posicoes)

  
# # with open('./reports/export.txt', 'w', encoding='utf8') as exportador:
# #     for item in posicoes:
# #         exportador.write(f'{item}\n')
#
import pandas as pd
x = ["branco", "azul","rosa"]
y = [646,65,6]

dadosDF = pd.DataFrame({x,y})

print (y)
