
from spellchecker import SpellChecker

spell = SpellChecker(language='pt')
mensagem = 'corrigir hogme'
misspelled = spell.unknown(mensagem.split())
palavra_errada = list(misspelled)[0]  # retorna a palavra que estava errada na frase
for palavra_final in misspelled:
    corrigir = spell.correction(palavra_final)
    candidatos = spell.candidates(palavra_final)
    mensagem_corrigida = mensagem.replace(palavra_errada,corrigir).replace('corrigir','')
    print(mensagem_corrigida)