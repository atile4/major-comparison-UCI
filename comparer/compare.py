from scrape import getTable
from major_info import MAJORS

# Converts and filters HTML scrape text for processing into lists
# @param website catalogue of a major
# @return table list (with headers) and course list (without headers)
def makeTableList(website : str) -> list | list:
    rows = getTable(website)

    table_list = []
    course_list = []
    
    for row in rows:
        cols = row.find_all('td')
        first_col = cols[0].get_text(strip=True).replace("\xa0", " ")
        if len(cols) == 1:
            table_list.append(first_col)
        else:
            title = cols[1].get_text(strip=True)
            table_list.append(first_col + " : " + title)
            course_list.append(first_col + " : " + title)
    return (table_list, course_list)

# Validates if an input is a valid major
# @param major input
# @return boolean if major is valid
def isMajor(response : str):
    return response.lower() in MAJORS

# Text output a formatted course list
# @param overlapping course list for one major
def printCourse(overlapping_course_list):
    for table_item in overlapping_course_list:
        if " : " in table_item:
            print("  - ", end="")
        print(table_item)

# Finds overlapping course requirements between majors with text inputted majors
# @param None
# @return None
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
