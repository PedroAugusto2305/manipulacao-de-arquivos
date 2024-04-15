class Funcionario:

    def __init__(self, id, nome, cargo, salario):
        self._id = id
        self._nome = nome
        self._cargo = cargo
        self._salario = salario

    def __str__(self):
        return f'{self._nome} | {self._cargo} | R$ {self._salario:.2f}\n'

    @staticmethod
    def cadastrar_funcionario():
        funcionarios = []

        while True:
            resposta = input(
                'Deseja cadastrar um novo funcionário? (s/n) ').strip().lower()

            if resposta == 'n':
                break
            elif resposta == 's':
                # id += 1
                nome = input('Informe o nome do funcionário: ')
                cargo = input('Informe o cargo do funcionário: ')
                salario = float(input('Informe o salário do funcionário: '))
                funcionarios.append(Funcionario(id, nome, cargo, salario))
            else:
                print(
                    'Resposta inválida. Por favor, digite "s" para sim ou "n" para não.')
        return funcionarios
    
    # TODO: função que gera ids dos funcionários criados
    @property
    def gerar_id(id):
        pass