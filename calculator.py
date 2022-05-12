"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

while True:
    user_input = input('What is your equation? ')
    tokens = user_input.split(' ')
       
    if len(tokens) == 1 and tokens[0] == 'q': 
        print('All done!')
        break
      
    operator = tokens[0]
    num1 = int(tokens[1])
    
    if len(tokens) == 3:
        num2 = int(tokens[2])
        if operator == '+':
            answer = add(num1, num2)
            
        elif operator == '-':
            answer = subtract(num1, num2)
        
        elif operator == '*':
            answer = multiply(num1, num2)

        elif operator == '/':
            answer = divide(num1, num2)
        
        elif operator == 'pow':
            answer = power(num1, num2)

        elif operator == 'mod':
            answer = mod(num1, num2)

    elif len(tokens) < 3:
       
        if operator == 'square':
            answer = square(num1)

        elif operator == 'cube':
            answer = cube(num1)

    


        

    print(answer)
# Replace this with your code
