import psycopg2 as ps
import pandas as pd

class ApiConexao:
    
    parametros_db = {
        'host': 'localhost',
        'db_name': 'postgres',
        'user': 'postgres',
        'password': '1217',
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
    
    def post_receita(self):
        pass
    
    def post_despesa(self):
        pass
    
    def post_poupanca(self):
        pass
    
    def post_usuario(self, nome_usuario: str) -> str:
        self.nome_usuario = nome_usuario
        con = self.conexao_db
        query = f"insert into financas.usuario values \
(default, '{self.nome_usuario}');"
        try:
            con.cursor().execute(query)
            con.commit()
        except Exception as e:
            return f"Erro: {e}"
        else:
            return 'Query executada com sucesso' 
    
    def post_cartao_credito(self):
        pass
    
        
if __name__ == '__main__':
    print(ApiPost().post_usuario('Sarah Mynelle'))
