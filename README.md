
[![Build](https://img.shields.io/badge/dev-gorpo-brightgreen.svg)]()
[![Stage](https://img.shields.io/badge/Release-Stable-brightgreen.svg)]()
[![Build](https://img.shields.io/badge/python-v3.7-blue.svg)]()
[![Build](https://img.shields.io/badge/windows-7%208%2010-blue.svg)]()
[![Build](https://img.shields.io/badge/arquiterura-64bits-blue.svg)]()<br>
  <h6 align="center">
   <img src="https://raw.githubusercontent.com/gorpo/Manicomio-Boot-Theme/master/manicomio/boot.png" width="55%"></img>
       <h2 align="center">Manicomio | Python Chatterbot Flask | Corpus Português | versao02</h2>
  </h6>
<h3> Chatbot em Python com uso das Libs Chatterbot e Flask e integração de treinamento Corpus</h3><br>
<img src="https://github.com/gorpo/Manicomio-Chatterbot-Python/blob/master/static/exemplo.png" width="100%"></img>

<p>Chatbot desenvolvido em python com auxilio das bibliotecas --chatterbot e --flask, este chatbot faz a leitura e treinamento com arquivos Corpus, os quais ja temos alguns --corpus inseridos nele e outros podem ser colocados para treinar melhor nosso chatbot.</p>

# Requisitos:
-Python3+<br>
-Flask<br>
-Chatterbot<br>
-Chatterbot Corpus<br>

# Instalação das libs:
- Chatterbot:
<code>pip install chatterbot</code>
- Chatterbot:
<code>pip install chatterbot-corpus</code>
- Flask:
<code>pip install flask</code>

# Sobre o Corpus:
<p>Corpus linguístico é o conjunto de textos escritos e registros orais em uma determinada língua e que serve como base de análise. O estudo de corpora (plural de corpus) apresenta muitas vantagens. Em vez de consultar nossas intuições, ou de ‘extrair’ informações dos falantes, penosamente, uma a uma, podemos examinar um vasto material que foi produzido espontaneamente na fala ou na escrita das pessoas, e portanto podemos fazer observações precisas sobre o real comportamento linguístico de gente real. Portanto os corpora podem nos proporcionar informações altamente confiáveis e isentas de opiniões e de julgamentos prévios, sobre os fatos de uma língua. O uso de corpora está associado à linguística de corpus. Este script ja vem com alguns Corpus em portugues, corpus de outras linguas podem ser inseridos bem como novos corpus criados. </p>

# Como rodar:
<p>Supomos que ja tenha o python3 ou superior, neste script usei o python3.7, apenas digite o comando <code>python3 manicomio.py</code> e o bot irá antes ler todos os corpus, após isto um endereço será fornecido, este é o endereço de seu bot rodando, caso queira alterar o endereço, na ultima linha identifique o IP e Porta que deseja rodar, por padrao este script roda no endereço http://127.0.0.1:5000</p>
<code>python3 manicomio.py</code><br>

<img src="https://github.com/gorpo/Manicomio-Chatterbot-Python/blob/master/static/run.gif" width="60%"></img>

# Correção de problemas:
<p>A Bibioteca YAML foi atualizada mas o chatterbot não!!! Possivelmente você verá este erro:<br>
<code>C:\Users\user\AppData\Local\Programs\Python\Python37\lib\site-packages\chatterbot\corpus.py:38: YAMLLoadWarning: calling yaml.load() without Loader=... is deprecated, as the default Loader is unsafe. Please read https://msg.pyyaml.org/load for full details.
  return yaml.load(data_file)</code><br>
  Para corrigir este erro basta ir no caminho e arquivo especificado e apos abrir o arquivo corpus.py procure pela linha 38, e altere de<br> <code>return yaml.load(data_file)</code><br> para<br> <code>return yaml.load(data_file,Loader=yaml.FullLoader)</code> <br>Bastando apenas acrescentar o parametro <b>Loader=yaml.FullLoader</b> após de data_file.  </p>
  
 # Referências e link's uteis:
 - Chatterbot: https://chatterbot.readthedocs.io/en/stable/index.html
 - Chatterbot Git: https://github.com/anikethsukhtankar/ChatterBot/blob/master/readme.pt.md
 - Chatterbot Corpus: https://github.com/gunthercox/chatterbot-corpus
 - Corpus, oque é: https://pt.wikipedia.org/wiki/Corpus_lingu%C3%ADstico
 - Flask: https://flask.palletsprojects.com/en/1.1.x/
 
 # Contato:
 - Mail: gorpoorko@protonmail.com
 - Telegram: https://t.me/tcxsproject2
 - Youtube: https://www.youtube.com/user/daimonae
 
