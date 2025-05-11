import json
from .bot import ChatBotPokemon
from chatterbot.trainers import ListTrainer
from typing import Type

class Training:
    """ CLASSE DE TREINAMENTO DO CHATBOT
    """
    @staticmethod
    def training_bot(param_bot:Type[ChatBotPokemon], param_training) -> None:
        """ MÉTODO ESTÁTICO  DE TREINAMENTO DO CHATBOT

        Args:
            param_bot (Type[ChatBotPokemon]): Espera como argumento uma instância da clase ChatBotPokemon
            
            param_training (String): Espera como argumento o caminho do arquivo de treinamneto no formato json
        """
        with open(param_training, 'r', encoding='utf-8') as t:
            dados_bot = json.load(t)

        training = []
        for i in dados_bot['conversas_bot']:
            training.append(i['pergunta'])
            training.append(i['resposta'])
            


        trainer = ListTrainer(param_bot)
        trainer.train(training)




