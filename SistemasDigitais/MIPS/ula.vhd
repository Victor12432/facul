library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity ULA is
	generic(width: positive := 16);
	port(
		op: in std_logic_vector(2 downto 0);  --000:AND , 001:OR , 010:ADD, 110:SUB, 111:SLT
		a, b: in std_logic_vector(width-1 downto 0);
		zero: out std_logic;
		res: out std_logic_vector(width-1 downto 0)
	);
end entity;

architecture Behavioral of ULA is
    -- COMPLETE (tente usar constantes inicializadas quando for util)
    constant opAnd:
    constant opOr:
    constant op
begin
    -- COMPLETE

end architecture;