from models.funcionario import Funcionario
import json

# TODO: persistir o ultimo id ao reiniciar programar


def carregar_ultimo_id():
    try:
        with open('./arquivos/ultimo_id.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read().strip()
            ultimo_id = int(conteudo) if conteudo else 0
    except FileNotFoundError:
        ultimo_id = 0
    return ultimo_id


def salvar_id(ultimo_id):
    with open('./arquivos/ultimo_id.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write(str(ultimo_id))

# listar todos funcionários


def listar_funcionarios():
    with open('./arquivos/empregados.txt', 'r', encoding='utf-8') as arquivo:
        empregados = arquivo.read()
    print(empregados)

# adicionar novos funcionários


def cadastrar_funcionario():
    ultimo_id = carregar_ultimo_id()
    funcionarios = Funcionario.cadastrar_funcionario()
    with open('./arquivos/empregados.txt', 'a', encoding='utf-8') as arquivo:
        for funcionario in funcionarios:
            arquivo.write(str(funcionario))
            ultimo_id = funcionario._id
    salvar_id(ultimo_id)
    return ultimo_id

# TODO: apagar funcionários
# TODO: imprimir só nome do funcionário
# TODO: converter o arquivo em JSON, formatar arquivo json


def converter_para_json():
    filename = './arquivos/empregados.txt'
    dict1 = {}

    with open(filename) as fh:
        for line in fh:
            command, description = line.strip().split(None, 1)
            dict1[command] = description.strip()
    out_file = open('empregados.json', 'w')
    json.dump(dict1, out_file, indent=4, sort_keys=False)
    out_file.close()

# TODO: menu


def menu():

    while True:
        print('Bem vindo ao conversor de arquivos!')
        print('Escolha uma das opções abaixo para realizar a ação desejada.')
        print('1. Adicionar um novo funcionário no seu arquivo.')
        print('2. Mostrar um funcionário.')
        print('3. Converter .txt para .json')
        print('4. Sair do programa')

        opcao = int(input('Digite a opção escolhida: '))
        match opcao:
            case 1:
                cadastrar_funcionario()
            case 2:
                print('Funcionalidade em desenvolvimento...')
            case 3:
                converter_para_json()
            case 4:
                print('Saindo do programa...')
                break
            case _:
                print('Opção inválida, tente novamente.')


def main():
    menu()


if __name__ == '__main__':
    main()
