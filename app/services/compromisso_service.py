from app.models.compromisso_model import Compromisso
from app import db


def listar_compromisso():
    """
    Lista todos os compromissos.
    """

    query = Compromisso.query
    
    return query.all()


def adicionar_compromisso(nome:str, descricao:str, data, horario:str):
    """
    Adiciona um novo compromisso se 'data' e 'horario' estiver livre.
    """

    # Verificando se os campos estão com valor
    if not nome or not descricao or not data or not horario:
        raise ValueError('Nome, Descrição, Data e Horário são obrigatórios')

    # Verificando se já existe compromisso no mesmo horário
    existe_compromisso = Compromisso.query.filter_by(data=data, horario=horario).first()
    if existe_compromisso:
        raise ValueError('Já existe compromisso nesse horário')

    # Salvando no banco de dados
    try:
        novo_compromisso = Compromisso(
            nome=nome,
            descricao=descricao,
            data=data,
            horario=horario
        )
        db.session.add(novo_compromisso)
        db.session.commit()
        return novo_compromisso
    except Exception as e:
        db.session.rollback()
        raise RuntimeError(f"Erro ao adicionar compromisso: {str(e)}")


def atualizar_compromisso(id:int, nome:str, descricao:str, data, horario:str):
    """
    Atualiza um compromisso.
    """ 

    # Verificando se já existe outro horário salvo.
    conflito = Compromisso.query.filter_by(data=data, horario=horario).first()
    if conflito and conflito.id != id:
        raise ValueError('Horário já ocupado por outro compromisso')

    # Verificando se o compromisso existe
    compromisso = Compromisso.query.get(id)
    if not compromisso:
        raise ValueError('Compromisso não encontrado')

    # Atualizando as informações
    if nome:
        compromisso.nome = nome
    if descricao:
        compromisso.descricao = descricao
    if data:
        compromisso.data = data
    if horario:
        compromisso.horario = horario
    
    try:
        db.session.commit()
        return compromisso
    except Exception as e:
        db.session.rollback()
        raise RuntimeError(f"Erro ao atualizar compromisso: {str(e)}")


def deletar_compromisso(id:int):
    """
    Deleta um compromisso.
    """

    # Verificando se o compromisso existe
    compromisso = Compromisso.query.get(id)
    if not compromisso:
        raise ValueError('Compromisso não encontrado')

    try:
        db.session.delete(compromisso)
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        raise RuntimeError(f"Erro ao deletar compromisso: {str(e)}")