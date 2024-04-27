print('''
This is an example of the order of operations: (a + b) - c / d * e = f
Input values from A to E in order to get an answer for F!
      ''')

input_a = int(input("What's your value for A? "))
input_b = int(input("What's your value for B? "))
input_c = int(input("What's your value for C? "))
input_d = int(input("What's your value for D? "))
input_e = int(input("What's your value for E? "))
final_answer = (input_a + input_b) - input_c / input_d * input_e

print(f"\nYour value give you the final answer of {final_answer}! Here's what you gave me: ({input_a} + {input_b}) - {input_c} / {input_d} * {input_e} = {final_answer}")5