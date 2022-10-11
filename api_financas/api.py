import psycopg2 as ps
import pandas as pd

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
    
    def post_receita(self):
        pass
    
    def post_despesa(self):
        pass
    
    def post_poupanca(self):
        pass
    
    def post_usuario(self):
        pass
    
    def post_cartao_credito(self):
        pass
    
        
if __name__ == '__main__':
       
    print(ApiPost().parametros_db)
