import customtkinter as ctk 

from training.MainTraining import MainProject
from PIL import Image

class InterfaceBot:
    """CLASSE DA INTERFACE GRAFICA
    """
    
    def __init__(self, loop):
        """MÉTODO CONTRUTOR DA INTERFACE GRAFICA

        Args:
            loop (ctk.CTk): espera uma instância do tipo ctk.CTk()
        """
        self.loop = loop
        self.loop.geometry('1000x1000')
        self.loop.title('Chat Bot')
        self.loop.resizable(False, False)
        ctk.set_appearance_mode('dark')

        self.bg_title = ctk.CTkImage(Image.open("./static/img/logo_pokemon.png"), size=(300,200))
        self.label_bg_title = ctk.CTkLabel(self.loop, text='', image=self.bg_title)
        self.label_bg_title.pack()

        self.bg_ash = ctk.CTkImage(Image.open("./static/img/ash.png"), size=(150,150))
        self.label_img_ash = ctk.CTkLabel(self.loop, text='', image=self.bg_ash)
        self.label_img_ash.place(x=800, y=400)

        self.img_butterfly = ctk.CTkImage(Image.open("./static/img/butterfly.png"), size=(80,80))
        self.label_img_butterfly = ctk.CTkLabel(self.loop, text='', image=self.img_butterfly)
        self.label_img_butterfly.place(x=800, y=50)

        self.img_eletrico = ctk.CTkImage(Image.open("./static/img/tipo_eletrico.png"), size=(150,150))
        self.label_img_eletrico = ctk.CTkLabel(self.loop, text='', image=self.img_eletrico)
        self.label_img_eletrico.place(x=50, y=50)

        self.img_pokemons = ctk.CTkImage(Image.open("./static/img/tipo_planta.png"), size=(100,100))
        self.label_img_pokemons = ctk.CTkLabel(self.loop, text='', image=self.img_pokemons)
        self.label_img_pokemons.place(x=70, y=470)
        
        self.input_var = ctk.CTkEntry(self.loop, placeholder_text='comece uma conversa', width=400, fg_color='black', font=('Times New Roman', 12))
        self.input_var.place(x=300, y=170)
        
        self.label_response = ctk.CTkLabel(loop, text=f' ', wraplength=400,  font=('Times New Roman', 18))
        self.label_response.place(x=300, y=350)
    
        self.botton = ctk.CTkButton(loop, text='ENVIAR', border_width=2, border_spacing=2, font=('Arial', 10),command=lambda:  MainProject.main_bot(self.return_entry(), self.label_response))
        self.botton.place(x=350, y=230)

        self.botton_clear = ctk.CTkButton(loop, text='LIMPAR', border_width=2, border_spacing=2, font=('Arial', 10), command=lambda: InterfaceBot.delete_result(self.label_response))
        self.botton_clear.place(x=500, y=230)
       
    @staticmethod
    def delete_result(entry:ctk.CTkLabel) -> str:
        """MÉTODO PARA DELETAR O VALOR TEXT DO CTKLABEL

        Args:
            entry (ctk.CTkLabel): espera uma instância do tipo  ctk.CTkLabel

        Returns:
            str : retorna o valor do atributo text da Label deletado ou um except error
        """
        try: 
            bot = entry.configure(text='')
            return bot
            
        except:
            return 'error ao deletar'
         
    def return_entry(self) -> str :
        """MÉTODO PARA PEGAR O VALOR DO CTKENTRY

        Returns:
            str: retorna o valor de CTKENTRY em string
        """
        
        response =  str(self.input_var.get())
        print(response)
        return response
   


