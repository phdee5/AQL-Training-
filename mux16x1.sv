module mux16x1(input logic IN1,IN2,IN3,IN4,IN5,IN6,IN7,IN8,IN9,IN10,IN11,IN12,IN13,IN14,IN15,IN16,S0,S1,S2,S3,
	       output logic OUT);
logic Y1,Y2,Y3,Y4;

mux4x1 m0(.IN1(IN1),.IN2(IN2),.IN3(IN3),.IN4(IN4),.S0(S0),.S1(S1),.Y1(Y1));
mux4x1 m1(.IN1(IN5),.IN2(IN6),.IN3(IN7),.IN4(IN8),.S0(S0),.S1(S1),.Y1(Y2));
mux4x1 m2(.IN1(IN9),.IN2(IN10),.IN3(IN11),.IN4(IN12),.S0(S0),.S1(S1),.Y1(Y3));
mux4x1 m3(.IN1(IN13),.IN2(IN14),.IN3(IN15),.IN4(IN16),.S0(S0),.S1(S1),.Y1(Y4));
mux4x1 m4(.IN1(Y1),.IN2(Y2),.IN3(Y3),.IN4(Y4),.S0(S2),.S1(S3),.Y1(OUT));
endmodule
		
