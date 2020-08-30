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


import os
import subprocess

def interpretadorPython(msg):
    with open("test2", "w") as f:
        codigo = str(msg).replace('python ','')
        f.write(codigo)

    (readend, writeend) = os.pipe()

    p = subprocess.Popen(['python', '-u', 'test2'], stdout=writeend, bufsize=0)
    still_open = True
    output = ""
    output_buf = os.read(readend, 100).decode()
    print(output_buf)

    while output_buf:
        print(output_buf)  #,end=""
        output += output_buf
        if still_open and p.poll() is not None:
            os.close(writeend)
            still_open = False
        output_buf = os.read(readend, 1).decode()
        if p.poll() is None:
            break
    print(output)
    return output

