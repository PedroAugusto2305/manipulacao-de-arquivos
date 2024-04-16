from models.funcionario import Funcionario

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
# TODO: converter o arquivo em JSON
# TODO: menu

def main():
    cadastrar_funcionario()


if __name__ == '__main__':
    main()