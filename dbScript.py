from insert_utilities import get_redshift_connection
import datetime
import dateutil.relativedelta



def get_seller_id(seller_name):
    connection = get_redshift_connection()
    query = "call us_gtmsales.usp_getselleruid('{}');".format(seller_name)

    rows = connection.execution_options(autocommit=True).execute(query)
    row = rows.fetchall()
    connection.close()
    return row[0][0]


def fetch_counts(year, month, seller_uid):
    connection = get_redshift_connection()
    if month > 1:
        month = month-1
    else:
        month = 12
        year = int(yearchk) - 1
    
    procedure_call = "select BoxYear,BoxMonth ,SellerUID,SellerCompanyName," \
                     "LeadCount,OpportunityCount,WinLossDateCount," \
                     "CampaignCount,InvestmentTotal,insertiondate from " \
                     "us_gtmsales.mst_SellerValidationAggregateCtr where boxyear={} " \
                     "and boxmonth={} and selleruid={}".format(year, month, seller_uid)


    df = connection.execute(procedure_call)
    row = df.fetchall()
    connection.close()

    if row:
        return row[0][4], row[0][5], row[0][6], row[0][7], row[0][8]
    else:
        return 0, 0, 0, 0, 0


def compare_count(box_year, box_month, seller_uid):
    connection = get_redshift_connection()

    # GET PREVIOUS MONTH DATE
    date = '2020-01-20'
    now = datetime.datetime.strptime(date, '%Y-%m-%d')
    prev_date = now + dateutil.relativedelta.relativedelta(months=-1)
    pre_date = prev_date.strftime("%m-%d-%Y")
    month, day, year = pre_date.split("-")

    compare = "Select Leads.BoxYear, Leads.BoxMonth ,Leads.SellerUID, Leads.SellerCompanyName, Leads.CAMPAIGNCOUNT1," \
              "Leads.LEADCOUNT ,Leads.OpportunityCOUNT, Leads.WinLossDateCOUNT, Campaign.CampaignCount2, " \
              "Campaign.InvestmentTotal, Getdate() from (SELECT BoxYear, BoxMonth, SellerUID, SellerCompanyName, " \
              "COUNT (DISTINCT (CRMSystemCampaignID)) CAMPAIGNCOUNT1, COUNT ( (leadid)) LEADCOUNT, " \
              "sum ( case when OpportunityID='' then  0 else 1 end )  OpportunityCOUNT, " \
              "sum ( case when WinLossDate='' then 0 else 1 end ) WinLossDateCOUNT FROM us_gtmsales.Stg_sellerleads_v1 where " \
              "BoxYear={} and  BoxMonth={} and SellerUID={} GROUP BY BoxYear, BoxMonth,SellerUID ,SellerCompanyName " \
              "ORDER BY  BoxYear, BoxMonth,SellerUID,SellerCompanyName) Leads inner join (select selleruid, sellercompanyname, " \
              "count(crmsystemcampaignid) CampaignCount2, sum(translate(investment, ',', '') ) InvestmentTotal from " \
              "us_gtmsales.stg_sellercampaigns_v1 where BoxYear={} and BoxMonth={} and selleruid={}  " \
              "group by BoxYear,BoxMonth,selleruid,sellercompanyname) Campaign " \
              "on Campaign.SellerUID=Leads.SellerUID;".format(month, year, seller_uid, box_year, box_month, seller_uid)
    rows = connection.execute(compare)
    row = rows.fetchall()
    connection.close()
    return row


def insert_count(year, month, seller_id, seller_company_name, lead_count, opportunity_count,
                 win_loss_count, campaign_count, total_investment):
    connection = get_redshift_connection()
    query_insert = "CALL us_gtmsales.usp_InsertSellerAggCtr({},{},{},'{}',{},{},{},{},{},'v_InsertedLog');".format(year,
                                                        month, seller_id, seller_company_name, lead_count,
                                                        opportunity_count, win_loss_count, campaign_count, total_investment)
    rows = connection.execution_options(autocommit=True).execute(query_insert)
    row = rows.fetchall()
    connection.close()
    return row


def delete_data():
    connection = get_redshift_connection()
    connection.execute('TRUNCATE TABLE us_gtmsales.stg_sellerleads_v1')
    connection.execute('TRUNCATE TABLE us_gtmsales.stg_selleropportunities_v1')
    connection.execute('TRUNCATE TABLE us_gtmsales.stg_sellercampaigns_v1')
    connection.close()


def update_file_data(box_year, box_month, seller_name, filename, migrate_status):
    connection = get_redshift_connection()
    query_insert = "call us_gtmsales.usp_insert_mst_sellerDataFile({}, {}, " \
                   "'{}', '{}', '{}')".format(box_year, box_month, seller_name, filename, migrate_status)
    connection.execution_options(autocommit=True).execute(query_insert)
    connection.close()
    return


def verify_master_data(box_year, box_month, seller_uid, seller_name):
    connection = get_redshift_connection()
    query_insert = "call us_gtmsales.usp_VerifyMasterData({}, {}, {}, '{}')".format(box_year, box_month, seller_uid, seller_name)
    connection.execution_options(autocommit=True).execute(query_insert)
    connection.close()
    return


def verify_master_only_data(box_year, box_month, seller_uid, seller_name):
    connection = get_redshift_connection()
    query_insert = "call us_gtmsales.usp_VerifyOnlyMasterData({}, {}, {}, '{}')".format(box_year, box_month, seller_uid, seller_name)
    connection.execution_options(autocommit=True).execute(query_insert)
    connection.close()
    return
