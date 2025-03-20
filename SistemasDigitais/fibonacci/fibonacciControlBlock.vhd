library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity  fibonacciControlBlock is
        port(
            clock, clear: in std_logic;
            ctrl1, ctrl2, ctrl3, ctrl4, ctrl5, ctrl6, ctrl7, ctrl8, ctrl9: out std_logic;
            stt1, stt2: in std_logic;
			iniciar: in std_logic;
			pronto: out std_logic
        );
end entity;

architecture BC of fibonacciControlBlock is
	type State is (S0, S1, S2, S3, S4, S5, S6);
	signal currentState, nextState: State;
begin
	-- NextState Logic
	--
	process(stt1, stt2, iniciar, currentState) is
	begin
	    nextState <= S0; -- caso de tudo errado
	
	    if currentState = S0 then
	        if iniciar = '0' then
	            nextState <= S0;
	        else
	            nextState <= S1;
	        end if;
	    
	    elsif currentState = S1 then
	        if stt1 = '1' then
	            nextState <= S2;
	        else
	            nextState <= S3;
	        end if;
	    
	    elsif currentState = S2 then
	        nextState <= S0;
	    
	    elsif currentState = S3 then
	        nextState <= S4;
	    
	    elsif currentState = S4 then
	        if stt2 = '1' then
	            nextState <= S5;
	        else
	            nextState <= S0;
	        end if;
	    
	    elsif currentState = S5 then
	        nextState <= S6;
	    
	    else -- currentState = S6 then
	        nextState <= S4;
	        
	    end if;
	    
	end process;
	-- COMPLETE
	--
	-- L01: unsigned int Fibonacci(unsigned int n) {
	-- L02: unsigned int res, i, t1, t2;  // declarations only
	-- L03: if (n <= 2)
	-- L04:     res=1;
	-- L05: else
	-- L06:      t1 = 1;
	-- L07:      t2 = 1;
	-- L08:      res = 2;
	-- L09:      i=3;
	-- L10:      while (i<n)
	-- L11:            t1 = t2;
	-- L12:            t2 = res;
	-- L13:            res = t1+t2;      
	-- L14:            i = i+1;
	-- L15: return res;
	
	-- L0: declara
	-- L1: if (n <= 2)
	-- L2:      res =1;
	-- L3: t1=1;t2=1;res=2;i=3
	-- L4: while (i<n)
	-- L5:      t1=t2;t2=res;
	-- L6:      res=t1+t2;i=i+1
	
	
	-- State Register
	process(clock, clear) is
	begin
		if clear='1' then
				currentState <= S0;-- COMPLETE (Estado inicial);
		elsif rising_edge(clock) then
				currentState <= nextState;
		end if;
	end process;
	
	-- Output Logic
	--
	ctrl1 <=
	    '1' when currentState = S3 else
	    '0';
	
	ctrl2 <=
	    '1' when currentState = S6 else
	    '0';
	
	ctrl3 <=
	    '1' when currentState = S3 else
	    '0';
	
	ctrl4 <=
	    '1' when currentState = S5 else
	    '0';
	
	ctrl5 <=
	    '1' when currentState = S3 else
	    '0';
	
	ctrl6 <=
	    '1' when currentState = S5 else
	    '0';
	
	ctrl7 <=
	    '1' when currentState = S2 else
	    '0';
	
	ctrl8 <=
	    '1' when currentState = S3 else
	    '0';
	
	ctrl9 <=
	    '1' when currentState = S6 else
	    '0';
	
	pronto <=
	    '1' when currentState = S0 else
	    '0';
	
	-- COMPLETE
	--
	-- L01: unsigned int Fibonacci(unsigned int n) {
	-- L02: unsigned int res, i, t1, t2;  // declarations only
	-- L03: if (n <= 2)
	-- L04:     res=1;
	-- L05: else
	-- L06:      t1 = 1;
	-- L07:      t2 = 1;
	-- L08:      res = 2;
	-- L09:      i=3;
	-- L10:      while (i<n)
	-- L11:            t1 = t2;
	-- L12:            t2 = res;
	-- L13:            res = t1+t2;      
	-- L14:            i = i+1;
	-- L15: return res;
	-- n<=2    ---> stt1
	-- i<n       ---> stt2
	-- i=3         ---> ctrl1
    -- i=i+1      ---> ctrl2
	--  t1 = 1     ---> ctrl3
	--  t1 = t2    ---> ctrl4 
	-- t2=1       ---> ctrl5
    -- t2=res    ---> ctrl6
	-- res = 1         ---> ctrl7
    -- res = 2         --->  ctrl8
    -- res = t1+t2   --->  ctrl9	
end architecture;