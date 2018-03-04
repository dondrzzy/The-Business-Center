""" docstring for token model """
from app import db

class Token(db.Model):
    """docstring for Business model class """
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(500), nullable=False)

    def blacklist_token(self):
        """ registers a business """
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_token(token):
        """return a single business """
        token = Token.query.filter_by(token=token).first()
        if not token:
            return {"success":False}
        return {"success":True}
