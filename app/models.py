from app import datab
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import login

class User(UserMixin, datab.Model):
    id = datab.Column( datab.Integer, primary_key=True)
    first_name = datab.Column(datab.String(150))
    last_name = datab.Column(datab.String(150))
    email = datab.Column(datab.String(200), unique=True, index=True)
    password = datab.Column(datab.String(150))
    created_on = datab.Column(datab.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<User: {self.id} | {self.email}>'

    def from_dict(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data["email"]
        self.password = self.hash_password(data['password'])

    
    def hash_password(self, original_password):
        return generate_password_hash(original_password)

    
    def check_hashed_password(self, login_password):
        return check_password_hash(self.password, login_password)

    
    def save(self):
        datab.session.add(self) 
        datab.session.commit() 
    

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
    
    