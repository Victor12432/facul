-- Descreva um circuito correspondente a um codificador de código gray de width bits. 
-- Esse codificador recebe um valor binário de width bits na entrada (binInput) e devolve o código gray correspondente na saída (grayOutput), também em width bits.
--Um exemplo de tabela-verdade da correspondência dos códigos binários e gray para o caso específico 3 bits é mostrado a seguir:

-- binInput	    grayOutput		binInput	grayOutput
-- 000	        000		        100	        110
-- 001	        001		        101	        111
-- 010	        011		        110	        101
-- 011	        010		        111	        100
-- Da análise dessas tabelas-verdade pode-se chegar à seguinte regra geral para descrição de cada bit do código gray (G) corresponde a um valor binário (B):

-- G[i] = B[i] xor B[i+1]

-- Não altere a descrição da entidade, apenas inclua possíveis declarações e comandos concorrentes na arquitetura da entidade. O uso de processos não é permitido.

library ieee;
use ieee.std_logic_1164.all;

entity grayEncoder is
	generic(width: natural);
	port(	binInput: in std_logic_vector(width-1 downto 0);
			grayOutput: out std_logic_vector(width-1 downto 0) );
end entity;

architecture concurrent_behav0 of grayEncoder is
begin
    COUNT: for i in 0 to width-2 generate
        grayOutput(i) <= binInput(i) xor binInput(i+1);
    end generate;
    grayOutput(width-1) <= binInput(width-1);
end architecture;

