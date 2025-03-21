--modulo m:
-- Complete abaixo com o nome dos alunos que fazem esta avaliacao (sem caracteres especiais nos nomes, como acentos)
-- ALUNO 1:
-- ALUNO 2:

library ieee;
use ieee.std_logic_1164.all;
use ieee.math_real.all;
use ieee.numeric_std.all;

entity moduleCounter is
	generic(	module: positive := 60;
				generateLoad: boolean := true;
				generateEnb: boolean := true;
				generateInc: boolean := true;
				resetValue: integer := 0 );
	port(	-- control
			clock, reset: in std_logic;
			load, enb, inc: in std_logic;
			-- data
			input: in std_logic_vector(integer(ceil(log2(real(module))))-1 downto 0);
			output: out std_logic_vector(integer(ceil(log2(real(module))))-1 downto 0)	);
end entity;


architecture behav0 of moduleCounter is
    -- Nao altere as duas linhas abaixo
    subtype state is unsigned(integer(ceil(log2(real(module))))-1 downto 0);
    signal nextState, currentState: state;
    -- COMPLETE AQUI, SE NECESSARIO
    signal temp0, temp1, temp2: state;
    signal sum, dim: state;
begin
	-- next-state logic (DO NOT CHANGE OR REMOVE THIS LINE)
	-- COMPLETE
	sum <= currentState + 1;
	dim <= currentState - 1;
	genInc: if generateInc generate
	    temp2 <=
	        sum when (inc = '1') and (currentState < module - 1) else
	        to_unsigned(0, temp2'length) when (inc = '1') else
	        dim when (inc = '0') and (currentState > 0) else
	        to_unsigned(module-1, temp2'length);
	end generate;
	notInc: if not generateInc generate
	    temp2 <=
	        sum when sum < module else
	        to_unsigned(0, temp2'length);
	end generate;
	
	
	genEnb: if generateEnb generate
	    temp1 <=
	        temp2 when enb = '1' else
	        currentState;
	end generate;
	notEnb: if not generateEnb generate
	    temp1 <= temp2;    
	end generate;
	
	
	genLoad: if generateLoad generate
	    temp0 <=
	        unsigned(input) when load = '1' else
	        temp1;
	end generate;
	notLoad: if not GenerateLoad generate
	    temp0 <= temp1;
	end generate;
	
	nextState <= temp0;
	-- end-next-state logic (DO NOT CHANGE OR REMOVE THIS LINE)
	
	-- memory register (DO NOT CHANGE OR REMOVE THIS LINE)
	process(clock, reset) is
	begin
		if reset='1' then
			currentState <= (to_unsigned(resetValue, currentState'length));
		elsif rising_edge(clock) then
			currentState <= nextState;
		end if;
	end process;
	-- memory register (DO NOT CHANGE OR REMOVE THIS LINE)
	
	
	-- output-logic (DO NOT CHANGE OR REMOVE THIS LINE)
    -- COMPLETE
    output <= std_logic_vector(currentState);
    -- end-output-logic (DO NOT CHANGE OR REMOVE THIS LINE)
end architecture