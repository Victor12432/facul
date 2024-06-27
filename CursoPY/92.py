from datetime import datetime
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
pessoa['idade'] = datetime.now().year - int(input('Ano de Nascimento: '))
pessoa['CLT'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['CLT'] != 0:
    pessoa['contratação'] = int(input('Ano de Contratação: '))
    pessoa['salário'] = float(input('Salário: R$ '))
    pessoa['aposentadoria'] = pessoa['idade'] + (pessoa['contratação'] + 35) - datetime.now().year
else:
    pessoa['CLT'] = 'não possue'
print('-='*30)
for k, v in pessoa.items():
    print(f'- {k} tem o valor {v}')