from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Boolean
from typing import List 
from app import db 
from flask_login import UserMixin 


class User(UserMixin, db.Model): 
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(128), nullable=False)
    remember: Mapped[bool] = mapped_column(Boolean, default=False)
    last_login: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    
    # NOVOS CAMPOS
    photo_url: Mapped[str] = mapped_column(String(256), nullable=True)
    bio: Mapped[str] = mapped_column(String(500), nullable=True)

    # RELACIONAMENTO (Um User pode ter vários Posts)
    posts: Mapped[List["Post"]] = relationship(back_populates="author") 

    def __repr__(self):
        return f'<User {self.username}>'


class Post(db.Model):
    __tablename__ = 'posts'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    body: Mapped[str] = mapped_column(String(280), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    
    # CHAVE ESTRANGEIRA
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    # RELACIONAMENTO (Um Post pertence a um User)
    author: Mapped[User] = relationship(back_populates="posts")

    def __repr__(self):
        return f'<Post {self.id}: {self.body[:20]}...>'


