insert into us_gtmsales.mst_SellerCampaigns
(
  selleruid,
  sellercompanyname,
  gtmcampaignsource,
  campaignname,
  crmsystemcampaignid,
  campaigncreatedate,
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
left(regexp_replace(campaigncreatedate, '\-|\\/|\:|\\.'), 8) campaigncreatedate,
investment,
boxmonth,
boxyear,
getdate()
from
us_gtmsales.stg_sellercampaigns;