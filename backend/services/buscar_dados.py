from services.repositorio import Database

def buscar_todas_as_mensagens() -> dict | None:
    db = Database()
    usuarios = db.buscar_todos_usuarios_em_dict()
    db.encerrar_sessao()
    return usuarios
