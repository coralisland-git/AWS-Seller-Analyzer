import xlrd
import pandas as pd
import re

def find_columns_tab1(loc, log_file):
    flag = 0
    wb = xlrd.open_workbook(loc)

    ################################## FOR SHEET ONE ###################################
    sheet = wb.sheet_by_index(0)
    numcols = sheet.ncols
    column_names = ["Seller Company Name", "GTM Campaign Source", "Campaign Name", "CRM System Campaign ID",
                    "Campaign Create Date",
                    "Lead ID",
                    "Create Date", "Lead Country", "Lead Type", "Lead Status", "Opportunity ID", "Convert Date",
                    "Opportunity Type",
                    "Opportunity Status", "AWS Marketplace Opportunity", "Pipeline Revenue", "Win Date",
                    "Billed Revenue"]
    missing_columns = [[], []]
    misplaced_columns = []

    length = len("AWS Marketplace Opportunity")

    # COUNTING NUMBER OF COLUMNS
    num_of_columns = 0
    for column in range(0, numcols):
        num_of_columns += 1
        if column_names[column] not in sheet.cell_value(0, column):
            flag = 1
            line = re.sub('[!@#$?]', '', sheet.cell_value(0, column))
            missing_columns[0].append(line)
            missing_columns[1].append(column + 1)
            length_1 = len(sheet.cell_value(0, column))
            val = length-length_1
            space = ""
            for index in range(0, val+3):
                space += " "
            print("{}{} : FAIL (Should be : {})".format(sheet.cell_value(0, column), space, column_names[column]), file = log_file)
        else:
            length_1 = len(sheet.cell_value(0, column))
            val = length-length_1
            space = ""
            for index in range(0, val+3):
                space += " "
            line = re.sub('[!@#$?]', '', sheet.cell_value(0, column))
            print("{}{} : PASS".format(line, space), file = log_file)


    # CHECK IF COLUMNS ARE MISPLACED OR SPELLING IS WRONG
    for names in range(0, len(missing_columns[0])):
        for column in range(0, numcols):
            if missing_columns[0][names] == sheet.cell_value(0, column):
                misplaced_columns.append(column + 1)

    if num_of_columns == 18 and flag == 0:
        print("Number of Columns in Tab1       : {} | PASS.\n".format(num_of_columns), file=log_file)
    else:
        print("Number of Columns in Tab1       : {} | FAIL.\n".format(num_of_columns), file=log_file)
        try:
            if missing_columns:
                print("Column Misplaced To", "Row:", 1, "Column:", missing_columns, "Value:",
                        missing_columns[0], file=log_file)
            else:
                print("Column Not Present : ",missing_columns[0], file=log_file)

        except:
            missing_columns[0][names] = re.sub('[!@#$?]', '', missing_columns[0][names])
            print("Column Not Present", missing_columns[0][names], file=log_file)

    return missing_columns[1], misplaced_columns


def find_columns_tab2(loc, log_file):
    ################################### FOR SHEET 2 ######################################
    wb = xlrd.open_workbook(loc)
    
    flag = 0
    sheet = wb.sheet_by_index(1)
    numcols = sheet.ncols

    column_names = ["Seller Company Name", "GTM Campaign Source", "Campaign Name", "CRM System Campaign ID",
                    "Campaign Create Date", "Investment"]

    missing_columns = [[], []]
    misplaced_columns = []

    length = len("Number of Columns in Tab2")

    # COUNTING NUMBER OF COLUMNS
    num_of_columns = 0
    for column in range(0, numcols):
        num_of_columns += 1
        if column_names[column] not in sheet.cell_value(0, column):
            flag = 1
            missing_columns[0].append(column_names[column])
            missing_columns[1].append(column + 1)
            length_1 = len(sheet.cell_value(0, column))
            val = length-length_1
            space = ""
            for index in range(0, val+3):
                space += " "
            line = re.sub('[!@#$?]', '', sheet.cell_value(0, column))
            print("{}{} : FAIL (Should be {})".format(line, space, column_names[column]), file = log_file)
        else:
            length_1 = len(sheet.cell_value(0, column))
            val = length-length_1
            space = ""
            for index in range(0, val+3):
                space += " "
            line = re.sub('[!@#$?]', '', sheet.cell_value(0, column))
            print("{}{} : PASS".format(line, space), file = log_file)

    # CHECK IF COLUMNS ARE MISPLACED OR SPELLING IS WRONG
    for names in range(0, len(missing_columns[0])):
        for column in range(0, numcols):
            if missing_columns[0][names] == sheet.cell_value(0, column):
                missing_columns.append(column + 1)

    if num_of_columns == 6 and flag == 0:
        print("Number of Columns in Tab2    : {} PASS\n".format(num_of_columns), file=log_file)
    else:
        print("Number of Columns in Tab2    : {} FAIL\n".format(num_of_columns), file=log_file)
        try:
            if missing_columns:
                print("Column Misplaced To", "Row:", 1, "Collumn:", missing_columns, "Value:",
                          missing_columns[0], file=log_file)
            else:
                print("Column Not Present", missing_columns[0], file=log_file)
        except:
            print("Column Not Present", " Value:",missing_columns[0], file=log_file)

    return missing_columns[1], misplaced_columns


def match_columns(file_loc):
        xls = pd.ExcelFile(file_loc)
        sheet_names = xls.sheet_names
        df1 = pd.read_excel(xls, sheet_names[0])
        df2 = pd.read_excel(xls, sheet_names[1])
        flag = 0

        try:
            seller_name_1 = df1['Seller Company Name*'].unique()
            seller_name_1 = [str(seller_name_1) for l in seller_name_1]
            seller_name_1.sort()

            seller_name_2 = df2['Seller Company Name*'].unique()
            seller_name_2 = [str(seller_name_2) for l in seller_name_2]
            seller_name_2.sort()

            if set(seller_name_1) != set(seller_name_2):
                flag = 1

            return flag
        except:
            flag = 1
            return flag


def get_current_count(file_loc):
    book = xlrd.open_workbook(file_loc)
    sheet = book.sheet_by_index(0)
    sheet_2 = book.sheet_by_index(1)

    lead_count = 0
    for row in range(1, sheet.nrows):
        if str(sheet.cell_value(row, 4)) != "":
            lead_count += 1

    opportunity_count = 0
    for row in range(1, sheet.nrows):
        if str(sheet.cell_value(row, 9)) != "":
            opportunity_count += 1

    win_loss_count = 0
    for row in range(1, sheet.nrows):
        if str(sheet.cell_value(row, 15)) != "":
            win_loss_count += 1

    campaign_count = 0
    for row in range(1, sheet_2.nrows):
        if str(sheet_2.cell_value(row, 3)) != "":
            campaign_count += 1

    total_investment_count = 0
    for row in range(1, sheet_2.nrows):
        if sheet_2.cell_value(row, 4) != "":
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            if(regex.search(str(sheet_2.cell_value(row, 4))) == None):
                total_investment_count += sheet_2.cell_value(row, 4)
            else:
                total_investment_count += 0
        else:
            total_investment_count += 0
                
    return lead_count, opportunity_count, win_loss_count, campaign_count, total_investment_count
