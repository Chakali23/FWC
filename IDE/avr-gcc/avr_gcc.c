#include <avr/io.h>
#include<stdbool.h>

int main(void)
{
	bool F;
	bool a0 = 0,a1 = 0,b0 = 0,b1 = 0;

	DDRD |=0b00000000; // declares the inputs as 2,3,6,7
	DDRB = (1<<PINB5); // declared 13 pin as output
	PORTD |= 0b11001100; // pullup inputs

	while(1)
	{
		a0 = (PIND & (1<<PIND3)) == (1<<PIND3);
		a1 = (PIND & (1<<PIND2)) == (1<<PIND2);
		b0 = (PIND & (1<<PIND7)) == (1<<PIND7);
		b1 = (PIND & (1<<PIND6)) == (1<<PIND6);

		F = (a1&!b1) | (a1&a0&!b0) | (a0&!b0&!b1);

		if(F)
		{
			PORTB = (1<<PINB5);
		}

		else
		{
			PORTB = !(1<<PINB5);
		}
	}
	return 0;
}
