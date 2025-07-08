from scrape import makeTableList, printCourse
from majorchecker import majorCheck, MAJORS_LIST
    
def comparer():
    response1 = input("Input the first major, as listed from the UCI catalogue.\n> ")        
    response2 = input("Input the second major, as listed from the UCI catalogue.\n> ")

    website1 = majorCheck(response1)
    table_list1, courselist1 = makeTableList(website1)
    website2 = majorCheck(response2)
    table_list2, courselist2 = makeTableList(website=website2)
    
    overlap = list(set(courselist1) & set(courselist2))
    overlap_length = len(overlap)
    newcourse1 = [x for x in table_list1 if x in overlap or " : " not in x]
    newcourse2 = [x for x in table_list2 if x in overlap or " : " not in x]
                
    print(response1.upper())
    printCourse(newcourse1)

    print("\n"+response2.upper())
    printCourse(newcourse2)
    
    print()
    print("For", response1.capitalize() + ",", str(overlap_length) + "/" + str(len(set(courselist1))) + " courses have overlap.")
    print("For", response2.capitalize() + ",", str(overlap_length) + "/" + str(len(set(courselist2))) + " courses have overlap.")
    
    print("\nNumber of courses that overlap between " + response1.capitalize() + " and " + response2.capitalize() + ":", overlap_length)
