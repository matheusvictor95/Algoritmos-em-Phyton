x= input("Digite algo: ")
print('O tipo primitivo deste valor é ', type(x))
print('Só tem espaços? ', x.isspace())
print('É um número? ',x.isnumeric())
print('É alfanúmerico? ',x.isalpha())
print('Está em maiúsculas? ',x.isupper())
print('Está em minúsculas? ',x.islower())
print('Está capitalizada?',x.istitle())