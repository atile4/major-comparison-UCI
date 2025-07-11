from scrape import makeTableList, printCourse
from major_info import MAJORS

def isMajor(response : str):
    return response.lower() in MAJORS

def comparer():
    response1 = input("Input the first major, as listed from the UCI catalogue.\n> ")
    while not isMajor(response1):
        if (response1 == "exit"):
            exit()
        else:
            response1 = input("Invalid major. Please input a major as listed from the UCI catalogue.\n> ")
    website1 = MAJORS[response1]
    
    response2 = input("Input the second major, as listed from the UCI catalogue.\n> ")
    
    while not isMajor(response2):
        if (response2 == "exit"): exit()
        else:
            response2 = input("Invalid major. Please input a major as listed from the UCI catalogue.\n> ")
    
    website2 = MAJORS[response2]
    
    table_list1, courselist1 = makeTableList(website=website1)  
    table_list2, courselist2 = makeTableList(website=website2)
    
    overlap = list(set(courselist1) & set(courselist2))
    overlap_length = len(overlap)
    newcourse1 = [x for x in table_list1 if x in overlap or " : " not in x]
    newcourse2 = [x for x in table_list2 if x in overlap or " : " not in x]
                
    print("\n"+response1.upper())
    printCourse(newcourse1)

    print("\n"+response2.upper())
    printCourse(newcourse2)
    
    print()
    print("For", response1.capitalize() + ",", str(overlap_length) + "/" + str(len(set(courselist1))) + " courses have overlap.")
    print("For", response2.capitalize() + ",", str(overlap_length) + "/" + str(len(set(courselist2))) + " courses have overlap.")
    
    print("\nNumber of courses that overlap between " + response1.capitalize() + " and " + response2.capitalize() + ":", overlap_length)
    print("\nInput your next command.")
