import os

s = """--SELECT * FROM audit.aaa
CREATE OR REPLACE TABLE audit.aaa
ENGINE = MergeTree()
ORDER BY tuple()
AS (

WITH
BPM AS (
SELECT
	id,
	order__id,
	created_date,
	--state,
	--order__transport_solution__location__from__catalog_id,
	--dictGet('dict_location', 'name', order__transport_solution__location__from__catalog_id) AS order__transport_solution__location__from__catalog_name,
	--dictGet('dict_location', 'name', order__transport_solution__location__to__catalog_id) AS order__transport_solution__location__to__catalog_name,
	--
	order__transport_solution__legs,
	arrayJoin(emptyArrayToSingle(JSONExtractArrayRaw(order__transport_solution__legs))) AS legs_array,
	JSONExtractInt(legs_array,'id') AS leg_id,
	--FROM
	JSONExtractString(JSONExtractRaw(JSONExtractRaw(legs_array,'points'),'from'),'catalog_id') AS leg_points_from_catalog_id,
	dictGet('dict_location', 'name', leg_points_from_catalog_id) AS leg_points_from_catalog_name,
	JSONExtractRaw(JSONExtractString(JSONExtractRaw(legs_array,'points'),'from'),'station_id') AS leg_points_from_station_id,
	dictGet('dict_stations', 'station_name',  leg_points_from_station_id) AS leg_points_from_station_name,	
	JSONExtractString(JSONExtractRaw(JSONExtractRaw(legs_array,'points'),'to'),'catalog_id') AS leg_points_to_catalog_id,
	--TO
	JSONExtractString(JSONExtractRaw(JSONExtractRaw(legs_array,'points'),'to'),'catalog_id') AS leg_points_to_catalog_id,
	dictGet('dict_location', 'name', leg_points_to_catalog_id) AS leg_points_to_catalog_name,
	JSONExtractString(JSONExtractRaw(JSONExtractRaw(legs_array,'points'),'to'),'station_id') AS leg_points_to_station_id,
	dictGet('dict_stations', 'station_name',  leg_points_to_station_id) AS leg_points_to_station_name,	
	JSONExtractString(JSONExtractRaw(JSONExtractRaw(legs_array,'points'),'to'),'catalog_id') AS leg_points_to_catalog_id,
	--
	arrayJoin(emptyArrayToSingle(JSONExtractArrayRaw(JSONExtractRaw(legs_array,'services')))) AS services_array,
	JSONExtractInt(services_array,'id') AS service_id,
	JSONExtractString(services_array,'epu_id') AS service_epu_id,			
	arrayJoin(emptyArrayToSingle(JSONExtractArrayRaw(services_array,'details'))) AS service_details_array,
	JSONExtractInt(service_details_array,'id') AS service_details_id,
	JSONExtractString(service_details_array,'esu_id') AS service_details_esu_id,
	JSONExtractFloat(service_details_array,'cost_per_unit') AS service_details_cost_per_unit,
	JSONExtractFloat(service_details_array,'cost_per_unit_in_contract_currency') AS service_details_cost_per_unit_in_contract_currency,
	order__add_info__organizations
FROM 
	bpm__order AS BPM	-- SELECT * FROM bpm__order
WHERE
	created_date>'2024-01-01' AND
	service_details_esu_id='0.01.03.01' --order__add_info__organizations
--) SELECT * FROM BPM --WHERE order__id=32673521
),
BPM AS (
SELECT
	id,order__id,created_date,--order__transport_solution__legs,legs_array,leg_id,leg_points_from_catalog_id,leg_points_from_catalog_name,leg_points_from_station_id,leg_points_from_station_name,leg_points_to_catalog_id,leg_points_to_catalog_name,leg_points_to_station_id,leg_points_to_station_name,services_array,
	service_id,service_epu_id,--service_details_array,service_details_id,service_details_esu_id,
	countIf(service_details_cost_per_unit<0) OVER (PARTITION BY id,order__id,created_date,service_id,service_epu_id) AS q,
	service_details_cost_per_unit,
	arrayStringConcat(groupArray(service_details_cost_per_unit) OVER (PARTITION BY id, order__id), '; ') AS service_details_cost_per_unit_info,	
	sum(service_details_cost_per_unit) OVER (PARTITION BY id, order__id) AS service_details_cost_per_unit_total,
	service_details_cost_per_unit_in_contract_currency,
	arrayStringConcat(groupArray(service_details_cost_per_unit_in_contract_currency) OVER (PARTITION BY id, order__id), '; ')  AS service_details_cost_per_unit_in_contract_currency_info,	
	sum(service_details_cost_per_unit_in_contract_currency) OVER (PARTITION BY id, order__id) AS service_details_cost_per_unit_in_contract_currency_total
	--,order__add_info__organizations
FROM
	BPM
--) SELECT * FROM BPM WHERE order__id=32673521
)
SELECT
	--id,
	order__id,created_date,--service_id,service_epu_id,q,
	arrayStringConcat(groupArray(service_details_cost_per_unit), ';' ) AS service_details_cost_per_unit_discounts,
	service_details_cost_per_unit_info,service_details_cost_per_unit_total,
	arrayStringConcat(groupArray(service_details_cost_per_unit_in_contract_currency), ';' ) AS service_details_cost_per_unit_in_contract_currency_discounts,
	service_details_cost_per_unit_in_contract_currency_info,service_details_cost_per_unit_in_contract_currency_total
FROM
	BPM WHERE q>1
GROUP BY
	--id,
	order__id,created_date,--service_id,service_epu_id,q,service_details_cost_per_unit,
	service_details_cost_per_unit_info,	service_details_cost_per_unit_total,--service_details_cost_per_unit_in_contract_currency,
	service_details_cost_per_unit_in_contract_currency_info,service_details_cost_per_unit_in_contract_currency_total
ORDER BY order__id

)

SELECT * FROM audit.bbb

CREATE OR REPLACE TABLE audit.bbb
ENGINE = MergeTree()
ORDER BY tuple()
AS (

WITH
SVOD AS (
SELECT
	order__id,created_date,service_details_cost_per_unit_discounts,service_details_cost_per_unit_info,service_details_cost_per_unit_total,service_details_cost_per_unit_in_contract_currency_discounts,service_details_cost_per_unit_in_contract_currency_info,service_details_cost_per_unit_in_contract_currency_total
FROM audit.aaa
--) SELECT * FROM SVOD 
),
RKS AS (
SELECT
    service_details_order_id,
    count(DISTINCT equipment_number) AS equipment_number_qty,
    ---------------------------------------------------------------------
    sum(amount_in_rub_without_vat) AS amount_in_rub_without_vat,
    sum(amount_in_contract_currency_without_vat) AS amount_in_contract_currency_without_vat,
    sum(amount_in_rub_with_vat) AS amount_in_rub_with_vat,
    sum(amount_in_contract_currency_with_vat) AS amount_in_contract_currency_with_vat    
FROM 
	(SELECT DISTINCT * FROM rks__directly WHERE client_number_id <> '0009309810' AND is_deleted=False AND date_end >= '2024-01-01')
WHERE
	esu_id IN ('0.01.03.01')
	AND service_details_order_id IN (SELECT order__id FROM SVOD)
GROUP BY 	
	service_details_order_id
HAVING
	(amount_in_rub_without_vat<>0 OR 
	amount_in_contract_currency_without_vat<>0 OR
	amount_in_rub_with_vat<>0 OR
    amount_in_contract_currency_with_vat<>0) 
--) SELECT * FROM RKS
),
ANSWER AS (
SELECT
	SVOD.*,
	'<==SVOD RKS==>',
	RKS.*
FROM
	SVOD
	LEFT JOIN RKS ON toString(SVOD.order__id) = RKS.service_details_order_id
)
SELECT
	order__id,created_date,service_details_cost_per_unit_discounts,service_details_cost_per_unit_info,service_details_cost_per_unit_total,service_details_cost_per_unit_in_contract_currency_discounts,service_details_cost_per_unit_in_contract_currency_info,
	service_details_cost_per_unit_in_contract_currency_total,
	service_details_cost_per_unit_in_contract_currency_total * equipment_number_qty AS `с учётом оборудования`,
	`'<==SVOD RKS==>'`,
	service_details_order_id,equipment_number_qty,amount_in_rub_without_vat,amount_in_contract_currency_without_vat,amount_in_rub_with_vat,amount_in_contract_currency_with_vat
FROM
	ANSWER

)

--download
SELECT * FROM audit.bbb
"""
path = os.path.join(os.getcwd(),s)
os.startfile(path)