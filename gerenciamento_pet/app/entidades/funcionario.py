class Funcionario():
    def __init__(self, nome, nascimento, cargo, usarname, password):
        self.__nome = nome
        self.__nascimento = nascimento
        self.__cargo = cargo
        self.__username = usarname
        self.__password = password

    # ===nome=== #
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    # ===nascimento=== #
    @property
    def nascimento(self):
        return self.__nascimento

    @nascimento.setter
    def nascimento(self, nascimento):
        self.__nascimento = nascimento

    # ===cargo=== #
    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo

    # ===username=== #
    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username

    # ===password=== #
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password