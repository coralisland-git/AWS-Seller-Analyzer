alter table us_gtmsales.stg_selleropportunities_v1 rename to stg_selleropportunities_v1_before_opportunityregion;

create table us_gtmsales.stg_selleropportunities_v1
(
  selleruid integer not null,
  sellercompanyname varchar(50) not null,
  crmsystemcampaignid varchar(30) not null,
  campaignname varchar(100) not null,
  gtmcampaignsource varchar(10) not null,
  campaigncreatedate varchar(50),
  opportunityid varchar(30),
  convertdate varchar(50),
  opportunitycountry varchar(20),  
  opportunitystatus varchar(6),
  awsmarketopportunity varchar(15),
  pipelinerevenue numeric,
  accountname varchar(30),
  accountid varchar(20),
  windate varchar(50),
  billedrevenue numeric,
  boxmonth integer,
  boxyear integer,
  insertiondate timestamp without time zone
);

insert into us_gtmsales.stg_selleropportunities_v1
(
  selleruid,
  sellercompanyname,
  crmsystemcampaignid,
  campaignname,
  gtmcampaignsource,
  campaigncreatedate,
  opportunityid,
  convertdate,
  opportunitycountry,
  opportunitystatus,
  awsmarketopportunity,
  pipelinerevenue,
  accountname,
  accountid,
  windate,
  billedrevenue,
  boxmonth,
  boxyear,
  insertiondate
)
select
  selleruid,
  sellercompanyname,
  crmsystemcampaignid,
  campaignname,
  gtmcampaignsource,
  campaigncreatedate,
  opportunityid,
  convertdate,
  opportunitycountry,
  opportunitystatus,
  awsmarketopportunity,
  pipelinerevenue,
  accountname,
  accountid,
  windate,
  billedrevenue,
  boxmonth,
  boxyear,
  insertiondate
from us_gtmsales.stg_selleropportunities_v1_before_opportunityregion;
