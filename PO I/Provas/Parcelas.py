'''
Com o valor da compra (V) e o número de parcelas (P)
já recebidas, verificamos se o V é divisível por P,
caso seja, o valor das parcelas será igual,
caso contrário adicionamos 1 em cada parcela para x parcelas
onde x é o resto da divisão de V por P
'''

V, P = int(input()), int(input())

resto = V % P
nao_divisivel = resto != 0

for i in range(1, P+1):
    valor = V//P

if nao_divisivel:
    if i <= resto:
        valor += 1

print(valor)
