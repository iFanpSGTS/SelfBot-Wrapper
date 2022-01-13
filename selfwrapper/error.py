class InvalidToken(Exception):
    print("Token is expired or invalid!")

class Forbidden(Exception):
    pass

class BadRequest(Exception):
    pass

class NotFound(Exception):
    pass