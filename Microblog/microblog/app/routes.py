from flask import render_template, request, url_for, redirect, flash
from app import app
from app import alquimias
from flask_login import (
    current_user,
    login_user,
    logout_user,
    login_required
)


# Rota Principal (index)
@app.route('/', methods=['GET', 'POST'])
@login_required 
def index():
    if request.method == 'POST':
        post_body = request.form['post_body']
        alquimias.create_post(post_body, current_user.id)
        flash('Post criado com sucesso!')
        return redirect(url_for('index')) 

    user = current_user if current_user.is_authenticated else None
    posts = alquimias.get_recent_posts()

    return render_template('index.html', user=user, posts=posts) 


# Rota de Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = request.form['username'].lower()
        password = request.form['password'].lower()

        user = alquimias.validate_user_password(username, password)

        if user:
            remember_me = request.form.get('remember_me') == 'on' 
            login_user(user, remember=remember_me)
            flash('Login bem sucedido!')
            return redirect(url_for('index'))
        else:
            flash('Usuário ou senha inválidos')
            return redirect(url_for('login'))
        
    return render_template('login.html')

# Rota GET: Exibe o formulário de cadastro
@app.route('/cadastro', methods=['GET'])
def show_cadastro_form():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    return render_template('cadastro.html')

# Rota POST: Processa os dados do formulário de cadastro
@app.route('/cadastro', methods=['POST'])
def cadastro():
    username = request.form['username'].lower()

    if alquimias.user_exists(username):
        flash('Usuário já existe!')
        return redirect(url_for('show_cadastro_form')) 
    else:
        password = request.form['password'].lower()
        remember = True if request.form.get('remember') == 'on' else False
        
        photo_url = request.form.get('photo_url') 
        bio = request.form.get('bio')
        
        user = alquimias.create_user(username, password, remember, photo_url=photo_url, bio=bio)
        
        login_user(user, remember=remember)
        flash('Cadastro realizado com sucesso!')
        
        return redirect(url_for('index'))

# Rota de Logout
@app.route('/logout')
def logout():
    logout_user()
    flash('Você foi desconectado.')
    return redirect(url_for('login'))


# Rota de Edição: GET para mostrar o formulário, POST para salvar
@app.route('/post/edit/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = alquimias.get_post_by_id(post_id)

    if post is None:
        flash('Post não encontrado.')
        return redirect(url_for('index'))
    
    if post.author.id != current_user.id:
        flash('Você não tem permissão para editar este post.')
        return redirect(url_for('index'))

    if request.method == 'POST':
        new_body = request.form['post_body']
        if new_body:
            alquimias.update_post_body(post, new_body)
            flash('Post atualizado com sucesso!')
            return redirect(url_for('index'))
        else:
            flash('O corpo do post não pode ser vazio.')

    return render_template('edit_post.html', post=post)


# Rota de Exclusão
@app.route('/post/delete/<int:post_id>', methods=['POST'])
@login_required
def delete_post_route(post_id):
    post = alquimias.get_post_by_id(post_id)

    if post is None:
        flash('Post não encontrado.')
        return redirect(url_for('index'))
    
    if post.author.id != current_user.id:
        flash('Você não tem permissão para excluir este post.')
        return redirect(url_for('index'))

    alquimias.delete_post(post)
    flash('Post excluído com sucesso!')
    return redirect(url_for('index'))

