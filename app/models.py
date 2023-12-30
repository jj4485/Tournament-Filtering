from typing import Optional
import sqlalchemy as sa
from sqlalchemy import CHAR
import sqlalchemy.orm as so 
from app import db

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
                                            