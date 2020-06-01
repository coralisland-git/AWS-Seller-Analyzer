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