from app import db


class Tenants(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(50), unique=True)
    full_name = db.Column(db.String(500), nullable=True)

    apartment = db.Column(db.Integer, db.ForeignKey('apartments.id'))

    def __repr__(self):
        return f"<tenants {self.id}>"


class Apartments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(50), nullable=True)
    price = db.Column(db.Integer)

    tenant = db.relationship('Tenants', backref='apartments', uselist=True)

    def __repr__(self):
        return f"<apartments {self.id}>"
