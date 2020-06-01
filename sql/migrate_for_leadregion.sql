alter table us_gtmsales.mst_sellerleads_v1 rename to mst_sellerleads_v1_before_leadregion;

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

-- copy in every field except lead_region because the original table did not contain leadregion
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
from us_gtmsales.mst_sellerleads_v1_before_leadregion;
