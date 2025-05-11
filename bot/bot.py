from spacy.cli import download
from chatterbot import ChatBot

class ENGSM:
    ISO_639_1 = 'en_core_web_sm'

class ChatBotPokemon(ChatBot):
    """CLASSE DE CRIÇÃO DO CHATBOT
    """
    def __init__(self):
        """MÉTODO CONSTRUTOR DO CHATBOT
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
        

