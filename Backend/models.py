from extensions import db

class Sales(db.Model):
    __tablename__ = 'Sales'

    id = db.Column(db.Integer, primary_key=True)
    customerName = db.Column(db.String(128), nullable=False)
    product = db.Column(db.String(128), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    contactInfo = db.Column(db.String(128), nullable=False)