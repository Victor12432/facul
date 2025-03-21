-- COMPLETE COM O NOME COMPLETO DOS ALUNOS QUE FAZEM ESTA AVALIACAO
-- Aluno 1:
-- Aluno 2:

library ieee;
use ieee.std_logic_1164.all;

entity shifterRotator is
	generic(
		width: positive;
		isShifter: boolean;
		isLogical: boolean;
		toLeft: boolean;
		bitsToShift: positive
	);
	port(
		input: in std_logic_vector(width-1 downto 0);
		output: out std_logic_vector(width-1 downto 0)
	);
	begin
		assert (bitsToShift < width) severity error;
end entity;

architecture behav of shifterRotator is
    -- Complete
	signal temp: std_logic_vector(width-1 downto 0);
	signal zero: std_logic_vector(width-1 downto 0) := (others => '0');
begin
    -- Complete
	temp <= (others => (input(width-1)));
	Desclocador: if isShifter generate
		
		DesloEsqueda: if toLeft generate
			output <= input(width-1 downto 0);
		end generate;

		DesloDireita: if not toLeft generate

			Logico: if isLogical generate
				output <= input(width-1 downto 0);
			end generate;

			Aritmerico: if not isLogical generate
				output <= input(width-1 downto 0);
			end generate;

		end generate;
	
	end generate;

	Rotacionador: if not isShifter generate
		
		RotaEsqueda: if toLeft generate

			output <= input(width-1 downto 0);
		end generate;

		RotaDireita: if not toLeft generate

			output <= input(width-1 downto 0);;

		end generate;
	
	end generate;

end architecture; 