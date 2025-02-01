#include <stdio.h>

int bits_len(int n)
{
	if (n == 0)
		return 0;
	int i = 0;
	while (n)
	{
		n /= 2;
		++i;
	}
	return i;
}

int max_abc(int a, int b, int c) {
	int max_a_b;

	if (a > b)
		max_a_b = a;
	else
		max_a_b = b;
	if (max_a_b < c)
		return c;
	else return max_a_b;
}
int minFlips(int a, int b, int c)
{
	int mask = 1;
	int i = 0;
	int flips = 0;
	//printf("a=%d, b=%d, c=%d, max_a_b_c=%d, bits_len=%d\n", a, b, c, max_abc(a,b,c), bits_len(max_abc(a,b,c)));
	int max = (max_abc(a,b,c));
	while (max)
	{
		flips += (c & mask) ? (a & mask) | (b & mask) : ( (!(c & mask)) && (!(b & mask)) ? 2 : 1 );

		++i;
		mask <<= 1;
		max /= 2;
	}
	return flips;
}

int main()
{
	printf("%d\n", minFlips(2, 6, 5));
	printf("%d\n", minFlips(4, 2, 7));
	printf("%d\n", minFlips(1,2,3));
	printf("%d\n", minFlips(9,10,240));
	printf("%d\n", minFlips(8,3,5));
}