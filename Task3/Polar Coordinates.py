import cmath
input_str = input()
try:
    z = complex(input_str)
except ValueError:
    print("Invalid input format")
    exit(1)
        
print(abs(z))
arg_z = cmath.phase(z)
print(arg_z)
