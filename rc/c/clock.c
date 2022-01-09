#include <stdio.h>
#include <windows.h>

struct Clock // composite data type
{
	int hours;
	int mins;
	int secs;
}; // represents the data

void tick(struct Clock *c)
{
	c->secs+=1;
	
	if (c->secs>59)
	{
		c->mins+=1;
		c->secs=0;
	}

	if (c->mins>59)
	{
		c->hours+=1;
		c->mins=0;
	}

	if (c->hours>12)
	{
		c->hours=1;
		c->mins=0;
		c->secs=0;
	}
}

// not changing Clock
void printClock(struct Clock c) // pass by value
{
	printf("\nClock");
	printf("\n%02d:%02d:%02d",c.hours,c.mins,c.secs);
}

// may change Clock
void validate(struct Clock *c) // pass by reference
{
	if (c->hours>12 || c->mins> 60 || c->secs>60)
	{
		c->hours=0;
		c->mins=0;
		c->secs=0;
	}
}

int main()
{
	struct Clock c={10,12,23}; // creating the struct
	validate(&c);
	while(1) // loop until true
	{
		tick(&c);
		printClock(c);
		Sleep(1000); // millisecond equals second
	}
	return 0;
}