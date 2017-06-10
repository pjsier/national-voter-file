  -- National Voter File Database Tables
-- This file contains the DDL for creating the tables, views, and indexes for
-- the national voter file data warehouse

  CREATE EXTENSION postgis;


DROP TABLE IF EXISTS DATE_DIM CASCADE;
CREATE TABLE DATE_DIM
(
  DATE_ID INTEGER NOT NULL PRIMARY KEY
, DATE_VALUE DATE NOT NULL
, DATE_FULL VARCHAR(29)
, DATE_LONG VARCHAR(19)
, DATE_MEDIUM VARCHAR(15)
, DATE_SHORT VARCHAR(8)
, DAY_ABBREVIATION VARCHAR(3)
, DAY_IN_MONTH INTEGER
, DAY_IN_YEAR INTEGER
, DAY_NAME VARCHAR(9)
, MONTH_ABBREVIATION CHAR(3)
, MONTH_NAME VARCHAR(9)
, MONTH_NUMBER INTEGER
, QUARTER_NAME CHAR(2)
, QUARTER_NUMBER INTEGER
, WEEK_IN_MONTH INTEGER
, WEEK_IN_YEAR INTEGER
, YEAR2 CHAR(2)
, YEAR4 CHAR(4)
, YEAR_MONTH_ABBREVIATION CHAR(8)
, YEAR_MONTH_NUMBER CHAR(7)
, YEAR_QUARTER CHAR(7)
, IS_FIRST_DAY_IN_MONTH BOOLEAN
, IS_LAST_DAY_IN_MONTH BOOLEAN
, IS_LAST_DAY_IN_WEEK BOOLEAN
, IS_FIRST_DAY_IN_WEEK BOOLEAN
)
;
DROP INDEX IF EXISTS DATE_DIM_DATE_IDX;
CREATE UNIQUE INDEX DATE_DIM_DATE_IDX on DATE_DIM(DATE_VALUE);

DROP TABLE IF EXISTS REPORTER_DIM CASCADE;
CREATE TABLE REPORTER_DIM
  (
    REPORTER_ID   SERIAL NOT NULL PRIMARY KEY ,
    REPORTER_NAME VARCHAR (50) ,
    REPORTER_TYPE VARCHAR (50)
  ) ;


DROP TABLE IF EXISTS PARTY_DIM CASCADE;
CREATE TABLE PARTY_DIM(
  PARTY_ID SERIAL NOT NULL PRIMARY KEY,
  PARTY_CODE VARCHAR(3) NOT NULL,
  PARTY_NAME VARCHAR(128) NOT NULL,
  VERSION		INTEGER NOT NULL DEFAULT(0),
  VALID_FROM		DATE NOT NULL DEFAULT('1900-01-01'),
  VALID_TO		DATE NOT NULL DEFAULT('2199-12-31')
);

DROP TABLE IF EXISTS PERSON_DIM CASCADE;
CREATE TABLE PERSON_DIM
  (
    PERSON_ID     BIGSERIAL NOT NULL PRIMARY KEY ,
    BIRTHDATE     DATE
  ) ;

DROP TABLE IF EXISTS VOTER_DIM CASCADE;
CREATE TABLE VOTER_DIM
  (
    VOTER_ID            	BIGSERIAL NOT NULL PRIMARY KEY,
    PERSON_KEY          	BIGINT NULL ,
    STATE_VOTER_REF   	VARCHAR (31) NULL ,
    COUNTY_VOTER_REF	VARCHAR(20) NULL,
    TITLE               	VARCHAR (5) NULL,
    FIRST_NAME               	VARCHAR (50) NULL ,
    MIDDLE_NAME               VARCHAR (50) NULL ,
    LAST_NAME               	VARCHAR (50) NULL ,
    NAME_SUFFIX          	VARCHAR (10) NULL ,
    GENDER              	CHAR (1) NULL,
    RACE                  CHAR(1) NULL,
    BIRTHDATE     		DATE NULL,
    BIRTH_STATE           CHAR(2) NULL,
    REGISTRATION_DATE   	DATE NULL,
    REGISTRATION_STATUS 	VARCHAR (15) NULL,
    ABSTENTEE_TYPE      	VARCHAR (1) NULL,
    EMAIL               	VARCHAR (50) NULL,
    PHONE               	VARCHAR (15) NULL,
    DO_NOT_CALL_STATUS  	VARCHAR (1) NULL,
    LANGUAGE_CHOICE     	VARCHAR (3) NULL,
    VERSION		INTEGER NOT NULL DEFAULT(0),
    VALID_FROM		DATE NOT NULL DEFAULT('1900-01-01'),
    VALID_TO		DATE NOT NULL DEFAULT('2199-12-31')
  ) ;
DROP INDEX IF EXISTS STATE_VOTER_REF_IDX;
  CREATE INDEX STATE_VOTER_REF_IDX ON VOTER_DIM(STATE_VOTER_REF);

  DROP INDEX IF EXISTS VOTER_PERSON_KEY_IDX;
  CREATE INDEX VOTER_PERSON_KEY_IDX ON VOTER_DIM(PERSON_KEY);


DROP TABLE IF EXISTS HOUSEHOLD_DIM CASCADE;
CREATE TABLE HOUSEHOLD_DIM
  (
    HOUSEHOLD_ID                 BIGSERIAL NOT NULL PRIMARY KEY,
    ADDRESS_NUMBER               VARCHAR(15) ,
    ADDRESS_NUMBER_PREFIX        VARCHAR(2) ,
    ADDRESS_NUMBER_SUFFIX        VARCHAR(5) ,
    BUILDING_NAME                VARCHAR(50) ,
    CORNER_OF                    VARCHAR(50) ,
    INTERSECTION_SEPARATOR       VARCHAR(5) ,
    LANDMARK_NAME                VARCHAR(50) ,
    NOT_ADDRESS                  VARCHAR(30) ,
    OCCUPANCY_TYPE               VARCHAR(20) ,
    OCCUPANCY_IDENTIFIER         VARCHAR(20) ,
    PLACE_NAME                   VARCHAR(50) ,
    STATE_NAME                   VARCHAR(15) ,
    STREET_NAME                  VARCHAR(50) ,
    STREET_NAME_PRE_DIRECTIONAL  VARCHAR(10) ,
    STREET_NAME_PRE_MODIFIER     VARCHAR(10) ,
    STREET_NAME_PRE_TYPE         VARCHAR(10) ,
    STREET_NAME_POST_DIRECTIONAL VARCHAR(10) ,
    STREET_NAME_POST_MODIFIER    VARCHAR(10) ,
    STREET_NAME_POST_TYPE        VARCHAR(10) ,
    SUBADDRESS_IDENTIFIER        VARCHAR(10) ,
    SUBADDRESS_TYPE              VARCHAR(10) ,
    USPS_BOX_GROUP_ID            VARCHAR(10) ,
    USPS_BOX_GROUP_TYPE          VARCHAR(2) ,
    USPS_BOX_ID                  VARCHAR(10) ,
    USPS_BOX_TYPE                VARCHAR(10) ,
    ZIP_CODE                     VARCHAR(10) ,
    RAW_ADDR1                    VARCHAR(110),
    RAW_ADDR2                    VARCHAR(50),
    RAW_CITY                     VARCHAR(50),
    RAW_ZIP                      VARCHAR(10),
    VALIDATION_STATUS            SMALLINT NOT NULL DEFAULT(0),
    GEOM                         GEOMETRY(Point, 4326) ,
    GEOCODE_STATUS               SMALLINT NOT NULL DEFAULT(1) ,
    HASHCODE		   BIGINT NOT NULL
 ) ;
DROP INDEX IF EXISTS HOUSEHOLD_ZIP_IDX;
CREATE INDEX HOUSEHOLD_ZIP_IDX on HOUSEHOLD_DIM(ZIP_CODE);

DROP INDEX IF EXISTS HOUSEHOLD_HASH_IDX;
CREATE INDEX HOUSEHOLD_HASH_IDX on HOUSEHOLD_DIM(HASHCODE);

DROP INDEX IF EXISTS HOUSEHOLD_GEOM_IDX;
CREATE INDEX HOUSEHOLD_GEOM_IDX on HOUSEHOLD_DIM USING GIST(GEOM);

DROP TABLE IF EXISTS MAILING_ADDRESS_DIM CASCADE;
CREATE TABLE MAILING_ADDRESS_DIM
(
	MAILING_ADDRESS_ID 	BIGSERIAL NOT NULL PRIMARY KEY
,	ADDRESS_LINE1	VARCHAR(110)
,	ADDRESS_LINE2	VARCHAR(50)
,	CITY		VARCHAR(50)
,	"STATE"		VARCHAR(20)
,	ZIP_CODE		VARCHAR(10)
,	COUNTRY   	VARCHAR(30)
,	HASHCODE		BIGINT NOT NULL
);
DROP INDEX IF EXISTS MAILING_ADDR_ZIP_IDX;
CREATE INDEX MAILING_ADDR_ZIP_IDX on MAILING_ADDRESS_DIM(ZIP_CODE);
DROP INDEX IF EXISTS MAILING_HASH_IDX;
CREATE INDEX MAILING_HASH_IDX on MAILING_ADDRESS_DIM(HASHCODE);


DROP TABLE IF EXISTS PRECINCT_DIM CASCADE;
CREATE TABLE PRECINCT_DIM(
  PRECINCT_ID SERIAL NOT NULL PRIMARY KEY
, COUNTY_CODE VARCHAR(5)
, COUNTY_NAME VARCHAR(50)
, DISTRICT_ID BIGINT  NULL
, DISTRICT_CODE VARCHAR(15) NULL
, PRECINCT_CODE VARCHAR(50)
, PRECINCT_NAME VARCHAR(50) NULL
, WARD VARCHAR(100) NULL
, TOWNSHIP VARCHAR(100) NULL
, VILLAGE VARCHAR(100) NULL
, CITY VARCHAR(100) NULL

, CONGRESSIONAL_DISTRICT VARCHAR(3) NULL
, UPPER_HOUSE_DISTRICT VARCHAR(3) NULL
, LOWER_HOUSE_DISTRICT VARCHAR(3) NULL
, COUNTY_DISTRICT_NAME VARCHAR(100) NULL
, COURT_OF_APPEALS VARCHAR(3) NULL
, MUNICIPAL_COURT_DISTRICT VARCHAR(25) NULL
, EMS_DISTRICT_NAME VARCHAR(100) NULL
, FIRE_DISTRICT_NAME VARCHAR(100) NULL

, JUDICIAL_DISTRICT_NAME VARCHAR(100) NULL
, COUNTY_COURT_DISTRICT VARCHAR(25) NULL
, LEGISLATIVE_DISTRICT_NAME VARCHAR(100) NULL
, LIBRARY_DISTRICT_NAME VARCHAR(100) NULL
, OTHER_DISTRICT_NAME VARCHAR(100) NULL
, PCO_DISTRICT_NAME VARCHAR(100) NULL
, PARK_AND_REC_DISTRICT_NAME VARCHAR(100) NULL
, PORT_DISTRICT_NAME VARCHAR(100) NULL
, PUBLIC_HOSPITAL_DISTRICT_NAME VARCHAR(100) NULL
, PUBLIC_UTILITY_DISTRICT_NAME VARCHAR(100) NULL
, SCHOOL_DISTRICT_NAME VARCHAR(100) NULL
, STATE_BOARD_OF_EDUCATION VARCHAR(3) NULL
, SEWER_DISTRICT_NAME VARCHAR(100) NULL
, STATE_DISTRICT_NAME VARCHAR(100) NULL
, TAX_DISTRICT_NAME VARCHAR(100) NULL
, TRANSPORTATION_DISTRICT_NAME VARCHAR(100) NULL
, WATER_DISTRICT_NAME VARCHAR(100) NULL
, CAREER_CENTER VARCHAR(100) NULL
, EDU_SERVICE_CENTER_DISTRICT VARCHAR(100) NULL
, STATE_ABBREVIATION CHAR(2)
, STATE_NAME CHAR(50)
, OCD_NAME VARCHAR(100) NULL
, OCD_ID VARCHAR(100)  NULL
, VERSION		INTEGER NOT NULL DEFAULT(0)
, VALID_FROM		DATE NOT NULL DEFAULT('1900-01-01')
, VALID_TO		DATE NOT NULL DEFAULT('2199-12-31')

)
;

DROP INDEX IF EXISTS PRECINCT_LOOKUP_IDX;
CREATE INDEX PRECINCT_LOOKUP_IDX on PRECINCT_DIM(STATE_ABBREVIATION, PRECINCT_CODE, COUNTY_CODE);


DROP TABLE IF EXISTS STAFFER_DIM;
CREATE TABLE STAFFER_DIM
  (
    STAFFER_ID INTEGER NOT NULL PRIMARY KEY,
    FIRST_NAME VARCHAR(45) ,
    LAST_NAME  VARCHAR(45) ,
    USERNAME   VARCHAR(25)
  );



DROP TABLE IF EXISTS ELECTION_DIM CASCADE;
  CREATE TABLE ELECTION_DIM
  (
    ELECTION_ID          SERIAL              NOT NULL PRIMARY KEY,
    "STATE"              CHAR(2),
    ELECTION_DATE        DATE,
    ELECTION_YEAR2       CHAR(2),
    ELECTION_YEAR4       CHAR(4),

    ELECTION_DATE_APPROX CHAR(1) DEFAULT 'N' NULL,
    ELECTION_TYPE        VARCHAR(50),
    ELECTION_TITLE       VARCHAR(150),
    HASHCODE             BIGINT              NOT NULL
  )
;

DROP INDEX IF EXISTS ELECTION_LOOKUP_IDX;
CREATE INDEX ELECTION_LOOKUP_IDX on ELECTION_DIM(HASHCODE);



DROP TABLE IF EXISTS JURISDICTION_DIM CASCADE;
CREATE TABLE PUBLIC.JURISDICTION_DIM(
  JURISDICTION_ID SERIAL NOT NULL PRIMARY KEY,
  GEOID CHARACTER VARYING(15),
  FIPS CHARACTER VARYING(25),
  VOTER_FILE_CODE CHARACTER VARYING(5),
  STATE_NAME CHARACTER VARYING(2),
  STATE_FIPS CHARACTER VARYING(2),
  ENTITY_NAME CHARACTER VARYING(75),
  ENTITY_TYPE CHARACTER VARYING(35),
  TOTAL_POP INTEGER,
  MALE_POP INTEGER,
  MALEUNDER_5_YEARS INTEGER,
  MALE5_TO_9_YEARS INTEGER,
  MALE10_TO_14_YEARS INTEGER,
  MALE15_TO_17_YEARS INTEGER,
  MALE18_AND_19_YEARS INTEGER,
  MALE20_YEARS INTEGER,
  MALE21_YEARS INTEGER,
  MALE22_TO_24_YEARS INTEGER,
  MALE25_TO_29_YEARS INTEGER,
  MALE30_TO_34_YEARS INTEGER,
  MALE35_TO_39_YEARS INTEGER,
  MALE40_TO_44_YEARS INTEGER,
  MALE45_TO_49_YEARS INTEGER,
  MALE50_TO_54_YEARS INTEGER,
  MALE55_TO_59_YEARS INTEGER,
  MALE60_AND_61_YEARS INTEGER,
  MALE62_TO_64_YEARS INTEGER,
  MALE65_AND_66_YEARS INTEGER,
  MALE67_TO_69_YEARS INTEGER,
  MALE70_TO_74_YEARS INTEGER,
  MALE75_TO_79_YEARS INTEGER,
  MALE80_TO_84_YEARS INTEGER,
  MALE85_YEARS_AND_OVER INTEGER,
  FEMALE_POP INTEGER,
  FEMALEUNDER_5_YEARS INTEGER,
  FEMALE5_TO_9_YEARS INTEGER,
  FEMALE10_TO_14_YEARS INTEGER,
  FEMALE15_TO_17_YEARS INTEGER,
  FEMALE18_AND_19_YEARS INTEGER,
  FEMALE20_YEARS INTEGER,
  FEMALE21_YEARS INTEGER,
  FEMALE22_TO_24_YEARS INTEGER,
  FEMALE25_TO_29_YEARS INTEGER,
  FEMALE30_TO_34_YEARS INTEGER,
  FEMALE35_TO_39_YEARS INTEGER,
  FEMALE40_TO_44_YEARS INTEGER,
  FEMALE45_TO_49_YEARS INTEGER,
  FEMALE50_TO_54_YEARS INTEGER,
  FEMALE55_TO_59_YEARS INTEGER,
  FEMALE60_AND_61_YEARS INTEGER,
  FEMALE62_TO_64_YEARS INTEGER,
  FEMALE65_AND_66_YEARS INTEGER,
  FEMALE67_TO_69_YEARS INTEGER,
  FEMALE70_TO_74_YEARS INTEGER,
  FEMALE75_TO_79_YEARS INTEGER,
  FEMALE80_TO_84_YEARS INTEGER,
  FEMALE85_YEARS_AND_OVER INTEGER,
  NOT_HISPANIC_OR_LATINO INTEGER,
  NOT_HISPANIC_OR_LATINOWHITE_ALONE INTEGER,
  NOT_HISPANIC_OR_LATINOBLACK_OR_AFRICAN_AMERICAN_ALONE INTEGER,
  NOT_HISPANIC_OR_LATINOAMERICAN_INDIAN_AND_ALASKA_NATIVE_ALONE INTEGER,
  NOT_HISPANIC_OR_LATINOASIAN_ALONE INTEGER,
  NOT_HISPANIC_OR_LATINONATIVE_HAWAIIAN_AND_OTHER_PACIFIC_ISLANDE INTEGER,
  NOT_HISPANIC_OR_LATINOSOME_OTHER_RACE_ALONE INTEGER,
  NOT_HISPANIC_OR_LATINOTWO_OR_MORE_RACES INTEGER,
  NOT_HISPANIC_OR_LATINOTWO_OR_MORE_RACESTWO_RACES_INCLUDING_SOME INTEGER,
  NOT_HISPANIC_OR_LATINOTWO_OR_MORE_RACESTWO_RACES_EXCLUDING_SOME INTEGER,
  HISPANIC_OR_LATINO INTEGER,
  HISPANIC_OR_LATINOWHITE_ALONE INTEGER,
  HISPANIC_OR_LATINOBLACK_OR_AFRICAN_AMERICAN_ALONE INTEGER,
  HISPANIC_OR_LATINOAMERICAN_INDIAN_AND_ALASKA_NATIVE_ALONE INTEGER,
  HISPANIC_OR_LATINOASIAN_ALONE INTEGER,
  HISPANIC_OR_LATINONATIVE_HAWAIIAN_AND_OTHER_PACIFIC_ISLANDER_AL INTEGER,
  HISPANIC_OR_LATINOSOME_OTHER_RACE_ALONE INTEGER,
  HISPANIC_OR_LATINOTWO_OR_MORE_RACES INTEGER,
  HISPANIC_OR_LATINOTWO_OR_MORE_RACESTWO_RACES_INCLUDING_SOME_OTH INTEGER,
  HISPANIC_OR_LATINOTWO_OR_MORE_RACESTWO_RACES_EXCLUDING_SOME_OTH INTEGER,
  TOTAL_MARRIED_OVER_15 INTEGER,
  NEVER_MARRIED INTEGER,
  NOW_MARRIED_EXCEPT_SEPARATED INTEGER,
  DIVORCED INTEGER,
  SEPARATED INTEGER,
  WIDOWED INTEGER,
  BORN_IN_STATE_OF_RESIDENCE INTEGER,
  BORN_IN_STATE_OF_RESIDENCENEVER_MARRIED INTEGER,
  BORN_IN_STATE_OF_RESIDENCENOW_MARRIED_EXCEPT_SEPARATED INTEGER,
  BORN_IN_STATE_OF_RESIDENCEDIVORCED INTEGER,
  BORN_IN_STATE_OF_RESIDENCESEPARATED INTEGER,
  BORN_IN_STATE_OF_RESIDENCEWIDOWED INTEGER,
  BORN_IN_OTHER_STATE_IN_THE_UNITED_STATES INTEGER,
  BORN_IN_OTHER_STATE_IN_THE_UNITED_STATESNEVER_MARRIED INTEGER,
  BORN_IN_OTHER_STATE_IN_THE_UNITED_STATESNOW_MARRIED_EXCEPT_SEPA INTEGER,
  BORN_IN_OTHER_STATE_IN_THE_UNITED_STATESDIVORCED INTEGER,
  BORN_IN_OTHER_STATE_IN_THE_UNITED_STATESSEPARATED INTEGER,
  BORN_IN_OTHER_STATE_IN_THE_UNITED_STATESWIDOWED INTEGER,
  NATIVE_BORN_OUTSIDE_THE_UNITED_STATES INTEGER,
  NATIVE_BORN_OUTSIDE_THE_UNITED_STATESNEVER_MARRIED INTEGER,
  NATIVE_BORN_OUTSIDE_THE_UNITED_STATESNOW_MARRIED_EXCEPT_SEPARAT INTEGER,
  NATIVE_BORN_OUTSIDE_THE_UNITED_STATESDIVORCED INTEGER,
  NATIVE_BORN_OUTSIDE_THE_UNITED_STATESSEPARATED INTEGER,
  NATIVE_BORN_OUTSIDE_THE_UNITED_STATESWIDOWED INTEGER,
  FOREIGN_BORN INTEGER,
  FOREIGN_BORNNEVER_MARRIED INTEGER,
  FOREIGN_BORNNOW_MARRIED_EXCEPT_SEPARATED INTEGER,
  FOREIGN_BORNDIVORCED INTEGER,
  FOREIGN_BORNSEPARATED INTEGER,
  FOREIGN_BORNWIDOWED INTEGER,
  INCOME_LESS_THAN_10000 INTEGER,
  INCOME_10000_TO_14999 INTEGER,
  INCOME_15000_TO_19999 INTEGER,
  INCOME_20000_TO_24999 INTEGER,
  INCOME_25000_TO_29999 INTEGER,
  INCOME_30000_TO_34999 INTEGER,
  INCOME_35000_TO_39999 INTEGER,
  INCOME_40000_TO_44999 INTEGER,
  INCOME_45000_TO_49999 INTEGER,
  INCOME_50000_TO_59999 INTEGER,
  INCOME_60000_TO_74999 INTEGER,
  INCOME_75000_TO_99999 INTEGER,
  INCOME_100000_TO_124999 INTEGER,
  INCOME_125000_TO_149999 INTEGER,
  INCOME_150000_TO_199999 INTEGER,
  INCOME_200000_OR_MORE INTEGER,
  MALE_OVER_16 INTEGER,
  MALE16_TO_19_YEARS INTEGER,
  MALE16_TO_19_YEARSIN_LABOR_FORCE INTEGER,
  MALE16_TO_19_YEARSIN_LABOR_FORCEIN_ARMED_FORCES INTEGER,
  MALE16_TO_19_YEARSIN_LABOR_FORCECIVILIAN INTEGER,
  MALE16_TO_19_YEARSIN_LABOR_FORCECIVILIANEMPLOYED INTEGER,
  MALE16_TO_19_YEARSIN_LABOR_FORCECIVILIANUNEMPLOYED INTEGER,
  MALE16_TO_19_YEARSNOT_IN_LABOR_FORCE INTEGER,
  MALE20_AND_21_YEARSIN_LABOR_FORCE INTEGER,
  MALE20_AND_21_YEARSIN_LABOR_FORCEIN_ARMED_FORCES INTEGER,
  MALE20_AND_21_YEARSIN_LABOR_FORCECIVILIAN INTEGER,
  MALE20_AND_21_YEARSIN_LABOR_FORCECIVILIANEMPLOYED INTEGER,
  MALE20_AND_21_YEARSIN_LABOR_FORCECIVILIANUNEMPLOYED INTEGER,
  MALE20_AND_21_YEARSNOT_IN_LABOR_FORCE INTEGER,
  MALE22_TO_24_YEARSIN_LABOR_FORCE INTEGER,
  MALE22_TO_24_YEARSIN_LABOR_FORCEIN_ARMED_FORCES INTEGER,
  MALE22_TO_24_YEARSIN_LABOR_FORCECIVILIAN INTEGER,
  MALE22_TO_24_YEARSIN_LABOR_FORCECIVILIANEMPLOYED INTEGER,
  MALE22_TO_24_YEARSIN_LABOR_FORCECIVILIANUNEMPLOYED INTEGER,
  MALE22_TO_24_YEARSNOT_IN_LABOR_FORCE INTEGER,
  MALE25_TO_29_YEARSIN_LABOR_FORCE INTEGER,
  MALE25_TO_29_YEARSIN_LABOR_FORCEIN_ARMED_FORCES INTEGER,
  MALE25_TO_29_YEARSIN_LABOR_FORCECIVILIAN INTEGER,
  MALE25_TO_29_YEARSIN_LABOR_FORCECIVILIANEMPLOYED INTEGER,
  MALE25_TO_29_YEARSIN_LABOR_FORCECIVILIANUNEMPLOYED INTEGER,
  MALE25_TO_29_YEARSNOT_IN_LABOR_FORCE INTEGER,
  MALE30_TO_34_YEARSIN_LABOR_FORCE INTEGER,
  MALE30_TO_34_YEARSIN_LABOR_FORCEIN_ARMED_FORCES INTEGER,
  MALE30_TO_34_YEARSIN_LABOR_FORCECIVILIAN INTEGER,
  MALE30_TO_34_YEARSIN_LABOR_FORCECIVILIANEMPLOYED INTEGER,
  MALE30_TO_34_YEARSIN_LABOR_FORCECIVILIANUNEMPLOYED INTEGER,
  MALE30_TO_34_YEARSNOT_IN_LABOR_FORCE INTEGER,
  MALE35_TO_44_YEARSIN_LABOR_FORCE INTEGER,
  MALE35_TO_44_YEARSIN_LABOR_FORCEIN_ARMED_FORCES INTEGER,
  MALE35_TO_44_YEARSIN_LABOR_FORCECIVILIAN INTEGER,
  MALE35_TO_44_YEARSIN_LABOR_FORCECIVILIANEMPLOYED INTEGER,
  MALE35_TO_44_YEARSIN_LABOR_FORCECIVILIANUNEMPLOYED INTEGER,
  MALE35_TO_44_YEARSNOT_IN_LABOR_FORCE INTEGER,
  MALE45_TO_54_YEARSIN_LABOR_FORCE INTEGER,
  MALE45_TO_54_YEARSIN_LABOR_FORCEIN_ARMED_FORCES INTEGER,
  MALE45_TO_54_YEARSIN_LABOR_FORCECIVILIAN INTEGER,
  MALE45_TO_54_YEARSIN_LABOR_FORCECIVILIANEMPLOYED INTEGER,
  MALE45_TO_54_YEARSIN_LABOR_FORCECIVILIANUNEMPLOYED INTEGER,
  MALE45_TO_54_YEARSNOT_IN_LABOR_FORCE INTEGER,
  MALE55_TO_59_YEARSIN_LABOR_FORCE INTEGER,
  MALE55_TO_59_YEARSIN_LABOR_FORCEIN_ARMED_FORCES INTEGER,
  MALE55_TO_59_YEARSIN_LABOR_FORCECIVILIAN INTEGER,
  MALE55_TO_59_YEARSIN_LABOR_FORCECIVILIANEMPLOYED INTEGER,
  MALE55_TO_59_YEARSIN_LABOR_FORCECIVILIANUNEMPLOYED INTEGER,
  MALE55_TO_59_YEARSNOT_IN_LABOR_FORCE INTEGER,
  MALE60_AND_61_YEARSIN_LABOR_FORCE INTEGER,
  MALE60_AND_61_YEARSIN_LABOR_FORCEIN_ARMED_FORCES INTEGER,
  MALE60_AND_61_YEARSIN_LABOR_FORCECIVILIAN INTEGER,
  MALE60_AND_61_YEARSIN_LABOR_FORCECIVILIANEMPLOYED INTEGER,
  MALE60_AND_61_YEARSIN_LABOR_FORCECIVILIANUNEMPLOYED INTEGER,
  MALE60_AND_61_YEARSNOT_IN_LABOR_FORCE INTEGER,
  MALE62_TO_64_YEARSIN_LABOR_FORCE INTEGER,
  MALE62_TO_64_YEARSIN_LABOR_FORCEIN_ARMED_FORCES INTEGER,
  MALE62_TO_64_YEARSIN_LABOR_FORCECIVILIAN INTEGER,
  MALE62_TO_64_YEARSIN_LABOR_FORCECIVILIANEMPLOYED INTEGER,
  MALE62_TO_64_YEARSIN_LABOR_FORCECIVILIANUNEMPLOYED INTEGER,
  MALE62_TO_64_YEARSNOT_IN_LABOR_FORCE INTEGER,
  MALE65_TO_69_YEARSIN_LABOR_FORCE INTEGER,
  MALE65_TO_69_YEARSIN_LABOR_FORCECIVILIANEMPLOYED INTEGER,
  MALE65_TO_69_YEARSIN_LABOR_FORCECIVILIANUNEMPLOYED INTEGER,
  MALE65_TO_69_YEARSNOT_IN_LABOR_FORCE INTEGER,
  MALE70_TO_74_YEARSIN_LABOR_FORCE INTEGER,
  MALE70_TO_74_YEARSIN_LABOR_FORCECIVILIANEMPLOYED INTEGER,
  MALE70_TO_74_YEARSIN_LABOR_FORCECIVILIANUNEMPLOYED INTEGER,
  MALE70_TO_74_YEARSNOT_IN_LABOR_FORCE INTEGER,
  MALE75_YEARS_AND_OVER INTEGER,
  MALE75_YEARS_AND_OVERIN_LABOR_FORCE INTEGER,
  MALE75_YEARS_AND_OVERIN_LABOR_FORCECIVILIANEMPLOYED INTEGER,
  MALE75_YEARS_AND_OVERIN_LABOR_FORCECIVILIANUNEMPLOYED INTEGER,
  MALE75_YEARS_AND_OVERNOT_IN_LABOR_FORCE INTEGER,
  FEMALE_OVER_16 INTEGER,
  FEMALE16_TO_19_YEARS INTEGER,
  FEMALE16_TO_19_YEARSIN_LABOR_FORCE INTEGER,
  FEMALE16_TO_19_YEARSIN_LABOR_FORCEIN_ARMED_FORCES INTEGER,
  FEMALE16_TO_19_YEARSIN_LABOR_FORCECIVILIAN INTEGER,
  FEMALE16_TO_19_YEARSIN_LABOR_FORCECIVILIANEMPLOYED INTEGER,
  FEMALE16_TO_19_YEARSIN_LABOR_FORCECIVILIANUNEMPLOYED INTEGER,
  FEMALE16_TO_19_YEARSNOT_IN_LABOR_FORCE INTEGER,
  FEMALE20_AND_21_YEARSIN_LABOR_FORCE INTEGER,
  FEMALE20_AND_21_YEARSIN_LABOR_FORCEIN_ARMED_FORCES INTEGER,
  FEMALE20_AND_21_YEARSIN_LABOR_FORCECIVILIAN INTEGER,
  FEMALE20_AND_21_YEARSIN_LABOR_FORCECIVILIANEMPLOYED INTEGER,
  FEMALE20_AND_21_YEARSIN_LABOR_FORCECIVILIANUNEMPLOYED INTEGER,
  FEMALE20_AND_21_YEARSNOT_IN_LABOR_FORCE INTEGER,
  FEMALE22_TO_24_YEARSIN_LABOR_FORCE INTEGER,
  FEMALE22_TO_24_YEARSIN_LABOR_FORCEIN_ARMED_FORCES INTEGER,
  FEMALE22_TO_24_YEARSIN_LABOR_FORCECIVILIAN INTEGER,
  FEMALE22_TO_24_YEARSIN_LABOR_FORCECIVILIANEMPLOYED INTEGER,
  FEMALE22_TO_24_YEARSIN_LABOR_FORCECIVILIANUNEMPLOYED INTEGER,
  FEMALE22_TO_24_YEARSNOT_IN_LABOR_FORCE INTEGER,
  FEMALE25_TO_29_YEARSIN_LABOR_FORCE INTEGER,
  FEMALE25_TO_29_YEARSIN_LABOR_FORCEIN_ARMED_FORCES INTEGER,
  FEMALE25_TO_29_YEARSIN_LABOR_FORCECIVILIAN INTEGER,
  FEMALE25_TO_29_YEARSIN_LABOR_FORCECIVILIANEMPLOYED INTEGER,
  FEMALE25_TO_29_YEARSIN_LABOR_FORCECIVILIANUNEMPLOYED INTEGER,
  FEMALE25_TO_29_YEARSNOT_IN_LABOR_FORCE INTEGER,
  FEMALE30_TO_34_YEARSIN_LABOR_FORCE INTEGER,
  FEMALE30_TO_34_YEARSIN_LABOR_FORCEIN_ARMED_FORCES INTEGER,
  FEMALE30_TO_34_YEARSIN_LABOR_FORCECIVILIAN INTEGER,
  FEMALE30_TO_34_YEARSIN_LABOR_FORCECIVILIANEMPLOYED INTEGER,
  FEMALE30_TO_34_YEARSIN_LABOR_FORCECIVILIANUNEMPLOYED INTEGER,
  FEMALE30_TO_34_YEARSNOT_IN_LABOR_FORCE INTEGER,
  FEMALE35_TO_44_YEARSIN_LABOR_FORCE INTEGER,
  FEMALE35_TO_44_YEARSIN_LABOR_FORCEIN_ARMED_FORCES INTEGER,
  FEMALE35_TO_44_YEARSIN_LABOR_FORCECIVILIAN INTEGER,
  FEMALE35_TO_44_YEARSIN_LABOR_FORCECIVILIANEMPLOYED INTEGER,
  FEMALE35_TO_44_YEARSIN_LABOR_FORCECIVILIANUNEMPLOYED INTEGER,
  FEMALE35_TO_44_YEARSNOT_IN_LABOR_FORCE INTEGER,
  FEMALE45_TO_54_YEARSIN_LABOR_FORCE INTEGER,
  FEMALE45_TO_54_YEARSIN_LABOR_FORCEIN_ARMED_FORCES INTEGER,
  FEMALE45_TO_54_YEARSIN_LABOR_FORCECIVILIAN INTEGER,
  FEMALE45_TO_54_YEARSIN_LABOR_FORCECIVILIANEMPLOYED INTEGER,
  FEMALE45_TO_54_YEARSIN_LABOR_FORCECIVILIANUNEMPLOYED INTEGER,
  FEMALE45_TO_54_YEARSNOT_IN_LABOR_FORCE INTEGER,
  FEMALE55_TO_59_YEARSIN_LABOR_FORCE INTEGER,
  FEMALE55_TO_59_YEARSIN_LABOR_FORCEIN_ARMED_FORCES INTEGER,
  FEMALE55_TO_59_YEARSIN_LABOR_FORCECIVILIAN INTEGER,
  FEMALE55_TO_59_YEARSIN_LABOR_FORCECIVILIANEMPLOYED INTEGER,
  FEMALE55_TO_59_YEARSIN_LABOR_FORCECIVILIANUNEMPLOYED INTEGER,
  FEMALE55_TO_59_YEARSNOT_IN_LABOR_FORCE INTEGER,
  FEMALE60_AND_61_YEARSIN_LABOR_FORCE INTEGER,
  FEMALE60_AND_61_YEARSIN_LABOR_FORCEIN_ARMED_FORCES INTEGER,
  FEMALE60_AND_61_YEARSIN_LABOR_FORCECIVILIAN INTEGER,
  FEMALE60_AND_61_YEARSIN_LABOR_FORCECIVILIANEMPLOYED INTEGER,
  FEMALE60_AND_61_YEARSIN_LABOR_FORCECIVILIANUNEMPLOYED INTEGER,
  FEMALE60_AND_61_YEARSNOT_IN_LABOR_FORCE INTEGER,
  FEMALE62_TO_64_YEARSIN_LABOR_FORCE INTEGER,
  FEMALE62_TO_64_YEARSIN_LABOR_FORCEIN_ARMED_FORCES INTEGER,
  FEMALE62_TO_64_YEARSIN_LABOR_FORCECIVILIAN INTEGER,
  FEMALE62_TO_64_YEARSIN_LABOR_FORCECIVILIANEMPLOYED INTEGER,
  FEMALE62_TO_64_YEARSIN_LABOR_FORCECIVILIANUNEMPLOYED INTEGER,
  FEMALE62_TO_64_YEARSNOT_IN_LABOR_FORCE INTEGER,
  FEMALE65_TO_69_YEARSIN_LABOR_FORCE INTEGER,
  FEMALE65_TO_69_YEARSIN_LABOR_FORCECIVILIANEMPLOYED INTEGER,
  FEMALE65_TO_69_YEARSIN_LABOR_FORCECIVILIANUNEMPLOYED INTEGER,
  FEMALE65_TO_69_YEARSNOT_IN_LABOR_FORCE INTEGER,
  FEMALE70_TO_74_YEARSIN_LABOR_FORCE INTEGER,
  FEMALE70_TO_74_YEARSIN_LABOR_FORCECIVILIANEMPLOYED INTEGER,
  FEMALE70_TO_74_YEARSIN_LABOR_FORCECIVILIANUNEMPLOYED INTEGER,
  FEMALE70_TO_74_YEARSNOT_IN_LABOR_FORCE INTEGER,
  FEMALE75_YEARS_AND_OVER INTEGER,
  FEMALE75_YEARS_AND_OVERIN_LABOR_FORCE INTEGER,
  FEMALE75_YEARS_AND_OVERIN_LABOR_FORCECIVILIANEMPLOYED INTEGER,
  FEMALE75_YEARS_AND_OVERIN_LABOR_FORCECIVILIANUNEMPLOYED INTEGER,
  FEMALE75_YEARS_AND_OVERNOT_IN_LABOR_FORCE INTEGER,
  HOUSEHOLD_TOTAL INTEGER,
  OWNER_OCCUPIED INTEGER,
  OWNER_OCCUPIED1PERSON_HOUSEHOLD INTEGER,
  OWNER_OCCUPIED2PERSON_HOUSEHOLD INTEGER,
  OWNER_OCCUPIED3PERSON_HOUSEHOLD INTEGER,
  OWNER_OCCUPIED4PERSON_HOUSEHOLD INTEGER,
  OWNER_OCCUPIED5PERSON_HOUSEHOLD INTEGER,
  OWNER_OCCUPIED6PERSON_HOUSEHOLD INTEGER,
  OWNER_OCCUPIED7ORMORE_PERSON_HOUSEHOLD INTEGER,
  RENTER_OCCUPIED INTEGER,
  RENTER_OCCUPIED1PERSON_HOUSEHOLD INTEGER,
  RENTER_OCCUPIED2PERSON_HOUSEHOLD INTEGER,
  RENTER_OCCUPIED3PERSON_HOUSEHOLD INTEGER,
  RENTER_OCCUPIED4PERSON_HOUSEHOLD INTEGER,
  RENTER_OCCUPIED5PERSON_HOUSEHOLD INTEGER,
  RENTER_OCCUPIED6PERSON_HOUSEHOLD INTEGER,
  RENTER_OCCUPIED7ORMORE_PERSON_HOUSEHOLD INTEGER,
  MEDIAN_VALUE_DOLLARS_OCCUPIED_HOUSEHOLD INTEGER,
  VERSION INTEGER,
  VALID_FROM DATE,
  VALID_TO DATE);

DROP INDEX IF EXISTS JURISDICTION_LOOKUP_IDX;
CREATE INDEX JURISDICTION_LOOKUP_IDX ON JURISDICTION_DIM(STATE_NAME, ENTITY_TYPE, VOTER_FILE_CODE);


DROP TABLE IF EXISTS VOTER_REPORT_FACT;
CREATE TABLE VOTER_REPORT_FACT
  (
    VOTER_REPORT_ID       	BIGSERIAL NOT NULL PRIMARY KEY ,
    VOTER_REPORT_DATE     	DATE NOT NULL,
    DATE_KEY		INTEGER NOT NULL REFERENCES DATE_DIM(DATE_ID),

    REPORT_STATUS         	VARCHAR(45) ,
    REPORTER_KEY          	INTEGER NOT NULL REFERENCES REPORTER_DIM(REPORTER_ID),
    VOTER_KEY	      	BIGINT NOT NULL REFERENCES VOTER_DIM(VOTER_ID),
    HOUSEHOLD_KEY	      	BIGINT NOT NULL REFERENCES HOUSEHOLD_DIM(HOUSEHOLD_ID) ,
    MAILING_ADDRESS_KEY	BIGINT NULL REFERENCES MAILING_ADDRESS_DIM(MAILING_ADDRESS_ID),
    SOCIAL_MEDIA_ACCOUNT_KEY 	INTEGER NULL ,
    PARTY_KEY INTEGER NULL REFERENCES PARTY_DIM(PARTY_ID),
    PRECINCT_KEY INTEGER NULL REFERENCES PRECINCT_DIM(PRECINCT_ID),
    COUNTY_KEY  		INTEGER NULL REFERENCES JURISDICTION_DIM(JURISDICTION_ID),
    WARD_KEY	      	INTEGER NULL REFERENCES JURISDICTION_DIM(JURISDICTION_ID),
    CONGRESSIONAL_DIST_KEY 	INTEGER NULL REFERENCES JURISDICTION_DIM(JURISDICTION_ID),
    COUNTY_DISTRICT_KEY	INTEGER NULL REFERENCES JURISDICTION_DIM(JURISDICTION_ID),
    STATE_KEY                 INTEGER NULL REFERENCES JURISDICTION_DIM(JURISDICTION_ID),
    LOWER_HOUSE_DIST_KEY	INTEGER NULL REFERENCES JURISDICTION_DIM(JURISDICTION_ID),
    UPPER_HOUSE_DIST_KEY	INTEGER NULL REFERENCES JURISDICTION_DIM(JURISDICTION_ID),
    UNIFIED_SCHOOL_DIST_KEY	INTEGER NULL REFERENCES JURISDICTION_DIM(JURISDICTION_ID),
    STAFFER_KEY	          INTEGER NULL ,
    CAMPAIGN_KEY		INTEGER NULL
  ) ;
DROP INDEX  if exists voter_report_fact_query__index;
  CREATE INDEX voter_report_fact_query__index ON public.voter_report_fact (reporter_key, date_key);



DROP TABLE IF EXISTS VOTE_FACT;
CREATE TABLE VOTE_FACT
  (
    VOTE_FACT_ID       	SERIAL NOT NULL PRIMARY KEY ,
    REPORT_DATE_KEY		INTEGER NOT NULL REFERENCES DATE_DIM(DATE_ID),
    REPORTER_KEY          	INTEGER NOT NULL REFERENCES REPORTER_DIM(REPORTER_ID),
    
    VOTER_KEY	      	INTEGER NOT NULL REFERENCES VOTER_DIM(VOTER_ID),
    HOUSEHOLD_KEY	      	INTEGER NULL REFERENCES HOUSEHOLD_DIM(HOUSEHOLD_ID) ,
    COUNTY_KEY  		INTEGER NULL REFERENCES JURISDICTION_DIM(JURISDICTION_ID),    
    PRECINCT_KEY INTEGER NULL REFERENCES PRECINCT_DIM(PRECINCT_ID),
    ELECTION_KEY INTEGER NOT NULL REFERENCES ELECTION_DIM(ELECTION_ID),
    VOTING_METHOD VARCHAR(50),
    DID_VOTE char(1) NULL,
    VOTE_COUNTED char(1) NULL 
  ) ;

select * from REPORTER_DIM;
DROP TABLE IF EXISTS STAFFER_DIM;
CREATE TABLE STAFFER_DIM
  (
    STAFFER_ID INTEGER NOT NULL PRIMARY KEY,
    FIRST_NAME VARCHAR(45) ,
    LAST_NAME  VARCHAR(45) ,
    USERNAME   VARCHAR(25)
  );

DROP TABLE IF EXISTS VOTER_REPORT_SUMMARY;
CREATE TABLE VOTER_REPORT_SUMMARY
  (
    VOTER_REPORT_KEY INTEGER NOT NULL REFERENCES VOTER_REPORT_FACT(VOTER_REPORT_ID),
    TOTAL INTEGER,
    ACTIVE INTEGER,
    INACTIVE INTEGER,
    MALE INTEGER,
    FEMALE INTEGER,
    AGE_18_24 INTEGER,
    AGE_25_34 INTEGER,
    AGE_35_44 INTEGER,
    AGE_45_54 INTEGER,
    AGE_55_64 INTEGER,
    AGE_GT_64 INTEGER,
    DEMOCRAT INTEGER,
    REPUBLICAN INTEGER
  );
