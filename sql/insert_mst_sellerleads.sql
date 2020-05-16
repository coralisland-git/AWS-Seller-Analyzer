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
  leadregion,
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
left(regexp_replace(campaigncreatedate, '\-|\\/|\:|\\.'), 8) campaigncreatedate,
leadid,
left(regexp_replace(createdate, '\-|\\/|\:|\\.'), 8) createdate,
leadcountry,
case
when upper(leadcountry) in
(
  select country_name
  from leadcountry_to_geo_code
)
then
(
  select distinct geo_code
  from leadcountry_to_geo_code
  where upper(leadcountry) = leadcountry_to_geo_code.country_name
  limit 1
 )
else null
end as leadregion,
leadtype,
leadstatus,
opportunityid,
left(regexp_replace(convertdate  , '\-|\\/|\:|\\.'), 8) convertdate,
opportunitytype,
opportunitystatus,
awsmarketopportunity,
case
when pipelinerevenue = ''
or pipelinerevenue is null
then 0
else cast (pipelinerevenue as decimal(20,2))
end,
left(regexp_replace(windate  , '\-|\\/|\:|\\.'), 8)  windate,
case when billedrevenue = ''
or billedrevenue is null
then 0
else cast (pipelinerevenue as decimal(20,2)) end,
boxmonth,
boxyear,
getdate() from us_gtmsales.stg_sellerleads;