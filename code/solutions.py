# range
def print_range(start, end):
	# Loop through the numbers from start to end
	n = start
	while n <= end:
        print(n)
        n += 1

print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 

# Prime factors

def prime_factors(number):
    """ prints out the the prime factors of a number """
    # Start with two, which is the first prime
    factor = 2
    # Keep going until the factor is larger than the number
    while factor <= number:
        # Check if factor is a divisor of number
        if number % factor == 0:
        # If it is, print it and divide the original number
        print(factor)
        number = number / factor
        else:
        # If it's not, increment the factor by one
        factor += 1
    return "Done"

prime_factors(100)

# Sum of divisors
def sum_divisors(n):
    # Return the sum of all divisors of n, not including n
    sum = 0
    i = 1
    
    # res = n % i
    # if n % i == 0 and i < n:
    #   while n != 0:
    #     sum = sum + i
    #     print("<><><>", sum)
    #   i += 1

    x = 1
    while n != 0 and x < n :   
        if n % x == 0  :
        sum += x
        else:
        sum += 0
        x += 1    
    
    return sum

    # while res == 0 and i < n:
    #   sum += i
    #   i += 1
    # if n % i == 0:
    return sum
