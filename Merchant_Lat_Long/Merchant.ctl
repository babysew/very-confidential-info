LOAD DATA
INFILE 'C:\Merchant_Lat_Long\Merchant.csv'  "str '\r\n'"
Replace
--Append
INTO TABLE Merchant_Lat_Long
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
TRAILING NULLCOLS
(
 	Original_Name
,	Original_City
,	Google_Search_Name
,	Address
,	Latitude
,	Longitude
)