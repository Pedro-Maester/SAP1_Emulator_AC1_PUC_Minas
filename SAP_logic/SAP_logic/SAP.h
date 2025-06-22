// SAPLOGIC.h - Contains declarations of math functions
#pragma once

#ifdef SAPLOGIC_EXPORTS
#define SAPLOGIC_API __declspec(dllexport)
#else
#define SAPLOGIC_API __declspec(dllimport)
#endif



// The Fibonacci recurrence relation describes a sequence F
// where F(n) is { n = 0, a
//               { n = 1, b
//               { n > 1, F(n-2) + F(n-1)
// for some initial integral values a and b.
// If the sequence is initialized F(0) = 1, F(1) = 1,
// then this relation produces the well-known Fibonacci
// sequence: 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

// Initialize a Fibonacci relation sequence
// such that F(0) = a, F(1) = b.
// This function must be called before any other function.
extern "C" SAPLOGIC_API void fibonacci_init(
    const unsigned long long a, const unsigned long long b);

// Produce the next value in the sequence.
// Returns true on success and updates current value and index;
// false on overflow, leaves current value and index unchanged.
extern "C" SAPLOGIC_API bool fibonacci_next();

// Get the current value in the sequence.
extern "C" SAPLOGIC_API unsigned long long fibonacci_current();

// Get the position of the current value in the sequence.
extern "C" SAPLOGIC_API unsigned fibonacci_index();

enum ins_id {Cp, Ep, nLm, nCE, nLi, nEi, nLa, Ea, Su, Eu, nLb, nLo, IncDec, RDnWR, Mul, Lp};

enum code {lda,add,sub,inc,dec,mul,jmp,sto,out=14,hlt =15};





extern "C" SAPLOGIC_API class Ins {
private:
    static unsigned short ins;
    static bool clk;
    static bool clr;
    static unsigned char clocks;
    void clear() {
        this->ins = 0x5e30;
    }
    //unsigned char n_i = 0;
    //ins_id* i_id = nullptr;
protected:
    bool get_activated(ins_id i) {
        return (this->ins >> i) & 1;
    }

    bool get_inactivated(ins_id i) {
        return (this->ins >> i) & 0;
    }
    
public:
    Ins() {
        
        
        
      //  this->n_i = 0;
       // this->i_id = nullptr;
    }
    //Ins(unsigned char ni,ins_id* ids) {
       // this->ins = 0;
        //this->clk;
       
       // this->n_i = ni;
       // this->i_id = new ins_id[this->n_i];
       // for (unsigned char i = 0; i < this->n_i; i += 1)this->i_id[i] = ids[i];

    //}
    
    bool get_clear() {
        return this->clr;
    }
    void clocking() {
        this->clocks = (this->clocks + 1);//atualiza os loops reiniciando a cada 6
        
    }
    void clks() {
        this->clk = !this->clk;
    }
    
    void clocking_reset() {
        this->clocks = 0;
    }
    unsigned short get_ins_code() {
        return this->ins;
    }
    bool get_clk() {
        return this->clk;
    }
    unsigned char get_clocks() {
        return this->clocks;
    }
    void set_ins(unsigned short i) {
        this->ins = i;
        return;

    }
    void clocking() {
        this->clocks = (this->clocks + 1) % 6;//atualiza os loops reiniciando a cada 6
    }
    void clocking_reset() {
        this->clocks = 0;
    }
    //unsigned char get_num_instructions() {
    //    return this->n_i;
    //}

    

    //ins_id get_ins_id(unsigned char i) {
     //   return this->i_id[i];
    //}
    
};
unsigned short Ins::ins = 0x5e30;
bool Ins::clk = false;
bool Ins::clr = false;
unsigned char Ins::clocks = 0;
extern "C" SAPLOGIC_API class Program_Counter:Ins{
private:
    unsigned char cp_in_out;
    unsigned char count;
    
public:
    Program_Counter() {
        this->cp_in_out = 0;
        //ins_id ids[3] = {Cp,Ep,Lp};
        //Ins((unsigned char)3,ids);
        
    }
    void clr() {
        this->cp_in_out = 0;
        return;
    }
    void Increment() {
        this->count += 1;
        return;
    }
    unsigned char get_count() {
        return this->count;
    }
    unsigned char get_cp_out() {
        return this->cp_in_out >> 4;
    }
    void cp_in(unsigned char input) {
        this->cp_in_out;
    }
    bool enabled_output() {
        return this->get_activated(Ep);
    }
    bool load_program() {
        return this->get_activated(Lp);
    }

    bool count_program() {
        return this->get_activated(Cp);
    }
    unsigned char* get_count_adress() {
        return &this->count;
    }
};



extern "C" SAPLOGIC_API class Ram:Ins {
private:
    unsigned char* mem = nullptr;
    unsigned char ptr = 0;
    unsigned char tam = 0;
public:
    Ram(unsigned char tam) {
        //ins_id ids[2] = { nCE,RDnWR };
        //Ins(2,ids);
        this->tam = tam;
        this->mem = new unsigned char[this->tam]();
        this->ptr = 0;
        
    }
    ~Ram() {
        delete[] mem;
    }
    void set_val_at_ptr(unsigned char val) {
        this->mem[this->ptr>>4] = val;

    }
    void set_val_at(unsigned char i, unsigned char val) {
        this->mem[i] = val;
        return;
    }
    void set_ptr(unsigned char p) {
        this->ptr = p;
    }
    unsigned char get_val_at(unsigned char i = 0) {
        return this->mem[i];
    }
    unsigned char get_val_at_ptr() {
        return this->mem[this->ptr>>4];
    }
    void clear_mem() {
        for (unsigned char i = 0; i < this->tam; i += 1)this->mem[i] = 0;
    }
    void reset_mem(unsigned char tam) {
        delete[] mem;
        this->tam = tam;
        this->mem = new unsigned char[this->tam]();
        this->ptr = 0;

    }
    unsigned char* get_mem_adress_at_ptr() {
        return &this->mem[this->ptr>>4];
    }
    unsigned char* get_ptr_adress() {
        return &this->ptr;
    }
    
};

extern "C" SAPLOGIC_API class ULA:Ins {
private:
    unsigned char dados = 0;
    unsigned char* a_input = nullptr;
    unsigned char* b_input = nullptr;
    bool su = false;
    unsigned char modo = 0;
    
public:
    void ativar() {
        switch (this->modo)
        {
        case IncDec:
            if (Su)this->dec();
            else this->inc();
            break;
        case Mul:
            if (Su)this->div();
            else this->mult();
        default:
            if (Su)this->sub();
            else this->sum();
            break;
        }
        this->su = false;
        this->modo = 0;
        return;
    }
    ULA(unsigned char* a, unsigned char* b):a_input(a),b_input(b){
    }
    void reverse_op() {
        this->su = true;
        return;
    }
    void set_modo(unsigned char m) {
        this->modo = m;
    }
    void CLR() {
        this->dados = 0;
    }
    void sum() {
        this->dados = *this->a_input + *this->b_input;
    }
    void sub() {
        this->dados = *this->a_input - *this->b_input;
    }
    void mult() {
        this->dados = *this->a_input * *this->b_input;
    }
    void div() {
        this->dados = *this->a_input / *this->b_input;
    }
    void mod() {
        this->dados = *this->a_input % *this->b_input;
    }

    void inc() {
        this->dados = *this->a_input +1;
    }
    void dec() {
        this->dados = *this->a_input -1;
    }
    unsigned char get_dados() {
        return this->dados;
    }
    unsigned char* get_dados_adress() {
        return &this->dados;
    }
    

};

extern "C" SAPLOGIC_API class Rem:Ins {
private:
    Ram* target;
    unsigned char mem_adress = 0;

public:
    Rem(Ram* target) {
        this->target = target;

    }
    void set_mem_adress(unsigned char m) {
        this->mem_adress = m;
        this->target->set_ptr(m);
        return;
    }
    unsigned char get_mem_adress() {
        return this->mem_adress;
    }
    unsigned char get_val_at_ram_target() {
        return this->target->get_val_at(this->mem_adress);
    }
    unsigned char* get_ptr_adress() {
        return this->target->get_ptr_adress();
    }

};


extern "C" SAPLOGIC_API class Register {
private:
    unsigned char dados;
    unsigned char* saida = nullptr;
public:
    Register() {
        this->dados = 0;
        this->saida = nullptr;
    }
    Register(unsigned char* s) {
        this->dados = 0;
        this->saida = s;
    }
    void set_dados(unsigned char d) {
        this->dados = d;
    }
    void exit_dados() {
        *this->saida = this->dados;
        return;
    }
    unsigned char get_dados() {
        return this->dados;
    }
    unsigned char* get_dados_adress() {
        return &this->dados;
    }
    void CLR() {
        this->dados = 0;
        return;
    }
    void Increment() {
        this->dados += 1;
        return;
    }
    void Decrement() {
        this->dados -= 1;
        return;
    }
    unsigned char* get_ref_dados() {
        return &this->dados;
    }
    void set_saida(unsigned char* s) {
        this->saida = s;
        return;
    }

    

};

extern "C" SAPLOGIC_API class Rom {
private:
    const unsigned char ins_adress[16] = {0x3,0x6,0x9,0x10,0x13,0x16,0x19,0x1c,0x00,0x00,0x00,0x00,0x00,0x0c,0x00};

    const unsigned char macro_codes[32] = { 0x5e30, 0xbe30, 0x2634, 0x1a30, 0x2c34, 0x3e30, 0x1a30, 0x2e14,
                                            0x3c70, 0x1a30, 0x2e14, 0x3cf0, 0x3f20, 0x3e30, 0x3e30, 0x0000,
                                            0x3c78, 0x3e30, 0x3e30, 0x3cf8, 0x3e30, 0x3e30 ,0x1a30, 0x2e14,
                                            0x3c32, 0x3a31, 0x3e30, 0x3e30, 0x1a30, 0x2f30, 0x3e30, 0x0000 };
public:
    const unsigned char get_ins_adress(code i) {
        return this->ins_adress[i];
    }
    const unsigned char get_macro_code(unsigned char m) {
        return this->macro_codes[m];
    }
    

};



extern "C" SAPLOGIC_API class Instruction_Controler_Sequencializador:Ins {
private:
    Register* registrador;
    Rom rom;
    unsigned char cur;
    
public:
    Instruction_Controler_Sequencializador(Register* I) {
        this->registrador = I;
    }
    void set_cur_ins(code i) {
        this->cur = this->rom.get_ins_adress(i);
    }
    void set_ins_code() {
        this->set_ins(this->rom.get_macro_code(this->get_clocks() / 3 * (this->cur + this->get_clocks() % 3)));//seta o codigo de instrução
        return;
    }
    
    
};

extern "C" SAPLOGIC_API class Registrador_Instrucoes :Ins {
    Instruction_Controler_Sequencializador ICS;


};


extern "C" SAPLOGIC_API class Buffer:Ins {
private:
    unsigned char dados = 0;
    unsigned char* read = nullptr;
    unsigned char* write = nullptr;
 
    Program_Counter pc;
    Ram ram = Ram(16);
    Rem rem = Rem(&this->ram);
    Register A = Register(&this->dados);
    Register B;
    Register O;
    Register I;
    Instruction_Controler_Sequencializador ICS = Instruction_Controler_Sequencializador(&this->I);
    ULA ops = ULA(this->A.get_dados_adress(), this->B.get_dados_adress());
    
   
    
public:
    Buffer() {
        this->dados = 0;

   }
    bool Operar() {
        if((pc.get_count() < 16) && (ram.get_val_at(pc.get_count() != 15))) {

            if(this->get_clocks() < 6) {
                this->write = this->read = nullptr;
                if (this->get_clk()) {
                    if (this->get_activated(Cp));
                    if (this->get_activated(Ep));
                    if (this->get_inactivated(nLm))this->write = this->rem.get_ptr_adress();
                    if (this->get_inactivated(nCE));
                    if (this->get_inactivated(nLi))this->write = this->I.get_dados_adress();
                    if (this->get_inactivated(nEi))this->read = this->I.get_dados_adress();
                    if (this->get_inactivated(nLa))this->write = this->A.get_dados_adress();
                    if (this->get_activated(Ea))this->read = this->A.get_dados_adress();
                    if (this->get_activated(Su))this->ops.reverse_op();
                    if (this->get_activated(Eu))this->read = this->ops.get_dados_adress();
                    if (this->get_inactivated(nLb))this->write = this->B.get_dados_adress();
                    if (this->get_inactivated(nLo))this->write = this->O.get_dados_adress();
                    if (this->get_activated(IncDec))this->ops.set_modo(IncDec);
                    if (this->get_activated(RDnWR))this->read = this->ram.get_mem_adress_at_ptr();
                    else this->write = this->ram.get_mem_adress_at_ptr();
                    if (this->get_activated(Mul))this->ops.set_modo(Mul);
                    if (this->get_activated(Lp))this->write = this->pc.get_count_adress();
                    if (this->get_clear());
                    this->clocking();
                    
                }
                this->ops.ativar();
                if (this->write && this->read)*this->write = *this->read;
                
                this->clks();
            }
            this->clocking_reset();
            return false;
        }
        return true;
    }
};
