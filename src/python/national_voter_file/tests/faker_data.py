from national_voter_file.transformers.base import (DATA_DIR,
                                                   BasePreparer,
                                                   BaseTransformer)
from national_voter_file.us_states.all import load_dict as load_states
from faker import Faker
import random
from random import randint
import string
import csv
import os
import sys


TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'test_data')
TEST_STATES = ['de', 'co', 'fl', 'mi', 'nc', 'nj', 'ny', 'oh', 'ok', 'pa',
              'ut', 'vt', 'wa']

NUM_ROWS = 100

fake = Faker()

# Helpers for making items empty easier
def _empty(item):
    return random.choice([item, ' '])

def _blank(item):
    return random.choice([item, ''])

# Obtain the information needed from individual states
state_modules = load_states(TEST_STATES)
CO = state_modules['co']
FL = state_modules['fl']
MI = state_modules['mi']
NJ = state_modules['nj']
NY = state_modules['ny']
OH = state_modules['oh']
PA = state_modules['pa']
OK = state_modules['ok']
UT = state_modules['ut']

colorado_party_keys = CO.transformer.StateTransformer().co_party_map.keys()
oklahoma_party_keys = OK.transformer.StateTransformer().oklahoma_party_map.keys()
ohio_party_keys = OH.transformer.StateTransformer().ohio_party_map.keys()
florida_party_keys = FL.transformer.StateTransformer().florida_party_map.keys()
florida_race_keys = FL.transformer.StateTransformer().florida_race_map.keys()
nj_party_keys = NJ.transformer.StateTransformer().nj_party_map.keys()
nj_county_keys = NJ.transformer.StateTransformer().nj_county_map.keys()
ny_party_keys = NY.transformer.StateTransformer().ny_party_map.keys()
ny_other_party_keys = NY.transformer.StateTransformer().ny_other_party_map.keys()
utah_party_keys = UT.transformer.StateTransformer().ut_party_map.keys()

OKLAHOMA_SCHEMA = {
        'Precinct': lambda: str(randint(1, 99)).zfill(2) + str(randint(1000, 9999)),
        'LastName': lambda: fake.last_name().upper(),
        'FirstName': lambda: fake.first_name().upper(),
        'MiddleName': lambda: _empty(fake.first_name().upper()),
        'Suffix': lambda: _empty(fake.suffix().upper()),
        'VoterID': lambda: fake.numerify(text='#########'),
        'PolitalAff': lambda: random.choice(list(oklahoma_party_keys)),
        'Status': lambda: random.choice(['A', 'I']),
        'StreetNum': lambda: _blank(random.choice([fake.building_number(), 'NE', 'SW', 'NW', 'SE', 'SE 1/4', 'NW1/4', 'SW OF', 'X'])),
        'StreetDir': lambda: _empty(random.choice(['N', 'S', 'E', 'W', 'NW', 'NE', 'SW', 'SE', 'OF'])),
        'StreetName': lambda: fake.street_name(),
        'StreetType': lambda: _empty(random.choice(['RD', 'AVE', 'ST', 'DR'])),
        'BldgNum': lambda: _empty(random.choice(['#', 'APT'])),
        'City': lambda: _empty(fake.city().upper()),
        'Zip': lambda: _empty(fake.zipcode()),
        'DateOfBirth': lambda: fake.date(pattern='%m/%d/%Y'),
        'OriginalRegistration': lambda: fake.date(pattern='%m/%d/%Y'),
        'MailStreet1': lambda: _empty(fake.street_address().upper()),
        'MailStreet2': lambda: _empty(fake.secondary_address().upper()),
        'MailCity': lambda: _empty(fake.city().upper()),
        'MailState': lambda: _empty(fake.state_abbr()),
        'MailZip': lambda: _empty(fake.zipcode()),
        'Muni': lambda: _empty('{} {} AT LARGE'.format(random.choice(['TOWN OF', 'CITY OF']), fake.city().upper())),
        'MuniSub': lambda: _empty(str(randint(1, 5))),
        'School': lambda: _empty('{} PUBLIC SCHOOLS AT LARGE'.format(fake.city().upper())),
        'SchoolSub': lambda: "",
        'TechCenter': lambda: _empty('{} TECHNOLOGY CENTER AT LARGE'.format(random.choice(['NORTHWEST', 'HIGH PLAINS', 'KIAMICHI']))),
        'TechCenterSub': lambda: _empty(str(randint(1, 6))),
        'CountyComm': lambda: _empty(str(randint(1, 5))),
        'VoterHist1': lambda: fake.date(pattern='%m/%d/%Y'),
        'HistMethod1': lambda: random.choice(['IP', 'AI', 'AB', 'PI', 'CI', 'EI', 'MI', 'OV', 'NH']),
        'VoterHist2': lambda: fake.date(pattern='%m/%d/%Y'),
        'HistMethod2': lambda: random.choice(['IP', 'AI', 'AB', 'PI', 'CI', 'EI', 'MI', 'OV', 'NH']),
        'VoterHist3': lambda: fake.date(pattern='%m/%d/%Y'),
        'HistMethod3': lambda: random.choice(['IP', 'AI', 'AB', 'PI', 'CI', 'EI', 'MI', 'OV', 'NH']),
        'VoterHist4': lambda: fake.date(pattern='%m/%d/%Y'),
        'HistMethod4': lambda: random.choice(['IP', 'AI', 'AB', 'PI', 'CI', 'EI', 'MI', 'OV', 'NH']),
        'VoterHist5': lambda: fake.date(pattern='%m/%d/%Y'),
        'HistMethod5': lambda: random.choice(['IP', 'AI', 'AB', 'PI', 'CI', 'EI', 'MI', 'OV', 'NH']),
        'VoterHist6': lambda: fake.date(pattern='%m/%d/%Y'),
        'HistMethod6': lambda: random.choice(['IP', 'AI', 'AB', 'PI', 'CI', 'EI', 'MI', 'OV', 'NH']),
        'VoterHist7': lambda: fake.date(pattern='%m/%d/%Y'),
        'HistMethod7': lambda: random.choice(['IP', 'AI', 'AB', 'PI', 'CI', 'EI', 'MI', 'OV', 'NH']),
        'VoterHist8': lambda: fake.date(pattern='%m/%d/%Y'),
        'HistMethod8': lambda: random.choice(['IP', 'AI', 'AB', 'PI', 'CI', 'EI', 'MI', 'OV', 'NH']),
        'VoterHist9': lambda: fake.date(pattern='%m/%d/%Y'),
        'HistMethod9': lambda: random.choice(['IP', 'AI', 'AB', 'PI', 'CI', 'EI', 'MI', 'OV', 'NH']),
        'VoterHist10': lambda: fake.date(pattern='%m/%d/%Y'),
        'HistMethod10': lambda: random.choice(['IP', 'AI', 'AB', 'PI', 'CI', 'EI', 'MI', 'OV', 'NH'])
    }



COLORADO_SCHEMA = {
    'VOTER_ID': lambda: str(randint(1000, 99999999)),
    'COUNTY_CODE': lambda: str(randint(1, 88)),
    'COUNTY': lambda: fake.city(),
    'LAST_NAME': lambda: fake.last_name(),
    'FIRST_NAME': lambda: fake.first_name(),
    'MIDDLE_NAME': lambda: _empty(fake.first_name()),
    'NAME_SUFFIX': lambda: _empty(random.choice(['Jr', 'Sr', 'II'])),
    'VOTER_NAME': lambda: '{}, {} {}'.format(fake.last_name(), fake.first_name(), _empty(fake.first_name())),
    'STATUS_CODE': lambda: random.choice(['A', 'I']),
    'PRECINCT_NAME': lambda: str(randint(1000, 99999999)),
    'ADDRESS_LIBRARY_ID': lambda: str(randint(1000, 99999999)),
    'HOUSE_NUM': lambda: str(randint(1000, 99999)),
    'HOUSE_SUFFIX': lambda: _empty(random.choice(['B'])),
    'PRE_DIR': lambda: _empty(random.choice(['N', 'S', 'E', 'W'])),
    'STREET_NAME': lambda: fake.street_name(),
    'STREET_TYPE': lambda: _empty(random.choice(['Drive', 'Terrace', 'Lane', 'Crossing'])),
    'POST_DIR': lambda: _empty(random.choice(['N', 'S', 'E', 'W'])),
    'UNIT_TYPE': lambda: _empty(random.choice(['#', 'APT'])),
    'UNIT_NUM': lambda: _empty(random.choice(['#', 'APT'])),
    'ADDRESS_NON_STD': lambda: "",
    'RESIDENTIAL_ADDRESS': lambda: _empty(fake.street_address().upper()),
    'RESIDENTIAL_CITY': lambda: _empty(fake.city().upper()),
    'RESIDENTIAL_STATE': lambda: _empty(fake.state_abbr()),
    'RESIDENTIAL_ZIP_CODE': lambda: _empty(fake.zipcode()),
    'RESIDENTIAL_ZIP_PLUS': lambda: _empty(fake.numerify(text='####')),
    'EFFECTIVE_DATE': lambda: fake.date(pattern='%m/%d/%Y'),
    'REGISTRATION_DATE': lambda: fake.date(pattern='%m/%d/%Y'),
    'STATUS': lambda: random.choice(['Active', 'Inactive']),
    'STATUS_REASON': lambda: random.choice(['Undeliverable Ballot', 'Returned Mail', 'NCOA', 'Failed to Vote']),
    'BIRTH_YEAR': lambda: str(randint(1910, 1999)),
    'GENDER': lambda: random.choice(['Male', 'Female']),
    'PRECINCT': lambda: str(randint(100000000, 999999999)),
    'SPLIT': lambda: str(randint(100, 999)),
    'VOTER_STATUS_ID': lambda: str(randint(1, 2)),
    'PARTY': lambda: random.choice(list(colorado_party_keys)),
    'PARTY_AFFILIATION_DATE': lambda: fake.date(pattern='%m/%d/%Y'),
    'PHONE_NUM': lambda: _empty(fake.phone_number()),
    'MAIL_ADDR1': lambda: _empty(fake.street_address().upper()),
    'MAIL_ADDR2': lambda: _empty(fake.street_address().upper()),
    'MAIL_ADDR3': lambda: _empty(fake.street_address().upper()),
    'MAILING_CITY': lambda: _empty(fake.city().upper()),
    'MAILING_STATE': lambda: _empty(fake.state_abbr()),
    'MAILING_ZIP_CODE': lambda: _empty(fake.zipcode()),
    'MAILING_ZIP_PLUS': lambda: _empty(fake.numerify(text='####')),
    'MAILING_COUNTRY': lambda: _empty('USA'),
    'SPL_ID': lambda: str(randint(100000000, 999999999)),
    'PERMANENT_MAIL_IN_VOTER': lambda: random.choice(['Yes', 'No']),
    'CONGRESSIONAL': lambda: 'Congressional {}'.format(str(randint(1, 45))),
    'STATE_SENATE': lambda: 'State Senate {}'.format(str(randint(1, 45))),
    'STATE_HOUSE': lambda: 'State House {}'.format(str(randint(1, 45))),
    'ID_REQUIRED': lambda: random.choice(['Y', 'N'])
}

DELAWARE_SCHEMA = {
    'UNIQUE-ID': lambda: str(randint(1000, 99999999)),
    'LAST-NAME': lambda: fake.last_name(),
    'FIRST-NAME': lambda: fake.first_name(),
    'MID-INIT': lambda: _empty(random.choice(string.ascii_letters)),
    'SUFFIX': lambda: _empty(random.choice(['Jr', 'Sr', 'II'])),
    'YEAR-OF-BIRTH': lambda: str(randint(1910, 1999)),
    'HOME-NO': lambda: str(randint(1000, 99999)),
    'HOME-APT': lambda: _empty(fake.secondary_address()),
    'HOME-STREET': lambda: fake.street_name(),
    'HOME-DEV': lambda: _empty(fake.lexify(text="???????????")),
    'HOME-CITY': lambda: fake.city(),
    'HOME-ZIPCODE': lambda: _empty(fake.zipcode()),
    'COUNTY': lambda: random.choice(['S', 'K', 'N']),
    'ED': lambda: fake.numerify(text="##"),
    'RD': lambda: fake.numerify(text="##"),
    'SD': lambda: fake.numerify(text="##"),
    'CNLEVY': lambda: fake.numerify(text="##"),
    'WILM': lambda: fake.numerify(text="#"),
    'CODE-HOME-CITY': lambda: _empty( fake.lexify(text="?").upper() + fake.numerify(text="##")),
    'SCH-DIST': lambda: fake.lexify(text="??").upper(),
    'PARTY': lambda: random.choice(['R', 'D', 'I' ]),
    'DATE-REG': lambda: random.choice([fake.date(pattern='%Y%m%d'), fake.date(pattern='%Y%m00')]),
    'PP-HIST-1': lambda: random.choice(['0', '2002', '2004', '2006', '2008', '2010', '2012', '2014', '2016' ]),
    'PP-HIST-2': lambda: random.choice(['0', '2002', '2004', '2006', '2008', '2010', '2012', '2014', '2016' ]),
    'PR-HIST-1': lambda: random.choice(['0', '2002', '2004', '2006', '2008', '2010', '2012', '2014', '2016' ]),
    'PR-HIST-2': lambda: random.choice(['0', '2002', '2004', '2006', '2008', '2010', '2012', '2014', '2016' ]),
    'GEN-HIST-1': lambda: random.choice(['0', '2002', '2004', '2006', '2008', '2010', '2012', '2014', '2016' ]),
    'GEN-HIST-2': lambda: random.choice(['0', '2002', '2004', '2006', '2008', '2010', '2012', '2014', '2016' ]),
    'GEN-HIST-3': lambda: random.choice(['0', '2002', '2004', '2006', '2008', '2010', '2012', '2014', '2016' ]),
    'GEN-HIST-4': lambda: random.choice(['0', '2002', '2004', '2006', '2008', '2010', '2012', '2014', '2016' ]),
    'GEN-HIST-5': lambda: random.choice(['0', '2002', '2004', '2006', '2008', '2010', '2012', '2014', '2016' ]),
    'MAIL-NO': lambda: _empty(str(randint(1000, 99999))),
    'MAIL-APT': lambda: _empty(fake.secondary_address()),
    'MAIL-STR': lambda: _empty(fake.street_name()),
    'MAIL-CITY': lambda: _empty(fake.city()),
    'MAIL-STATE': lambda: _empty('DE'),
    'MAIL-ZIP': lambda: _empty(fake.zipcode()),
    'DATE-LAST-CHG': lambda: fake.date(pattern='%Y%m%d'),
    'CODE-CHANGE': lambda: random.choice(['CR', 'P6', 'P1']),
    'STATUS': lambda: random.choice(['A', 'I' ])
}

OHIO_SCHEMA = {
    'SOS_VOTERID': lambda: 'OH{}'.format(str(randint(1000, 999999)).zfill(10)),
    'COUNTY_NUMBER': lambda: str(randint(1, 88)),
    'COUNTY_ID': lambda: str(randint(1000, 999999999)),
    'LAST_NAME': lambda: fake.last_name().upper(),
    'FIRST_NAME': lambda: fake.first_name().upper(),
    'MIDDLE_NAME': lambda: _empty(fake.first_name().upper()),
    'SUFFIX': lambda: _empty(fake.suffix().upper()),
    'DATE_OF_BIRTH': lambda: fake.date(pattern='%Y-%m-%d'),
    'REGISTRATION_DATE': lambda: fake.date(pattern='%Y-%m-%d'),
    'VOTER_STATUS': lambda: random.choice(['ACTIVE', 'INACTIVE', 'CONFIRMATION']),
    'PARTY_AFFILIATION': lambda: random.choice(list(ohio_party_keys)),
    'RESIDENTIAL_ADDRESS1': lambda: fake.street_address().upper(),
    'RESIDENTIAL_SECONDARY_ADDR': lambda: _empty(fake.secondary_address().upper()),
    'RESIDENTIAL_CITY': lambda: fake.city().upper(),
    'RESIDENTIAL_STATE': lambda: 'OH',
    'RESIDENTIAL_ZIP': lambda: fake.zipcode(),
    'RESIDENTIAL_ZIP_PLUS4': lambda: _empty(fake.numerify(text='####')),
    'RESIDENTIAL_COUNTRY': lambda: 'USA',
    'RESIDENTIAL_POSTCODE': lambda: fake.zipcode(),
    'MAILING_ADDRESS1': lambda: _empty(fake.street_address().upper()),
    'MAILING_SECONDARY_ADDRESS': lambda: _empty(fake.street_address().upper()),
    'MAILING_CITY': lambda: _empty(fake.city().upper()),
    'MAILING_STATE': lambda: _empty(fake.state_abbr()),
    'MAILING_ZIP': lambda: _empty(fake.zipcode()),
    'MAILING_ZIP_PLUS4': lambda: _empty(fake.numerify(text='####')),
    'MAILING_COUNTRY': lambda: _empty(fake.state_abbr()),
    'MAILING_POSTAL_CODE': lambda: _empty(fake.zipcode()),
    'CAREER_CENTER': lambda: fake.city().upper(),
    'CITY': lambda: fake.city().upper(),
    'CITY_SCHOOL_DISTRICT': lambda: fake.city().upper(),
    'COUNTY_COURT_DISTRICT': lambda: str(randint(1, 99)).zfill(2),
    'CONGRESSIONAL_DISTRICT': lambda: str(randint(1, 99)).zfill(2),
    'COURT_OF_APPEALS': lambda: str(randint(1, 99)).zfill(2),
    'EDU_SERVICE_CENTER_DISTRICT': lambda: str(randint(1, 99)).zfill(2),
    'EXEMPTED_VILL_SCHOOL_DISTRICT': lambda: _empty(str(randint(1, 99)).zfill(2)),
    'LIBRARY': lambda: _empty(str(randint(1, 99)).zfill(2)),
    'LOCAL_SCHOOL_DISTRICT': lambda: _empty(str(randint(1, 99)).zfill(2)),
    'MUNICIPAL_COURT_DISTRICT': lambda: _empty(str(randint(1, 99)).zfill(2)),
    'PRECINCT_NAME': lambda: fake.city().upper(),
    'PRECINCT_CODE': lambda: '{}-{}'.format(randint(10,80), fake.lexify(text='???').upper()),
    'STATE_BOARD_OF_EDUCATION': lambda: str(randint(1, 100)),
    'STATE_REPRESENTATIVE_DISTRICT': lambda: str(randint(1, 100)),
    'STATE_SENATE_DISTRICT': lambda: str(randint(1, 100)),
    'TOWNSHIP': lambda: _empty(fake.city().upper()),
    'VILLAGE': lambda: _empty(fake.city().upper()),
    'WARD': lambda: _empty(fake.city().upper()),
    'PRIMARY-05/07/2013': lambda: _blank(random.choice(['R', 'D'])),
    'GENERAL-11/03/2015': lambda: _blank('X')
}


# Defining fields because order matters for csvs without header rows
FLORIDA_FIELDS = [
    'County Code',
    'Voter ID',
    'Name Last',
    'Name Suffix',
    'Name First',
    'Name Middle',
    'Requested public records exemption',
    'Residence Address Line 1',
    'Residence Address Line 2',
    'Residence City (USPS)',
    'Residence State',
    'Residence Zipcode',
    'Mailing Address Line 1',
    'Mailing Address Line 2',
    'Mailing Address Line 3',
    'Mailing City',
    'Mailing State',
    'Mailing Zipcode',
    'Mailing Country',
    'Gender',
    'Race',
    'Birth Date',
    'Registration Date',
    'Party Affiliation',
    'Precinct',
    'Precinct Group',
    'Precinct Split',
    'Precinct Suffix',
    'Voter Status',
    'Congressional District',
    'House District',
    'Senate District',
    'County Commission District',
    'School Board District',
    'Daytime Area Code',
    'Daytime Phone Number',
    'Daytime Phone Extension',
    'Email address'
]

FLORIDA_SCHEMA = {
    'County Code': lambda: random.choice(['OKE', 'ALA', 'ABC']),
    'Voter ID': lambda: fake.numerify(text='##########'),
    'Name Last': lambda: fake.last_name().upper(),
    'Name Suffix': lambda: _empty(fake.suffix().upper()),
    'Name First': lambda: fake.first_name().upper(),
    'Name Middle': lambda: _empty(fake.first_name().upper()),
    'Requested public records exemption': lambda: random.choice(['Y', 'N']),
    'Residence Address Line 1': lambda: fake.street_address().upper(),
    'Residence Address Line 2': lambda: _empty(fake.secondary_address().upper()),
    'Residence City (USPS)': lambda: fake.city().upper(),
    'Residence State': lambda: ' ',
    'Residence Zipcode': lambda: fake.zipcode(),
    'Mailing Address Line 1': lambda: _empty(fake.street_address().upper()),
    'Mailing Address Line 2': lambda: _empty(fake.secondary_address().upper()),
    'Mailing Address Line 3': lambda: _empty(fake.secondary_address().upper()),
    'Mailing City': lambda: _empty(fake.city().upper()),
    'Mailing State': lambda: _empty(fake.state_abbr()),
    'Mailing Zipcode': lambda: _empty(fake.zipcode()),
    'Mailing Country': lambda: _empty(fake.state_abbr()),
    'Gender': lambda: _empty(random.choice(['F', 'M', 'U'])),
    'Race': lambda: random.choice(list(florida_race_keys)),
    'Birth Date': lambda: _empty(fake.date(pattern='%m/%d/%Y')),
    'Registration Date': lambda: fake.date(pattern='%m/%d/%Y'),
    'Party Affiliation': lambda: random.choice(list(florida_party_keys)),
    'Precinct': lambda: str(randint(1, 100)),
    'Precinct Group': lambda: str(randint(1, 100)),
    'Precinct Split': lambda: '{0:.1f}'.format(random.uniform(1, 12)),
    'Precinct Suffix': lambda: ' ',
    'Voter Status': lambda: random.choice(['ACT', 'INA', 'PRE']),
    'Congressional District': lambda: str(randint(1, 27)),
    'House District': lambda: str(randint(1, 120)),
    'Senate District': lambda: str(randint(1, 120)),
    'County Commission District': lambda: str(randint(1, 100)),
    'School Board District': lambda: str(randint(1, 100)),
    'Daytime Area Code': lambda: _empty(fake.numerify(text='###')),
    'Daytime Phone Number': lambda: _empty(fake.numerify(text='#######')),
    'Daytime Phone Extension': lambda: _empty(str(randint(10, 9999))),
    'Email address': lambda: _empty(fake.email().upper())
}

NEW_JERSEY_FIELDS = [
    'COUNTY',
    'VOTER ID',
    'LEGACY ID',
    'LAST NAME',
    'FIRST NAME',
    'MIDDLE NAME',
    'SUFFIX',
    'STREET NUMBER',
    'SUFF A',
    'SUFF B',
    'STREET NAME',
    'APT/UNIT NO',
    'CITY',
    'MUNICIPALITY',
    'ZIP',
    'DOB',
    'PARTY CODE',
    'WARD',
    'DISTRICT',
    'STATUS',
    'CONGRESSIONAL',
    'LEGISLATIVE',
    'FREEHOLDER',
    'SCHOOL',
    'REGIONAL SCHOOL',
    'FIRE'
]

NEW_JERSEY_SCHEMA = {
    'COUNTY':           lambda : random.choice(list(nj_county_keys)),
    'VOTER ID':         lambda : fake.numerify(text='#########'),
    'LEGACY ID':        lambda : fake.lexify(text='??') + fake.numerify(text='#######'),
    'LAST NAME':        lambda : fake.last_name(),
    'FIRST NAME':       lambda : fake.first_name(),
    'MIDDLE NAME':      lambda : _empty(fake.first_name()),
    'SUFFIX':           lambda : _empty(fake.suffix().upper()),
    'STREET NUMBER':    lambda : str(randint(1000, 99999)),
    'SUFF A':           lambda : random.choice(['SW', 'N', 'NE', 'NW', '']),
    'SUFF B':           lambda : random.choice(['SW', 'N', 'NE', 'NW', '']),
    'STREET NAME':      lambda : fake.street_name(),
    'APT/UNIT NO':      lambda : random.choice(['A', 'B', '1', '2', '3', '']),
    'CITY':             lambda : fake.city(),
    'MUNICIPALITY':     lambda : fake.city(),
    'ZIP':              lambda : _empty(fake.zipcode()),
    'DOB':              lambda : fake.date(pattern="%m/%d/%Y"),
    'PARTY CODE':       lambda : random.choice(list(nj_party_keys)),
    'WARD':             lambda : fake.numerify(text='##'),
    'DISTRICT':         lambda : fake.numerify(text='##'),
    'STATUS':           lambda: _empty(['A', 'AD', 'AF', 'IF', 'ID', 'P']),
    'CONGRESSIONAL':    lambda : randint(1,12),
    'LEGISLATIVE':      lambda : randint(1,40),
    'FREEHOLDER':       lambda : randint(1,21),
    'SCHOOL':           lambda : fake.numerify(text='##') + '.' + fake.numerify(text='####'),
    'REGIONAL SCHOOL':  lambda : fake.numerify(text='##') + '.' + fake.numerify(text='####'),
    'FIRE':             lambda : fake.numerify(text='##') + '.' + fake.numerify(text='####')
}

NEW_YORK_FIELDS = [
    'LASTNAME',
    'FIRSTNAME',
    'MIDDLENAME',
    'NAMESUFFIX',
    'RADDNUMBER',
    'RHALFCODE',
    'RAPARTMENT',
    'RPREDIRECTION',
    'RSTREETNAME',
    'RPOSTDIRECTION',
    'RCITY',
    'RZIP5',
    'RZIP4',
    'MAILADD1',
    'MAILADD2',
    'MAILADD3',
    'MAILADD4',
    'DOB',
    'GENDER',
    'ENROLLMENT',
    'OTHERPARTY',
    'COUNTYCODE',
    'ED',
    'LD',
    'TOWNCITY',
    'WARD',
    'CD',
    'SD',
    'AD',
    'LASTVOTEDDATE',
    'PREVYEARVOTED',
    'PREVCOUNTY',
    'PREVADDRESS',
    'PREVNAME',
    'COUNTYVRNUMBER',
    'REGDATE',
    'VRSOURCE',
    'IDREQUIRED',
    'IDMET',
    'STATUS',
    'REASONCODE',
    'INACT_DATE',
    'PURGE_DATE',
    'SBOEID',
    'VoterHistory'
]

NEW_YORK_SCHEMA = {
    'LASTNAME': lambda: fake.last_name(),
    'FIRSTNAME': lambda: fake.first_name(),
    'MIDDLENAME': lambda: _empty(fake.first_name()),
    'NAMESUFFIX': lambda: _empty(fake.suffix()),
    'RADDNUMBER': lambda: fake.building_number(),
    'RHALFCODE': lambda: _empty(random.choice(['1/2', '1/3'])),
    'RAPARTMENT': lambda: _empty(random.choice([fake.numerify(text='###'), 'GRD'])),
    'RPREDIRECTION': lambda: _empty(random.choice(['N', 'S', 'E', 'W'])),
    'RSTREETNAME': lambda: fake.street_name(),
    'RPOSTDIRECTION': lambda: _empty(random.choice(['N', 'S', 'E', 'W'])),
    'RCITY': lambda: fake.city(),
    'RZIP5': lambda: fake.zipcode(),
    'RZIP4': lambda: _empty(fake.numerify(text='####')),
    'MAILADD1': lambda: _empty(fake.street_address()),
    'MAILADD2': lambda: _empty(fake.secondary_address()),
    'MAILADD3': lambda: _empty(fake.street_address()),
    'MAILADD4': lambda: _empty(fake.street_address()),
    'DOB': lambda: fake.date(pattern='%Y%m%d'),
    'GENDER': lambda: random.choice(['M', 'F']),
    'ENROLLMENT': lambda: random.choice(list(ny_party_keys)),
    'OTHERPARTY': lambda: _empty(random.choice(list(ny_other_party_keys))),
    'COUNTYCODE': lambda: fake.numerify(text='##'),
    'ED': lambda: str(randint(1, 100)),
    'LD': lambda: str(randint(1, 100)),
    'TOWNCITY': lambda: fake.city(),
    'WARD': lambda: str(randint(1, 100)),
    'CD': lambda: str(randint(1, 27)),
    'SD': lambda: str(randint(1, 100)),
    'AD': lambda: str(randint(1, 100)),
    'LASTVOTEDDATE': lambda: _empty(fake.date(pattern='%Y%m%d')),
    'PREVYEARVOTED': lambda: _empty(fake.year()),
    'PREVCOUNTY': lambda: _empty(fake.city()),
    'PREVADDRESS': lambda: _empty(fake.street_address()),
    'PREVNAME': lambda: _empty(fake.name()),
    'COUNTYVRNUMBER': lambda: fake.numerify(text='#######'),
    'REGDATE': lambda: fake.date(pattern='%Y%m%d'),
    'VRSOURCE': lambda: random.choice(['AGCY', 'CBOE', 'DMV', 'LOCALREG', 'MAIL', 'SCHOOL']),
    'IDREQUIRED': lambda: random.choice(['Y', 'N']),
    'IDMET': lambda: random.choice(['Y', 'N']),
    'STATUS': lambda: random.choice(['A', 'AM', 'AF', 'AP', 'AU', 'I', 'P', '17']),
    'REASONCODE': lambda: random.choice(['ADJ-INCOMP', 'DEATH', 'DUPLICATE', 'FELON', 'MAIL-CHECK', 'MOVED', 'NCOA', 'NVRA', 'RETURN-MAIL', 'VOTER-REQ']),
    'INACT_DATE': lambda: _empty(fake.date(pattern='%Y%m%d')),
    'PURGE_DATE': lambda: _empty(fake.date(pattern='%Y%m%d')),
    'SBOEID': lambda: 'NY{}'.format(fake.numerify('#########').zfill(18)),
    'VoterHistory': lambda: _empty(random.choice(['2004;General Election', '2012']))
}


NORTH_CAROLINA_SCHEMA = {
    'county_id': lambda: str(randint(1, 90)),
    'county_desc': lambda: fake.city().upper(),
    'voter_reg_num': lambda: str(randint(10000, 999999999)),
    'status_cd': lambda: random.choice(['A', 'I']),
    'voter_status_desc': lambda: random.choice(['ACTIVE', 'INACTIVE']),
    'reason_cd': lambda: random.choice(['A1', 'A2', 'AL', 'AN', 'AP', 'AV', 'IN', 'IU']),
    'voter_status_reason_desc': lambda: random.choice(['CONFIRMATION NOT RETURNED', 'CONFIRMATION PENDING', 'CONFIRMATION RETURNED UNDELIVERABLE', 'LEGACY DATA', 'UNVERIFIED', 'UNVERIFIED NEW', 'VERIFICATION PENDING', 'VERIFIED']),
    'absent_ind': lambda: ' ',
    'name_prefx_cd': lambda: ' ',
    'last_name': lambda: fake.last_name().upper(),
    'first_name': lambda: fake.first_name().upper(),
    'middle_name': lambda: _empty(fake.first_name().upper()),
    'name_suffix_lbl': lambda: _empty(fake.suffix().upper()),
    'res_street_address': lambda: fake.street_address().upper(),
    'res_city_desc': lambda: fake.city().upper(),
    'state_cd': lambda: 'NC',
    'zip_code': lambda: fake.zipcode(),
    'mail_addr1': lambda: _empty(fake.street_address().upper()),
    'mail_addr2': lambda: _empty(fake.secondary_address().upper()),
    'mail_addr3': lambda: _empty(fake.street_address().upper()),
    'mail_addr4': lambda: _empty(fake.street_address().upper()),
    'mail_city': lambda: _empty(fake.city().upper()),
    'mail_state': lambda: _empty(fake.state_abbr()),
    'mail_zipcode': lambda: _empty(fake.zipcode()),
    'full_phone_number': lambda: _empty(fake.phone_number().replace('-', '')),
    'race_code': lambda: random.choice(['B', 'I', 'O', 'W', 'U', 'A', 'M']),
    'ethnic_code': lambda: random.choice(['HL', 'NL', 'UN']),
    'party_cd': lambda: random.choice(['DEM', 'REP', 'LIB', 'UNA']),
    'gender_code': lambda: random.choice(['F', 'M', 'U']),
    'birth_age': lambda: str(randint(18, 100)),
    'birth_state': lambda: fake.state_abbr(),
    'drivers_lic': lambda: random.choice(['Y', 'N']),
    'registr_dt': lambda: fake.date(pattern='%m/%d/%Y'),
    'precinct_abbrv': lambda: random.choice(['CAR', '08N', '1/7']),
    'precinct_desc': lambda: fake.city().upper(),
    'municipality_abbrv': lambda: _empty(fake.state_abbr()),
    'municipality_desc': lambda: _empty(fake.city().upper()),
    'ward_abbrv': lambda: _empty(random.choice(['7', '5', 'R-B'])),
    'ward_desc': lambda: _empty(random.choice(['RALEIGH MUNICIPAL DISTRICT B', 'SOUTHWEST WARD'])),
    'cong_dist_abbrv': lambda: _empty(str(randint(1, 13))),
    'super_court_abbrv': lambda: _empty(str(randint(1, 30)).zfill(2) + random.choice(['A', 'B'])),
    'judic_dis_abbrv': lambda: _empty(random.choice([str(randint(1, 30)), '20A'])),
    'nc_senate_abbrv': lambda: _empty(str(randint(1, 100))),
    'nc_house_abbrv': lambda: _empty(str(randint(1, 100))),
    'county_commiss_abbrv': lambda: _empty(random.choice(['CM03', '6', '4'])),
    'county_commiss_desc': lambda: _empty(random.choice(['COMMISSION #4', 'COMMISSION #7'])),
    'township_abbrv': lambda: _empty(random.choice(['1', '4' ,'5', 'G', 'GAST'])),
    'township_desc': lambda: _empty(random.choice(['DALLAS', 'IRONTON'])),
    'school_dist_abbrv': lambda: _empty(random.choice(['CH/CHAR', '4', 'S06', 'ROBE'])),
    'school_dist_desc': lambda: _empty(random.choice(['SCHOOL #3', 'CHAPEL HILL'])),
    'fire_dist_abbrv': lambda: _empty(random.choice(['NEFD', 'PC11', '15'])),
    'fire_dist_desc': lambda: _empty(random.choice(['NORTHEAST FIRE DISTRICT', 'PUMPKIN CENTER', 'NEWTON'])),
    'water_dist_abbrv': lambda: _empty(random.choice(['1', '8', 'CL/U', 'CLWA'])),
    'water_dist_desc': lambda: _empty(random.choice(['CENTRAL', 'CITY COUNCIL DIST 1', 'PINETOPS'])),
    'sewer_dist_abbrv': lambda: _empty(random.choice(['1', '2', 'EL'])),
    'sewer_dist_desc': lambda: _empty(random.choice(['DISTRICT 1', 'DISTRICT 2', 'EAST LINCOLN'])),
    'sanit_dist_abbrv': lambda: _empty(random.choice(['B P', 'EOSD', '26'])),
    'sanit_dist_desc': lambda: _empty(random.choice(['EASTERN WAYNE', 'EAST CRAVEN'])),
    'rescue_dist_abbrv': lambda: _empty(random.choice(['WHRD', 'NARD', '50'])),
    'rescue_dist_desc': lambda: _empty(random.choice(['GSO CITY COUNCIL 1', 'HOSPITAL DIST 50'])),
    'munic_dist_abbrv': lambda: _empty(fake.state_abbr()),
    'munic_dist_desc': lambda: _empty(fake.city().upper()),
    'dist_1_abbrv': lambda: _empty(random.choice(['20', '30', '29A'])),
    'dist_1_desc': lambda: _empty(random.choice(['26TH PROS DIST', '05 PROSECUTORIAL'])),
    'dist_2_abbrv': lambda: ' ',
    'dist_2_desc': lambda: ' ',
    'Confidential_ind': lambda: 'N',
    'age': lambda: str(randint(18, 100)),
    'ncid': lambda: '{}{}'.format(fake.lexify(text='??').upper(), fake.numerify(text='######')),
    'vtd_abbrv': lambda: random.choice(['CAR', '08N', '1/7']),
    'vtd_desc': lambda: random.choice(['CAR', '08N', '1/7'])
}

OKLAHOMA_FIELDS = [
    'Precinct',
    'LastName',
    'FirstName',
    'MiddleName',
    'Suffix',
    'VoterID',
    'PolitalAff',
    'Status',
    'StreetNum',
    'StreetDir',
    'StreetName',
    'StreetType',
    'BldgNum',
    'City',
    'Zip',
    'DateOfBirth',
    'OriginalRegistration',
    'MailStreet1',
    'MailStreet2',
    'MailCity',
    'MailState',
    'MailZip',
    'Muni',
    'MuniSub',
    'School',
    'SchoolSub',
    'TechCenter',
    'TechCenterSub',
    'CountyComm',
    'VoterHist1',
    'HistMethod1',
    'VoterHist2',
    'HistMethod2',
    'VoterHist3',
    'HistMethod3',
    'VoterHist4',
    'HistMethod4',
    'VoterHist5',
    'HistMethod5',
    'VoterHist6',
    'HistMethod6',
    'VoterHist7',
    'HistMethod7',
    'VoterHist8',
    'HistMethod8',
    'VoterHist9',
    'HistMethod9',
    'VoterHist10',
    'HistMethod10'
]

PENNSYLVANIA_SCHEMA = {
    'STATE_VOTER_REF': lambda: str(randint(1, 1000000)),
    'TITLE': lambda: fake.prefix(),
    'LAST_NAME': lambda: fake.last_name().upper(),
    'FIRST_NAME': lambda: _blank(fake.first_name().upper()),
    'MIDDLE_NAME': lambda: _blank(fake.first_name().upper()),
    'NAME_SUFFIX': lambda: _empty(fake.suffix()),
    'GENDER': lambda: random.choice(['M', 'F', 'U', '']),
    'BIRTHDATE': lambda: _blank(fake.date(pattern='%m/%d/%Y')),
    'REGISTRATION_DATE': lambda: _blank(fake.date(pattern='%m/%d/%Y')),
    'REGISTRATION_STATUS': lambda: random.choice(['I', 'A']),
    '_STATUS_CHANGE_DATE': lambda: _blank(fake.date(pattern='%m/%d/%Y')),
    '_PARTY_CODE': lambda: random.choice(['D', 'R', 'IND', "", "GR", "RANDOMOTHER"]),
    'ADDRESS_NUMBER': lambda: _blank(fake.building_number()),
    'ADDRESS_NUMBER_SUFFIX': lambda: _blank(fake.building_number()),
    'STREET_NAME': lambda: fake.street_name().upper(),
    '_ADDRESS_APARTMENT_NUM': lambda: _blank(fake.building_number()),
    '_ADDRESS_LINE2': lambda: _blank(fake.secondary_address().upper()),
    '_REGISTRATION_CITY': lambda: fake.city().upper(),
    'STATE_NAME': lambda: _blank(fake.state_abbr().upper()),
    'ZIP_CODE': lambda: _blank(fake.zipcode()),
    'MAIL_ADDRESS_LINE1': lambda: _blank(fake.street_address().upper()),
    'MAIL_ADDRESS_LINE2': lambda: _blank(fake.secondary_address().upper()),
    'MAIL_CITY': lambda: fake.city().upper(),
    'MAIL_STATE': lambda: _blank(fake.state_abbr().upper()),
    'MAIL_ZIP_CODE': lambda: _blank(fake.zipcode()),
    '_LASTVOTE': lambda: _blank(fake.date(pattern='%m/%d/%Y')),
    '_PRECINCT_CODE': lambda: str(randint(1, 1000000)),
    'PRECINCT_SPLIT': lambda: '%d-%d' % (randint(1, 1000000), randint(1,50)),
    '_LAST_CHANGE_DATE': lambda: _blank(fake.date(pattern='%m/%d/%Y')),
    '_LEGACY_SYSTEM_ID': lambda: str(randint(800000, 10000000)),
    'PHONE': lambda: _blank(fake.phone_number().replace('-', '')),
    'COUNTYCODE': lambda: fake.city().upper(),
    'MAIL_COUNTRY': lambda: _blank(fake.state_abbr()),
}

MICHIGAN_SCHEMA = {
    'LAST_NAME': lambda: fake.last_name().upper(),
    'FIRST_NAME': lambda: fake.first_name().upper(),
    'MIDDLE_NAME': lambda: _blank(fake.first_name().upper()),
    'NAME_SUFFIX': lambda: _empty(fake.suffix()),
    'BIRTH_YEAR': lambda: fake.year(),
    'GENDER': lambda: _blank(random.choice(['F', 'M', '1', '2'])),
    'DATE_OF_REGISTRATION': lambda: fake.date(pattern='%m%d%Y'),
    'HOUSE_NUM_CHARACTER': lambda: _empty(random.choice(['N', 'S', 'E', 'W'])),
    'RESIDENCE_STREET_NUMBER': lambda: _blank(fake.building_number()),
    'HOUSE_SUFFIX': lambda: _empty(random.choice(['1/2', '1/3'])),
    'PRE_DIRECTION': lambda: _empty(random.choice(['N', 'S', 'E', 'W'])),
    'STREET_NAME': lambda: fake.street_name().upper(),
    'STREET_TYPE': lambda: fake.street_suffix().upper(),
    'SUFFIX_DIRECTION': lambda: _empty(random.choice(['N', 'S', 'E', 'W'])),
    'RESIDENCE_EXTENSION': lambda: _empty(random.choice(['APT', 'LOT'])),
    'CITY': lambda: fake.city().upper(),
    # 'STATE': lambda: fake.state_abbr(),
    'STATE': lambda: random.choice(['MI']),
    'ZIP': lambda: fake.zipcode(),
    'MAIL_ADDR_1': lambda: _blank(fake.street_address().upper()),
    'MAIL_ADDR_2': lambda: _blank(fake.secondary_address().upper()),
    'MAIL_ADDR_3': lambda: fake.city().upper(),
    'MAIL_ADDR_4': lambda: _blank(fake.state_abbr().upper()),
    'MAIL_ADDR_5': lambda: _blank(fake.zipcode()),
    'STATE_VOTER_REF': lambda: fake.numerify(text=('#'*13)),
    # 'COUNTYCODE': lambda: fake.numerify(text='##'),
    'COUNTYCODE': lambda: random.choice(list(range(10, 25))),
    # 'JURISDICTION': lambda: fake.numerify(text='####'),
    'JURISDICTION': lambda: _empty(random.choice(['00300', '00320', '00980'])),
    'WARD_PRECINCT': lambda: fake.numerify(text='####'),
    # 'SCHOOL_CODE': lambda: fake.numerify(text='##'),
    'SCHOOL_CODE': lambda: _empty(random.choice(['00007', '00006', '00010'])),
    'LOWER_HOUSE_DIST': lambda: fake.numerify(text='##'),
    'UPPER_HOUSE_DIST': lambda: fake.numerify(text='##'),
    'CONGRESSIONAL_DIST': lambda: str(randint(1, 16)),
    'COUNTY_BOARD_DIST': lambda: _empty(str(randint(1, 50))),
    # 'VILLAGE_CODE': lambda: _empty(fake.numerify(text='####')),
    'VILLAGE_CODE': lambda: _empty(random.choice(['00380', '01800', '06980'])),
    'VILLAGE_PRECINCT': lambda: _empty(fake.numerify(text='###')),
    'SCHOOL_PRECINCT': lambda: _empty(fake.numerify(text='###')),
    'PERMANENT_ABSENTEE_IND': lambda: random.choice(['Y', 'N']),
    'REGISTRATION_STATUS': lambda: random.choice(['A', 'V', 'C', 'R', 'CH']),
    'UOCAVA_STATUS': lambda: random.choice(['M', 'C', 'N', 'O'])
    # 'ELECTION_DATE': lambda: fake.date(pattern='%m%d%Y'),
    # 'ELECTION_TYPE': lambda: _empty(random.choice(['SPECIAL', 'GENERAL'])),
    # 'ABSENTEE_TYPE': lambda: random.choice(['Y', 'N'])
}


UTAH_SCHEMA = {
    'Voter ID': lambda: str(randint(1, 1000000)),
    'Last Name': lambda: fake.last_name(),
    'First Name': lambda: _blank(fake.first_name()), # First Name can be missing
    'Middle Name': lambda: _blank(fake.first_name()),
    'Name Suffix': lambda: fake.suffix(),
    'Status': lambda: random.choice(['Active', 'Inactive']),
    'Absentee': lambda: _blank(random.choice([0, 1])),
    'UOCAVA': lambda: _blank('YES'),
    'Registration Date': lambda: random.choice([fake.date(pattern='%m/%d/%Y'), '12:00:00 AM']), # some weird data
    'Original Registration Date': lambda: random.choice([fake.date(pattern='%m/%d/%Y'), '12:00:00 AM']),
    'Party': lambda: random.choice(list(utah_party_keys)),
    'Phone': lambda: _blank(fake.phone_number()),
    'Mailing Address': lambda: _blank(fake.street_address()),
    'Mailing city, state  zip': lambda: _blank('%s, %s  %s' % (fake.city(), fake.state_abbr().upper(), fake.zipcode())),
    'County ID': lambda: random.choice(['Salt Lake', 'Utah', 'Davis', 'Weber', 'Washington']),
    'Precinct': lambda: random.choice(['PR09', 'SLC080:00', 'COT036:01', 'LA29:I-N-', '41']),
    'House Number': lambda: fake.building_number(),
    'House Number Suffix': lambda: _blank('1/2'),
    'Direction Prefix': lambda: _blank(random.choice(['E', 'N', 'S', 'W'])),
    'Street': lambda: fake.street_name(),
    'Direction Suffix': lambda: _blank(random.choice(['E', 'N', 'S', 'W'])),
    'Street Type': lambda: _blank(random.choice(['Dr', 'St', 'Rd', 'Ln', 'Cir', 'Ave', 'Way', 'Ct', 'Blvd', 'Pl'])),
    'Unit Type': lambda: _blank(random.choice(['Apt', 'Bldg', 'Bsmt', 'Lot', 'Ste', 'Trlr', 'Unit', '#'])),
    'Unit Number': lambda: random.choice(['123', '5c', 'F-101', 'Front']),
    'City': lambda: fake.city(),
    'Zip': lambda: fake.zipcode(),
    'DOB': lambda: random.choice([fake.date(pattern='%m/%d/%Y'), '12:00:00 AM']),  # some weird data in the file
    'Congressional': lambda: _blank(random.randint(1, 4)),
    'State House': lambda: _blank(random.randint(1, 75)),
    'State Senate': lambda: _blank(random.randint(1, 29)),
    'State Schoolboard': lambda: _blank(random.randint(1, 15)),
    'Local Schoolboard': lambda: _blank(random.choice(['Granite School Board 1', 'Cache County Sch District 8', 'SB 2'])),
    'County Council': lambda: _blank(random.randint(1, 6)),
    'City Council': lambda: _blank(random.choice(['Salt Lake City Council 6', 'Cedar City Council 2'])),
    '11/6/1990': lambda: _blank('11/6/1990'),
    '11/5/1991': lambda: _blank('11/5/1991'),
    '11/3/1992': lambda: _blank('11/3/1992'),
    '11/2/1993': lambda: _blank('11/2/1993'),
    '11/8/1994': lambda: _blank('11/8/1994'),
    '5/23/1995': lambda: _blank('5/23/1995'),
    '9/12/1995': lambda: _blank('9/12/1995'),
    '10/3/1995': lambda: _blank('10/3/1995'),
    '11/7/1995': lambda: _blank('11/7/1995'),
    '6/25/1996': lambda: _blank('6/25/1996'),
    '8/6/1996': lambda: _blank('8/6/1996'),
    '11/5/1996': lambda: _blank('11/5/1996'),
    '2/4/1997': lambda: _blank('2/4/1997'),
    '5/6/1997': lambda: _blank('5/6/1997'),
    '8/1/1997': lambda: _blank('8/1/1997'),
    '10/7/1997': lambda: _blank('10/7/1997'),
    '11/4/1997': lambda: _blank('11/4/1997'),
    '6/23/1998': lambda: _blank('6/23/1998'),
    '11/3/1998': lambda: _blank('11/3/1998'),
    '5/4/1999': lambda: _blank('5/4/1999'),
    '8/3/1999': lambda: _blank('8/3/1999'),
    '10/5/1999': lambda: _blank('10/5/1999'),
    '11/2/1999': lambda: _blank('11/2/1999'),
    '5/2/2000': lambda: _blank('5/2/2000'),
    '6/27/2000': lambda: _blank('6/27/2000'),
    '11/7/2000': lambda: _blank('11/7/2000'),
    '2/6/2001': lambda: _blank('2/6/2001'),
    '10/2/2001': lambda: _blank('10/2/2001'),
    '11/6/2001': lambda: _blank('11/6/2001'),
    '6/25/2002': lambda: _blank('6/25/2002'),
    '11/5/2002': lambda: _blank('11/5/2002'),
    '2/4/2003': lambda: _blank('2/4/2003'),
    '8/5/2003': lambda: _blank('8/5/2003'),
    '10/7/2003': lambda: _blank('10/7/2003'),
    '11/4/2003': lambda: _blank('11/4/2003'),
    '5/4/2004': lambda: _blank('5/4/2004'),
    '6/22/2004': lambda: _blank('6/22/2004'),
    '8/3/2004': lambda: _blank('8/3/2004'),
    '11/2/2004': lambda: _blank('11/2/2004'),
    '10/4/2005': lambda: _blank('10/4/2005'),
    '11/8/2005': lambda: _blank('11/8/2005'),
    '6/27/2006': lambda: _blank('6/27/2006'),
    '11/7/2006': lambda: _blank('11/7/2006'),
    '6/26/2007': lambda: _blank('6/26/2007'),
    '9/11/2007': lambda: _blank('9/11/2007'),
    '11/6/2007': lambda: _blank('11/6/2007'),
    '2/5/2008': lambda: _blank('2/5/2008'),
    '6/24/2008': lambda: _blank('6/24/2008'),
    '11/4/2008': lambda: _blank('11/4/2008'),
    '9/15/2009': lambda: _blank('9/15/2009'),
    '11/4/2009': lambda: _blank('11/4/2009'),
    '6/22/2010': lambda: _blank('6/22/2010'),
    '11/2/2010': lambda: _blank('11/2/2010'),
    '9/13/2011': lambda: _blank('9/13/2011'),
    '11/8/2011': lambda: _blank('11/8/2011'),
    '6/26/2012': lambda: _blank('6/26/2012'),
    '11/6/2012': lambda: _blank('11/6/2012'),
    '8/13/2013': lambda: _blank('8/13/2013'),
    '11/5/2013': lambda: _blank('11/5/2013')
}

VERMONT_SCHEMA = {
    '2008 Gen Election Participation': lambda: random.choice(['T', 'F']),
    '2010 Gen Election Participation': lambda: random.choice(['T', 'F']),
    '2012 Gen Election Participation': lambda: random.choice(['T', 'F']),
    '2014 Gen Election Participation': lambda: random.choice(['T', 'F']),
    'County': lambda: random.choice(['ADDISON','BENNINGTON','CALEDONIA','CHITTENDEN','ESSEX','FRANKLIN','GRAND ISLE','LAMOILLE','ORANGE','ORLEANS','RUTLAND','WASHINGTON','WINDHAM','WINDSOR']),
    'Date last Voted': lambda: _blank(fake.date(pattern='%m/%d/%Y')),
    'Date of Registration': lambda: fake.date(pattern='%m/%d/%Y'),
    'Fire District': lambda: _blank(fake.city().upper()),
    'First Name': lambda: fake.first_name().upper(),
    'Garbage District': lambda: _blank(fake.city().upper()),
    'Last Name': lambda: fake.last_name().upper(),
    'Legal Address City': lambda: fake.city().upper(),
    'Legal Address Line 1': lambda: _blank(fake.street_address().upper()),
    'Legal Address Line 2': lambda: _blank(fake.secondary_address().upper()),
    'Legal Address State': lambda: 'VT',
    'Legal Address Zip': lambda: _blank(fake.zipcode()),
    'Mailing Address City': lambda: fake.city().upper(),
    'Mailing Address Line 1': lambda: _blank(fake.street_address().upper()),
    'Mailing Address Line 2': lambda: _blank(fake.secondary_address().upper()),
    'Mailing Address State': lambda: 'VT',
    'Mailing Address Zip': lambda: _blank(fake.zipcode()),
    'Mailing Address in care of': lambda: '',
    'Middle Name': lambda: _empty(fake.first_name().upper()),
    'Police District': lambda: _blank(fake.city().upper()),
    'Polling Location': lambda: _blank(fake.street_address().upper()),
    'School District': lambda: _blank(fake.city().upper()),
    'Senate District': lambda: fake.lexify(text="???").upper(),
    'Sewer District': lambda: _blank(fake.city().upper()),
    'Status': lambda: 'ACTIVE',
    'Suffix': lambda:  _blank(fake.suffix().upper()),
    'Telephone': lambda: _blank(fake.phone_number()),
    'Town of Registration': lambda: _blank(fake.city().upper()),
    'Town-Nemrc Number': lambda: fake.numerify(text="##"),
    'Village': lambda: '',
    'VoterID': lambda: '000{}'.format(str(randint(100000, 999999))),
    'Voting District': lambda: fake.bothify(text="???-#-#"),
    'Ward': lambda: '',
    'Water District': lambda: '',
    'Year of Birth': lambda: str(randint(1910, 1999))
}

WASHINGTON_SCHEMA = {
'StateVoterID': lambda:'WA{}'.format(str(randint(1000, 999999)).zfill(10)),
'CountyVoterID': lambda:  str(randint(1, 88)),
'Title': lambda: ' ',
'FName': lambda:  fake.first_name().upper(),
'MName': lambda:  fake.first_name().upper(),
'LName': lambda:  fake.last_name().upper(),
'NameSuffix': lambda:  _empty(fake.suffix().upper()),
'Birthdate': lambda:  _empty(fake.date(pattern='%m/%d/%Y')),
'Gender': lambda:  random.choice(['F', 'M', 'U']),
'RegStNum': lambda:  _empty(fake.building_number()),
'RegStFrac': lambda: _empty(str(randint(1, 13))) ,
'RegStName': lambda:  fake.street_name().upper(),
'RegStType': lambda:  fake.street_suffix(),
'RegUnitType': lambda:  _empty(random.choice(['APT', 'UNIT', 'FLOOR', "", ])),
'RegStPreDirection': lambda:  _empty(random.choice(['S', 'E', 'W', "", ])),
'RegStPostDirection': lambda:  _empty(random.choice(['S', 'E', 'W', "", ])),
'RegUnitNum': lambda:  _blank(fake.building_number()),
'RegCity': lambda:  fake.city().upper(),
'RegState': lambda:  _blank(fake.state_abbr().upper()),
'RegZipCode': lambda:  _blank(fake.zipcode()),
'CountyCode': lambda:  random.choice(['SN','CR','AS','PI']),
'PrecinctCode': lambda: str(randint(1, 999999)) ,
'PrecinctPart': lambda:  str(randint(1, 999999)) ,
'LegislativeDistrict': lambda:  _empty(str(randint(1, 100))),
'CongressionalDistrict': lambda:  _empty(str(randint(1, 100))),
'Mail1': lambda:  _blank(fake.street_address().upper()),
'Mail2': lambda:  _blank(fake.secondary_address().upper()),
'Mail3': lambda:  _blank(fake.secondary_address().upper()),
'Mail4': lambda:  _blank(fake.secondary_address().upper()),
'MailCity': lambda:  fake.city().upper(),
'MailZip': lambda:  _blank(fake.zipcode()),
'MailState': lambda:  _blank(fake.state_abbr().upper()),
'MailCountry': lambda:  ' ',
'Registrationdate': lambda:  _empty(fake.date(pattern='%m/%d/%Y')),
'AbsenteeType': lambda:  random.choice(['N', 'P', ' ', 'V']),
'LastVoted': lambda:  _empty(fake.date(pattern='%m/%d/%Y')),
'StatusCode': lambda:  random.choice(['A', 'I']),
'Dflag': lambda:  ' '
}


def fakePAdistrict():
    prefix = random.choice(['LG', 'SN', 'MN', 'CO', 'CN', 'SAN', randint(1,1000)])
    return '%s%s%d' % (prefix, random.choice(['', '-']), randint(1,100000))

for d in range(40):
    PENNSYLVANIA_SCHEMA['_DISTRICT%d' % (d+1)] = fakePAdistrict

for d in range(1,40):
    PENNSYLVANIA_SCHEMA['_VOTEHISTORY_%d' % (2*d)] = lambda: random.choice(['','AP','AB','P'])
    PENNSYLVANIA_SCHEMA['_VOTEHISTORY_%d' % (2*d+1)] = PENNSYLVANIA_SCHEMA['_PARTY_CODE']


def make_state_data(state_name, state_schema,
                    sep=',', has_header=True, input_fields=None):
    state_rows = []
    while len(state_rows) < NUM_ROWS:
        r  = {}
        for k in state_schema.keys():
            r[k] = state_schema[k]()
        state_rows.append(r)

    if input_fields is None:
        input_fields = state_rows[0].keys()

    with open(os.path.join(TEST_DATA_DIR, state_name + '.csv'), 'w') as f:
        w = csv.DictWriter(f, fieldnames=input_fields, delimiter=sep)
        if has_header:
            w.writeheader()
        w.writerows(state_rows)


def make_mi_data():
    state_rows = []
    while len(state_rows) < NUM_ROWS:
        r = []
        for k in  MI.transformer.StateTransformer.input_fields:
            r.append(str(MICHIGAN_SCHEMA[k]()))
        state_rows.append(r)

    col_indices = MI.transformer.StatePreparer.col_indices
    with open('sample_entire_state_v.lst', 'w') as f:
        for row in state_rows:
            row_str = ''
            for i, r in enumerate(row):
                col_len = col_indices[i][1] - col_indices[i][0]
                if len(r) > col_len:
                    r = r[:col_len]
                row_str += r + (' ' * (col_len - len(r)))
            row_str += '\n'
            f.write(row_str)

    hist_voters = [[r[23], r[24], r[25], r[27]] for r in state_rows]
    hist_rows = []
    for i, hv in enumerate(hist_voters):
        hv.append(random.choice(['102000004', '102000017', '102000022']))
        hv.append(random.choice(['Y', 'N']))
        hist_rows.append(hv)

    history_indices = MI.transformer.StatePreparer.history_indices

    with open('sample_entire_state_h.lst', 'w') as f:
        for row in hist_rows:
            row_str = ''
            for i, r in enumerate(row):
                col_len = history_indices[i][1] - history_indices[i][0]
                if len(r) > col_len:
                    r = r[:col_len]
                row_str += r + (' ' * (col_len - len(r)))
            row_str += '\n'
            f.write(row_str)


if __name__ == '__main__':
    # make_mi_data()
    states = {'de': ([DELAWARE_SCHEMA],
                       {}),
              'co': ([COLORADO_SCHEMA],
                       {}),
              'oh': ([OHIO_SCHEMA],
                       {}),
              'ok': ([OKLAHOMA_SCHEMA],
                       {'has_header': False,
                        'input_fields': OKLAHOMA_FIELDS}),
              'fl': ([FLORIDA_SCHEMA],
                          {'sep': '\t',
                           'has_header': False,
                           'input_fields': FLORIDA_FIELDS}),
              'nj': ([NEW_JERSEY_SCHEMA],
                          {'sep' : '|',
                           'has_header' : False,
                           'input_fields' : NEW_JERSEY_FIELDS}),
              'ny': ([NEW_YORK_SCHEMA],
                           {'has_header': False,
                            'input_fields': NEW_YORK_FIELDS}),
              'nc': ([NORTH_CAROLINA_SCHEMA],
                                 {'sep':'\t'}),
              'pa': ([PENNSYLVANIA_SCHEMA],
                               {'sep':'\t',
                                'has_header': False,
                                'input_fields': PA.transformer.StateTransformer.input_fields}),
              'mi': ([MICHIGAN_SCHEMA],
                           {'input_fields': MI.transformer.StateTransformer.input_fields +
                            ['ELECTION_DATE', 'ELECTION_TYPE', 'ABSENTEE_TYPE']}),
              'ut': ([UTAH_SCHEMA], {}),
              'vt': ([VERMONT_SCHEMA],
                                 {'sep':'|'}),
              'wa': ([WASHINGTON_SCHEMA],
                                {'sep':'\t'}),
    }
    keys = states.keys()
    if len(sys.argv) > 1:
        keys = sys.argv[1:]
    for state in keys:
        args, kwargs = states[state]
        make_state_data(state, *args, **kwargs)
