from bot.bot import ChatBotPokemon
from bot.training import Training
import customtkinter as ctk


class MainProject:
        """_summary_ """
        global var_bot_pokemon
        var_bot_pokemon = ChatBotPokemon()
        
        @staticmethod
        def main_training(param_arq_training:str) -> str | None:
            """_summary_

            Args:
                param_arq_training (str): _description_

            Returns:
                str | None: _description_
            """
            try:
                Training.training_bot(var_bot_pokemon, param_arq_training)
                
            except:
                return 'error main_training'

        @staticmethod
        def main_bot(view, label_view:ctk.CTkLabel) -> str | None:
            """_summary_

            Args:
                view (_type_): _description_
                label_view (ctk.CTkLabel): _description_

            Returns:
                str | None: _description_


            """
           
            try:
                response = var_bot_pokemon.get_response(view)
                if response:
                    label_view.configure(text=f'🤖: {response}')

                else:
                     "error response"
                
             
            except:
                return 'error main_bot'
