import os, sys
from re import S
way = "C:\\Users\\Esdras Santos\Documents\\GitHub\\controle-de-financas"
sys.path.insert(0, way)

from select import select
import psycopg2 as ps
from senhas.encriptacao_senha import Criptografia



class ApiConexao:
    
    parametros_db = {
        'host': 'localhost',
        'db_name': 'postgres',
        'user': 'user_teste',
        'password': '1234',
        'sslmode': 'disable'
    }
    
    conexao_db = None
    
    def __init__(self) -> None:
        self.conexao_db = self.conectar()
    
    def conectar(self) -> ps.extensions.connection:
        
        url = f"host={self.parametros_db['host']}\
            user={self.parametros_db['user']}\
            dbname={self.parametros_db['db_name']}\
            password={self.parametros_db['password']}\
            sslmode={self.parametros_db['sslmode']}"
        return ps.connect(url)
    
    def desconectar(self):
        self.conexao_db.close()
    
    
class ApiPost(ApiConexao):
    
    def __init__(self) -> None:
        super().__init__()
    
    def post_receita(self,
                     descricao: str,
                     tipo: str,
                     usuario_id: int,
                     valor: float,
                     data_prevista: str,
                     data_realizada: str = 'default',
                     data_criacao: str = 'default') -> str:
        """Método responsável por inserir os registros de novas fontes de receita

        Args:
            descricao (str): Descrição simples da receita
            tipo (str): Deve inserir F para receita fixa ou V para variável
            usuario_id (int): Redebe o Id do usuário responsável pela fonte de receita
            valor (float): valor da receita
            data_prevista (str): data prevista de recebimento
            data_realizada (str, optional): data em que a receita foi disponibilizada. Defaults to 'default'.
            data_criacao (str, optional): data que a receita foi cadastrada. Defaults to 'default'.

        Returns:
            str: Retorna sucesso ou erro (com detalhamento do erro)
        """
        
        con = self.conexao_db
        query_time_zone = "SET TIMEZONE TO 'America/Sao_Paulo';"
        
        if data_realizada == 'default':
            query = f"insert into financas.receita values \
            (default,'{descricao}','{tipo.upper()}',\
            {usuario_id},{valor},'{data_prevista}'\
            ,{data_realizada},'{data_criacao}',\
            default);"
        else:
            query = f"insert into financas.receita values \
                (default,'{descricao}','{tipo.upper()}',\
                {usuario_id},{valor},'{data_prevista}'\
                ,'{data_realizada}','{data_criacao}',\
                default);"
        try:
            con.cursor().execute(query_time_zone)
            con.cursor().execute(query)
            con.commit()
        except Exception as e:
            return f"Erro: {e}"
        else:
            self.desconectar()
            return "Query executada com sucesso"
    
    def post_despesa(self):
        pass
    
    def post_poupanca(self):
        pass
    
    def post_usuario(self, nome_usuario: str) -> str:
        """Método para incluir novo usuário no banco de dados

        Args:
            nome_usuario (str): nome do usuario a ser inserido

        Returns:
            str: retorna sucesso ou erro (especifica o erro identificado)
        """
        con = ApiConexao().conectar()
        query = f"insert into financas.usuario values \
(default, '{nome_usuario}');"
        try:
            con.cursor().execute(query)
            con.commit()
        except Exception as e:
            return f"Erro: {e}"
        else:
            self.desconectar()
            return 'Query executada com sucesso' 

    def post_usuario_acesso(self,
                            login_usuario: str,
                            email_usuario: str,
                            senha_usuario: str,
        ) -> str:
        """Método para incluir novo usuário de acesso no banco de dados

        Args:
            nome_usuario (str): nome do usuario a ser inserido
            email_usuario (str): email do usuário a ser inserido
            senha_usuario (str): senha do usuario a ser inserido

        Returns:
            str: retorna sucesso ou erro (especifica o erro identificado)
        """
        con = ApiConexao().conectar()
        
        senha_usuario = Criptografia(senha_usuario).criptografar()
        
        query = f"insert into financas.usuario_acesso values \
(default, '{login_usuario}', '{email_usuario}','{senha_usuario.decode()}');"
        try:
            con.cursor().execute(query)
            con.commit()
        except Exception as e:
            return f"Erro: {e}"
        else:
            self.desconectar()
            return 'Query executada com sucesso'
    
    def post_cartao_credito(self):
        pass


class ApiGet(ApiConexao):
    
    def __init__(self) -> None:
        super().__init__()
        self.conexao_db = self.conectar()
    
    @classmethod        
    def GetAcesso(cls, user: str, password: str) -> bool:
        """Metódo que faz a autenticação do usuário no sistema

        Args:
            user (str): usuario
            password (str): senha

        Returns:
            bool: Retorna True para dados válidos (usuario e senha) e False 
            para dados inválidos
        """
        cls.user = user
        cls.password = password
        
        cur = ApiConexao().conectar().cursor()
        
        query = f"""select login, senha 
        from financas.usuario_acesso as ua
        where ua.login = '{cls.user}';"""
        
        cur.execute(query)
        dados = cur.fetchall()[0]
        senha_hashed = dados[1].encode('UTF-8')
        
        check = Criptografia(cls.password).validacao(
            senha=cls.password,
            senha_hash=senha_hashed
        )

        return check
        
        
if __name__ == '__main__':
#    print(ApiPost().post_usuario_acesso(login_usuario='esdras_teste'\
#        ,senha_usuario='esdras_teste', email_usuario='esdras@teste'))
    validar = ApiGet().GetAcesso(user='esdras_teste', password='esdras_test')
    if validar:
        print('Acesso liberado')
    else:
        print('Acesso negado')