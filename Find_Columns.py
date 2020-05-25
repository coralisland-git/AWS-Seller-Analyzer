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
                    "Campaign Create Date", "Lead ID", "Create Date", "Lead Country", "Lead Status"]
    missing_columns = [[], []]
    misplaced_columns = []

    length = len("AWS Marketplace Opportunity")

    # COUNTING NUMBER OF COLUMNS
    num_of_columns = 0
    for column in range(0, numcols):
        num_of_columns += 1
        column_title = sheet.cell_value(0, column).replace('\n', ' ')
        if column_names[column] not in column_title:
            flag = 1
            line = re.sub('[!@#$?]', '', column_title)
            missing_columns[0].append(line)
            missing_columns[1].append(column + 1)
            length_1 = len(column_title)
            val = length-length_1
            space = ""
            for index in range(0, val+3):
                space += " "
            print("{}{} : FAIL (Should be : {})".format(column_title, space, column_names[column]), file = log_file)
        else:
            length_1 = len(column_title)
            val = length-length_1
            space = ""
            for index in range(0, val+3):
                space += " "
            line = re.sub('[!@#$?]', '', column_title)
            print("{}{} : PASS".format(line, space), file = log_file)


    # CHECK IF COLUMNS ARE MISPLACED OR SPELLING IS WRONG
    for names in range(0, len(missing_columns[0])):
        for column in range(0, numcols):
            column_title = sheet.cell_value(0, column).replace('\n', ' ')
            if missing_columns[0][names] == column_title:
                misplaced_columns.append(column + 1)

    if num_of_columns == 9 and flag == 0:
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
    flag = 0
    wb = xlrd.open_workbook(loc)

    ################################## FOR SHEET 2 ###################################
    sheet = wb.sheet_by_index(1)
    numcols = sheet.ncols
    column_names = ["Seller Company Name", "GTM Campaign Source", "Campaign Name", "CRM System Campaign ID",
                    "Campaign Create Date", "Opportunity ID", "Convert Date", 
                    "Opportunity Country", "Opportunity Status", "AWS Marketplace Opportunity", "Pipeline Revenue", 
                    "Account Name", "Account ID", "Win Date", "Billed Revenue"]
    missing_columns = [[], []]
    misplaced_columns = []    
    length = len("AWS Marketplace Opportunity")

    # COUNTING NUMBER OF COLUMNS
    num_of_columns = 0
    for column in range(0, numcols):
        num_of_columns += 1
        column_title = sheet.cell_value(0, column).replace('\n', ' ')
        if column_names[column] not in column_title:
            flag = 1
            line = re.sub('[!@#$?]', '', column_title)
            missing_columns[0].append(line)
            missing_columns[1].append(column + 1)
            import pdb
            pdb.set_trace()
            length_1 = len(column_title)
            val = length-length_1
            space = ""
            for index in range(0, val+3):
                space += " "
            print("{}{} : FAIL (Should be : {})".format(column_title, space, column_names[column]), file = log_file)
        else:
            length_1 = len(column_title)
            val = length-length_1
            space = ""
            for index in range(0, val+3):
                space += " "
            line = re.sub('[!@#$?]', '', column_title)
            print("{}{} : PASS".format(line, space), file = log_file)


    # CHECK IF COLUMNS ARE MISPLACED OR SPELLING IS WRONG
    for names in range(0, len(missing_columns[0])):
        for column in range(0, numcols):
            column_title = sheet.cell_value(0, column).replace('\n', ' ')
            if missing_columns[0][names] == column_title:
                misplaced_columns.append(column + 1)

    if num_of_columns == 15 and flag == 0:
        print("Number of Columns in Tab2       : {} | PASS.\n".format(num_of_columns), file=log_file)
    else:
        print("Number of Columns in Tab2       : {} | FAIL.\n".format(num_of_columns), file=log_file)
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


def find_columns_tab3(loc, log_file):
    ################################### FOR SHEET 3 ######################################
    wb = xlrd.open_workbook(loc)
    
    flag = 0
    sheet = wb.sheet_by_index(2)
    numcols = sheet.ncols

    column_names = ["Seller Company Name", "GTM Campaign Source", "Campaign Name", "CRM System Campaign ID",
                    "Campaign Create Date", "Investment"]

    missing_columns = [[], []]
    misplaced_columns = []

    length = len("Number of Columns in Tab3")

    # COUNTING NUMBER OF COLUMNS
    num_of_columns = 0
    for column in range(0, numcols):
        num_of_columns += 1
        column_title = sheet.cell_value(0, column).replace('\n', ' ')
        if column_names[column] not in column_title:
            flag = 1
            missing_columns[0].append(column_names[column])
            missing_columns[1].append(column + 1)
            length_1 = len(column_title)
            val = length-length_1
            space = ""
            for index in range(0, val+3):
                space += " "
            line = re.sub('[!@#$?]', '', column_title)
            print("{}{} : FAIL (Should be {})".format(line, space, column_names[column]), file = log_file)
        else:
            length_1 = len(column_title)
            val = length-length_1
            space = ""
            for index in range(0, val+3):
                space += " "
            line = re.sub('[!@#$?]', '', column_title)
            print("{}{} : PASS".format(line, space), file = log_file)

    # CHECK IF COLUMNS ARE MISPLACED OR SPELLING IS WRONG
    for names in range(0, len(missing_columns[0])):
        for column in range(0, numcols):
            column_title = sheet.cell_value(0, column).replace('\n', ' ')
            if missing_columns[0][names] == column_title:
                missing_columns.append(column + 1)

    if num_of_columns == 6 and flag == 0:
        print("Number of Columns in Tab3    : {} PASS\n".format(num_of_columns), file=log_file)
    else:
        print("Number of Columns in Tab3    : {} FAIL\n".format(num_of_columns), file=log_file)
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
    sheet_3 = book.sheet_by_index(2)

    lead_count = 0
    for row in range(1, sheet.nrows):
        if str(sheet.cell_value(row, 4)) != "":
            lead_count += 1

    opportunity_count = 0
    for row in range(1, sheet_2.nrows):
        if str(sheet_2.cell_value(row, 5)) != "":
            opportunity_count += 1

    win_loss_count = 0
    for row in range(1, sheet_2.nrows):
        if str(sheet_2.cell_value(row, 13)) != "":
            win_loss_count += 1

    campaign_count = 0
    for row in range(1, sheet_3.nrows):
        if str(sheet_3.cell_value(row, 3)) != "":
            campaign_count += 1

    total_investment_count = 0
    for row in range(1, sheet_3.nrows):
        if sheet_3.cell_value(row, 5) != "":
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            if(regex.search(str(sheet_3.cell_value(row, 5))) == None):
                total_investment_count += sheet_3.cell_value(row, 5)
            else:
                total_investment_count += 0
        else:
            total_investment_count += 0
                
    return lead_count, opportunity_count, win_loss_count, campaign_count, total_investment_count
