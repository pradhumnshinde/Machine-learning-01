# This is example code for simple intrest 
P = float(input('please enter the principal in INR :'))
N = float(input('please enter the period in years :'))
R = float(input('please enter the rate od intrest in %p.a. : '))
# calculate the simple intrest
I = (P*N*R)/100
A = P + I
# print the result
print(f'simple intrest : {I:.2f} INR')
print(f'Amount : {A:.2f} INR')