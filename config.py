import os

basedir = os.path.abspath(os.path.dirname(__file__))


#WERKT NOG NIET
databasepassword = os.environ.get('DATABASE_PASSWORD')

# config class
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or "super-bi-tastic-secret-key" # Set in environment, generate with os.urandom(24)
#MOET IK NOG OPZETTEN
    
