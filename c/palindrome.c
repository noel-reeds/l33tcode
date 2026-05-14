#include <stdbool.h>
#include <math.h>
#include <stdio.h>
#include <stdint.h>

bool isPalindrome(int x) {
	if (x < 0)
		return false;
	int64_t rx = x;
	int64_t d_x = 0;
	int64_t value_x = 0;
	int64_t place_value = 1;
	while(x) {
		d_x = x % 10;
		value_x += d_x * place_value;
		if (x >= 10)
			place_value *= 10;
		x = floor(x/10);
	}
	int64_t value_rx = 0;
	int64_t d_rx = 0;
	while(place_value >= 1) {
		d_rx = rx % 10;
		value_rx += d_rx * place_value;
		rx = floor(rx/10);
		place_value = floor(place_value/10);
	}
	if (value_x != value_rx)
		return false;
	else
		return true;
}

int main() {
	if(isPalindrome(100000001))
		printf("%s\n", "true");
	else
		printf("%s\n", "false");
	return 0;
}
