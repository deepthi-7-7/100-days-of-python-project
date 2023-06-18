from replit import clear
logo = """

_____________________
|  _________________  |
| | Pythonista   0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | | 
| |___|___|___| |___| | 
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|



  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. |
| |     ______   | || |      __      | || |   _____      | || |     ______   | |
| |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' | 
 '----------------'   '----------------'  '----------------'  '----------------'

 """

print(logo)

def add(num1,num2):
  return num1+num2
def sub(num1,num2):
  return num1-num2
def mul(num1,num2):
  return num1*num2
def div(num1,num2):
  return num1/num2
  
cal_loop=True

def calc(one):
  choice=input("\nSelect an operation: \n")
  two=float(input("\nEnter the next number:\n"))
  function=operations[choice]
  result=function(one,two)
  print(f"\n{one} {choice} {two} = {result}\n")

  conti=input(f"type 'yes' to continue calculation with {result} or type 'no' to start a new calculation:\n").lower()

  if conti=='yes':
    cal_loop=False
    calc(result)
  elif conti=='no':
    clear()
    cal_loop=True


while cal_loop:

  n1=float(input("Enter the first number: \n"))
  operations={'+':add,'-':sub,'*':mul,'/':div}
  
  for op in operations:
    print(op)
  calc(n1)

