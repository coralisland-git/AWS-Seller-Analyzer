drop table if exists us_gtmsales.stg_sellercampaigns;
drop table if exists us_gtmsales.stg_sellerleads;

create table us_gtmsales.stg_sellercampaigns
(
	selleruid integer not null,
	sellercompanyname varchar(50) not null,
	gtmcampaignsource varchar(10) not null,
	campaignname varchar(100) not null,
	crmsystemcampaignid varchar(30) not null,
	campaigncreatedate varchar(50),
	investment numeric,
	boxmonth integer,
	boxyear integer,
	insertiondate timestamp without time zone
);

create table us_gtmsales.stg_sellerleads
(
	selleruid integer not null,
	sellercompanyname varchar(50) not null,
	crmsystemcampaignid varchar(30) not null,
	campaignname varchar(100) not null,
	gtmcampaignsource varchar(10) not null,
	campaigncreatedate varchar(50),
	leadid varchar(30) not null,
	createdate varchar(50) not null,
	leadcountry varchar(50) not null,
	leadtype varchar(3) not null,
	leadstatus varchar(6) not null,
	opportunityid varchar(30),
	convertdate varchar(50),
	opportunitytype varchar(3),
	opportunitystatus varchar(6),
	awsmarketopportunity varchar(15),
	pipelinerevenue varchar(20),
	windate varchar(50),
	billedrevenue varchar(20),
	boxmonth integer,
	boxyear integer,
	insertiondate timestamp without time zone
);

create table us_gtmsales.mst_sellercampaigns_bak as select * from us_gtmsales.mst_sellercampaigns;
create table us_gtmsales.mst_sellerleads_bak as select * from us_gtmsales.mst_sellerleads;

drop table if exists us_gtmsales.mst_sellercampaigns;
drop table if exists us_gtmsales.mst_sellerleads;

create table us_gtmsales.mst_sellercampaigns
(
  selleruid integer not null,
  sellercompanyname varchar(50) not null,
  gtmcampaignsource varchar(10) not null,
  campaignname varchar(100) not null,
  crmsystemcampaignid varchar(30) not null,
  campaigncreatedate varchar(50),
  investment numeric,
  boxmonth integer,
  boxyear integer,
  insertiondate timestamp without time zone
);

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

insert into us_gtmsales.mst_sellercampaigns
(
  selleruid,
  sellercompanyname,
  gtmcampaignsource,
  campaignname,
  crmsystemcampaignid,
  investment,
  boxmonth,
  boxyear,
  insertiondate
)
select
selleruid,
sellercompanyname,
gtmcampaignsource,
campaignname,
crmsystemcampaignid,
investment,
boxmonth,
boxyear,
insertiondate
from us_gtmsales.mst_sellercampaigns_bak;

insert into us_gtmsales.mst_sellerleads
(
  selleruid,
  sellercompanyname,
  crmsystemcampaignid,
  campaignname,
  gtmcampaignsource,
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
from us_gtmsales.mst_sellerleads_bak;