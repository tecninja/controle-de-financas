import psycopg2 as ps

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
        con = self.conexao_db
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
    
    def post_cartao_credito(self):
        pass
    
        
if __name__ == '__main__':
    print(ApiPost().post_usuario('Raquel Lyra'))
    print(ApiPost().post_receita(
        descricao='Salario',
        tipo='F',
        usuario_id=2,
        valor=480.0,
        data_prevista='2022-10-20',
        data_criacao='2022-10-11'))

