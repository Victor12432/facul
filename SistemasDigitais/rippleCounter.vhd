ripple parametrizavel:
-- Complete abaixo com o nome dos alunos que fazem esta avaliacao (sem caracteres especiais nos nomes, como acentos)
-- ALUNO 1: Thiago Seberino Pereira
-- ALUNO 2:

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity rippleCounter is
	generic(	width: positive := 8;
				generateLoad: boolean := true;
				generateEnb: boolean := true;
				generateInc: boolean := true);
	port(	-- control
			clock, reset: in std_logic;
			load, enb, inc: in std_logic;
			-- data
			input: in std_logic_vector(width-1 downto 0);
			output: out std_logic_vector(width-1 downto 0)	);
end entity;


architecture behav0 of rippleCounter is
    -- Nao altere as duas linhas abaixo
    subtype state is unsigned(width-1 downto 0);
    signal nextState, currentState: state;
    -- COMPLETE AQUI, SE NECESSARIO
    signal temp0, temp1, temp2: state;
    signal msb: integer := -1;
begin
	-- next-state logic (DO NOT CHANGE OR REMOVE THIS LINE)
	-- COMPLETE
	
	genInc: if generateInc generate
	
	    process(currentState, inc) is
	    begin
	        msb <= -1;
	        if inc = '1' then
    	        for i in width-1 downto 0 loop
    	            if currentState(i) = '1' and i = width-1 then
    	                msb <= 0;
    	                exit;
    	            elsif currentState(i) = '1' then
    	                msb <= i+1;
    	                exit;
    	            end if;
    	        end loop;
    	    else
    	        for i in width-1 downto 0 loop
    	            if currentState(i) = '1' and i = 0 then
    	                msb <= width-1;
    	                exit;
    	            elsif currentState(i) = '1' then
    	                msb <= i-1;
    	                exit;
    	            end if;
    	        end loop;
    	    end if;
	    end process;
	
	    process(msb) is
	    begin
	        for j in width-1 downto 0 loop
	            if j = msb then
	                temp2(j) <= '1';
	            else
	                temp2(j) <= '0';
	            end if;
	        end loop;
	    end process;
	    
	end generate;
	notInc: if not generateInc generate
	    
	    process(currentState, inc) is
	    begin
	        msb <= -1;
	        for i in width-1 downto 0 loop
	            if currentState(i) = '1' and i = width-1 then
	                msb <= 0;
	                exit;
	            elsif currentState(i) = '1' then
	                msb <= i+1;
	                exit;
	            end if;
	        end loop;
	        
	    end process;
	
	    process(msb) is
	    begin
	        for j in width-1 downto 0 loop
	            if j = msb then
	                temp2(j) <= '1';
	            else
	                temp2(j) <= '0';
	            end if;
	        end loop;
	    end process;
	    
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
	        temp1 when load = '0' else
	        unsigned(input);
	end generate;
	notLoad: if not generateLoad generate
	    temp0 <= temp1;
	end generate;
	
	nextState <= temp0;
	-- end-next-state logic (DO NOT CHANGE OR REMOVE THIS LINE)
	
	
	-- memory register (DO NOT CHANGE OR REMOVE THIS LINE)
	process(clock, reset) is
	begin
		if reset='1' then
			currentState <= to_unsigned(1, currentState'length);
		elsif rising_edge(clock) then
			currentState <= nextState;
		end if;
	end process;
	-- memory register (DO NOT CHANGE OR REMOVE THIS LINE)
	
	
	-- output-logic (DO NOT CHANGE OR REMOVE THIS LINE)
    -- COMPLETE
    output <= std_logic_vector(currentState);
    -- end-output-logic (DO NOT CHANGE OR REMOVE THIS LINE)
end architecture;