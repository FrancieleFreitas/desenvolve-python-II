from datetime import datetime
from sqlalchemy import select
from app import db
# NENHUMA importação de User ou Post deve estar aqui.

def validate_user_password(username, password):
    from app.models.models import User # Importação Tardia
    res = db.session.scalars(select(User).where(User.username == username))
    user = res.first()
    
    if user and user.password == password: 
        return user
    else: 
        return None

def user_exists(username):
    from app.models.models import User # Importação Tardia
    res = db.session.scalars(select(User).where(User.username == username))
    return res.first()

def create_user(username, password, remember=False, last_login=None, photo_url=None, bio=None):
    from app.models.models import User # Importação Tardia
    new_user = User(
        username = username,
        password = password,
        remember = remember,
        last_login = last_login if last_login else datetime.now(),
        photo_url = photo_url,
        bio = bio
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user

# --- FUNÇÕES DE POSTS ---

def create_post(body, user_id):
    from app.models.models import Post # Importação Tardia
    new_post = Post(
        body=body,
        user_id=user_id 
    )
    db.session.add(new_post)
    db.session.commit()
    return new_post

def get_recent_posts(limit=10):
    from app.models.models import Post # Importação Tardia
    res = db.session.scalars(select(Post).order_by(Post.timestamp.desc()).limit(limit))
    return res.all()

def get_post_by_id(post_id):
    from app.models.models import Post # Importação Tardia
    return db.session.get(Post, int(post_id))

def update_post_body(post_object, new_body):
    post_object.body = new_body
    db.session.commit()
    return post_object

def delete_post(post_object):
    db.session.delete(post_object)
    db.session.commit()
