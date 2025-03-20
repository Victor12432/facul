library ieee;
use ieee.std_logic_1164.all;

entity divisaoInt is
    generic(largDividendo: integer;
            largDivisor: integer);
    port (  
        clock, iniciar: in std_logic;
        dividendo: in std_logic_vector(largDividendo-1 downto 0);
        divisor: in std_logic_vector(largDivisor-1 downto 0);
        quociente: out std_logic_vector(largDividendo-1 downto 0);
        resto: out std_logic_vector(largDivisor-1 downto 0);
        retorno: out std_logic);
end entity;

architecture SD of divisaoInt is

    component blocoControle is
        port(
            -- control in
            clock, stt1, iniciar: in std_logic;
            -- control out
            retorno, cmd1, cmd2: out std_logic
        );
    end component;
    
    component blocoOperativo is
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
    end component;

    signal stt1: std_logic;
    signal cmd1, cmd2: std_logic;
begin

    bc: blocoControle
        port map(
            clock => clock,
            iniciar => iniciar,
            stt1 => stt1,
            retorno => retorno,
            cmd1 => cmd1,
            cmd2 => cmd2
        );
    
    bo: blocoOperativo
        generic map(
            largDividendo => largDividendo,
            largDivisor => largDivisor
        )
        port map(
            dividendo => dividendo,
            divisor => divisor,
            clock => clock,
            cmd1 => cmd1,
            cmd2 => cmd2,
            quociente => quociente,
            resto => resto,
            stt1 => stt1
        );
        
end architecture;