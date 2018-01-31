"""
Lab 2 Test Function
lab2run.py
Patrick R. McElhiney
1/30/2018
"""

import lab2

def run_squared_nums():
    """
    Demo many uses of the function squared_nums( )
    """

    num_list = [1, 2, 3]
    res = lab2.squared_nums(num_list)
    print('lab2.squared_nums({}) -> {}'.format(num_list, res))

    num_list = []
    res = lab2.squared_nums(num_list)
    print('lab2.squared_nums({}) -> {}'.format(num_list, res))

    num_list = [-1, -2, -3]
    res = lab2.squared_nums(num_list)
    print('lab2.squared_nums({}) -> {}'.format(num_list, res))

    num_list = [1, 0]
    res = lab2.squared_nums(num_list)
    print('lab2.squared_nums({}) -> {}'.format(num_list, res))

def run_check_title():
    """
    Demo many uses of the function check_title( )
    """

    title_list = ['Hello World', 'Hello_world', 'Title']
    res = lab2.check_title(title_list)
    print('lab2.check_title({}) -> {}'.format(title_list, res))

    title_list = ['Hello_World', 'A great 3 Days', 'hello World']
    res = lab2.check_title(title_list)
    print('lab2.check_title({}) -> {}'.format(title_list, res))

    title_list = ['10, 11, 12']
    res = lab2.check_title(title_list)
    print('lab2.check_title({}) -> {}'.format(title_list, res))

def run_restock_inventory():
    """
    Demo many uses of the function restock_inventory( )
    """

    inventory = {'pencil':10, 'pen':8, 'paper':7}
    res = lab2.restock_inventory(inventory)
    print('lab2.restock_inventory({}) -> {}'.format(inventory, res))

    inventory = {'pencil':0, 'pen':-3, 'paper':-11}
    res = lab2.restock_inventory(inventory)
    print('lab2.restock_inventory({}) -> {}'.format(inventory, res))

    inventory = {'pencil':0.5, 'pen':-3.2, 'paper':11.0}
    res = lab2.restock_inventory(inventory)
    print('lab2.restock_inventory({}) -> {}'.format(inventory, res))

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

if __name__ == "__main__":
	main()
