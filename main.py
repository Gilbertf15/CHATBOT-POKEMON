
import customtkinter as ctk
from interface.interface_bot import MainProject, InterfaceBot 

if __name__ == '__main__':
    class Main:
        """MÉTOD MAIN DO PROJETO
        """

        # chamando o método estárico de treinamento do bot passando os arquivos json no argumnento
        MainProject.main_training('./training/training_bot.json')
        MainProject.main_training('./training/training_characters.json')
        MainProject.main_training('./training/training_gym.json')
        MainProject.main_training('./training/training_pokemon_dragon.json')
        MainProject.main_training('./training/training_pokemon_earth.json')
        
        # Instânciando a interface
        loop = ctk.CTk()
        mainloop1 = InterfaceBot(loop)
        loop.mainloop()
   
   