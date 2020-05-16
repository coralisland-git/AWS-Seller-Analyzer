create table us_gtmsales.region_goals_2020
(
	goals2020 text,
	mal integer,
	sql integer,
	pipeline decimal(12,2),
	wins integer,
	gms$ decimal(12,2),
	tcv$ decimal(12,2),
	roi decimal(12,2),
	mdfinvestment$ decimal(12,2)
);

insert into us_gtmsales.region_goals_2020 (goals2020) values ('Worldwide');
insert into us_gtmsales.region_goals_2020 (goals2020) values ('EMEA');
insert into us_gtmsales.region_goals_2020 (goals2020) values ('APAC');

create table us_gtmsales.seller_billed_rev_type
(
	selleruid bigint,
	sellercompanyname text,
	billedrevenuetype text,
	billedrevenuecalctogms text
);

insert into us_gtmsales.seller_billed_rev_type (selleruid, sellercompanyname, billedrevenuetype, billedrevenuecalctogms) values ((select selleruid from us_gtmsales.mst_sellerparticipant where sellercompanyname = 'AppDynamics'), 'AppDynamics','TCV','TCV/1.583');
insert into us_gtmsales.seller_billed_rev_type (selleruid, sellercompanyname, billedrevenuetype, billedrevenuecalctogms) values ((select selleruid from us_gtmsales.mst_sellerparticipant where sellercompanyname = 'CrowdStrike'), 'CrowdStrike','ACV','Same as GMS');
insert into us_gtmsales.seller_billed_rev_type (selleruid, sellercompanyname) values ((select selleruid from us_gtmsales.mst_sellerparticipant where sellercompanyname = 'Fortinet'), 'Fortinet');
insert into us_gtmsales.seller_billed_rev_type (selleruid, sellercompanyname) values ((select selleruid from us_gtmsales.mst_sellerparticipant where sellercompanyname = 'Matillion'), 'Matillion');
insert into us_gtmsales.seller_billed_rev_type (selleruid, sellercompanyname, billedrevenuetype, billedrevenuecalctogms) values ((select selleruid from us_gtmsales.mst_sellerparticipant where sellercompanyname = 'N2WS'), 'N2WS','TCV','TCV/1.583');
insert into us_gtmsales.seller_billed_rev_type (selleruid, sellercompanyname) values ((select selleruid from us_gtmsales.mst_sellerparticipant where sellercompanyname = 'NetApp'), 'NetApp');
insert into us_gtmsales.seller_billed_rev_type (selleruid, sellercompanyname, billedrevenuetype, billedrevenuecalctogms) values ((select selleruid from us_gtmsales.mst_sellerparticipant where sellercompanyname = 'NewRelic'), 'NewRelic','ARR','Same as GMS');
insert into us_gtmsales.seller_billed_rev_type (selleruid, sellercompanyname, billedrevenuetype) values ((select selleruid from us_gtmsales.mst_sellerparticipant where sellercompanyname = 'PaloAltoNetworks'), 'PaloAltoNetworks','TCV');
insert into us_gtmsales.seller_billed_rev_type (selleruid, sellercompanyname) values ((select selleruid from us_gtmsales.mst_sellerparticipant where sellercompanyname = 'Splunk'), 'Splunk');
insert into us_gtmsales.seller_billed_rev_type (selleruid, sellercompanyname, billedrevenuetype, billedrevenuecalctogms) values ((select selleruid from us_gtmsales.mst_sellerparticipant where sellercompanyname = 'SumoLogic'), 'SumoLogic','TCV','TCV/1.583');
insert into us_gtmsales.seller_billed_rev_type (selleruid, sellercompanyname) values ((select selleruid from us_gtmsales.mst_sellerparticipant where sellercompanyname = 'Trend Micro'), 'Trend Micro');
insert into us_gtmsales.seller_billed_rev_type (selleruid, sellercompanyname) values ((select selleruid from us_gtmsales.mst_sellerparticipant where sellercompanyname = 'Druva'), 'Druva');

create table us_gtmsales.seller_plan_data_2020
(
	sellercompanyname text,
	totalgmsgoal$ decimal(12,2),
	gtmgmsgoal$ decimal(12,2),
	awsprogrambudget decimal(12,2),
	sellerbudgetcommitted decimal(12,2),
	mal integer,
	mql integer,
	sql integer,
	pipeline decimal(12,2),
	wins integer
);

insert into us_gtmsales.seller_plan_data_2020 (sellercompanyname) values ('Druva');
insert into us_gtmsales.seller_plan_data_2020 (sellercompanyname) values ('NewRelic');
insert into us_gtmsales.seller_plan_data_2020 (sellercompanyname) values ('NetApp');
insert into us_gtmsales.seller_plan_data_2020 (sellercompanyname) values ('Splunk');
insert into us_gtmsales.seller_plan_data_2020 (sellercompanyname) values ('Trend Micro');
insert into us_gtmsales.seller_plan_data_2020 (sellercompanyname) values ('Fortinet Inc.');
insert into us_gtmsales.seller_plan_data_2020 (sellercompanyname) values ('CrowdStrike');
insert into us_gtmsales.seller_plan_data_2020 (sellercompanyname) values ('PANW');
insert into us_gtmsales.seller_plan_data_2020 (sellercompanyname) values ('SumoLogic');
insert into us_gtmsales.seller_plan_data_2020 (sellercompanyname) values ('N2W Software');
insert into us_gtmsales.seller_plan_data_2020 (sellercompanyname) values ('Matillion');
insert into us_gtmsales.seller_plan_data_2020 (sellercompanyname) values ('AppD');

create table us_gtmsales.demand_gen_seasonality_2020
(
	source text,
	jan decimal(3,2),
	feb decimal(3,2),
	mar decimal(3,2),
	apr decimal(3,2),
	may decimal(3,2),
	jun decimal(3,2),
	jul decimal(3,2),
	aug decimal(3,2),
	sep decimal(3,2),
	oct decimal(3,2),
	nov decimal(3,2),
	dec decimal(3,2)
);

insert into us_gtmsales.demand_gen_seasonality_2020(source, jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec) values('MAL',0.02,0.07,0.13,0.22,0.32,0.44,0.56,0.68,0.8,0.9,0.98,1);
insert into us_gtmsales.demand_gen_seasonality_2020(source, jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec) values('SQL/Pipeline Rev',0.03,0.07,0.13,0.21,0.31,0.43,0.55,0.67,0.81,0.93,0.99,1);
insert into us_gtmsales.demand_gen_seasonality_2020(source, jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec) values('GMS/Win/Billed Rev',0.02,0.07,0.12,0.18,0.26,0.36,0.46,0.54,0.64,0.76,0.88,1);

