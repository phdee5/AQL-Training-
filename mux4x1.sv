module mux4x1(input logic IN1,IN2,IN3,IN4,S0,S1, output logic Y1);
always_comb
begin
	case({S1,S0})
	2'b00: Y1=IN1;
	2'b01: Y1=IN2;
	2'b10: Y1=IN3;
	2'b11: Y1=IN4;
	default Y1=1'bx;
endcase
end
endmodule

