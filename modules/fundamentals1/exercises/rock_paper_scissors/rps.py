""" Determine the winner of rock, paper, scissors """

while True:
    p1 = input("Enter player 1's hand shape ('r', 'p', or 's'): ")
    p2 = input("Enter player 2's hand shape ('r', 'p', or 's'): ")
    # assume p1 and p2 are valid ('r', 'p', or 's')
    result = ("Tie!" if p1 == p2 else
              "Player 1 wins!" if (p1 == "r" and p2 == "s" or
                                   p1 == "s" and p2 == "p" or
                                   p1 == "p" and p2 == "r") else
              "Player 2 wins!")
    print(result)
    if input("Do you want to do another round? ('y' or 'n') ") == 'n':
        print("Goodbye!")
        break
