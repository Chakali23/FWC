
.include "/storage/self/primary/Documents/Assembly/m328pdef.inc"

SBI DDRB,5
ldi r16,0b00000000
out DDRD,r16

k:in r16,PIND
mov r17,r16

andi r16,0b00000100
LSR r16
LSR r16
ldi r18,0b00000001
eor r16,r18

mov r18,r17
andi r18,0b00001000
LSR r18
LSR r18
LSR r18

mov r19,r17
andi r19,0b00010000
LSR r19
LSR r19
LSR r19
LSR r19
ldi r20,0b00000001
eor r19,r20

or r16,r18
and r16,r19
LSL r16
LSL r16
LSL r16
LSL r16
LSL r16
out PORTB,r16
rjmp k

