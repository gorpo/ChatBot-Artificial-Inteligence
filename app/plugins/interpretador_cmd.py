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

import subprocess
import os

def interpretadorCMD(msg):
    comando = msg.replace('cmd','')
    proc = subprocess.Popen(comando, shell=True,  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()

    f =  open('foo.txt', 'a')
    f.write(str(stdout.decode('Windows-1252')))
    f.close()

    r = open('foo.txt','r').readlines()

    todas = []
    separador = ' '
    for line in r:
        line1 = line.replace('   ','')
        if line1 == '\n':
            pass
        else:
            todas.append(line1)
    os.remove('foo.txt')

    retorno = separador.join(map(str, todas))
    print(retorno)
    return f'{retorno}'