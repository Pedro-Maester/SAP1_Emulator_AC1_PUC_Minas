#pragma once 


#ifdef SAPLOGIC_EXPORTS
#define SAPLOGIC_API __declspec(dllexport)
#else
#define SAPLOGIC_API __declspec(dllimport)
#endif


extern "C" SAPLOGIC_API void Create_SAP();

extern "C" SAPLOGIC_API void Delete_SAP();

extern "C" SAPLOGIC_API unsigned short  get_instruction();

extern "C" SAPLOGIC_API const unsigned char get_N_chips();

extern "C" SAPLOGIC_API const unsigned short get_rom_at(unsigned char i);

extern "C" SAPLOGIC_API const unsigned short get_rom_ins_adress_at(unsigned char i);

extern "C" SAPLOGIC_API const unsigned short get_rom_ins_adress_at_ptr();

extern "C" SAPLOGIC_API const unsigned char get_ram_tam();

extern "C" SAPLOGIC_API const unsigned char get_rom_ins_tam();

extern "C" SAPLOGIC_API const unsigned char get_rom_code_tam();

extern "C" SAPLOGIC_API bool get_working_clock();

extern "C" SAPLOGIC_API unsigned char get_CP_data();

extern "C" SAPLOGIC_API unsigned char get_CP_less_data();

extern "C" SAPLOGIC_API unsigned char get_CP_most_data();

extern "C" SAPLOGIC_API unsigned char get_A_data();

extern "C" SAPLOGIC_API unsigned char get_A_less_data();

extern "C" SAPLOGIC_API unsigned char get_A_most_data();

extern "C" SAPLOGIC_API unsigned char get_B_data();

extern "C" SAPLOGIC_API unsigned char get_B_less_data();

extern "C" SAPLOGIC_API unsigned char get_B_most_data();

extern "C" SAPLOGIC_API unsigned char get_I_data();

extern "C" SAPLOGIC_API unsigned char get_I_less_data();

extern "C" SAPLOGIC_API unsigned char get_I_most_data();

extern "C" SAPLOGIC_API unsigned char get_O_data();

extern "C" SAPLOGIC_API unsigned char get_rem_data();

extern "C" SAPLOGIC_API unsigned char get_ri_data();

extern "C" SAPLOGIC_API unsigned char get_ula_data();

extern "C" SAPLOGIC_API unsigned char get_ula_less_data();

extern "C" SAPLOGIC_API unsigned char get_ula_most_data();

extern "C" SAPLOGIC_API unsigned char get_rem_less_data();

extern "C" SAPLOGIC_API unsigned char get_ri_less_data();

extern "C" SAPLOGIC_API unsigned char get_rem_most_data();

extern "C" SAPLOGIC_API unsigned char get_ri_most_data();

extern "C" SAPLOGIC_API unsigned char get_ram_at_ptr();

extern "C" SAPLOGIC_API unsigned char get_ram_less_at_ptr();

extern "C" SAPLOGIC_API unsigned char get_ram_most_at_ptr();

extern "C" SAPLOGIC_API unsigned char get_ram_at(unsigned char i);

extern "C" SAPLOGIC_API unsigned char get_curr_reading_chip();

extern "C" SAPLOGIC_API unsigned char get_curr_writing_chip();

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

extern "C" SAPLOGIC_API void set_input_data(unsigned char data);

extern "C" SAPLOGIC_API void update_ram(unsigned char i, unsigned char hs);