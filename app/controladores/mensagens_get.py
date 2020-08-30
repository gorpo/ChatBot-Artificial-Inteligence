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
from flask import request

#imports da inteligência
from app.chatterbot_files.chatbot_trainer import chatbot
from app.plugins.gifs import gifInternet
from app.plugins import corrige_palavras
from app.plugins import wiki_ia


#funções de resposta com texto do bot com base nos plugins
@app.route("/get")
def get_user_response():
    msg = request.args.get('msg')

    if msg == 'oi':
        return 'oi'

    if 'fale sobre' in msg.lower():
        return wiki_ia.faleSobre(msg)

    if msg.split()[0] == 'corrigir':
        return corrige_palavras.corrigirPalavras(msg)

    if msg == 'internet':
        return gifInternet()

    else:
        return str(chatbot.get_response(msg))


