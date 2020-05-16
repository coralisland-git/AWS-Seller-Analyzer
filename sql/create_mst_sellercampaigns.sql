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