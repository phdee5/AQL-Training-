module tb();
logic IN1,IN2,IN3,IN4,IN5,IN6,IN7,IN8,IN9,IN10,IN11,IN12,IN13,IN14,IN15,IN16,S0,S1,S2,S3,OUT;
mux16x1 m(IN1,IN2,IN3,IN4,IN5,IN6,IN7,IN8,IN9,IN10,IN11,IN12,IN13,IN14,IN15,IN16,S0,S1,S2,S3,OUT);
initial begin
for(int i=0; i<1048576; i++)
begin
	{IN1,IN2,IN3,IN4,IN5,IN6,IN7,IN8,IN9,IN10,IN11,IN12,IN13,IN14,IN15,IN16,S0,S1,S2,S3}=i;
	#10;
end

end
endmodule
