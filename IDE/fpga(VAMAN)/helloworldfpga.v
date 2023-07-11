module helloworldfpga(input wire A, input wire B, output wire F);
always @(*)
begin
	F = (!(A&B));
end
endmodule
