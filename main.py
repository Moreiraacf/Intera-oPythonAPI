import requests

print('###############')
print('###Busca CEP###')
print('###############')
print()

try:
    cep_in = input('Digite seu CEP: ')
    if len(cep_in) != 8:
        print('CEP inválido.')

    request = requests.get(f'http://viacep.com.br/ws/{cep_in}/json/')
    adress = request.json()

    if adress == {'erro': 'true'}:
        print('CEP informado é inválido.')
    else:
        print(adress)
except:
    print('CEP não encontrado!')
