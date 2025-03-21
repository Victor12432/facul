--codificador binario de prioridade parametrizavel:
-- COMPLETE COM O NOME COMPLETO DOS ALUNOS QUE FAZEM ESTA AVALIACAO
-- Aluno 1:
-- Aluno 2:

library ieee;
use ieee.std_logic_1164.all;
use ieee.math_real.all;
use ieee.numeric_std.all;

entity binaryEncoder is
	generic(inputWidth: positive;
			priorityMSB: boolean;
			generateValid: boolean);
	port(input: in std_logic_vector(inputWidth-1 downto 0);
		valid: out std_logic;
		output: out std_logic_vector(integer(ceil(log2(real(inputWidth))))-1 downto 0) );
end entity;

architecture behav0 of binaryEncoder is
    signal index: integer := -1;
begin
-- Complete

    process(input) is
    begin
        index <= -1;

        for i in inputWidth-1 downto 0 loop
            if input(i) = '1' then
                
                index <= i;
                    
                if priorityMSB then
                    exit;
                end if;
                    
            end if;
        end loop;
    end process;
    
    output <= (others => '0') when index = -1 else
              std_logic_vector(to_unsigned(index, output'length));
    
    genValid: if generateValid generate
        valid <= '0' when index = -1 else
                 '1';
    end generate;
    
end architecture;