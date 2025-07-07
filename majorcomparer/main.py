from scrape import make_table_list
from majorchecker import majorCheck

def main():
    print("----------------------------------------\n"
      "|         UCI Major Comparison         |\n"
      "|                                      |\n"
      "|           written by atile           |\n"
      "----------------------------------------\n")

    print("Welcome to UCI Major Comparison!\n\nType help to get started.")

    run = True
    while run:
        cmd : str = input("> ")
        print()
        if (cmd == "help"):
            print("\n========COMMANDS========\n"
                    "help: Displays this page\n"
                    "exit: terminates the program\n"
                    "compare: input 2 majors to compare\n"+
                    ("=")*23)
        elif (cmd == "compare"):
            response1 = input("Input the first major, as listed from the UCI catalogue.\n> ")
            website1 = majorCheck(response1)
            table_list1, courselist1 = make_table_list(website1)
            
            response2 = input("Input the first major, as listed from the UCI catalogue.\n> ")
            website2 = majorCheck(response2)
            table_list2, courselist2 = make_table_list(website=website2)
            
            overlap = list(set(courselist1) & set(courselist2))
            overlap_length = len(overlap)
            newcourse1 = [x for x in table_list1 if x in overlap or " : " not in x]
            newcourse2 = [x for x in table_list2 if x in overlap or " : " not in x]
            print("\nNumber of courses that overlap between " + response1.capitalize() + " and " + response2.capitalize() + ":", overlap_length)
            print("For", response1.capitalize() + ",", str(overlap_length) + "/" + str(len(set(courselist1))) + " have overlap.")
            print("For", response2.capitalize() + ",", str(overlap_length) + "/" + str(len(set(courselist2))) + " have overlap.") 
            
        elif (cmd == "exit"):
            print("Thanks for using.")
            run = False
        else:
            print("Invalid command. Type help for a list of commands.")



    



    
