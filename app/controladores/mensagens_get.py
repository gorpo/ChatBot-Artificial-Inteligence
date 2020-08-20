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

from app import app
import os
from app.chatterbot_files.chatbot_trainer import chatbot
import wikipedia
from spellchecker import SpellChecker
from flask import flash, request, redirect, url_for, render_template


def faleSobre(msg):
    termo = msg[10:]
    wikipedia.set_lang("pt")
    pesquisa = wikipedia.summary(termo)
    return pesquisa

def corrigirPalavras(msg):
    spell = SpellChecker(language='pt')
    mensagem = msg
    misspelled = spell.unknown(mensagem.split())
    palavra_errada = list(misspelled)[0]  # retorna a palavra que estava errada na frase
    for palavra_final in misspelled:
        corrigir = spell.correction(palavra_final)
        candidatos = spell.candidates(palavra_final)
        mensagem_corrigida = mensagem.replace(palavra_errada, corrigir).replace('corrigir', '')
    return  mensagem_corrigida

app.config['a'] = os.path.join('static', 'images')
@app.route('/')
@app.route('/index')
def show_index():
    full_filename = os.path.join(app.config['a'], 'gorpo.jpg')
    return render_template("envioImagemBot.html", user_image = full_filename)





@app.route("/get")
def get_user_response():
    msg = request.args.get('msg')
    if msg == 'oi':
        return 'oi'
    if 'fale sobre' in msg.lower():
        return faleSobre(msg)
    if msg.split()[0] == 'corrigir':
        return corrigirPalavras(msg)
    if msg == 'teste':

        return show_index()


    else:
        return str(chatbot.get_response(msg))