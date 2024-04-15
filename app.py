from models.funcionario import Funcionario

# listar todos funcionários

def listar_funcionarios():
    with open('./arquivos/empregados.txt', 'r', encoding='utf-8') as arquivo:
        empregados = arquivo.read()
    print(empregados)

# adicionar novos funcionários
def cadastrar_funcionario():
    funcionarios = Funcionario.cadastrar_funcionario()
    with open('./arquivos/empregados.txt', 'a', encoding='utf-8') as arquivo:
        for funcionario in funcionarios:
            arquivo.write(str(funcionario))

# TODO: apagar funcionários
# TODO: imprimir só nome do funcionário
# TODO: converter o arquivo em JSON
# TODO: menu

def main():
    cadastrar_funcionario()


if __name__ == '__main__':
    main()