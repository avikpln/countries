-- TODO

CREATE DATABASE IF NOT EXISTS World;
USE World;

DROP TABLE IF EXISTS Country;

START TRANSACTION;

CREATE TABLE Country (
  CountryID INTEGER PRIMARY KEY AUTO_INCREMENT,
  CountryName VARCHAR(255) NOT NULL,
  CountryCode VARCHAR(255) NOT NULL,
  Capital VARCHAR(255) NOT NULL,
  Continent VARCHAR(255) NOT NULL,
--  CONSTRAINT PK_Country PRIMARY KEY (CountryID),
  CONSTRAINT UC_CountryName UNIQUE (CountryName),
  CONSTRAINT UC_CountryCode UNIQUE (CountryCode)
);

/* Doesn't work :( The MySQL server is running with the --secure-file-priv option so it cannot execute this statement */
LOAD DATA INFILE 'countries.csv' INTO TABLE Country
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

COMMIT;