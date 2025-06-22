import tkinter
import os
import configparser

class Basicos:
    def __init__(self, nome: str, ativo:bool , cor_ativa:tuple[3],cor_desativa:tuple[3]):
        self.nome:str = str(nome)
        self.ativo:bool = ativo
        self.cor_ativa:tuple[3] =cor_ativa
        self.cor_desativa: tuple[3] = cor_desativa
        self.pos_x:float
        self.pos_y:float
        self.val:hex
        self.valb:bin 


class Linha(Basicos):
    def __init__(self,nome: str,ativo:bool):

#
        pass

class Caixa:
    def __init__(self,nome: str):
        self.nome:str = str(nome)
        self.ligado:bool = False

        pass
class Ediqueta:
    def __init__(self):
        self.nome:str = str()

        pass
class Janela:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.wm_title("SAP Emulator")
        self.config = configparser.ConfigParser()
        if not os.path.exists("config.ini"):
            self.config["DEFAULT"] = {'width': str(self.root.winfo_screenwidth()),
                                 'height': str(self.root.winfo_screenheight()),
                                 'fullscreen': 'no',
                                 'darkmode': 'no'
                                 }
            with open("config.ini", 'w') as cf:
                self.config.write(cf)
        else:
            self.config.read("config.ini")

        if (self.config["DEFAULT"]["fullscreen"] != 'no'):
            self.root.attributes("-fullscreen", True)
        else:
            self.root.geometry(self.config["DEFAULT"]["width"] + 'x' + self.config["DEFAULT"]["height"])

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        self.config["DEFAULT"]["width"] = str(self.root.winfo_width())
        self.config["DEFAULT"]["height"] = str(self.root.winfo_height())
        with open("config.ini", 'w') as cf:
            self.config.write(cf)
        self.root.destroy()
        return None

    def change_fullscreen(self):
        if (self.config["DEFAULT"]["fullscreen"] == 'no'):
            self.config["DEFAULT"]["fullscreen"] = 'no'
            self.root.attributes("-fullscreen", False)
        else:
            self.config["DEFAULT"]["fullscreen"] = 'yes'
            self.root.attributes("-fullscreen", True)

    def change_darkmode(self):
        if(self.config["DEFAULT"]["darkmode"] == 'no'):
            self.config["DEFAULT"]["darkmode"] = 'yes'
        else:
            self.config["DEFAULT"]["darkmode"] = 'no'


    #area do SAP
    #area dos codigos

    def win_loop(self):
        self.root.mainloop()

def teste()->bool:
    return False
if __name__ == "__main__":
    janela = Janela()
    b =Basicos("oi",teste,(2,1,1),(0,2,2))
    print(b.ativo())
    janela.win_loop()













