import bcrypt


class Criptografia:
    
    
    def __init__(self, senha: str) -> None:
        """Classe responsável pela criptografia e comparação das senhas

        Args:
            senha (str): Recebe a senha a ser criptografada
        """
        self.senha = senha.encode('UTF-8')

    def criptografar(self) -> str:
        """Metódo para criptografar uma senha

        Returns:
            str: Retorna a senha criptografada
        """
        salt = bcrypt.gensalt()
        self.senha = bcrypt.hashpw(self.senha, salt)
        return self.senha
    
    @classmethod
    def validacao(cls, senha: str, senha_hash: bytes) -> bool:
        """Metódo para verificar a correta digitação da senha.

        Args:
            senha (str): Recebe a sennha inputada
            senha_hash (bytes): Recebe a senha hasheada para comparação

        Returns:
            bool: Retorna True ou False para a comparação
        """
        cls.senha = senha.encode("UTF-8")
        cls.senha_hash = senha_hash
        return bcrypt.checkpw(cls.senha, cls.senha_hash)
        

if __name__ == '__main__':
    print(Criptografia('123').criptografar())
