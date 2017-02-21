__author__ = 'KhayKode'

# Solution to question 1 in python 3

print(",".join([str(number) for number in range(2000, 3201)
                if number % 7 == 0 and number % 5 != 0]))