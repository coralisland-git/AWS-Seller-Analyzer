drop table if exists us_gtmsales.leads_opps_wins;

create table us_gtmsales.leads_opps_wins
(
  seller_report_order int,
  seller_company_name text,
  gtm_campaign_source text,
  gtm_campaign_source_grouped text,
  campaign_name text,
  crm_system_campaign_id text,
  campaign_create_date date,
  lead_id text,
  create_date date,
  lead_country text,
  lead_type text,
  lead_status text,
  lead_region text,
  opportunity_id text,
  convert_date date,
  opportunity_type text,
  opportunity_status text,
  aws_marketplace_opportunity text,
  pipeline_revenue decimal(12,2),
  pipeline_revenue_in_gms decimal(12,2),
  win_date date,
  billed_revenue decimal(12,2),
  billed_revenue_in_gms decimal(12,2),
  revenue_type text,
  revenue_calculation_to_gms text
);

drop table if exists us_gtmsales.campaigns;

create table us_gtmsales.campaigns
(
  seller_report_order int,
  seller_company_name text,
  gtm_campaign_source text,
  gtm_campaign_source_grouped text,
  campaign_name text,
  crm_system_campaign_id text,
  campaign_create_date date,
  investment decimal(12,2),
  revised_investment decimal(12,2),
  aws_investment decimal(12,2)
);

drop table if exists us_gtmsales.internal_goals;

create table us_gtmsales.internal_goals
(
  seller_report_order int,
  seller_company_name text,
  total_gms_goal decimal(12,2),
  gtm_gms_goal decimal(12,2),
  aws_program_budget decimal(12,2),
  seller_budget_committed decimal(12,2),
  mal int,
  sql int,
  pipeline decimal(12,2),
  wins int,
  region text,
  campaign_source text
);

drop table if exists us_gtmsales.external_goals;

create table us_gtmsales.external_goals
(
  seller_report_order int,
  seller_company_name text,
  gtm_gms_goal decimal(12,2),
  aws_mdf decimal (12,2),
  seller_budget_committed decimal(12,2),
  mals int,
  sqls int,
  wins int,
  tcv decimal(12,2),
  pipeline decimal(12,2),
  region text,
  campaign_source text
);
