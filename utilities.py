import configparser
import boto3
import sys
import time
from sqlalchemy.engine import url as sa_url
from sqlalchemy import create_engine



def get_month_from_sys_args():
    return sys.argv[1].split("/")[2]


def get_month_as_int():
    return time.strptime(get_month_from_sys_args(), "%B").tm_mon


def get_year_from_sys_args():
    return sys.argv[1].split("/")[1]


def get_s3_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['s3']


def get_s3_bucket():
    s3_config = get_s3_config()
    return s3_config['bucket']


def get_s3_client():
    s3_config = get_s3_config()

    return boto3.client(
        's3',
        aws_access_key_id=s3_config['access_key_id'],
        aws_secret_access_key=s3_config['secret_access_key']
    )


def get_redshift_connection():
    # get Redshift configuration values from file
    config = configparser.ConfigParser()
    config.read('config.ini')
    redshift_config = config['redshift']

    # connect to Redshift
    db_connect_url = sa_url.URL(
            drivername='postgresql+psycopg2',
            username=redshift_config['user'],
            password=redshift_config['password'],
            host=redshift_config['host'],
            port=redshift_config['port'],
            database=redshift_config['dbname']
        )
    engine = create_engine(db_connect_url)
    return engine.connect()
