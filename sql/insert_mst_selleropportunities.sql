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
left(regexp_replace(campaigncreatedate, '\-|\\/|\:|\\.'), 8) campaigncreatedate,
opportunityid,
left(regexp_replace(convertdate  , '\-|\\/|\:|\\.'), 8) convertdate,
opportunitycountry,
opportunitystatus,
awsmarketopportunity,
case
when pipelinerevenue is null
then 0
else cast (pipelinerevenue as decimal(20,2))
end,
accountname,
accountid,
left(regexp_replace(windate  , '\-|\\/|\:|\\.'), 8)  windate,
case when billedrevenue is null
then 0
else cast (pipelinerevenue as decimal(20,2)) end,
boxmonth,
boxyear,
getdate() from us_gtmsales.stg_selleropportunities_v1;