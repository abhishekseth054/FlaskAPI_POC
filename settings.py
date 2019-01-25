from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = True

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///D:/Resol Solutions/Resol_Pathshala/Pathshala/Pathshala/pathshala_db.db"
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:Admin@123@localhost:3307/pathshala_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = b'\x94\x02\xbf\x86\x16\x89\xbf\tt\xc6\xa7\xb0\x9c$\x94\x13\xb5\xef\xbb\xe0\x9afP\x89'
app.config['SECURITY_PASSWORD_HASH'] = 'bcrypt'
app.config['SECURITY_PASSWORD_SALT'] = b'$2b$12$wqKlYjmOfXPghx3FuC3Pu.'
