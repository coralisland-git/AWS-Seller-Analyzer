import sys
from utilities import get_s3_bucket
from utilities import get_s3_client
from utilities import get_s3_config
from utilities import get_redshift_connection
from utilities import get_month_from_sys_args
from utilities import get_year_from_sys_args


def log_message(msg, log_file):
    print(msg)
    log_file.write('\n' + msg)


def get_input_filename():
    return sys.argv[1].split("/")[3]


def get_tab1_filename():
    return get_input_filename() + 'Tab1_accepted.csv'


def download_tab1():
    tab1_filename = get_tab1_filename()

    s3_tab1_key = '{}/{}/Successful Files/{}'.format(
        get_year_from_sys_args(),
        get_month_from_sys_args(),
        tab1_filename
    )
    s3_client = get_s3_client()
    s3_client.download_file(get_s3_bucket(), s3_tab1_key, s3_tab1_key)


def get_tab2_filename():
    return get_input_filename() + 'tab2_accepted.csv'


def download_tab2():
    tab2_filename = get_tab2_filename()

    s3_tab2_key = '{}/{}/Successful Files/{}'.format(
        get_year_from_sys_args(),
        get_month_from_sys_args(),
        tab2_filename
    )
    s3_client = get_s3_client()
    s3_client.download_file(get_s3_bucket(), s3_tab2_key, s3_tab2_key)


def get_tab3_filename():
    return get_input_filename() + 'tab3_accepted.csv'


def download_tab3():
    tab3_filename = get_tab3_filename()

    s3_tab3_key = '{}/{}/Successful Files/{}'.format(
        get_year_from_sys_args(),
        get_month_from_sys_args(),
        tab3_filename
    )
    s3_client = get_s3_client()
    s3_client.download_file(get_s3_bucket(), s3_tab3_key, s3_tab3_key)


def get_log_file_prefix():
    return 'Log_{}'.format(get_input_filename())


def get_s3_log_prefix():
    return '{}/{}/Log Files/{}'.format(
        get_year_from_sys_args(),
        get_month_from_sys_args(),
        get_log_file_prefix()
    )


def get_log_s3_key():
    s3_client = get_s3_client()
    log_prefix = get_s3_log_prefix()
    resp = s3_client.list_objects_v2(Bucket=get_s3_bucket(),
                                     Prefix=log_prefix)

    last_log_mod_datetime = None
    latest_log_s3_key = None
    for obj in resp['Contents']:
        if last_log_mod_datetime is None or obj['LastModified'] > last_log_mod_datetime:
            latest_log_s3_key = obj['Key']
            last_log_mod_datetime = obj['LastModified']

    return latest_log_s3_key


def download_log():
    log_s3_key = get_log_s3_key()
    s3_client = get_s3_client()
    s3_client.download_file(get_s3_bucket(),
                            log_s3_key,
                            log_s3_key)


def upload_log():
    log_s3_key = get_log_s3_key()
    s3_client = get_s3_client()
    s3_client.upload_file(log_s3_key,
                          get_s3_bucket(),
                          log_s3_key)


def insert_csv_data_tab1():
    connection = get_redshift_connection()

    q3 = "COPY us_gtmsales.stg_sellerleads(selleruid, sellercompanyname, gtmcampaignsource, campaignname, " \
         "crmsystemcampaignid, campaigncreatedate, leadid, createdate, leadcountry, leadtype, leadstatus, " \
         "boxmonth, boxyear, insertiondate) " \
         "FROM 's3://{}/{}/{}/Successful Files/{}' " \
         "CREDENTIALS 'aws_access_key_id={};aws_secret_access_key={}' " \
         "CSV timeformat 'auto' dateformat 'auto';".format(get_s3_bucket(),
                                                           get_year_from_sys_args(),
                                                           get_month_from_sys_args(),
                                                           get_tab1_filename(),
                                                           get_s3_config()['access_key_id'],
                                                           get_s3_config()['secret_access_key'])

    connection.execution_options(autocommit=True).execute(q3)
    connection.close()


def insert_csv_data_tab2():
    connection = get_redshift_connection()

    q3 = "COPY us_gtmsales.stg_selleropportunities(" \
         "selleruid, campaigncreatedate, opportunityid, convertdate, opportunitycountry, opportunitytype, " \
         "opportunitystatus, awsmarketopportunity, pipelinerevenue, accountname, accountid, windate, billedrevenue, " \
         "boxmonth, boxyear, insertiondate )" \
         "FROM 's3://{}/{}/{}/Successful Files/{}' " \
         "CREDENTIALS 'aws_access_key_id={};aws_secret_access_key={}' " \
         "CSV timeformat 'auto' dateformat 'auto';".format(get_s3_bucket(),
                                                           get_year_from_sys_args(),
                                                           get_month_from_sys_args(),
                                                           get_tab2_filename(),
                                                           get_s3_config()['access_key_id'],
                                                           get_s3_config()['secret_access_key'])

    connection.execution_options(autocommit=True).execute(q3)
    connection.close()


def insert_csv_data_tab3():
    connection = get_redshift_connection()

    q3="COPY us_gtmsales.stg_sellercampaigns(selleruid, sellercompanyname, gtmcampaignsource, campaignname, " \
       "crmsystemcampaignid,campaigncreatedate,investment,boxmonth,boxyear,insertiondate) " \
       "FROM 's3://{}/{}/{}/Successful Files/{}' " \
       "CREDENTIALS 'aws_access_key_id={};aws_secret_access_key={}' " \
       "CSV timeformat 'auto' dateformat 'auto';".format(get_s3_bucket(),
                                                        get_year_from_sys_args(),
                                                        get_month_from_sys_args(),
                                                        get_tab3_filename(),
                                                        get_s3_config()['access_key_id'],
                                                        get_s3_config()['secret_access_key'])

    connection.execution_options(autocommit=True).execute(q3)
    connection.close()


def insert_master():
    connection = get_redshift_connection()
    connection.execution_options(autocommit=True).execute(open('sql/create_leadcountry_to_geo_code.sql', 'r').read())
    connection.execution_options(autocommit=True).execute(open('sql/insert_mst_sellerleads.sql', 'r').read())
    connection.execution_options(autocommit=True).execute(open('sql/insert_mst_sellercampaigns.sql', 'r').read())
    connection.close()
