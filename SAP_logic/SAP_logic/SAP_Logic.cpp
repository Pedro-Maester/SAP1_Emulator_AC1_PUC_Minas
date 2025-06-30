#pragma once
#include "pch.h" 
#include "SAP_Logic.h"
#include <string>

/*static SAP_Logic* sap = nullptr;


void Create() {
	Delete();
	sap = new SAP_Logic();
}

void Delete() {
	if (sap != nullptr)delete sap;
}

unsigned short get_instruction() {
	return sap->get_instruction();
}

const unsigned short get_rom_at(unsigned char i) {
	return sap->get_rom_at(i);
}

const unsigned char get_ram_tam() {
	return sap->get_ram_tam();
}

const unsigned char get_rom_ins_tam() {
	return sap->get_rom_ins_tam();
}

const unsigned char get_rom_code_tam() {
	return sap->get_rom_code_tam();
}

bool get_working_clock() {
	return sap->get_clock_working();
}

unsigned char get_CP_data() {
	return sap->get_CP_data();
}

unsigned char get_A_data() {
	return sap->get_A_data();
}

unsigned char get_B_data() {
	return sap->get_B_data();
}

unsigned char get_I_data() {
	return sap->get_I_data();
}

unsigned char get_O_data() {
	return sap->get_O_data();
}

unsigned char get_rem_data() {
	return sap->get_rem_data();
}

unsigned char get_ri_data() {
	return sap->get_ri_data();
}

unsigned char get_ula_data() {
	return sap->get_ula_data();
}

unsigned char get_rem_less_data() {
	return sap->get_rem_less_data();
}

unsigned char get_ri_less_data() {
	return sap->get_ri_less_data();
}

unsigned char get_rem_most_data() {
	return sap->get_rem_most_data();
}

unsigned char get_ri_most_data() {
	return sap->get_ri_most_data();
}

unsigned char get_ram_at_ptr() {
	return sap->get_ram_at_ptr();
}

unsigned char get_ram_at(unsigned char i) {
	return sap->get_ram_at(i);
}


bool get_activated_Cp() {
	return sap->get_activated(Cp);
}

bool get_activated_Ep() {
	return sap->get_activated(Ep);
}

 bool get_activated_nLm() {
	 return sap->get_inactivated(nLm);
 }
 bool get_activated_nCE() {
	 return sap->get_inactivated(nCE);
 }

 bool get_activated_nLi() {
	 return sap->get_inactivated(nLi);
 }

 bool get_activated_nEi() {
	 return sap->get_inactivated(nEi);
 }
 bool get_activated_nLa() {
	 return sap->get_inactivated(nLa);
 }

 bool get_activated_Ea() {
	 return sap->get_activated(Ea);
 }

 bool get_activated_Su() {
	 return sap->get_activated(Su);
 }

 bool get_activated_Eu() {
	 return sap->get_activated(Eu);
 }

 bool get_activated_nLb() {
	 return sap->get_inactivated(nLb);
 }

 bool get_activated_nLo() {
	 return sap->get_inactivated(nLo);
 }

 bool get_activated_IncDec() {
	 return sap->get_activated(IncDec);
 }

 bool get_activated_RDnWR() {
	 return sap->get_activated(RDnWR);
 }

 bool get_activated_Ein() {
	 return sap->get_activated(Ein);
 }

 bool get_activated_Lp() {
	 return sap->get_activated(Lp);
 }

 void clk() {
	 sap->clk();
}

 void start() {
	 sap->start();
}

 void stop() {
	 sap->stop();
}

 void clear() {
	 sap->clear();
}

 void update_ram(unsigned char i, const char* hs) {
	 sap->update_ram(i, hs);
}*/


Register::Register() {
	this->data = 0;
}
void Register::Count() {
	this->data += 1;
}
unsigned char* Register::get_data_adress() {
	return &this->data;
}
unsigned char Register::get_data_val() {
	return this->data;
}
unsigned char Register::get_most_val_bits() {
	return this->data >> 4;
}
unsigned char Register::get_less_val_bits() {
	return this->data % 16;
}
void Register::set_value(unsigned char data) {
	this->data = data;
	return;
}

void Register::clear() {
	this->data = 0;
}

void Ula::ativar() {
	if (this->modo == IncDec) {
		if (su)this->dec();
		else this->inc();
	}
	else {
		if (su)this->sub();
		else this->sum();
	}
	this->su = false;
	this->modo = 0;
	return;
}
Ula::Ula(unsigned char* a, unsigned char* b) :a_input(a), b_input(b),modo(0),su(false) {
}
void Ula::reverse_op() {
	this->su = true;
	return;
}
void Ula::set_modo(unsigned char m) {
	this->modo = m;
}

void Ula::sum() {
	this->data = *this->a_input + *this->b_input;
}
void Ula::sub() {
	this->data = *this->a_input - *this->b_input;
}

void Ula::inc() {
	this->data = *this->a_input + 1;
}
void Ula::dec() {
	this->data = *this->a_input - 1;
}

Ram::Ram(unsigned char* ptr) {
	this->ptr = ptr;
}
unsigned char Ram::get_ptr_val() {
	return (*this->ptr)%16 ;//bits mais significativos
}
unsigned char* Ram::get_ptr_adress() {
	return &this->mem[this->get_ptr_val()];
}
unsigned char Ram::get_val_at_ptr() {
	return this->mem[this->get_ptr_val()];
}
unsigned char Ram::get_val_at(unsigned char i) {
	return this->mem[i % 16];
}

void Ram::set_val_at(unsigned char i, unsigned char val) {
	this->mem[i % 16] = val;
	return;
}
void Ram::set_val_at_by_str(unsigned char i, const char* hs) {
	this->mem[i % 16] = std::stoul(hs, nullptr, 16) % 256;
}
void Ram::clear() {
	for (unsigned char i = 0; i < 16; i += 1)this->mem[i] = 0;
}
void Ram::cpy(Ram* other) {
	for (unsigned char i = 0; i < 16; i += 1)this->mem[i] = other->get_val_at(i);
}

const unsigned char Ram::get_tam() {
	return this->tam;
}

Rom::Rom(unsigned char* ptr) {
	this->ptr = ptr;
}
unsigned char Rom::get_ptr_val() {
	return (*this->ptr)/16;
}
const unsigned short Rom::get_instruction() {
	if (this->clocks < this->fetch_clocks)return this->macro_codes[this->clocks];
	else return this->macro_codes[(this->clocks % 3 )+ this->ins_adress[this->get_ptr_val()]];
	//return this->macro_codes[(this->clocks / this->fetch_clocks) * (this->ins_adress[this->get_ptr_val()] + (this->clocks % 3))];
}

const unsigned short Rom::get_instruction_at(unsigned char i) {
	return this->macro_codes[i%this->tam_codes];
}

const unsigned char Rom::get_ins_adress_at(unsigned char i) {
	return this->ins_adress[i%16];
}

const unsigned char Rom::get_ins_adress_at_ptr() {
	return this->ins_adress[this->get_ptr_val()];
}

const unsigned char Rom::get_ins_tam() {
	return this->tam_ins;
}
const unsigned char Rom::get_code_tam() {
	return this->tam_codes;
}

void Rom::clocar() {
	this->clocks = (this->clocks + 1) % (this->tempo);
}

SAP_Logic::SAP_Logic() {

}

void SAP_Logic::update_instruction() {
	this->instruction = this->rom.get_instruction();
}
const unsigned char SAP_Logic::get_N_chips() {
	return this->N_chips;
}

const unsigned char SAP_Logic::get_ram_tam() {
	return this->ram.get_tam();
}

const unsigned char SAP_Logic::get_rom_ins_tam() {
	return this->rom.get_ins_tam();
}

const unsigned char SAP_Logic::get_rom_code_tam() {
	return this->rom.get_code_tam();
}

const unsigned char SAP_Logic::get_ins_adress_at_ptr() {
	return this->rom.get_ins_adress_at_ptr();
}
const unsigned char SAP_Logic::get_ins_adress_at(unsigned char i) {
	return this->rom.get_ins_adress_at(i);
}


unsigned char SAP_Logic::get_CP_data() {
	return this->cp.get_data_val();
}
unsigned char SAP_Logic::get_A_data() {
	return this->A.get_data_val();
}
unsigned char SAP_Logic::get_B_data() {
	return this->B.get_data_val();
}
unsigned char SAP_Logic::get_I_data() {
	return this->I.get_data_val();
}
unsigned char SAP_Logic::get_O_data() {
	return this->O.get_data_val();
}
unsigned char SAP_Logic::get_rem_data() {
	return this->rem.get_data_val();
}
unsigned char SAP_Logic::get_ri_data() {
	return this->ri.get_data_val();
}
unsigned char SAP_Logic::get_ula_data() {
	return this->ula.get_data_val();
}
unsigned char SAP_Logic::get_rem_less_data() {
	return this->rem.get_less_val_bits();
}
unsigned char SAP_Logic::get_ri_less_data() {
	return this->ri.get_less_val_bits();
}
unsigned char SAP_Logic::get_rem_most_data() {
	return this->rem.get_most_val_bits();
}
unsigned char SAP_Logic::get_ri_most_data() {
	return this->ri.get_most_val_bits();
}


unsigned char SAP_Logic::get_ram_at_ptr() {
	return this->ram.get_val_at_ptr();
}
unsigned char SAP_Logic::get_ram_at(unsigned char i) {
	return this->ram.get_val_at(i);
}

const unsigned short SAP_Logic::get_rom_at(unsigned char i) {
	return this->rom.get_instruction_at(i);
}

unsigned short SAP_Logic::get_instruction() {
	return this->instruction;
}

bool SAP_Logic::get_clock_working() {
	return this->clock_working;
}
bool SAP_Logic::get_activated(ins_id i) {
	//unsigned short n = pow(2, i);
	return ((this->instruction >> i) & 1 )==1;
}
bool SAP_Logic::get_inactivated(ins_id i) {
	//unsigned short n = pow(2, i)
	return (this->instruction >> i & 1) != 1 ;
}

unsigned char SAP_Logic::get_curr_reading_chip() {
	return this->curr_read;
}
unsigned char SAP_Logic::get_curr_writing_chip() {
	return this->curr_write;
}
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

void SAP_Logic::clk() {
	
	
	if (this->cp.get_data_val() < 16 && this->clock_working) {
		this->curr_read = this->N_chips;
		this->curr_write = this->N_chips;
		this->writing = nullptr;
		this->reading = nullptr;
		//unsigned char r = 0;
		unsigned char n_w = 0;
		//unsigned char* write = nullptr;
		//unsigned char read = 0;

		if (this->get_activated(Cp))this->cp.Count();
		if (this->get_activated(Su))this->ula.reverse_op();
		if (this->get_activated(IncDec))this->ula.set_modo(IncDec);
		if (this->get_activated(Ep)) this->reading = this->cp.get_data_adress(),this->curr_read = CP ;//read = this->cp.get_less_val_bits(),
		else {
			if (this->get_activated(Ea))this->reading = this->A.get_data_adress(), this->curr_read = ACC;//read = this->A.get_data_val(),  
			else {
				if (this->get_activated(Eu)) {
					this->ula.ativar();
					this->reading = this->ula.get_data_adress();
					this->curr_read = ULA;
				}//read = this->ula.get_data_val(), 
				else {
					if (this->get_activated(Ein)) this->reading = this->I.get_data_adress(), this->curr_read = INP;//read = this->I.get_data_val(),
					else {
						if (this->get_inactivated(nEi)) this->reading = this->ri.get_data_adress(), this->curr_read = RI;//read = this->ri.get_less_val_bits(),
						else {
							if (this->get_inactivated(nCE) && this->get_activated(RDnWR)) this->reading = this->ram.get_ptr_adress(), this->curr_read = RAM;//read = this->ram.get_ptr_val(),
						}
					}
				}
		}
		}
		if (this->reading != nullptr) {
			unsigned char r = *this->reading;
			if (this->curr_read == RI)r = r%16;
			if (this->get_inactivated(nCE) && this->get_inactivated(RDnWR))*this->ram.get_ptr_adress() = r;//*this->reading;
				if (this->get_inactivated(nLm))*this->rem.get_data_adress() = r;// *this->reading;
				if (this->get_inactivated(nLa))*this->A.get_data_adress() = r; *this->reading;
				if (this->get_inactivated(nLi))*this->ri.get_data_adress() = r; *this->reading;
				if (this->get_inactivated(nLb))*this->B.get_data_adress() = r; *this->reading;
				if (this->get_inactivated(nLo))*this->O.get_data_adress() = r; *this->reading;
				if (this->get_activated(Lp))*this->cp.get_data_adress() = r; *this->reading;
		}
		/*if (this->get_inactivated(nCE) && this->get_inactivated(RDnWR))n_w += 1;
			this->writing = this->ram.get_ptr_adress(), this->curr_write = RAM;
			if (this->get_inactivated(nLm))n_w += 1;
			//this->writing = this->rem.get_data_adress(), this->curr_write = REM;
		if (this->get_inactivated(nLa))n_w += 1; 
		//this->writing = this->A.get_data_adress(), this->curr_write = ACC;
		if (this->get_inactivated(nLi))n_w += 1; 
		//this->writing = this->ri.get_data_adress(), this->curr_write = RI;
		if (this->get_inactivated(nLb))n_w += 1; 
		//this->writing = this->B.get_data_adress(), this->curr_write = BCC;
		if (this->get_inactivated(nLo))n_w += 1; 
		//this->writing = this->O.get_data_adress(), this->curr_write = OUTP;
		if (this->get_activated(Lp))n_w += 1; 
		//this->writing = this->cp.get_data_adress(), this->curr_write = CP;
		if (n_w > 0 && this->reading != nullptr) {

			unsigned char n = 0;
			unsigned char** w = new unsigned char*[n_w];
			if (this->get_inactivated(nCE) && this->get_inactivated(RDnWR))w[n++] = this->ram.get_ptr_adress(), this->curr_write = RAM;
			if (this->get_inactivated(nLm))w[n++] = this->rem.get_data_adress(), this->curr_write = REM;
			if (this->get_inactivated(nLa))w[n++] = this->A.get_data_adress(), this->curr_write = ACC;
			if (this->get_inactivated(nLi))w[n++] = this->ri.get_data_adress(), this->curr_write = RI;
			if (this->get_inactivated(nLb))w[n++] = this->B.get_data_adress(), this->curr_write = BCC;
			if (this->get_inactivated(nLo))w[n++] = this->O.get_data_adress(), this->curr_write = OUTP;
			if (this->get_activated(Lp))w[n++] = this->cp.get_data_adress(), this->curr_write = CP;
			n = 0;
			while(n < n_w)*w[n++] = *this->reading;
		}*/

		
		
		this->update_instruction();
		
		this->clock_working = ((this->ri.get_data_val())>>4 != 0xf) && (this->cp.get_data_val() < 16);//((this->ri.get_data_val() >> 4) != 0xf) && (this->cp.get_data_val() < 16);

		//TODO: Loads
	}
	this->rom.clocar();
	return;
}

void SAP_Logic::start() {
	this->instruction = 0x5e30;
	this->cp.clear();
	this->clock_working = true;
	this->ram.cpy(&this->og);
}
void SAP_Logic::stop() {
	this->clock_working = false;
}

void SAP_Logic::clear() {
	this->og.clear();
	this->ram.clear();
	this->cp.clear();
	this->A.clear();
	this->B.clear();
	this->I.clear();
	this->O.clear();
	this->rem.clear();
	this->ri.clear();
}

void SAP_Logic::set_input_data(unsigned char data) {
	this->I.set_value(data);
}
void SAP_Logic::update_ram(unsigned char i, unsigned char hs) {
	this->og.set_val_at(i, hs);
	this->ram.cpy(&this->og);
}

