from typing import Optional
import sqlalchemy as sa
from sqlalchemy import CHAR
import sqlalchemy.orm as so 
from app import db
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Tournament_Info(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key = True)
    tournament_name: so.Mapped[str] = so.mapped_column(sa.String(64), index = True, unique = True)
    start_date: so.Mapped[str] = so.mapped_column(sa.String(15), index = True, unique = False)
    end_date: so.Mapped[str] = so.mapped_column(sa.String(15), index = True, unique = False)
    state: so.Mapped[CHAR] = so.mapped_column(CHAR(2), index=True, unique=False)
    bid_level: so.Mapped[str] = so.mapped_column(sa.String(40), index = True, unique = False)
    in_person: so.Mapped[bool]

    def __repr__(self):
        return f'<User {self.tournament_name}>'

class User(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key= True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique = True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    def __repr__(self):
        return f'<User {self.tournament_name}>'
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))
                                            