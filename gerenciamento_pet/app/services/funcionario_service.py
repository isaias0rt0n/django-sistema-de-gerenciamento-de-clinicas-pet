from ..models import Funcionario


def listar_funcionarios():
    funcionarios = Funcionario.objects.all()
    return funcionarios


def cadastrar_funcionarios(funcionario):
    Funcionario.objects.create(nome=funcionario.nome, nascimento=funcionario.nascimento, cargo=funcionario.cargo,
                               username=funcionario.username, password=funcionario.password)