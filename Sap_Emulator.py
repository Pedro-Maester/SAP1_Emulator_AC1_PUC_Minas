
import Sap_GUI
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
'''class Janela:
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

pyinstaller Sap_Emulator.py --icon=computer.ico --onefile --windowed 

    #area do SAP
    #area dos codigos

    def win_loop(self):
        self.root.mainloop()
'''
def teste()->bool:
    return False
if __name__ == "__main__":

    #i:Sap_GUI.Ins = Sap_GUI.Ins("teste",2.3,1.8,0.5,0.5,(1,2,3),(0,9,8),teste)
    #print(i.fun_ativa())
    Sap_GUI.Janela().win_loop()
    '''sap = ctypes.CDLL("dlls/SAP.dll")
    sap.Create_SAP()
    bo = ctypes.c_bool(sap.get_working_clock_SAP())
    print(bo.value)
    i = 0

    python_string = "e".encode("utf-8").hex()
    print(python_string)
    sap.update_ram_SAP.argtypes = [ctypes.c_ubyte, ctypes.c_ubyte]
    sap.update_ram_SAP.restype = None
    sap.get_ram_at.argtypes =[ctypes.c_ubyte]
    sap.get_ram_at.restype = ctypes.c_ubyte



    sap.update_ram_SAP(i,int("f",16))
    sap.start_SAP()
    print(hex(sap.get_ram_at(i)))


    #sap = mydll.Sap_Logic()
    #print(sap.get_clock_working())
    janela = Janela()
    b =Basicos("oi",teste,(2,1,1),(0,2,2))
    print(b.ativo())
    janela.win_loop()'''













