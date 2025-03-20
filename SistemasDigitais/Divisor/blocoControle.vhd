library ieee;
use ieee.std_logic_1164.all;

entity blocoControle is
    port(
        -- control in
        clock, stt1, iniciar: in std_logic;
        -- control out
        retorno, cmd1, cmd2: out std_logic
    );
end entity;

architecture bhv of blocoControle is
    type state is (L0, L1, L2, L3);
    signal currentState, nextState: state;
begin

    -- nextState logic
    process(currentState, iniciar, stt1) is
    begin
        if currentState = L0 then
            if iniciar = '1' then
                nextState <= L1;
            else
                nextState <= L0;
            end if;
        
        elsif currentState = L1 then
            if stt1 = '1' then
                nextState <= L2;
            else
                nextState <= L3;
            end if;
        
        elsif currentState = L2 then
            nextState <= L1;
        
        else
            nextState <= L0;
        
        end if;
        
    end process;

    -- registrador
    process(clock) is
    begin
        if rising_edge(clock) then
            currentState <= nextState;
        end if;
    end process;
    
    -- output logic
    retorno <=
        '1' when currentState = L0 else
        '0';
    
    cmd1 <=
        '1' when currentState = L0 else
        '0';
    
    cmd2 <=
        '1' when currentState = L2 else
        '0';
    
end architecture;