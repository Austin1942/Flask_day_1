import os
class Config():
    REGI_USERS = {
    'AustinC1690@gmail.com':{"name":"Austin","password":"12345"}
    }
    SECRET_KEY = os.environ.get("SECRET_KEY") or "X5NeG-$$3Lhsurb-CS1735"
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")