from chatterbot import ChatBot

chatbot = ChatBot('Marcinho',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',

    database_uri='sqlite:///database.sqlite3'
)

# Treinando perguntas padrao com documento de pergunta/resposta
from chatterbot.trainers import ListTrainer
trainer = ListTrainer(chatbot)
perguntas_respostas = open('training_data/perguntas_respostas.txt').read().splitlines()
questoes_covid = open('training_data/questoes_covid.txt').read().splitlines()
training_data = questoes_covid + perguntas_respostas
trainer.train(training_data)

# Training com Corpus
from chatterbot.trainers import ChatterBotCorpusTrainer
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.Portuguese")
trainer.train('corpus_portugues/tcxs.yml',)
trainer.train('corpus_portugues/compliment.yml',)
trainer.train('corpus_portugues/conversations.yml')
trainer.train('corpus_portugues/games.yml',)
trainer.train('corpus_portugues/greetings.yml')
trainer.train('corpus_portugues/linguistic_knowledge.yml',)
trainer.train('corpus_portugues/money.yml')
trainer.train('corpus_portugues/proverbs.yml',)
trainer.train('corpus_portugues/suggestions.yml')
trainer.train('corpus_portugues/trivia.yml',)
trainer.train('corpus_portugues/unilab.yml')
