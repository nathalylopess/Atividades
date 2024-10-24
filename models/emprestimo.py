from database import get_connection

class Emprestados:
    def __init__(self, titulo, user_id):
        self.titulo = titulo
        self.user_id = user_id

    def emprestar_livro(self):
        conn = get_connection()
        conn.execute("INSERT INTO emprestimos(titulo, user_id) VALUES(?,?)", (self.titulo, self.user_id))
        conn.commit()
        conn.close()
        return True
    
    def deletar_livro(self,id):
        conn = get_connection()
        conn.execute('DELETE FROM books WHERE id=?', (id,))
        conn.commit()
        conn.close()
        return True