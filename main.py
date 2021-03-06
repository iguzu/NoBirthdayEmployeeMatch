import argparse
import csv

CBX_ID = 0
CBX_FIRSTNAME = 1
CBX_LASTNAME = 2
CBX_BIRTHDATE = 3
CBX_COMPANY = 4

HC_FIRSTNAME = 0
HC_LASTNAME = 1
HC_COMPANY = 2


# define commandline parser
parser = argparse.ArgumentParser(description='Tool to match employees without birthday to employees ID in CBX, all input/output files must be in the current directory')
parser.add_argument('cbx_list',
                    help='UTF-8 csv DB export of employees with the following columns: ID, firstname, lastname, birthday, company')
parser.add_argument('hc_list',
                    help='Windows 1252 csv file with the following columns: firstname, lastname, company')
parser.add_argument('output',
                    help='csv file with the following columns: firstname, lastname, company')
args = parser.parse_args()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data_path = './data/'
    cbx_file = data_path + args.cbx_list
    hc_file = data_path + args.hc_list
    output_file = data_path + args.output

    # output parameters used
    print(f'Reading CBX list: {args.cbx_list}')
    print(f'Reading HC list: {args.hc_list}')
    print(f'Outputing results in: {args.output}')

    # read data
    cbx_data = []
    hc_data = []
    with open(cbx_file, 'r', encoding="utf-8") as cbx:
        for row in csv.reader(cbx):
            cbx_data.append(row)
    with open(hc_file, 'r', encoding="cp1252") as hc:
        for row in csv.reader(hc):
            hc_data.append(row)
    with open(output_file, 'w', newline='', encoding='cp1252') as resultfile:
        writer = csv.writer(resultfile)
        for row in cbx_data:
            writer.writerow(row)

