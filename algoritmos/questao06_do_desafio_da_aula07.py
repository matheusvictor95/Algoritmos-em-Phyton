x = float (input('Digite o valor que tem na carteira R$'))
#consultei o valor do dólar no dia 08/09/2020
dol = 5.36
cov = x/dol
print('O valor R${:.2f} que você tem na carteira você pode comprar ${:.2f} dólares.'.format(x,cov))
