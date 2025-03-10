from spacy.cli import download
from chatterbot import ChatBot

class ENGSM:
    ISO_639_1 = 'en_core_web_sm'

class ChatBotPokemon(ChatBot):
    """_summary_

    Args:
        ChatBot (_type_): _description_
    """
    def __init__(self):
        """_summary_
        """
        super().__init__("Bot Pokemon",
                            #logic_adapters=[
                            #       "chatterbot.logic.BestMatch"
                            #],
                            #statement_comparison_function="levenshtein_distance",
                            preprocessors=[
                                'chatterbot.preprocessors.clean_whitespace'
                            ],
                            tagger_language=ENGSM,
                            
                            read_only=False
                            )
        

