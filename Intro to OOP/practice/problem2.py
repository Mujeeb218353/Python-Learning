class Calculator:

    def square(n):
        return n*n
    
    def cube(n):
        return n*n*n
    
    def square_root(n):
        return n**0.5
    
calculator = Calculator()

print(calculator.square(2), calculator.cube(5), Calculator.square_root(16))