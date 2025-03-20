library IEEE;
use ieee.std_logic_1164.all;

entity extensaoSinal is
	generic(	larguraSaida:  integer;
				larguraEntrada: integer);
	port(
		entrada:  in  std_logic_vector(larguraEntrada-1 downto 0);
		saida: out std_logic_vector(larguraSaida-1 downto 0)
	);
end entity;


architecture behavioral of extensaoSinal is 
begin
    -- COMPLETE
    saida <= (larguraSaida-1 downto larguraSaida-larguraEntrada => entrada(larguraEntrada-1)) & entrada;
end architecture;