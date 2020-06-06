drop table if exists us_gtmsales.stg_sellercampaigns_v1;
drop table if exists us_gtmsales.stg_sellerleads_v1;
drop table if exists us_gtmsales.stg_selleropportunities_v1;


create table us_gtmsales.stg_sellercampaigns_v1
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

create table us_gtmsales.stg_sellerleads_v1
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
  leadstatus varchar(6) not null,
  boxmonth integer,
  boxyear integer,
  insertiondate timestamp without time zone
);

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
  accountname varchar(150),
  accountid varchar(100),
  windate varchar(50),
  billedrevenue numeric,
  boxmonth integer,
  boxyear integer,
  insertiondate timestamp without time zone
);


create table us_gtmsales.mst_sellercampaigns_v1_bak as select * from us_gtmsales.mst_sellercampaigns_v1;
create table us_gtmsales.mst_sellerleads_v1_bak as select * from us_gtmsales.mst_sellerleads_v1;
create table us_gtmsales.mst_selleropportunities_v1_bak as select * from us_gtmsales.mst_selleropportunities_v1;

drop table if exists us_gtmsales.mst_sellercampaigns_v1;
drop table if exists us_gtmsales.mst_sellerleads_v1;
drop table if exists us_gtmsales.mst_selleropportunities_v1;

create table us_gtmsales.mst_sellercampaigns_v1
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

create table us_gtmsales.mst_sellerleads_v1
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
  leadstatus varchar(6) not null,
  boxmonth integer,
  boxyear integer,
  insertiondate timestamp without time zone
);

create table us_gtmsales.mst_selleropportunities_v1
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
  accountname varchar(150),
  accountid varchar(100),
  windate varchar(50),
  billedrevenue numeric,
  boxmonth integer,
  boxyear integer,
  insertiondate timestamp without time zone
);

insert into us_gtmsales.mst_sellercampaigns_v1
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
from us_gtmsales.mst_sellercampaigns_v1_bak;

insert into us_gtmsales.mst_sellerleads_v1
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
  leadstatus,
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
  leadstatus,
  boxmonth,
  boxyear,
  insertiondate
from us_gtmsales.mst_sellerleads_v1_bak;

insert into us_gtmsales.mst_selleropportunities_v1
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
from us_gtmsales.mst_selleropportunities_v1_bak;