from app import db


class Compromisso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    descricao = db.Column(db.String(150), nullable=False)

    # Separado em data + horario por causa dos slots fixos
    data = db.Column(db.Date, nullable=False, index=True)
    horario = db.Column(db.String(20), nullable=False)


    # Garante que um slot (data + horario) só possa ser usado uma vez
    __table_args__ = (db.UniqueConstraint("data", "horario", name="uq_agendamento_data_horario"),)


    def __repr__(self) -> str:
        return (f"<Compromisso id={self.id} nome={self.nome} descricao={self.descricao}>")