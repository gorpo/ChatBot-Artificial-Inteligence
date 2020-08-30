# -*- coding: utf-8 -*-
# ███╗   ███╗ █████╗ ███╗   ██╗██╗ ██████╗ ██████╗ ███╗   ███╗██╗ ██████╗
# ████╗ ████║██╔══██╗████╗  ██║██║██╔════╝██╔═══██╗████╗ ████║██║██╔═══██╗
# ██╔████╔██║███████║██╔██╗ ██║██║██║     ██║   ██║██╔████╔██║██║██║   ██║
# ██║╚██╔╝██║██╔══██║██║╚██╗██║██║██║     ██║   ██║██║╚██╔╝██║██║██║   ██║
# ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║╚██████╗╚██████╔╝██║ ╚═╝ ██║██║╚██████╔╝
# ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝
#     [+] @GorpoOrko 2020 - Telegram Bot and Personal Assistant [+]
#     |   TCXS Project Hacker Team - https://tcxsproject.com.br   |
#     |   Telegram: @GorpoOrko Mail:gorpoorko@protonmail.com      |
#     [+]        Github Gorpo Dev: https://github.com/gorpo     [+]

from app import app, extensoes
import os
from werkzeug.utils import secure_filename
from flask import flash, request, redirect, url_for, render_template
from app.deepnude_files import deepfake
import subprocess


def verificaArquivo(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in extensoes


imagens = []


@app.route('/', methods=['POST'])
def uploadImagem():
    if 'file' not in request.files:
        # ativação do deepnude pelo append do caminho da Imagem
        if request.method == 'POST':
            if request.form.get('Encrypt') == 'Encrypt':
                caminho = f"app/static/uploads/{imagens[0]}"
                caminho_saida = f"app/static/uploads/render_{imagens[0]}"
                deepfake.main(caminho, caminho_saida)
                return render_template('index.html', filename=f"render_{imagens[0]}")
    # faz upload das imagens
    file = request.files['file']
    if file.filename == '':
        flash('Nehuma imagem para upload')
        return redirect(request.url)
        pass
    if file and verificaArquivo(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # print('upload_image filename: ' + filename)
        flash('Imagem upada com sucesso')
        imagens.append(filename)
        return render_template('index.html', filename=filename)
    else:
        flash('Somente são aceitos formatos -> png, jpg, jpeg, gif')
        return redirect(request.url)


# exibe a imagem ---------------->
@app.route('/display/<filename>')
def exibeImagem(filename):
    # print('imagem: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)
