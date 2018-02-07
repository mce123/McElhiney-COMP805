"""
Lab 3
lab3.py
Patrick R. McElhiney
1/30/2018
"""

def squared_nums(num_list):
    """
    Squares numbers in num_list
    num_list: list of numbers
    Returns: list of these numbers squared
    """
    return [pow(num, 2) for num in num_list]

def check_title(title_list):
    """
    Removes strings in title_list that have numbers and aren't title case
    title_list: list of strings
    Returns: list of strings that are titles
    """
    return [title for title in title_list if title.istitle() and not any(char.isdigit() for char in title_list)]

def restock_inventory(inventory):
    """
    Increases inventory of each item in dictionary by 10
    inventory: a dictionary with:
    ** key: string that is the name of the inventory item**
    ** value: integer that equals the number of that item currently on hand**
    Returns: updated dictionary where each inventory item is restocked
    """
    return_dict = {}
    for key, value in inventory.items():
        return_dict[key] = inventory[key] + 10
    return return_dict

def filter_0_items(inventory):
    """
    Removes items that have a value of 0 from a dictionary of inventories
    inventory: dictionary with:
    ** key: tring that is the name of the inventory item**
    ** value: nteger that equals the number of that item currently on hand**
    Returns: return_dict created from inventory dictionary with any item that had 0 quantity removed
    """
    return_dict = {}
    for key, value in inventory.items():
        if inventory[key] != 0:
            return_dict[key] = inventory[key]
    return return_dict

def average_grades(grades):
    """
    Takes grade values from a dictionary and averages them into a final grade
    grades: a dictionary of grades with:
    key: string of students name
    value: list of integer grades received in class
    Returns: dictionary that averages out the grades of each student
    """
    return_dict = {}
    for student_name, student_grades in grades.items():
        these_grades = 0
        num_grades = 0
        for grade in student_grades:
            num_grades += 1
            these_grades += grade
        final_grade = these_grades / num_grades
        return_dict[student_name] = final_grade
    return return_dict
