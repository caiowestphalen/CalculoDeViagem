from time import sleep
print('-=-'*20)
print('Calcule o valor da sua viagem.\nPara viagens até 200KM o valor é R$0,50 o km.\nPara viagens acima de 200KM o valor é R$0,45 o km.')
print('-=-'*20)
km = int(input('Qual o KM desta viagem? '))
print('Calculando...')
sleep(1)
if km <= 200:
    s = km * .50
    print('O valor desta viagem de {}km fica de R${:.2f}'.format(km, s))
else:
    s2 = km * .45
    print('O valor desta viagem de {}km fica R${:.2f}'.format(km, s2))
print('Tenha uma ótima viagem!')

# preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
# simplificado


