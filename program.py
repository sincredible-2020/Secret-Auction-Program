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
from os import system, name


# define our clear function
def clear():
    # for windows the name is 'nt'
    if name == 'nt':
        _ = system('cls')

    # and for mac and linux, the os.name is 'posix'
    else:
        _ = system('clear')

print(logo,"\nWelcome to the Secret Auction Program!")

auction = {}
winning_bid = 0

name = input("What is your name? ")
bid = int(input("What's your bid? $"))
auction[name] = bid
proceed = input("Are there any other bidders? Type 'yes' or 'no'.\n")

while proceed == "yes":
    name = input("What is your name? ")
    bid = int(input("What's your bid? $"))
    auction[name] = bid
    proceed = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    clear()

for avalue in auction.values():
    if avalue > winning_bid:
        winning_bid = avalue

print("The Winner is", list(auction.keys())[list(auction.values()).index(winning_bid)], f"with a bid of ${winning_bid}")

