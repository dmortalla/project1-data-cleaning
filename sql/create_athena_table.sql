CREATE DATABASE IF NOT EXISTS superstore_sales;
CREATE EXTERNAL TABLE IF NOT EXISTS superstore_sales.region_summary (
  Region string,
  Sales double,
  Profit double
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES ('serialization.format' = ',')
LOCATION 's3://superstore-processed-data/'
TBLPROPERTIES ('has_encrypted_data'='false');
