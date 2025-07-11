from major_info import MAJORS_LIST
from compare import comparer

def main():
    print("----------------------------------------\n"
      "|         UCI Major Comparison         |\n"
      "|                                      |\n"
      "|           written by atile           |\n"
      "----------------------------------------\n")
    print("Welcome to UCI Major Comparison!\n\n"
          "Type help to get started.")

    run = True
    while run:
        cmd : str = input("> ")
        print()
        
        match cmd:
            case "compare":
                comparer()
            case "help":
               print("\n========COMMANDS========\n"
                    "help: Displays this page\n"
                    "exit: terminates the program\n"
                    "majors: list of majors\n"
                    "compare: input 2 majors to compare\n"+
                    "=========================") 
            case "majors": print(MAJORS_LIST)
            case "exit" | "quit":
                print("Thanks for using.")
                run = False
            case _: print("Invalid command. Type help for a list of commands.")
main()
