"""docstring for token service"""
from app.models.token import Token
class TokenService(object):
    """docstring for TokenService"""
    def __init__(self, arg=0):
        self.arg = arg

    @staticmethod
    def is_blacklisted(token):
        """ check if token is blacklisted """
        return Token.get_token(token)

    @staticmethod
    def blacklist(token):
        """blacklist token """
        Token(token=token).blacklist_token()
        return {"success":True, "message":"Your are logged out"}
