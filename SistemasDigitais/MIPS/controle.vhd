library ieee;
use ieee.std_logic_1164.all;

entity Controle is
	port(
		Opcode: in std_logic_vector(5 downto 0);
		RegDst, DvCeq, DvCne, DvI, LerMem, MemParaReg, EscMem, ULAFonte, EscReg: out std_logic;
		ULAOp: out std_logic_vector(1 downto 0)
	);
end entity;

architecture comportamento of Controle is
    -- COMPLETE (tentar usar constants)
    constant r: std_logic_vector(5 downto 0) := "000000";
    constant lw: std_logic_vector(5 downto 0) := "100011";
    constant sw: std_logic_vector(5 downto 0) := "101011";
    constant beq: std_logic_vector(5 downto 0) := "000100";
    constant jump: std_logic_vector(5 downto 0) := "000010";
begin
    -- COMPLETE
    RegDst <= '1' when Opcode = r else '0';
    DvCeq <= '1' when Opcode = beq else '0';
    DvI <= '1' when Opcode = jump else '0';
    DvCne <= '0';
    LerMem <= '1' when Opcode = lw else '0';
    MemParaReg <= '1' when Opcode = lw else '0'; 
    EscMem <= '1' when Opcode = sw else '0';
    ULAFonte <= '1' when Opcode = lw or Opcode = sw else '0';
    EscReg <=  '1' when Opcode = r or Opcode = lw else '0';
    ULAOp(1) <= '1' when Opcode = r or Opcode = jump else '0';
    ULAOp(0) <= '1' when Opcode = beq else '0';
    
end architecture;  