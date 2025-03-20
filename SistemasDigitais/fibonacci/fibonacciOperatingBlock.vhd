library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity fibonacciOperatingBlock is
        generic(width: positive);
        port(
            clock, clear: in std_logic;
            ctrl1, ctrl2, ctrl3, ctrl4, ctrl5, ctrl6, ctrl7, ctrl8, ctrl9: in std_logic;
            stt1, stt2: out std_logic;
            n: in std_logic_vector(width-1 downto 0);
            nterm: out std_logic_vector(width-1 downto 0)
        );
end entity;

architecture structure of fibonacciOperatingBlock is
	component registerN is
	generic(	width: positive;
				generateLoad: boolean := false;
				clearValue: integer := 0 );
	port(	-- control
			clock, clear, load: in std_logic;
			-- data
			input: in std_logic_vector(width-1 downto 0);
			output: out std_logic_vector(width-1 downto 0));
	end component;
	
	component addersubtractor is
	generic(	width: positive;
			isAdder: boolean := false;
			isSubtractor: boolean := false;
			generateCout: boolean := false;
			generateOvf: boolean := false;
			fixedSecodOperand: integer := 0);
	port(	
		a, b: in std_logic_vector(width-1 downto 0);
		op: in std_logic;
		result: out std_logic_vector(width-1 downto 0);
		ovf, cout: out std_logic );
	end component;
	
	component compare is
	generic(	width: positive;
				isSigned: boolean := false;
				generateEqual: boolean := false ;
				generateLessThan: boolean := false;
				useFixedSecodOperand: boolean := false;
				fixedSecodOperand: integer := 0 );
	port(	input0, input1: in std_logic_vector(width-1 downto 0);
			lessThan, equal: out std_logic );
	end component;
	
	component multiplexer2x1 is
	generic(	width: positive );
	port(	input0, input1: in std_logic_vector(width-1 downto 0);
			sel: in std_logic;
			output: out std_logic_vector(width-1 downto 0) );
	end component;
	
	signal stt1_less, stt1_eq: std_logic;
	signal i, next_i, i_plus1, t1, next_t1, t2, next_t2, res, next_res, t1t2: std_logic_vector(width-1 downto 0);
	signal one, two, three: std_logic_vector(width-1 downto 0);
	
begin
    one <= std_logic_vector(to_unsigned(1, one'length));
    two <= std_logic_vector(to_unsigned(2, two'length));
    three <= std_logic_vector(to_unsigned(3, three'length));
    
	-- n<=2    ---> stt1
	st1: compare
	    generic map(
	        width => width,
	        isSigned => false,
	        generateEqual => true,
	        generateLessThan => true,
	        useFixedSecodOperand => true,
	        fixedSecodOperand => 2
	    )
	    port map(
	        input0 => n,
	        input1 => std_logic_vector(to_unsigned(0, width)),
	        lessThan => stt1_less,
	        equal => stt1_eq
	    );
	stt1 <= '1' when (stt1_less = '1') and (stt1_eq ='1') else '0';


	-- i<n       ---> stt2
	st2: compare
	    generic map(
	        width => width,
	        isSigned => false,
	        generateEqual => false,
	        generateLessThan => true,
	        useFixedSecodOperand => false,
	        fixedSecodOperand => 0
	    )
	    port map(
	        input0 => i,
	        input1 => n,
	        lessThan => stt2,
	        equal => open
	    );


	-- i=3         ---> ctrl1
    -- i=i+1      ---> ctrl2
    ipp: addersubtractor
        generic map(
            width => width,
            isAdder => true,
            isSubtractor => false,
            generateCout => false,
            generateOvf => false,
            FixedSecodOperand => 0
        )
        port map(
            a => i,
            b => std_logic_vector(to_unsigned(1, width)),
            op => '0',
            result => i_plus1,
            ovf => open,
            cout => open
        );
    
    process(clock, ctrl1, ctrl2) is
    begin
        if rising_edge(clock) then
            if ctrl1 = '1' then 
                next_i <= three;
            elsif ctrl2 = '1' then
                next_i <= i_plus1;
            else
                next_i <= i;
            end if;
        end if;
    end process;
    i <= one when clear = '1' else next_i;
	
	
	--  t1 = 1     ---> ctrl3
	--  t1 = t2    ---> ctrl4 
	process(clock, ctrl3, ctrl4) is
	begin
	    if rising_edge(clock) then
	        next_t1 <= t1;
	        if ctrl3 = '1' then
	            next_t1 <= one;
	        elsif ctrl4 = '1' then
	            next_t1 <= t2;
	        end if;
	    end if;
	end process;
	t1 <= one when clear = '1' else next_t1;
	    
	-- t2=1       ---> ctrl5
    -- t2=res    ---> ctrl6
    process(clock, ctrl5, ctrl6) is
    begin
        if rising_edge(clock) then
            next_t2 <= t2;
            if ctrl5 = '1' then
                next_t2 <= one;
            elsif ctrl6 = '1' then
                next_t2 <= res;
            end if;
        end if;
    end process;
    t2 <= one when clear = '1' else next_t2;
    
	-- res = 1         ---> ctrl7
    -- res = 2         --->  ctrl8
    -- res = t1+t2   --->  ctrl9
    t1pt2: addersubtractor
        generic map(
            width => width,
            isAdder => true,
            isSubtractor => false,
            generateCout => false,
            generateOvf => false,
            FixedSecodOperand => 0
        )
        port map(
            a => t1,
            b => t2,
            op => '0',
            result => t1t2,
            ovf => open,
            cout => open
        );

    process(clock, ctrl7, ctrl8, ctrl9) is
    begin
        if rising_edge(clock) then
            next_res <= res;
            if ctrl7 = '1' then
                next_res <= one;
            elsif ctrl8 = '1' then
                next_res <= two;
            elsif ctrl9 = '1' then
                next_res <= t1t2;
            end if;
        end if;
    end process;
    res <= one when clear = '1' else next_res;
	
	nterm <= res;
end architecture;