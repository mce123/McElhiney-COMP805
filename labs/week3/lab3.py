"""
Lab 3
lab3.py
Patrick R. McElhiney
2/13/2018
"""

def squared_nums(num_list):
    """
    Squares numbers in num_list
    num_list: list of numbers
    Returns: list of these numbers squared

    >>> squared_nums([1, 2, 3])
    [1, 4, 9]
    >>> squared_nums([])
    []
    >>> squared_nums([2, 4, 6])
    [4, 16, 36]
    """
    return [pow(num, 2) for num in num_list]

def check_title(title_list):
    """
    Removes strings in title_list that have numbers and aren't title case
    title_list: list of strings
    Returns: list of strings that are titles

    >>> check_title(['Hello World', 'Hello_world', 'Hello_World'])
    ['Hello World', 'Hello_World']
    >>> check_title([])
    []
    >>> check_title(['Hi There'])
    ['Hi There']
    """
    return [title for title in title_list if title.istitle() and not any(char.isdigit() for char in title_list)]

def restock_inventory(inventory):
    """
    Increases inventory of each item in dictionary by 10
    inventory: a dictionary with:
    ** key: string that is the name of the inventory item**
    ** value: integer that equals the number of that item currently on hand**
    Returns: updated dictionary where each inventory item is restocked

    >>> restock_inventory({'apples':5, 'oranges':10, 'peaches':50})
    {'peaches': 60, 'apples': 15, 'oranges': 20}
    >>> restock_inventory({})
    {}
    >>> restock_inventory({'bullets':100, 'guns':25, 'grenades':50})
    {'bullets': 110, 'guns': 35, 'grenades': 60}
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

    >>> filter_0_items({'apples':0, 'oranges':10, 'peaches':50})
    {'peaches': 50, 'oranges': 10}
    >>> filter_0_items({'apples':0, 'oranges':0, 'peaches':250})
    {'peaches': 250}
    >>> filter_0_items({'bullets':100, 'guns':0, 'grenades':50})
    {'bullets': 100, 'grenades': 50}
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

    >>> average_grades({'Michael' :[100, 78, 88, 900/10], 'Daniel':[80, 95, 77, 64.0], 'Josh':[99, 89, 94, 66]})
    {'Michael': 89, 'Daniel': 79.0, 'Josh': 87}
    >>> average_grades({'Michael':[5*20, 188 * .5, 88], 'Daniel':[80.5, .15, 66, 64.0], 'Josh':[99 + 1 * -2, 40/.5]})
    {'Michael': 94.0, 'Daniel': 52.6625, 'Josh': 88.5}
    >>> average_grades({'Michael' :[78], 'Daniel':[90], 'Josh':[900/-9]})
    {'Michael': 78, 'Daniel': 90, 'Josh': -100}
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

if __name__ == '__main__':
    import doctest
    doctest.testmod()
