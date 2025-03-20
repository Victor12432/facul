library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity blocoOperativo is
    generic(
        largDividendo: integer;
        largDivisor: integer
    );
    port(
        -- data in
        dividendo: in std_logic_vector(largDividendo-1 downto 0);
        divisor: in std_logic_vector(largDivisor-1 downto 0);
        -- control in
        clock, cmd1, cmd2: in std_logic;
        -- data out
        quociente: out std_logic_vector(largDividendo-1 downto 0);
        resto: out std_logic_vector(largDivisor-1 downto 0);
        -- control out
        stt1: out std_logic
    );
end entity;

architecture bhv of blocoOperativo is
    signal divd, next_divd: std_logic_vector(dividendo'range);
    signal next_quociente: std_logic_vector(quociente'range);
begin

    process(clock, cmd1, cmd2) is
    begin
        if rising_edge(clock) then
            if cmd1 = '1' then
                next_divd <= dividendo;
            elsif cmd2 = '1' then
                next_divd <= std_logic_vector(signed(next_divd) - signed(divisor));
            else
                next_divd <= next_divd;
            end if;
        end if;
    end process;
    divd <= next_divd;

    process(clock, cmd1, cmd2) is
    begin
        if rising_edge(clock) then
            if cmd1 = '1' then
                next_quociente <= std_logic_vector(to_unsigned(0, quociente'length));
            elsif cmd2 = '1' then
                next_quociente <= std_logic_vector(signed(next_quociente) + 1);
            else
                next_quociente <= next_quociente;
            end if;
        end if;
    end process;
    quociente <= next_quociente;
    
    resto <= divd;

    stt1 <=
        '1' when divd >= divisor else
        '0';
end architecture;