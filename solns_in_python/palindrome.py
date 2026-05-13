class Solution:
	def isPalindrome(self, x: int) -> bool:
		if x <= 0:
			return False
		rx = x
		d_x = 0
		value_x = 0
		place_value = 1
		while(x):
			d_x = x % 10
			value_x += d_x * place_value
			if x >= 10:
				place_value *= 10
			x //= 10
		value_rx = 0
		d_rx = 0
		while(place_value):
			d_rx = rx % 10
			value_rx += d_rx * place_value
			rx //= 10
			place_value //= 10
		if value_x != value_rx:
			return False
		else:
			return True
