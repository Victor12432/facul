library ieee;
use ieee.std_logic_1164.all;
-- pg364

entity ManchesterEncoder is
	port(
		-- control inputs
		clock, reset: in std_logic;
		-- data inputs
		v, d: in std_logic;
		-- control outputs
		-- data outputs
		y: out std_logic
	);
end entity;

architecture studenttry of ManchesterEncoder is
	type State is (idle, s0a, s1a, s0b, s1b);-- COMPLETE
	signal currentState, nextState: State;
begin
	-- next-state logic (DO NOT CHANGE OR REMOVE THIS LINE)
	-- COMPLETE
	process(v, d, currentState) is
	begin
	    if currentState = idle then
	        if v = '0' then
	            nextState <= idle;
	        elsif d = '1' then
	            nextState <= s1a;
	        else
	            nextState <= s0a;
	        end if;
	        
	    elsif currentState = s0a then
	        nextState <= s0b;
	    
	    elsif currentState = s0b then
	        if v = '0' then
	            nextState <= idle;
	        elsif d = '1' then
	            nextState <= s1a;
	        else
	            nextState <= s0a;
	        end if;
	    
	    elsif currentState = s1a then
	        nextState <= s1b;
	    
	    else -- currentState = s1b then
	        if v = '0' then
	            nextState <= idle;
	        elsif d = '1' then
	            nextState <= s1a;
	        else
	            nextState <= s0a;
	        end if;
	    
	    end if;
	end process;
	-- end-next-state logic (DO NOT CHANGE OR REMOVE THIS LINE)
	
	
	-- memory register (DO NOT CHANGE OR REMOVE THIS LINE)
	-- COMPLETE
	process(clock, reset) is
	begin
	    if reset = '1' then
	        currentState <= idle;
	    elsif rising_edge(clock) then
	        currentState <= nextState;
	    end if;
	end process;
	-- memory register (DO NOT CHANGE OR REMOVE THIS LINE)
	
	
	-- output-logic (DO NOT CHANGE OR REMOVE THIS LINE)
    -- COMPLETE
     y <= '1' when (currentState = s1a) or (currentState = s0b) else '0';
    -- end-output-logic (DO NOT CHANGE OR REMOVE THIS LINE)
end architecture;