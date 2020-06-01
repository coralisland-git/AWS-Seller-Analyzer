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
left(regexp_replace(campaigncreatedate, '\-|\\/|\:|\\.'), 8) campaigncreatedate,
leadid,
left(regexp_replace(createdate, '\-|\\/|\:|\\.'), 8) createdate,
leadcountry,
leadstatus,
boxmonth,
boxyear,
getdate() from us_gtmsales.stg_sellerleads_v1;