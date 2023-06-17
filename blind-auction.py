from replit import clear
# from art import logo
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

bid_dict={}
bid_finish=False

    
def bidder_finder():
  highest_bid=0
  winner=''
  for bidder in bid_dict:
    bid_value=bid_dict[bidder]
    if bid_value>highest_bid:
      highest_bid=bid_value
      winner=bidder

  print(f"\nThe winner of the bid is {winner} with bid {highest_bid}")


while bid_finish==False:
  name=input("Enter your name: \n")
  bid=int(input("Enter the bid of yours: \n"))
  bid_dict[name]=bid
  option=input("Is there anyone who wanted to bid?(type yes/no) \n").lower()
  
  if option=="yes":
    clear()
    
  elif option=="no":
    bid_finish=True
    clear()
    print(bid_dict)
    bidder_finder()
