from enum import Enum


class Countries(Enum):
    scotland = "Scotland"
    wales = "Wales"
    england = "England"
    northern_ireland = "Northern Ireland"


class Regions(Enum):
    scotland = "Scotland"
    wales = "Wales"
    south_east = "South East"
    south_west = "South West"
    london = "London"
    east_of_england = "East of England"
    west_midlands = "West Midlands"
    yorkshire_and_the_humber = "Yorkshire and The Humber"
    northern_ireland = "Northern Ireland"
    east_midlands = "East Midlands"
    north_west = "North West"
    north_east = "North East"


class Student_cols(Enum):
    UKPRN = "UKPRN"
    HE_provider_name = "HE provider"
    country = "Country of HE provider"
    region = "Region of HE provider"
    first_year_marker = "First year marker"
    level_of_study = "Level of study"
    mode_of_study = "Mode of study"
    academic_year = "Academic Year"
    category_marker = "Category marker"
    category = "Category"
    number = "Number"


class Staff_cols(Enum):
    UKPRN = "UKPRN"
    HE_provider_name = "HE Provider"
    country = "Country of HE provider"
    region = "Region of HE provider"
    mode_of_employment = "Mode of employment"
    atypical_marker = "Atypical marker"
    academic_marker = "Academic marker"
    contract_marker = "Contract marker"
    academic_year = "Academic Year"
    activity_standard_occupational_classification = (
        "Activity standard occupational classification"
    )
    number = "Number"


class First_year_marker(Enum):
    first_year = "First year"
    other_years = "Other years"


class Mode_of_study(Enum):
    full_tile = "Full-time"
    part_time = "Part-time"


class Mode_of_employment(Enum):
    full_tile = "Full-time"
    part_time = "Part-time"
    total = "All"


class Atypical_marker(Enum):
    academic_atypical = "Academic atypical"
    non_atypical = "Non-atypical"


class Contract_marker(Enum):
    academic = "Academic"
    non_academic = "Non-academic"
    total_excl_atypical = "All (excluding atypical)"


class Academic_marker(Enum):
    academic = "Academic"
    non_academic = "Non-academic"


class Category_marker(Enum):
    sex = "Sex"
    domicile = "Domicile"
    total = "Total"


class Category_sex(Enum):
    male = "Male"
    female = "Female"
    other = "Other"
    not_known = "Not known"


class Category_domicile(Enum):
    england = "England"
    scotland = "Scotland"
    wales = "Wales"
    northern_ireland = "Northern Ireland"
    other_UK = "Other UK"
    total_UK = "Total UK "
    EU = "European Union"
    non_EU = "Non-European Union"
    total_non_UK = "Total Non-UK"
    not_known = "Not known "


class Category_total(Enum):
    total = "Total"
