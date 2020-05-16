create temp table leadcountry_to_geo_code as
(
  select country_name, geo_code
  from us_gtmsales.countries
  union
  select country_code, geo_code
  from us_gtmsales.countries
  union
  select country_code_iso_3a, geo_code
  from us_gtmsales.countries
);