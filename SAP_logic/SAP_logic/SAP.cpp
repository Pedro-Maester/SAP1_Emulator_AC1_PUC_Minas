// SAPLOGIC.cpp : Defines the exported functions for the DLL.
#include "pch.h" // use stdafx.h in Visual Studio 2017 and earlier

#include "SAP.h"
#include "SAP_Logic.h"

static SAP_Logic* sap = nullptr;


void Create_SAP() {
	Delete_SAP();
	sap = new SAP_Logic();
}

void Delete_SAP() {
	if (sap != nullptr)delete sap;
}

unsigned short get_instruction() {
	return sap->get_instruction();
}

const unsigned short get_rom_at(unsigned char i) {
	return sap->get_rom_at(i);
}

const unsigned char get_N_chips() {
	return sap->get_N_chips();
}

unsigned char get_curr_reading_chip() {
	return sap->get_curr_reading_chip();
}

unsigned char get_curr_writing_chip() {
	return sap->get_curr_writing_chip();
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

const unsigned short get_rom_ins_adress_at(unsigned char i) {
	return sap->get_ins_adress_at(i);
}

const unsigned short get_rom_ins_adress_at_ptr() {
	return sap->get_ins_adress_at_ptr();
}

bool get_working_clock() {
	return sap->get_clock_working();
}

unsigned char get_CP_data() {
	return sap->get_CP_data();
}

unsigned char get_CP_less_data() {
	return sap->get_CP_data()%16;
}

unsigned char get_CP_most_data() {
	return sap->get_CP_data()>>4;
}


unsigned char get_A_data() {
	return sap->get_A_data();
}

unsigned char get_A_less_data() {
	return sap->get_A_data() % 16;
}

unsigned char get_A_most_data() {
	return sap->get_A_data() >> 4;
}

unsigned char get_B_data() {
	return sap->get_B_data();
}

unsigned char get_B_less_data() {
	return sap->get_B_data() % 16;
}

unsigned char get_B_most_data() {
	return sap->get_B_data() >> 4;
}

unsigned char get_I_data() {
	return sap->get_I_data();
}

unsigned char get_I_less_data() {
	return sap->get_I_data() % 16;
}

unsigned char get_I_most_data() {
	return sap->get_I_data() >> 4;
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

unsigned char get_ula_less_data() {
	return sap->get_ula_data() % 16;
}

unsigned char get_ula_most_data() {
	return sap->get_ula_data() >> 4;
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

void set_input_data(unsigned char data) {
	sap->set_input_data(data);
}

void update_ram(unsigned char i, unsigned char hs) {
	sap->update_ram(i, hs);
}
