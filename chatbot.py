from chatterbot import ChatBot
import time
time.clock=time.time

chatbot = ChatBot(
    'CoronaBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning. For more details on NUSET visit <a href "https://setnu.in/">here</a>',
            'maximum_similarity_threshold': 0.90
        },
        # {
        #     'import_path': 'chatterbot.logic.TimeLogicAdapter',
        #     'default_response': 'I am sorry, but I do not understand. I am still learning.',
        #     'maximum_similarity_threshold': 0.10
        # }
    ],
    database_uri='sqlite:///database.sqlite3'
)


# Training With Own Questions 
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(chatbot)

training_data_quesans = open('training_data/ques_ans.txt').read().splitlines()
training_data_personal = open('training_data/personal_ques.txt').read().splitlines()

training_data = training_data_quesans + training_data_personal

trainer.train(training_data)
#trainer.export_for_training('./my_ex.json')
# Training With Corpus 
# from chatterbot.trainers import ChatterBotCorpusTrainer

# trainer_corpus = ChatterBotCorpusTrainer(chatbot)
# trainer_corpus.train(
#     'chatterbot.corpus.english'
#  )
 #trainer.export_for_training('./my_export.json')