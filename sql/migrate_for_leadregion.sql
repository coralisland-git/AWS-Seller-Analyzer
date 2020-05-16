alter table us_gtmsales.mst_sellerleads rename to mst_sellerleads_before_leadregion;

create table us_gtmsales.mst_sellerleads
(
  selleruid integer not null,
  sellercompanyname varchar(50) not null,
  crmsystemcampaignid varchar(30) not null,
  campaignname varchar(100) not null,
  gtmcampaignsource varchar(10) not null,
  campaigncreatedate varchar(50),
  leadid varchar(30) not null,
  createdate varchar(50) not null,
  leadcountry varchar(100) not null,
  leadregion varchar(100),
  leadtype varchar(3) not null,
  leadstatus varchar(6) not null,
  opportunityid varchar(30),
  convertdate varchar(50),
  opportunitytype varchar(3),
  opportunitystatus varchar(6),
  awsmarketopportunity varchar(15),
  pipelinerevenue numeric,
  windate varchar(50),
  billedrevenue numeric,
  boxmonth integer,
  boxyear integer,
  insertiondate timestamp without time zone
);

-- copy in every field except lead_region because the original table did not contain leadregion
insert into us_gtmsales.mst_sellerleads
(
  selleruid,
  sellercompanyname,
  crmsystemcampaignid,
  campaignname,
  gtmcampaignsource,
  campaigncreatedate,
  leadid,
  createdate,
  leadcountry,
  leadtype,
  leadstatus,
  opportunityid,
  convertdate,
  opportunitytype,
  opportunitystatus,
  awsmarketopportunity,
  pipelinerevenue,
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
leadid,
createdate,
leadcountry,
leadtype,
leadstatus,
opportunityid,
convertdate,
opportunitytype,
opportunitystatus,
awsmarketopportunity,
pipelinerevenue,
windate,
billedrevenue,
boxmonth,
boxyear,
insertiondate
from us_gtmsales.mst_sellerleads_before_leadregion;
