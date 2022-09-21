# Use this file to calculate the amount of compound interest. Follow the instructions on the
# Variables and Expressions sheet carefully.

P = 10000
n = 12
r = 0.08
t = 10
A = P * (1+r/n) ** (n * t)

print("The amount of compound intrest is", A)
