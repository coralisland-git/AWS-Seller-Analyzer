import sys
import time
import pandas as pd
from utilities import get_month_from_sys_args
from utilities import get_year_from_sys_args
from utilities import get_redshift_connection


def get_seller_name():
    return get_src_filename().split("_")[1]


def get_src_filename():
    return sys.argv[1].split("/")[3]


def get_year_as_int():
    return int(get_year_from_sys_args())


def get_date_from_src_filename():
    date_dot_ext = get_src_filename().split("_")[2]
    return date_dot_ext.split(".")[0]


def get_ext_from_src_filename():
    date_dot_ext = get_src_filename().split("_")[2]
    return date_dot_ext.split(".")[1]


def get_src_file_dir():
    return '{}/{}/Raw Files/'.format(get_year_from_sys_args(), get_month_from_sys_args())


def get_src_file_path():
    return get_src_file_dir() + get_src_filename()


def get_log_path():
    return '{}/{}/Log Files/Log_{}_{}.txt'.format(
        get_year_from_sys_args(),
        get_month_from_sys_args(),
        get_src_filename(),
        time.strftime("%H:%M:%S")
    )


def is_alnum_max_50_chars(crm_system_campaign_id):
    success = False
    if crm_system_campaign_id or isinstance(crm_system_campaign_id, bool) or isinstance(crm_system_campaign_id, float):
        # the only valid floats are whole numbers, only zeroes after the decimal
        if isinstance(crm_system_campaign_id, float):
            if crm_system_campaign_id.is_integer():
                # convert the valid float to an int
                crm_system_campaign_id = int(crm_system_campaign_id)

        # convert to string, even if it already is one
        crm_system_campaign_id = str(crm_system_campaign_id)

        # must be alphanumeric and no more than 50 characters
        if crm_system_campaign_id.isalnum() and len(crm_system_campaign_id) <= 50:
            success = True

    return success


def validate_lead_country_column(sheet, numrows, col, Column_missing_tab1, one_based_column_position, log_file):
    err_cnt_lead_country = 0

    # query for obtaining all the possible names of a lead country
    sql_possible_countries = '''SELECT country_name FROM us_gtmsales.countries
                                UNION
                                SELECT country_code FROM us_gtmsales.countries
                                UNION
                                SELECT country_code_iso_3a FROM us_gtmsales.countries;'''

    # open one Redshift connection to use for the lead country value in each row
    redshift_connection = get_redshift_connection()

    # query Redshift and get the results in a dataframe
    df_possible_countries = pd.read_sql(sql_possible_countries,
                                        con=redshift_connection)

    # store the possible countries in a set for faster lookups
    set_possible_countries = set(df_possible_countries['country_name'])

    for row in range(1, numrows):
        lead_country = sheet.cell_value(row, col)
        err_msg_lead_country = 'Lead Country column error on Row: {} Column: {} Value: {}'.format(row + 1,
                                                                                                  col + 1,
                                                                                                  lead_country)
        try:
            if lead_country.upper() not in set_possible_countries:
                err_cnt_lead_country += 1
                print(err_msg_lead_country, file=log_file)
        except:
            err_cnt_lead_country += 1
            print(err_msg_lead_country, file=log_file)

    passed = numrows - err_cnt_lead_country
    if err_cnt_lead_country == 0 and one_based_column_position not in Column_missing_tab1:
        print('Validation on Lead Country 		   : PASS (Satisfied Conditions :: found lead country and corresponding lead region)', file=log_file)
        print('Total number of rows PASSED                : {}'.format(passed - 1), file=log_file)
        print('Total number of rows FAILED                : {}'.format(err_cnt_lead_country), file=log_file)
    else:
        print('Validation on Lead Country 		   : FAIL', file=log_file)
        print('Total number of rows PASSED                : {}'.format(passed - 1), file=log_file)
        print('Total number of rows FAILED                : {}'.format(err_cnt_lead_country), file=log_file)

    # close the Redshift connection
    redshift_connection.close()

    return err_cnt_lead_country
