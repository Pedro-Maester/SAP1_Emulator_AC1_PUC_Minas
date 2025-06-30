enum ins_id { Lp, Ein, RDnWR, IncDec, nLo, nLb, Eu, Su, Ea, nLa, nEi, nLi, nCE, nLm, Ep, Cp };//{Cp, Ep, nLm, nCE, nLi, nEi, nLa, Ea, Su, Eu, nLb, nLo, IncDec, RDnWR, Mul, Lp};
enum chips { CP, INP,REM,RAM,RI,ACC,ULA,BCC,OUTP};
//enum code { lda, add, sub, inc, dec, inp, jmp, sto, out = 14, hlt = 15 };
/*extern "C" SAPLOGIC_API void Create();

extern "C" SAPLOGIC_API void Delete();

extern "C" SAPLOGIC_API unsigned short  get_instruction();

extern "C" SAPLOGIC_API const unsigned short get_rom_at(unsigned char i);

extern "C" SAPLOGIC_API const unsigned char get_ram_tam();

extern "C" SAPLOGIC_API const unsigned char get_rom_ins_tam();

extern "C" SAPLOGIC_API const unsigned char get_rom_code_tam();

extern "C" SAPLOGIC_API bool get_working_clock();

extern "C" SAPLOGIC_API unsigned char get_CP_data();

extern "C" SAPLOGIC_API unsigned char get_A_data();

extern "C" SAPLOGIC_API unsigned char get_B_data();

extern "C" SAPLOGIC_API unsigned char get_I_data();

extern "C" SAPLOGIC_API unsigned char get_O_data();

extern "C" SAPLOGIC_API unsigned char get_rem_data();

extern "C" SAPLOGIC_API unsigned char get_ri_data();

extern "C" SAPLOGIC_API unsigned char get_ula_data();

extern "C" SAPLOGIC_API unsigned char get_rem_less_data();

extern "C" SAPLOGIC_API unsigned char get_ri_less_data();

extern "C" SAPLOGIC_API unsigned char get_rem_most_data();

extern "C" SAPLOGIC_API unsigned char get_ri_most_data();

extern "C" SAPLOGIC_API unsigned char get_ram_at_ptr();

extern "C" SAPLOGIC_API unsigned char get_ram_at(unsigned char i);

extern "C" SAPLOGIC_API bool get_activated_Cp();

extern "C" SAPLOGIC_API bool get_activated_Ep();

extern "C" SAPLOGIC_API bool get_activated_nLm();

extern "C" SAPLOGIC_API bool get_activated_nCE();

extern "C" SAPLOGIC_API bool get_activated_nLi();

extern "C" SAPLOGIC_API bool get_activated_nEi();

extern "C" SAPLOGIC_API bool get_activated_nLa();

extern "C" SAPLOGIC_API bool get_activated_Ea();

extern "C" SAPLOGIC_API bool get_activated_Su();

extern "C" SAPLOGIC_API bool get_activated_Eu();

extern "C" SAPLOGIC_API bool get_activated_nLb();

extern "C" SAPLOGIC_API bool get_activated_nLo();

extern "C" SAPLOGIC_API bool get_activated_IncDec();

extern "C" SAPLOGIC_API bool get_activated_RDnWR();

extern "C" SAPLOGIC_API bool get_activated_Ein();

extern "C" SAPLOGIC_API bool get_activated_Lp();

extern "C" SAPLOGIC_API void clk();

extern "C" SAPLOGIC_API void start();

extern "C" SAPLOGIC_API void stop();

extern "C" SAPLOGIC_API void clear();

extern "C" SAPLOGIC_API void update_ram(unsigned char i , const char* hs);*/
class Register {
protected:
	unsigned char data;
public:
	Register();
	void Count();
	unsigned char* get_data_adress();
	unsigned char get_data_val();
	unsigned char get_most_val_bits();
	unsigned char get_less_val_bits();
	void set_value(unsigned char data);
	void clear();
};

class Ula:public Register {
	unsigned char* a_input = nullptr;
	unsigned char* b_input = nullptr;
	bool su = false;
	unsigned char modo = 0;
public:
	void ativar();
	Ula(unsigned char* a, unsigned char* b);
	void reverse_op();
	void set_modo(unsigned char m);
	
	void sum();
	void sub();
	

	void inc();
	void dec();
	
};

class Ram {
	unsigned char mem[16] = { 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 };
	unsigned char* ptr = nullptr;
	const unsigned char tam = 16;
public:
	Ram(unsigned char* ptr);
	unsigned char get_ptr_val();
	unsigned char* get_ptr_adress();
	unsigned char get_val_at_ptr();
	unsigned char get_val_at(unsigned char i);
	const unsigned char get_tam();
	void set_val_at(unsigned char i, unsigned char val);
	void set_val_at_by_str(unsigned char i, const char* hs);
	void clear();
	void cpy(Ram* other);

	
	 
};


class Rom {
	unsigned char clocks = 0;
	const unsigned char tempo = 6;
	const unsigned char fetch_clocks = 3;
	const unsigned char tam_ins = 16;
	const unsigned char ins_adress[16] = { 0x3,0x6,0x9,0x10,0x13,0x16,0x19,0x1c,0x00,0x00,0x00,0x00,0x00,0xc,0x00 };//{ 0x3,0x6,0x9,0xc,0xf,0x12,0x15,0x18,0x00,0x00,0x00,0x00,0x00,0x0c,0x00 };
	const unsigned char tam_codes = 32;
	const unsigned short macro_codes[32]=  { 0x5e30, 0xbe30, 0x2634, 0x1a30, 0x2c34, 0x3e30, 0x1a30, 0x2e14,
											0x3c70, 0x1a30, 0x2e14, 0x3cf0, 0x3f20, 0x3e30, 0x3e30, 0x0000,
											0x3c78, 0x3e30, 0x3e30, 0x3cf8, 0x3e30, 0x3e30 ,0x3c32, 0x3e30,
											0x3e30, 0x3a31, 0x3e30, 0x3e30, 0x1a30, 0x2f30, 0x3e30, 0x0000 };
	unsigned char* ptr = nullptr;
public:
	Rom(unsigned char* ptr);
	unsigned char get_ptr_val();
	const unsigned short get_instruction();
	const unsigned short get_instruction_at(unsigned char i);
	const unsigned char get_ins_tam();
	const unsigned char get_code_tam();
	const unsigned char get_ins_adress_at_ptr();
	const unsigned char get_ins_adress_at(unsigned char i);
	void clocar();
};

class SAP_Logic {
private:
	bool clock_working = true;
	const unsigned char N_chips = 9;
	unsigned short instruction = 0x5e30;
	unsigned char *reading, *writing;
	unsigned char curr_read = 0;
	unsigned char curr_write = 0;
	Register cp, A, B, I, O, rem, ri;
	Ula ula = Ula(this->A.get_data_adress(), this->B.get_data_adress());
	Ram ram = Ram(this->rem.get_data_adress());
	Ram og = Ram(this->rem.get_data_adress());
	Rom rom = Rom(this->ri.get_data_adress());

	void update_instruction();
public:
	SAP_Logic();
	const unsigned char get_N_chips();
	const unsigned char get_ram_tam();
	const unsigned char get_rom_ins_tam();
	const unsigned char get_rom_code_tam();
	const unsigned char get_ins_adress_at_ptr();
	const unsigned char get_ins_adress_at(unsigned char i);

	unsigned char get_CP_data();
	unsigned char get_A_data();
	unsigned char get_B_data();
	unsigned char get_I_data();
	unsigned char get_O_data();
	unsigned char get_rem_data();
	unsigned char get_ri_data();
	unsigned char get_ula_data();
	unsigned char get_rem_less_data();
	unsigned char get_ri_less_data();
	unsigned char get_rem_most_data();
	unsigned char get_ri_most_data();
	unsigned char get_ram_at_ptr();
	unsigned char get_ram_at(unsigned char i);
	unsigned char get_curr_reading_chip();
	unsigned char get_curr_writing_chip();
	
	const unsigned short get_rom_at(unsigned char i);

	unsigned short get_instruction();

	bool get_clock_working();
	bool get_activated(ins_id i);
	bool get_inactivated(ins_id i);
	/*
	bool get_Cp_activated() {
		return this->get_activated(Cp);
	}
	bool get_Ep_activated() {
		return this->get_activated(Ep);
	}
	bool get_nLm_activated() {
		return this->get_inactivated(nLm);
	}
	bool get_nCE_activated() {
		return this->get_inactivated(nCE);
	}
	bool get_nLi_activated() {
		return this->get_inactivated(nLi);
	}
	bool get_nEi_activated() {
		return this->get_inactivated(nEi);
	}
	bool get_nLa_activated() {
		return this->get_inactivated(nLa);
	}
	bool get_Ea_activated() {
		return this->get_activated(Ea);
	}
	bool get_Su_activated() {
		return this->get_activated(Su);
	}
	bool get_Eu_activated() {
		return this->get_activated(Eu);
	}
	bool get_nLb_activated() {
		return this->get_inactivated(nLb);
	}
	bool get_nLo_activated() {
		return this->get_activated(nLo);
	}
	bool get_IncDec_activated() {
		return this->get_activated(IncDec);
	}
	bool get_RDnWR_activated() {
		return this->get_activated(RDnWR);
	}
	bool get_Ein_activated() {
		return this->get_activated(Ein);
	}
	bool get_Lp_activated() {
		return this->get_activated(Lp);
	}*/

	void clk();

	void start();
	void stop();
	void set_input_data(unsigned char data);
	void clear();
	void update_ram(unsigned char i, unsigned char hs);



}; 
