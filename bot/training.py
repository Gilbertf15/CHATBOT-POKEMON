import json
from .bot import ChatBotPokemon
from chatterbot.trainers import ListTrainer
from typing import Type

class Training:
    """_summary_
    """
    @staticmethod
    def training_bot(param_bot:Type[ChatBotPokemon], param_training) -> None:
        """_summary_

        Args:
            param_bot (Type[ChatBotPokemon]): _description_
            param_training (_type_): _description_
        """
        with open(param_training, 'r', encoding='utf-8') as t:
            dados_bot = json.load(t)

        training = []
        for i in dados_bot['conversas_bot']:
            training.append(i['pergunta'])
            training.append(i['resposta'])
            


        trainer = ListTrainer(param_bot)
        trainer.train(training)




