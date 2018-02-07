"""
Lab 3 Test Function
lab3run.py
Patrick R. McElhiney
1/30/2018
"""

import lab3

def run_squared_nums():
    """
    Demo many uses of the function squared_nums( )
    """

    num_list = [1, 2, 3]
    res = lab3.squared_nums(num_list)
    print('lab3.squared_nums({}) -> {}'.format(num_list, res))

    num_list = []
    res = lab3.squared_nums(num_list)
    print('lab3.squared_nums({}) -> {}'.format(num_list, res))

    num_list = [-1, -2, -3]
    res = lab3.squared_nums(num_list)
    print('lab3.squared_nums({}) -> {}'.format(num_list, res))

    num_list = [1, 0]
    res = lab3.squared_nums(num_list)
    print('lab3.squared_nums({}) -> {}'.format(num_list, res))

def run_check_title():
    """
    Demo many uses of the function check_title( )
    """

    title_list = ['Hello World', 'Hello_world', 'Title']
    res = lab3.check_title(title_list)
    print('lab3.check_title({}) -> {}'.format(title_list, res))

    title_list = ['Hello_World', 'A great 3 Days', 'hello World']
    res = lab3.check_title(title_list)
    print('lab3.check_title({}) -> {}'.format(title_list, res))

    title_list = ['10, 11, 12']
    res = lab3.check_title(title_list)
    print('lab3.check_title({}) -> {}'.format(title_list, res))

def run_restock_inventory():
    """
    Demo many uses of the function restock_inventory( )
    """

    inventory = {'pencil':10, 'pen':8, 'paper':7}
    res = lab3.restock_inventory(inventory)
    print('lab3.restock_inventory({}) -> {}'.format(inventory, res))

    inventory = {'pencil':0, 'pen':-3, 'paper':-11}
    res = lab3.restock_inventory(inventory)
    print('lab3.restock_inventory({}) -> {}'.format(inventory, res))

    inventory = {'pencil':0.5, 'pen':-3.2, 'paper':11.0}
    res = lab3.restock_inventory(inventory)
    print('lab3.restock_inventory({}) -> {}'.format(inventory, res))

def run_filter_0_items():
    """
    Demo many uses of the function filter_0_items( )
    """

    inventory = {'pencil':10, 'pen':8, 'paper':7}
    res = lab3.filter_0_items(inventory)
    print('lab3.filter_0_items({}) -> {}'.format(inventory, res))

    inventory = {'pencil':0, 'pen':-3, 'paper':-11}
    res = lab3.filter_0_items(inventory)
    print('lab3.filter_0_items({}) -> {}'.format(inventory, res))

    inventory = {'pencil':0.5, 'pen':-3.2, 'paper':0.0}
    res = lab3.filter_0_items(inventory)
    print('lab3.filter_0_items({}) -> {}'.format(inventory, res))

def run_average_grades():
    """
    Demo many uses of the function average_grades( )
    """

    grades = {'Michael':[100, 78, 88, 900/10], 'Daniel':[80, 95, 77, 64.0], 'Josh':[99, 89, 94, 66]}
    res = lab3.average_grades(grades)
    print('lab3.average_grades({}) -> {}'.format(grades, res))

    grades = {'Michael':[5 * 20, 188 * .5, 88], 'Daniel':[80.5, .15, 66, 64.0], 'Josh':[99 + 1 * -2, 40/.5]}
    res = lab3.average_grades(grades)
    print('lab3.average_grades({}) -> {}'.format(grades, res))

    grades = {'Michael':[78], 'Daniel':[90], 'Josh':[900/-9]}
    res = lab3.average_grades(grades)
    print('lab3.average_grades({}) -> {}'.format(grades, res))

def main( ):
    """
    Wrapper function that calls all the testing functions
    """
    run_squared_nums()
    print("")

    run_check_title()
    print("")

    run_restock_inventory()
    print("")

    run_filter_0_items()
    print("")

    run_average_grades()
    print("")

if __name__ == "__main__":
	main()
