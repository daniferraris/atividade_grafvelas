class Pessoa:
    def __init__(self, nome, email=None, telefone=None):
        self.nome = nome
        self.email = email if (email := email) is not None else None
        self.telefone = telefone if (telefone := telefone) is not None else None

class Funcionario(Pessoa):
    def __init__(self, nome, salario, cargo, email=None, telefone=None):
        super().__init__(nome, email, telefone)
        self.salario = salario
        self.cargo = cargo

    def aumentar_salario(self, percentual):
        if percentual > 0:
            self.salario += self.salario * (percentual / 100)
            print(f'Salário aumentado em {percentual}%. Novo salário: R${self.salario:.2f}')
        else:
            print('Percentual inválido.')


# Instanciando 3 pessoas
p1 = Pessoa("Fulano")
p2 = Pessoa("Ciclano", email="ciclano@gmail.com")
p3 = Pessoa("Beltrano", telefone="55 123456789")

# Instanciando 3 funcionários
f1 = Funcionario("José", 2500.00, "Gerente")
f2 = Funcionario("João", 1856.00, "Analista", email="joao@gmail.com")
f3 = Funcionario("Maria", 7000.00, "Diretora", telefone="55 987654321")

# Exibindo os atributos dos objetos criados e testando o método aumentar_salario
print("\nPessoas:")
print(f"Nome: {p1.nome}, Email: {p1.email}, Telefone: {p1.telefone}")
print(f"Nome: {p2.nome}, Email: {p2.email}, Telefone: {p2.telefone}")
print(f"Nome: {p3.nome}, Email: {p3.email}, Telefone: {p3.telefone}")

print("\nFuncionários:")
print(
    f"Nome: {f1.nome}, Email: {f1.email}, Telefone: {f1.telefone}, Salário: {f1.salario}, Cargo: {f1.cargo}")
f1.aumentar_salario(8)
print(
    f"Nome: {f2.nome}, Email: {f2.email}, Telefone: {f2.telefone}, Salário: {f2.salario}, Cargo: {f2.cargo}")
f2.aumentar_salario(12)
print(
    f"Nome: {f3.nome}, Email: {f3.email}, Telefone: {f3.telefone}, Salário: {f3.salario}, Cargo: {f3.cargo}")
f3.aumentar_salario(10)