import argparse
import io
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
parser = argparse.ArgumentParser(description='Tool to match employees without birthday to employees ID in CBX')
parser.add_argument('cbx_list',
                    help='UTF-8 csv export of employees with the following columns: ID, firstname, lastname, birthday, company')
parser.add_argument('hc_list',
                    help='csv file with the following columns: firstname, lastname, company')


f = open('./out/a.out','w')
f.write('Hello')
f.close()

def print_hi(name):
    args = parser.parse_args()
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(f'CBX list: {args.hc_list}')
    print(f'HC list: {args.cbx_list}')
    f = open('./out/a.out','w')
    f.write('Hello')
    f.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
