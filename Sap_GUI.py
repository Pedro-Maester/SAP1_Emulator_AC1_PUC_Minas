
import tkinter
import os
import configparser
import ctypes

#lda ok
#add ok
#sub ok
#inc ok
#dec ok
#inp x
# jmp ok
# sto ok
# out x
# hlt ok

fundo: str = "gray"
def fun_holder()->bool:
    return True
class SAP:
    def __init__(self):
        self.dll = ctypes.CDLL("dlls/SAP.dll")

    def get_working_clock(self):
        return  self.dll.get_working_clock()
    def get_ram_tam(self):
        return self.dll.get_ram_tam()

    def get_ram_at(self, i:int):
        return hex(self.dll.get_ram_at(i))
    def get_CP_data(self):
        return hex(self.dll.get_CP_data())
    def get_I_data(self):
        return hex(self.dll.get_I_data())

    def get_O_data(self):
        return hex(self.dll.get_O_data())

    def get_A_data(self):
        return hex(self.dll.get_A_data())

    def get_B_data(self):
        return hex(self.dll.get_B_data())

    def get_ula_data(self):
        return hex(self.dll.get_ula_data())

    def get_ri_data(self):
        return hex(self.dll.get_ri_data())

    def get_rem_data(self):
        return hex(self.dll.get_rem_data())

    def get_ram_at_ptr(self):
        return hex(self.dll.get_ram_at_ptr())
    def get_rom_ins_at_ptr(self):
        return hex(self.dll.get_rom_ins_adress_at_ptr())

    def get_instruction(self):
        return bin(self.dll.get_instruction())


    def get_activated_Cp(self):
        return bool(self.dll.get_activated_Cp())

    def get_activated_Ep(self):
        return bool(self.dll.get_activated_Ep())

    def  get_activated_nLm(self):
        return bool(self.dll. get_activated_nLm())

    def  get_activated_nCE(self):
        return bool(self.dll. get_activated_nCE())

    def get_activated_nLi(self):
        return bool(self.dll.get_activated_nLi())

    def get_activated_nEi(self):
        return bool(self.dll.get_activated_nEi())

    def get_activated_nLa(self):
        return bool(self.dll.get_activated_nLa())

    def get_activated_Ea(self):
        return bool(self.dll.get_activated_Ea())

    def get_activated_Su(self):
        return bool(self.dll.get_activated_Su())

    def get_activated_Eu(self):
        return bool(self.dll.get_activated_Eu())


    def get_activated_nLb(self):
        return bool(self.dll.get_activated_nLb())

    def get_activated_nLo(self):
        return bool(self.dll.get_activated_nLo())

    def get_activated_IncDec(self):
        return bool(self.dll.get_activated_IncDec())

    def get_activated_RDnWR(self):
        return bool(self.dll.get_activated_RDnWR())

    def get_activated_Ein(self):
        return bool(self.dll.get_activated_Ein())

    def get_activated_Lp(self):
        return bool(self.dll.get_activated_Lp())

    def clk(self):
        self.dll.clk()

    def start(self):
        self.dll.start()

    def stop(self):
        self.dll.stop()

    def clear(self):
        self.dll.clear()

    def set_input_data(self,data:int):
        self.dll.set_input_data(data)

    def update_ram(self,i:int,data:int):

        self.dll.update_ram(ctypes.c_ubyte(i),ctypes.c_ubyte(data))
        print(data)

    def get_clock_ativo(self):
        return


class Selecter:
    def __init__(self,root,sap:SAP):
        self.selecter:int = 0
        self.sap:SAP = sap
        self.buttons:list[tkinter.Button] = list()
        self.ram_vars: list[tkinter.StringVar] = list()
        for r in range(16):
            self.ram_vars.append(tkinter.StringVar(root))
            self.ram_vars[r].set(sap.get_ram_at(r))


        self.buttons.append(tkinter.Button(root,background="black",fg="white",textvariable=self.ram_vars[0], command= self.val_0))
        self.buttons.append(tkinter.Button(root,background="white",fg="black", textvariable=self.ram_vars[1], command=self.val_1))
        self.buttons.append(tkinter.Button(root,background="white",fg="black", textvariable=self.ram_vars[2], command=self.val_2))
        self.buttons.append(tkinter.Button(root,background="white",fg="black", textvariable=self.ram_vars[3], command=self.val_3))
        self.buttons.append(tkinter.Button(root,background="white",fg="black", textvariable=self.ram_vars[4], command=self.val_4))
        self.buttons.append(tkinter.Button(root,background="white",fg="black", textvariable=self.ram_vars[5], command=self.val_5))
        self.buttons.append(tkinter.Button(root,background="white",fg="black", textvariable=self.ram_vars[6], command=self.val_6))
        self.buttons.append(tkinter.Button(root,background="white",fg="black", textvariable=self.ram_vars[7], command=self.val_7))
        self.buttons.append(tkinter.Button(root,background="white",fg="black", textvariable=self.ram_vars[8], command=self.val_8))
        self.buttons.append(tkinter.Button(root,background="white",fg="black", textvariable=self.ram_vars[9], command=self.val_9))
        self.buttons.append(tkinter.Button(root,background="white",fg="black", textvariable=self.ram_vars[10], command=self.val_a))
        self.buttons.append(tkinter.Button(root, background="white",fg="black",textvariable=self.ram_vars[11], command=self.val_b))
        self.buttons.append(tkinter.Button(root, background="white",fg="black",textvariable=self.ram_vars[12], command=self.val_c))
        self.buttons.append(tkinter.Button(root,background="white",fg="black", textvariable=self.ram_vars[13], command=self.val_d))
        self.buttons.append(tkinter.Button(root,background="white",fg="black", textvariable=self.ram_vars[14], command=self.val_e))
        self.buttons.append(tkinter.Button(root,background="white",fg="black", textvariable=self.ram_vars[15], command=self.val_f))

        for b in range(len(self.buttons)):
            self.buttons[b].grid(row= int(b/4),column=b%4)


    def update(self):

        self.buttons[self.selecter].config(bg="black",fg="white")

    def update_ram(self):

        for r in range(16):
            self.ram_vars[r].set(self.sap.get_ram_at(r))



    def normal(self):
        self.buttons[self.selecter].config(bg="white",fg="black")
    def val_0(self):
        self.normal()
        self.selecter = 0
        self.update()

    def val_1(self):
        self.normal()
        self.selecter = 1
        self.update()

    def val_2(self):
        self.normal()
        self.selecter = 2
        self.update()

    def val_3(self):
        self.normal()
        self.selecter =3
        self.update()

    def val_4(self):
        self.normal()
        self.selecter =4
        self.update()

    def val_5(self):
        self.normal()
        self.selecter =5
        self.update()

    def val_6(self):
        self.normal()
        self.selecter =6
        self.update()

    def val_7(self):
        self.normal()
        self.selecter =7
        self.update()

    def val_8(self):
        self.normal()
        self.selecter =8
        self.update()

    def val_9(self):
        self.normal()
        self.selecter=9
        self.update()

    def val_a(self):
        self.normal()
        self.selecter =10
        self.update()

    def val_b(self):
        self.normal()
        self.selecter =11
        self.update()

    def val_c(self):
        self.normal()
        self.selecter =12
        self.update()

    def val_d(self):
        self.normal()
        self.selecter =13
        self.update()

    def val_e(self):
        self.normal()
        self.selecter =14
        self.update()

    def val_f(self):
        self.normal()
        self.selecter =15
        self.update()


class Inputer:
    def __init__(self,root):
        self.input_str:str = ""
        self.inputer_var:tkinter.StringVar = tkinter.StringVar(root)
    def update(self):
        self.inputer_var.set(self.input_str)
    def remover(self):
        if len(self.input_str) >1:
            self.input_str = self.input_str[:1]
        self.update()
    def remove(self):
        if len(self.input_str) >1:
            self.input_str = self.input_str[1:]
        self.update()
    def val_0(self):
        self.input_str +='0'
        self.update()
        if len(self.input_str) >2:
            self.remove()

    def val_1(self):
        self.input_str +='1'
        self.update()
        if len(self.input_str) >2:
            self.remove()
    def val_2(self):
        self.input_str +='2'
        self.update()
        if len(self.input_str) >2:
            self.remove()
    def val_3(self):
        self.input_str +='3'
        self.update()
        if len(self.input_str) >2:
            self.remove()
    def val_4(self):
        self.input_str +='4'
        self.update()
        if len(self.input_str) >2:
            self.remove()
    def val_5(self):
        self.input_str +='5'
        self.update()
        if len(self.input_str) >2:
            self.remove()
    def val_6(self):
        self.input_str +='6'
        self.update()
        if len(self.input_str) >2:
            self.remove()
    def val_7(self):
        self.input_str +='7'
        self.update()
        if len(self.input_str) >2:
            self.remove()
    def val_8(self):
        self.input_str +='8'
        self.update()
        if len(self.input_str) >2:
            self.remove()
    def val_9(self):
        self.input_str +='9'
        self.update()
        if len(self.input_str) >2:
            self.remove()
    def val_a(self):
        self.input_str +='a'
        self.update()
        if len(self.input_str) >2:
            self.remove()
    def val_b(self):
        self.input_str +='b'
        self.update()
        if len(self.input_str) >2:
            self.remove()
    def val_c(self):
        self.input_str +='c'
        self.update()
        if len(self.input_str) >2:
            self.remove()
    def val_d(self):
        self.input_str +='d'
        self.update()
        if len(self.input_str) >2:
            self.remove()
    def val_e(self):
        self.input_str +='e'
        self.update()
        if len(self.input_str) >2:
            self.remove()
    def val_f(self):
        self.input_str +='f'
        self.update()
        if len(self.input_str) >2:
            self.remove()


class Janela:

    def __init__(self):


        self.root = tkinter.Tk()
        self.root.wm_title("SAP Emulator")
        self.outra: tkinter.Toplevel = None
        self.config = configparser.ConfigParser()
        self.sap = SAP()
        self.sap.dll.Create_SAP()
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

        if (self.config["DEFAULT"]["fullscreen"] == "yes"):
            self.root.attributes("-fullscreen", True)
        else:
            self.root.geometry(self.config["DEFAULT"]["width"] + 'x' + self.config["DEFAULT"]["height"])
        if(self.config["DEFAULT"]["darkmode"]=='no'):
            fundo = "lightgray"
        else:
            fundo = "gray"

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.menu = tkinter.Menu(self.root)
        self.menu.add_command(label='Fullscreen',command=self.change_fullscreen)

        #self.menu.add_command(label='Dark Mode', command=self.change_darkmode)
        self.menu.add_command(label='CLK', command=self.Clocar)

        self.menu.add_command(label='START', command=self.Start)
        self.menu.add_command(label='Input',command=self.inputar)
        self.menu.add_command(label='RAM',command=self.change_ram)

        #self.menu.add_command(label='Ram')
        self.menu.add_separator()
        self.menu.add_command(label="Exit", command=self.on_closing)

        self.menu.add_command(label='CLEAR', command=self.clear)
        #self.file_menu = tkinter.Menu(self.menu,tearoff=0)

        #self.file_menu.add_command(label='Fullscreen',command=self.change_fullscreen)
        #self.file_menu.add_command(label='Dark Mode',command=self.change_darkmode)

        #self.file_menu.add_separator()

        #self.file_menu.add_command(label="Exit",command = self.on_closing)
        #self.menu.add_cascade(label='file',menu = self.file_menu)


        self.root.config(menu=self.menu)
        self.menu.entryconfig("CLK", state="disabled")
        self.esq = tkinter.Frame(self.root,background=fundo)
        self.dir = tkinter.Frame(self.root,background="blue")
        self.dir_main = tkinter.Frame(self.dir,background="yellow")

        self.esq.grid_columnconfigure(0,weight=1)
        self.esq.grid_rowconfigure(0, weight=1)
        self.esq.grid_rowconfigure(1, weight=10)
        self.esq.grid_rowconfigure(2, weight=1)


        self.transferencia = tkinter.Frame(self.esq, background="brown")

        self.caminho = tkinter.Frame(self.esq,background="red")

        self.instrucao = tkinter.Frame(self.esq,background="pink")#tkinter.Frame(self.esq,background="pink")
        #primeiro declarar codes -> code_blocks -> Ins_Blocks -> chips
        #code_blocks a serem reutilizados
        self.clock_code:Codes=Codes("clk",["red","green"],None,1)
        self.clock_code_block = Code_Blocks(self.clock_code)
        self.code_list:list[Codes]=[Codes("Lp",["lightgray","green"],self.sap.get_activated_Lp,1),Codes("Ein",["lightgray","green"],self.sap.get_activated_Ein,1),Codes("RDnWR",["red","green"],self.sap.get_activated_RDnWR,1),
         Codes("IncDec",["lightgray","green"],self.sap.get_activated_IncDec,1),Codes("nLo",["lightgray","red"],self.sap.get_activated_nLo,0),Codes("nLb",["lightgray","red"],self.sap.get_activated_nLb,0)
         ,Codes("Eu",["lightgray","green"],self.sap.get_activated_Eu,1),Codes("Su",["lightgray","green"],self.sap.get_activated_Su,1),Codes("Ea",["lightgray","green"],self.sap.get_activated_Ea,1)
         ,Codes("nLa",["lightgray","red"],self.sap.get_activated_nLa,0),Codes("nEi",["lightgray","red"],self.sap.get_activated_nEi,0),Codes("nLi",["lightgray","red"],self.sap.get_activated_nLi,0)
         ,Codes("nCE",["lightgray","red"],self.sap.get_activated_nCE,0),Codes("nLm",["lightgray","red"],self.sap.get_activated_nLm,1),Codes("Ep",["lightgray","green"],self.sap.get_activated_Ep,1)
         ,Codes("Cp",["lightgray","green"],self.sap.get_activated_Cp,1)]
        self.code_blocks_list:list[Code_Blocks] = list()
        self.code_blocks_list2: list[Code_Blocks] = list()
        for c in self.code_list:
            self.code_blocks_list.append(Code_Blocks(c))
            self.code_blocks_list2.append(Code_Blocks(c))
        i:int = 0
        for c in self.code_blocks_list2:

            c.colocar_ins(self.instrucao,0,i)
            i+=1

        self.chips: list[Chips] = list()
        self.areas:list[Area] = list()
        self.chip_conection:list[Buffer_area] = list()
        for i in range(9):
            for j in range(3):
                self.caminho.rowconfigure(i,weight=1)
                self.caminho.columnconfigure(j,weight=1)
                self.areas.append(Area(self.caminho, i, j))
        instmp: Instructions_Blocks = Instructions_Blocks(
            [self.clock_code_block, self.code_blocks_list[15], self.code_blocks_list[14], self.code_blocks_list[0]])

        self.chips.append(Chips(self.areas[0].area,"CP",self.sap.get_CP_data,instmp,True))

        instmp = Instructions_Blocks(
            [self.clock_code_block, self.code_blocks_list[1]])
        self.chips.append(Chips(self.areas[2].area, "IN", self.sap.get_I_data, instmp, False))

        self.buffers_list: list[Buffer] = list()
        tmp_buffers_list: list[Buffer] = list()
        self.buffers_area_list: list[Buffer_area] = list()

        tmp_buffer0: Buffer = Buffer(3,3)
        tmp_buffer0.set_f0(self.code_list[0].fun_ativa)
        tmp_buffer0.set_f1( self.code_list[14].fun_ativa)

        tmp_buffer1: Buffer = Buffer(5,5)
        tmp_buffer1.set_f0( self.code_list[1].fun_ativa)
        tmp_buffer1.set_f1( self.code_list[1].fun_ativa)

        tmp_buffer2: Buffer = Buffer(4,4)
        tmp_buffer3: Buffer = Buffer(7,7)

        self.buffers_list.append(tmp_buffer0)
        tmp_buffers_list.append(tmp_buffer0)

        self.buffers_list.append(tmp_buffer1)
        tmp_buffers_list.append(tmp_buffer1)

        self.buffers_list.append(tmp_buffer2)
        tmp_buffers_list.append(tmp_buffer2)

        self.buffers_list.append(tmp_buffer3)
        tmp_buffers_list.append(tmp_buffer3)

        self.buffers_area_list.append(Buffer_area(self.areas[1].area,tmp_buffers_list))

        tmp_buffers_list = list()

        instmp= Instructions_Blocks(
            [self.clock_code_block, self.code_blocks_list[13]])

        self.chips.append(Chips(self.areas[6].area, "REM", self.sap.get_rem_data, instmp, True))

        tmp_buffer0 = Buffer(1,10)
        tmp_buffer1 = Buffer(4,13)
        tmp_buffer2 = Buffer(7,16)

        self.buffers_list.append(tmp_buffer0)
        tmp_buffers_list.append(tmp_buffer0)

        self.buffers_list.append(tmp_buffer1)
        tmp_buffers_list.append(tmp_buffer1)

        self.buffers_list.append(tmp_buffer2)
        tmp_buffers_list.append(tmp_buffer2)

        #self.buffers_area_list.append(Buffer_area(self.areas[1].area, tmp_buffers_list))
        self.buffers_area_list.append(Buffer_area(self.areas[4].area, tmp_buffers_list))
        tmp_buffers_list = list()

        tmp_buffer0 = Buffer(1,19)
        tmp_buffer1 = Buffer(3,21)
        tmp_buffer2 = Buffer(4,22)
        tmp_buffer3 = Buffer(5,23)
        tmp_buffer4:Buffer = Buffer(7,25)

        tmp_buffer1.set_f0(self.code_list[13].fun_ativa)
        tmp_buffer1.set_f1(self.code_list[13].fun_ativa)

        tmp_buffer3.set_f0(self.code_list[8].fun_ativa)
        tmp_buffer3.set_f1(self.code_list[9].fun_ativa)

        self.buffers_list.append(tmp_buffer0)
        tmp_buffers_list.append(tmp_buffer0)

        self.buffers_list.append(tmp_buffer1)
        tmp_buffers_list.append(tmp_buffer1)

        self.buffers_list.append(tmp_buffer2)
        tmp_buffers_list.append(tmp_buffer2)

        self.buffers_list.append(tmp_buffer3)
        tmp_buffers_list.append(tmp_buffer3)

        self.buffers_list.append(tmp_buffer4)
        tmp_buffers_list.append(tmp_buffer4)

        self.buffers_area_list.append(Buffer_area(self.areas[7].area, tmp_buffers_list))
        tmp_buffers_list = list()

        instmp = Instructions_Blocks(
            [self.clock_code_block, self.code_blocks_list[8],self.code_blocks_list[9]])

        self.chips.append(Chips(self.areas[8].area, "A", self.sap.get_A_data, instmp, False))

        tmp_buffer0 = Buffer(1)
        tmp_buffer1 = Buffer(4)
        tmp_buffer2 = Buffer(7)

        tmp_buffer0.ativado = True
        tmp_buffer1.ativado = True
        tmp_buffer2.ativado = True

        tmp_buffers_list.append(tmp_buffer0)

        tmp_buffers_list.append(tmp_buffer1)

        tmp_buffers_list.append(tmp_buffer2)

        self.chip_conection.append(Buffer_area(self.areas[9].area,tmp_buffers_list))
        tmp_buffers_list = list()

        tmp_buffer0 = Buffer(1,28)
        tmp_buffer1 = Buffer(4,31)
        tmp_buffer2 = Buffer(7,34)

        self.buffers_list.append(tmp_buffer0)
        tmp_buffers_list.append(tmp_buffer0)

        self.buffers_list.append(tmp_buffer1)
        tmp_buffers_list.append(tmp_buffer1)

        self.buffers_list.append(tmp_buffer2)
        tmp_buffers_list.append(tmp_buffer2)

        self.buffers_area_list.append(Buffer_area(self.areas[10].area,tmp_buffers_list))
        tmp_buffers_list = list()

        tmp_buffer0 = Buffer(1)
        tmp_buffer1 = Buffer(4)
        tmp_buffer2 = Buffer(7)

        tmp_buffer0.ativado = True
        tmp_buffer1.ativado = True
        tmp_buffer2.ativado = True

        tmp_buffers_list.append(tmp_buffer0)

        tmp_buffers_list.append(tmp_buffer1)

        tmp_buffers_list.append(tmp_buffer2)

        self.chip_conection.append(Buffer_area(self.areas[11].area, tmp_buffers_list))
        tmp_buffers_list = list()

        instmp = Instructions_Blocks(
            [self.clock_code_block, self.code_blocks_list[12],self.code_blocks_list[2]])

        self.chips.append(Chips(self.areas[12].area, "RAM", self.sap.get_ram_at_ptr, instmp, True))

        tmp_buffer0 = Buffer(1,37)
        tmp_buffer1 = Buffer(3,39)
        tmp_buffer2 = Buffer(4,40)
        tmp_buffer3 = Buffer(5,41)
        tmp_buffer4= Buffer(7,43)

        tmp_buffer1.set_f0(self.code_list[12].fun_ativa)
        tmp_buffer1.set_f1(self.code_list[12].fun_ativa)

        tmp_buffer3.set_f0(self.code_list[6].fun_ativa)
        tmp_buffer3.set_f1(self.code_list[6].fun_ativa)

        self.buffers_list.append(tmp_buffer0)
        tmp_buffers_list.append(tmp_buffer0)

        self.buffers_list.append(tmp_buffer1)
        tmp_buffers_list.append(tmp_buffer1)

        self.buffers_list.append(tmp_buffer2)
        tmp_buffers_list.append(tmp_buffer2)

        self.buffers_list.append(tmp_buffer3)
        tmp_buffers_list.append(tmp_buffer3)

        self.buffers_list.append(tmp_buffer4)
        tmp_buffers_list.append(tmp_buffer4)

        self.buffers_area_list.append(Buffer_area(self.areas[13].area, tmp_buffers_list))
        tmp_buffers_list = list()

        instmp = Instructions_Blocks(
            [ self.code_blocks_list[3], self.code_blocks_list[6],self.code_blocks_list[7]])

        self.chips.append(Chips(self.areas[14].area, "ULA", self.sap.get_ula_data, instmp, False))

        tmp_buffer0 = Buffer(1,46)
        tmp_buffer1 = Buffer(4,49)
        tmp_buffer2 = Buffer(7,52)

        self.buffers_list.append(tmp_buffer0)
        tmp_buffers_list.append(tmp_buffer0)

        self.buffers_list.append(tmp_buffer1)
        tmp_buffers_list.append(tmp_buffer1)

        self.buffers_list.append(tmp_buffer2)
        tmp_buffers_list.append(tmp_buffer2)

        # self.buffers_area_list.append(Buffer_area(self.areas[1].area, tmp_buffers_list))
        self.buffers_area_list.append(Buffer_area(self.areas[16].area, tmp_buffers_list))
        tmp_buffers_list = list()

        tmp_buffer0 = Buffer(1)
        tmp_buffer1 = Buffer(4)
        tmp_buffer2 = Buffer(7)

        tmp_buffer0.ativado = True
        tmp_buffer1.ativado = True
        tmp_buffer2.ativado = True

        tmp_buffers_list.append(tmp_buffer0)

        tmp_buffers_list.append(tmp_buffer1)

        tmp_buffers_list.append(tmp_buffer2)

        self.chip_conection.append(Buffer_area(self.areas[17].area, tmp_buffers_list))
        tmp_buffers_list = list()

        instmp = Instructions_Blocks(
            [self.clock_code_block, self.code_blocks_list[10], self.code_blocks_list[11]])

        self.chips.append(Chips(self.areas[18].area, "RI", self.sap.get_ri_data, instmp, True))

        tmp_buffer0 = Buffer(1,55)
        tmp_buffer1 = Buffer(3,57)
        tmp_buffer2 = Buffer(4,58)
        tmp_buffer3 = Buffer(5,59)
        tmp_buffer4 = Buffer(7,61)

        tmp_buffer1.set_f0(self.code_list[10].fun_ativa)
        tmp_buffer1.set_f1(self.code_list[11].fun_ativa)

        tmp_buffer3.set_f0(self.code_list[5].fun_ativa)
        tmp_buffer3.set_f1(self.code_list[5].fun_ativa)

        #tmp_buffer4.set_f0(self.code_list[4].fun_ativa)
        #tmp_buffer4.set_f1(self.code_list[4].fun_ativa)

        self.buffers_list.append(tmp_buffer0)
        tmp_buffers_list.append(tmp_buffer0)

        self.buffers_list.append(tmp_buffer1)
        tmp_buffers_list.append(tmp_buffer1)

        self.buffers_list.append(tmp_buffer2)
        tmp_buffers_list.append(tmp_buffer2)

        self.buffers_list.append(tmp_buffer3)
        tmp_buffers_list.append(tmp_buffer3)

        self.buffers_list.append(tmp_buffer4)
        tmp_buffers_list.append(tmp_buffer4)

        self.buffers_area_list.append(Buffer_area(self.areas[19].area, tmp_buffers_list))
        tmp_buffers_list = list()

        instmp = Instructions_Blocks(
            [self.clock_code_block, self.code_blocks_list[5]])

        self.chips.append(Chips(self.areas[20].area, "B", self.sap.get_B_data, instmp, False))

        tmp_buffer0 = Buffer(1)
        tmp_buffer1 = Buffer(4)
        tmp_buffer2 = Buffer(7)

        tmp_buffer0.ativado = True
        tmp_buffer1.ativado = True
        tmp_buffer2.ativado = True

        tmp_buffers_list.append(tmp_buffer0)

        tmp_buffers_list.append(tmp_buffer1)

        tmp_buffers_list.append(tmp_buffer2)

        self.chip_conection.append(Buffer_area(self.areas[21].area, tmp_buffers_list))
        tmp_buffers_list = list()

        tmp_buffer0 = Buffer(1,64)
        tmp_buffer1 = Buffer(4,67)
        tmp_buffer2 = Buffer(7,70)

        self.buffers_list.append(tmp_buffer0)
        tmp_buffers_list.append(tmp_buffer0)

        self.buffers_list.append(tmp_buffer1)
        tmp_buffers_list.append(tmp_buffer1)

        self.buffers_list.append(tmp_buffer2)
        tmp_buffers_list.append(tmp_buffer2)

        # self.buffers_area_list.append(Buffer_area(self.areas[1].area, tmp_buffers_list))
        self.buffers_area_list.append(Buffer_area(self.areas[22].area, tmp_buffers_list))
        tmp_buffers_list = list()

        tmp_buffer0 = Buffer(1,71)
        tmp_buffer1 = Buffer(4,76)
        tmp_buffer2 = Buffer(5,77)

        tmp_buffer2.set_f0(self.code_list[4].fun_ativa)
        tmp_buffer2.set_f1(self.code_list[4].fun_ativa)

        self.buffers_list.append(tmp_buffer0)
        tmp_buffers_list.append(tmp_buffer0)

        self.buffers_list.append(tmp_buffer1)
        tmp_buffers_list.append(tmp_buffer1)

        self.buffers_list.append(tmp_buffer2)
        tmp_buffers_list.append(tmp_buffer2)

        # self.buffers_area_list.append(Buffer_area(self.areas[1].area, tmp_buffers_list))
        self.buffers_area_list.append(Buffer_area(self.areas[25].area, tmp_buffers_list))
        tmp_buffers_list = list()

        instmp = Instructions_Blocks(
            [self.clock_code_block, self.code_blocks_list[4]])

        self.chips.append(Chips(self.areas[26].area, "OUT", self.sap.get_O_data, instmp, False))


        instmp = Instructions_Blocks(
            [self.clock_code_block])#, self.code_blocks_list[10], self.code_blocks_list[11]])

        self.chips.append(Chips(self.areas[24].area, "CS",self.sap.get_instruction , instmp, True))#self.sap.get_rom_ins_at_ptr

        '''#self.codes:list = list()
        self.b_area:list[Buffer_area] = list[Buffer_area]()
        self.buffers_list:list[Buffer] = list()
        self.buffers_area_list:list[Buffer_area]= list()

        buffer_tmp:Buffer = Buffer(3)#buffer 0 area 1

        buffer_tmp_list:list[Buffer] = list()
        #self.buffers:list[Buffer] = [Buffer(self.teste,self.teste,1),Buffer(self.teste,self.teste,4),Buffer(self.teste,self.teste,7)]
        self.chips:list[Chips]= list()
        #self.chips = list()
        #self.buffers = list()

        bc:list = [Code_Blocks(Codes("Lp",["red","gray"])),Code_Blocks(Codes("Ep",["gray","green"])),Code_Blocks(Codes("CLK",["blue","gray"]))]
        ins = Instructions_Blocks(bc)
        self.chips:list[Chips] = [Chips(self.areas[0].area,"CP",self.teste,ins,True),Chips(self.areas[2].area,"IN",self.teste,ins,False)]
        self.b_area.append(Buffer_area(self.areas[1].area,self.buffers))
        self.chips[0].colocar()
        self.b_area[0].colocar()
        self.chips[1].colocar()'''
        for chip in self.chips:
            chip.colocar()

        for cc in self.chip_conection:
            cc.colocar()
        for ba in self.buffers_area_list:
            ba.colocar()

        for a in self.areas:
            a.colocar()

        #self.code_blocks_list2 = self.code_blocks_list.copy()

        #for cb in range(len(self.code_blocks_list2)):
        #    self.code_blocks_list2[cb].colocar_ins(self.instrucao,0,cb)



        self.transferencia.grid(row=0, column=0,columnspan=3,sticky="nsew")
        self.caminho.grid(row=1, column=0, columnspan=3,sticky="nsew")
        self.instrucao.grid(row=2, column=0, columnspan=3,sticky="nsew")
        self.esq.pack(side = tkinter.LEFT,fill='both',expand =True)


        #self.dir_main.pack(fill='both', expand= True)


        #self.dir.pack(side = tkinter.RIGHT,fill='both', expand= True)



        #self.esq.grid(row=0,column = 0,rowspan = 1 , columnspan = 1)
        #self.dir.grid(row=0, column=1,rowspan = 1 , columnspan = 1)



        #self.dir_main.pack(fill='both', expand= True)
    def criar_Outra_Janela(self,titulo:str):
        self.outra:tkinter.Toplevel = tkinter.Toplevel(self.root)
        self.outra.title(titulo)
        self.outra.geometry("300x400")


    def destruir_Janela(self):
        self.menu.entryconfig("Input", state="normal")
        self.menu.entryconfig("RAM", state="normal")
        self.menu.entryconfig("Fullscreen", state="normal")
        self.menu.entryconfig("START", state="normal")
        self.menu.entryconfig("CLK", state="normal")
        self.menu.entryconfig("Exit", state="normal")
        self.menu.entryconfig("CLEAR", state="normal")
        self.outra.destroy()
        self.outra = None

    def set_input_val(self):
        self.sap.set_input_data(int(self.inputer.input_str,16)%256)
        self.chips[1].update()



    def inputar(self):
        self.menu.entryconfig("Input",state="disabled")
        self.menu.entryconfig("RAM", state="disabled")
        self.menu.entryconfig("Fullscreen", state="disabled")
        self.menu.entryconfig("START", state="disabled")
        self.menu.entryconfig("CLK", state="disabled")
        self.menu.entryconfig("Exit", state="disabled")
        self.menu.entryconfig("CLEAR", state="disabled")
        self.criar_Outra_Janela("Input")
        self.inputer:Inputer = Inputer(self.outra)
        self.outra.protocol("WM_DELETE_WINDOW", self.destruir_Janela)
        #self.cancelar = tkinter.Button(self.outra, text= "cancel",command=self.destruir_Janela)
        self.enviar = tkinter.Button(self.outra,text="set input val",command=self.set_input_val)
        self.button_0 = tkinter.Button(self.outra,text="0",command=self.inputer.val_0)
        self.button_1 = tkinter.Button(self.outra, text="1", command=self.inputer.val_1)
        self.button_2 = tkinter.Button(self.outra, text="2", command=self.inputer.val_2)
        self.button_3 = tkinter.Button(self.outra, text="3", command=self.inputer.val_3)
        self.button_4 = tkinter.Button(self.outra, text="4", command=self.inputer.val_4)
        self.button_5 = tkinter.Button(self.outra, text="5", command=self.inputer.val_5)
        self.button_6 = tkinter.Button(self.outra, text="6", command=self.inputer.val_6)
        self.button_7 = tkinter.Button(self.outra, text="7", command=self.inputer.val_7)
        self.button_8 = tkinter.Button(self.outra, text="8", command=self.inputer.val_8)
        self.button_9 = tkinter.Button(self.outra, text="9", command=self.inputer.val_9)
        self.button_a = tkinter.Button(self.outra, text="a", command=self.inputer.val_a)
        self.button_b = tkinter.Button(self.outra, text="b", command=self.inputer.val_b)
        self.button_c = tkinter.Button(self.outra, text="c", command=self.inputer.val_c)
        self.button_d = tkinter.Button(self.outra, text="d", command=self.inputer.val_d)
        self.button_e = tkinter.Button(self.outra, text="e", command=self.inputer.val_e)
        self.button_f = tkinter.Button(self.outra, text="f", command=self.inputer.val_f)
        self.button_remove = tkinter.Button(self.outra, text="back", command=self.inputer.remover)

        self.input_label = tkinter.Label(self.outra,textvariable=self.inputer.inputer_var,background="white")
        self.input_label.grid(row=0,column=0, columnspan = 4)

        self.button_0.grid(row=1,column=0, columnspan = 1)
        self.button_1.grid(row=1, column=1, columnspan=1)
        self.button_2.grid(row=1, column=2, columnspan=1)
        self.button_3.grid(row=1, column=3, columnspan=1)
        self.button_4.grid(row=2, column=0, columnspan=1)
        self.button_5.grid(row=2, column=1, columnspan=1)
        self.button_6.grid(row=2, column=2, columnspan=1)
        self.button_7.grid(row=2, column=3, columnspan=1)
        self.button_8.grid(row=3, column=0, columnspan=1)
        self.button_9.grid(row=3, column=1, columnspan=1)
        self.button_a.grid(row=3, column=2, columnspan=1)
        self.button_b.grid(row=3, column=3, columnspan=1)
        self.button_c.grid(row=4, column=0, columnspan=1)
        self.button_d.grid(row=4, column=1, columnspan=1)
        self.button_e.grid(row=4, column=2, columnspan=1)
        self.button_f.grid(row=4, column=3, columnspan=1)
        self.enviar.grid(row=5,column=0,columnspan=2)
        self.button_remove.grid(row=5,column=2,columnspan=2)




    def caminhar(self):
        self.reset_buffers()
        bp:list[Buffer] =[None,None]
        i:int = 0
        for b in self.buffers_list:
            if b.get_ativado():
                bp[i%2] = b
                i+=1
        if(bp[0] != None and bp[1] != None ):
            meio0:int = bp[0].global_id
            if meio0%3 == 2:
                meio0-=1
            else:
                meio0+=1
            meio1: int = bp[0].global_id
            if meio1%3 == 2:
                meio1-=1
            else:
                meio1+=1
            delta:int = 1
            if meio0 > meio1:
                delta = -1


            for b in self.buffers_list:
                if b.global_id == meio0:
                    meio0+= delta
                    b.ativado = True
                elif b.global_id == meio1:
                    meio1-= delta
                    b.ativado = True
                if meio0 == meio1:
                    break



        for ba in self.buffers_area_list:
            ba.update()

    def set_selected_ram(self):
        self.sap.update_ram(self.selecter.selecter,int(self.inputer.input_str,16)%256)
        self.selecter.update_ram()

    def change_ram(self):
        self.menu.entryconfig("Input", state="disabled")
        self.menu.entryconfig("RAM", state="disabled")
        self.menu.entryconfig("Fullscreen", state="disabled")
        self.menu.entryconfig("START", state="disabled")
        self.menu.entryconfig("CLK", state="disabled")
        self.menu.entryconfig("Exit", state="disabled")
        self.menu.entryconfig("CLEAR", state="disabled")
        self.criar_Outra_Janela("RAM")

        self.inputer: Inputer = Inputer(self.outra)

        self.outra.protocol("WM_DELETE_WINDOW", self.destruir_Janela)
        self.ram_label:tkinter.Frame = tkinter.Frame(self.outra)




        self.selecter:Selecter = Selecter(self.ram_label,self.sap)

            #self.ram_vars.append(tkinter.StringVar(self.ram_label))
            #self.ram_buttons.append(tkinter.Button(self.ram_label,textvariable=self.ram_vars[i]))
        self.ram_label.pack()
        self.value_frame:tkinter.Frame = tkinter.Frame(self.outra)
        self.enviar = tkinter.Button(self.value_frame, text="set input val", command=self.set_selected_ram)
        self.button_0 = tkinter.Button(self.value_frame, text="0", command=self.inputer.val_0)
        self.button_1 = tkinter.Button(self.value_frame, text="1", command=self.inputer.val_1)
        self.button_2 = tkinter.Button(self.value_frame, text="2", command=self.inputer.val_2)
        self.button_3 = tkinter.Button(self.value_frame, text="3", command=self.inputer.val_3)
        self.button_4 = tkinter.Button(self.value_frame, text="4", command=self.inputer.val_4)
        self.button_5 = tkinter.Button(self.value_frame, text="5", command=self.inputer.val_5)
        self.button_6 = tkinter.Button(self.value_frame, text="6", command=self.inputer.val_6)
        self.button_7 = tkinter.Button(self.value_frame, text="7", command=self.inputer.val_7)
        self.button_8 = tkinter.Button(self.value_frame, text="8", command=self.inputer.val_8)
        self.button_9 = tkinter.Button(self.value_frame, text="9", command=self.inputer.val_9)
        self.button_a = tkinter.Button(self.value_frame, text="a", command=self.inputer.val_a)
        self.button_b = tkinter.Button(self.value_frame, text="b", command=self.inputer.val_b)
        self.button_c = tkinter.Button(self.value_frame, text="c", command=self.inputer.val_c)
        self.button_d = tkinter.Button(self.value_frame, text="d", command=self.inputer.val_d)
        self.button_e = tkinter.Button(self.value_frame, text="e", command=self.inputer.val_e)
        self.button_f = tkinter.Button(self.value_frame, text="f", command=self.inputer.val_f)
        self.button_remove = tkinter.Button(self.value_frame, text="back", command=self.inputer.remover)

        self.input_label = tkinter.Label(self.value_frame, textvariable=self.inputer.inputer_var, background="white")
        self.input_label.grid(row=0, column=0, columnspan=4)

        self.button_0.grid(row=1, column=0, columnspan=1)
        self.button_1.grid(row=1, column=1, columnspan=1)
        self.button_2.grid(row=1, column=2, columnspan=1)
        self.button_3.grid(row=1, column=3, columnspan=1)
        self.button_4.grid(row=2, column=0, columnspan=1)
        self.button_5.grid(row=2, column=1, columnspan=1)
        self.button_6.grid(row=2, column=2, columnspan=1)
        self.button_7.grid(row=2, column=3, columnspan=1)
        self.button_8.grid(row=3, column=0, columnspan=1)
        self.button_9.grid(row=3, column=1, columnspan=1)
        self.button_a.grid(row=3, column=2, columnspan=1)
        self.button_b.grid(row=3, column=3, columnspan=1)
        self.button_c.grid(row=4, column=0, columnspan=1)
        self.button_d.grid(row=4, column=1, columnspan=1)
        self.button_e.grid(row=4, column=2, columnspan=1)
        self.button_f.grid(row=4, column=3, columnspan=1)
        self.enviar.grid(row=5, column=0, columnspan=2)
        self.button_remove.grid(row=5, column=2, columnspan=2)
        self.value_frame.pack()


    def on_closing(self):
        if self.outra != None:
            self.destruir_Janela()
        if self.config["DEFAULT"]["fullscreen"] == "no":
            self.config["DEFAULT"]["width"] = str(self.root.winfo_width())
            self.config["DEFAULT"]["height"] = str(self.root.winfo_height())
        with open("config.ini", 'w') as cf:
            self.config.write(cf)
        self.root.destroy()
        return None

    def change_fullscreen(self):
        if (self.config["DEFAULT"]["fullscreen"] == "yes"):
            self.config["DEFAULT"]["fullscreen"] = "no"

            self.root.attributes("-fullscreen", False)
            self.root.geometry(self.config["DEFAULT"]["width"] + 'x' + self.config["DEFAULT"]["height"])
        else:
            self.config["DEFAULT"]["fullscreen"] = "yes"
            self.root.attributes("-fullscreen", True)
        self.root.update()

    def reset_buffers(self):
        for b in self.buffers_list:
            b.ativado = False
    def change_darkmode(self):
        if(self.config["DEFAULT"]["darkmode"] == "no"):
            self.config["DEFAULT"]["darkmode"] = "yes"
            #fundo = "gray"
        else:
            self.config["DEFAULT"]["darkmode"] = "no"
            #fundo = "lightgray"
        self.root.update()

    def Clocar(self):
        if self.sap.get_working_clock():
            self.sap.clk()
            self.update()
            self.caminhar()
        else:
            self.menu.entryconfig("CLK",state="disabled")



    def Start(self):
        print(self.sap.get_activated_Cp())
        self.sap.start()
        self.menu.entryconfig("CLK", state="normal")
        self.reset_buffers()
        self.update()
        self.caminhar()

    def update(self):
        for cb in self.code_blocks_list:
            cb.update()
        for cb2 in self.code_blocks_list2:
            cb2.update()
        for c in self.chips:
            c.update()
        for ba in self.buffers_area_list:
            ba.update()

        self.root.update()

    def clear(self):
        self.sap.clear()
        self.reset_buffers()
        self.update()
        self.caminhar()
        self.menu.entryconfig("CLK", state="disabled")
    def win_loop(self):
        self.root.mainloop()

    def teste(self) -> bool:
        return self.config["DEFAULT"]["darkmode"] == 'no'
class Codes:
    def __init__(self,tag:str,cores:list[str],fun_ativa,ativador:int):#,fun_ativa):
        self.tag:str = str(tag)
        self.cores:list[str]= cores.copy()
        self.ativador:int = int(ativador)

        self.fun_ativa= fun_holder
        self.status= False
        self.fun_ativa = fun_ativa
        #self.frames:list = list([,tkinter.Frame(root2, background=self.cores[0])])
class Code_Blocks:
    def __init__(self,code:Codes):
        self.code = code
        self.frame:tkinter.Frame = None#= tkinter.Frame(root, background=self.code.cores[0])
        self.label:tkinter.Label
        self.framei: tkinter.Frame = None  # = tkinter.Frame(root, background=self.code.cores[0])
        self.labeli: tkinter.Label
    def colocar(self,root,r:int,c:int):

        self.frame = tkinter.Frame(root, background=self.code.cores[0])
        self.label = tkinter.Label(self.frame,text= self.code.tag,background=self.code.cores[0])
        self.label.pack(expand = True,fill=tkinter.BOTH)
        #self.frame = tkinter.Frame(root, background="lightgreen")
        #self.frame.grid(row = r , column=c,sticky="nsew")
        self.frame.pack(fill=tkinter.BOTH,expand=True)
    def colocar_ins(self,root,r:int,c:int):

        self.framei = tkinter.Frame(root, background=self.code.cores[0])
        self.labeli = tkinter.Label(self.framei,text= self.code.tag,background=self.code.cores[0])
        self.labeli.pack(expand = True,fill=tkinter.BOTH)
        #self.frame = tkinter.Frame(root, background="lightgreen")
        #self.frame.grid(row = r , column=c,sticky="nsew")
        self.framei.pack(fill=tkinter.BOTH,expand=True,side="left")
    def update(self):
        if self.code.fun_ativa !=None:
            if self.code.fun_ativa():
                if self.frame != None and self.label != None:
                    self.frame.config(bg=self.code.cores[1])
                    self.label.config(bg=self.code.cores[1])
                if self.framei != None and self.labeli != None:
                    self.framei.config(bg=self.code.cores[1])
                    self.labeli.config(bg=self.code.cores[1])

            else:
                if self.frame != None and self.label != None:
                    self.frame.config(bg=self.code.cores[0])
                    self.label.config(bg=self.code.cores[0])
                if self.framei != None and self.labeli != None:
                    self.framei.config(bg=self.code.cores[0])
                    self.labeli.config(bg=self.code.cores[0])



class Instructions_Blocks:
    def __init__(self,b_codes:list[Code_Blocks]):
        self.frame: tkinter.Frame = None
        self.b_codes:list = b_codes
        pass
    def colocar(self,root,c:int):
        self.frame = tkinter.Frame(root, background="orange")  # self.code.cores[0])

        for i in range(len(self.b_codes)):
           self.b_codes[i].colocar(self.frame,i,0)
        self.frame.grid(column=c,row=0,sticky="nsew")
    def num_codes(self)->int:
        return len(self.b_codes)

        #root.grid_rowconfigure(0,weight=3)
        #self.frame.grid(row=0,column=0,rowspan=3,sticky="nsew")

        #self.frame.pack(fill=tkinter.BOTH, expand=True)


class Chips:
    def __init__(self,root,tag: str,fun_data,ins:Instructions_Blocks,ins_esq:bool):
        self.root = root
        #self.code:list[Codes]= code.copy()
        self.fun_data = fun_data
        self.ins = ins
        self.frame = tkinter.Frame(root,background="cyan")
        self.sub_frame = tkinter.Frame(self.frame,background="purple")
        self.tag = tkinter.Label(self.sub_frame,text=str(tag))
        self.data_tag_var = tkinter.StringVar(self.sub_frame,str(self.fun_data()))
        self.data_tag = tkinter.Label(self.sub_frame,textvariable=self.data_tag_var)
        self.ins_esq:bool = bool(ins_esq)
    def colocar(self):
        c= 1
        s = 0
        if self.ins_esq:
            c =0
            s=1
        #,r:int):
        self.tag.pack(fill=tkinter.BOTH,expand=True)
        self.data_tag.pack(fill=tkinter.BOTH, expand=True)
        #self.data_tag.pack()
        #self.frame.pack(fill=tkinter.BOTH,expand=True)
        self.root.grid_columnconfigure(s,weight=1)
        self.root.grid_rowconfigure(c,weight=1)
        #self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(c,weight=1)
        self.frame.grid_columnconfigure(s, weight=9)
        self.frame.grid_rowconfigure(0, weight=1)
        self.sub_frame.grid(column=s, row=0, sticky="nsew")
        self.ins.colocar(self.frame,c)

        self.frame.grid(column=0,row=0,columnspan=4,rowspan=self.ins.num_codes() ,sticky="nsew")
    def update(self):
        self.data_tag_var.set(self.fun_data())
        for b in self.ins.b_codes:
            b.update()

class Buffer:
    def __init__(self,id:int,g:int = 0):
        self.f0 = None
        self.f1 = None
        self.id = int(id)
        self.global_id = int(g)
        self.ativado:bool = False
    def ativa0(self)->bool:
        return self.f0()
    def ativa1(self)->bool:
        return self.f1()

    def get_ativado(self)->bool:
        if (self.f0 != None) and (self.f1 != None):
            self.ativado = (self.f0() or self.f1())
        else:
            if self.f0 != None:
                self.ativado = self.f0()
            if self.f1 != None:
                self.ativado = self.f1()

        return self.ativado

    def set_f0(self,f0):
        self.f0 = f0
    def set_f1(self,f1):
        self.f1 = f1
class Buffer_area:
    def __init__(self,root,buffers:list[Buffer]):
        self.root = root
        self.buffers:list[Buffer]= buffers.copy()
        self.areas:list[tkinter.Frame] = list()
    def colocar(self):
        for i in range(9):
            self.areas.append(tkinter.Frame(self.root,background=fundo))
            #self.areas[i].pack(fill=tkinter.BOTH, expand=True, side=tkinter.TOP)
            self.areas[i].grid(row= int(i/3),column= i %3,sticky="nsew")
            self.root.grid_rowconfigure(int(i/3), weight=1)
            self.root.grid_columnconfigure(i%3, weight=1)

        for b in self.buffers:
            if b.ativado:
                self.areas[b.id].config(bg="lime")
            else:
                self.areas[b.id].config(bg="black")

    def reset(self):
        for b in self.buffers:
            b.ativado = False
    def update(self):
        for b in self.buffers:
            if b.ativado:
                self.areas[b.id].config(bg="green")
            else:
                self.areas[b.id].config(bg="black")




class Area:
    def __init__(self,root,r:int,c:int):
        self.r:int = int(r)
        self.c:int = int(c)
        self.area = tkinter.Frame(root,background="gray",)
    def colocar(self):
        self.area.grid(row=self.r,column=self.c ,sticky="nsew")

