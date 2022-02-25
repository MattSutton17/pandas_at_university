# Pandas at University

The Higher Education Statistics Authority (HESA) collects and publishes a range of data on UK universities (or slightly more broadly, HE providers). This exercise challenges you to answer some questions about staff and students at those HE providers using real HESA data.

A template.py file has been created which loads in the data to get you started.

## The Task

Using the data provided, find the following:

1. What was the ratio of male to female students at the University of Sussex (UKPRN: 10007806) in 2020/21?
1. What were the names of the top 10 Scottish HE Providers (in order) by number of academic staff as an average of the available years?
1. Which HE provider had the most EU students in 2020/21?
1. Which HE provider in Wales saw the largest absolute growth in students between 2019/20 and 2020/21? How many additional students did they have in 2020/21?
1. In 2020/21, what were the top 5 universities (in order) in terms of the ratio of  students to academic staff? Fewer students per staff member is better.

## The Data

The data is stored in 2 csvs, one containing data on student enrolments and the other on the number of staff. These are laid out in a similar way to data extracted from SQL would look, with most columns offering indexing and a final column with the data.

For your convenience, enums for the columns and valid indexes have been provided.

The data provided has been taken from the HESA website ([www.hesa.ac.uk](www.hesa.ac.uk)). Student data for multiple years has been combined into one table, aggregated rows have been removed and some redundent columns have been removed. Data published on HESA website is free to copy, use, share, and adapt for any purpose. HESA open data is published under the [Creative Commons Attribution 4.0 International (CC BY 4.0) licence](https://creativecommons.org/licenses/by/4.0/).

### Student Enrolements

Student enrolments provides data on the number of students attending each HE provider from 2016/17 to 2020/21.

The columns are as follows:
- **UKPRN:** A unique numerical identifier for each HE provider.
- **HE provider:** The name of the HE provider. Note that (as often the case with name data), these are not necessarily always consistent for a given provider e.g. may be name differences like 'St. Andrews' vs 'St Andrews'.
- **Country of HE provider:** Which country the HE provider is in.
- **Region of HE provider:** Which region the HE provider is in.
- **First year marker:** Whether the students are in the first year of study (`First year`) or not (`Other years`).
- **Mode of study:** Whether students are `Full-time` or `Part-time`.
- **Academic Year:** Academic year of the data.
- **Category marker:** Breakdowns are available by either `Sex`, `Domicile` or `Total`, and this indicates which breakdown is being looked at. Domicile refers to the country of the student's home address.
- **Category:** The breakdown, from within the types in `Category marker`. Valid options for each `Category marker` are:
    - **Sex:** `Female`, `Male`, `Other`, `Not known`
    - **Domicile:** `England`, `Scotland`, `Wales`, `Northern Ireland`, `Other UK`, `European Union`, `Non-European Union` (note this doesn't include UK students), `Not known `
    - **Total**: `Total`
- **Number:** The number of students in categories set out by the other columns.

### Staff Numbers

Staff numbers provides data on the number of staff employed at each HE provider from 2014/15 to 2020/21. 

The columns are as follows:
- **UKPRN:** A unique numerical identifier for each HE provider.
- **HE Provider:** The name of the HE provider.
- **Country of HE provider:** Which country the HE provider is in.
- **Region of HE provider:** Which region the HE provider is in.
- **Mode of employment:** Whether staff are `Full-time` or `Part-time`.
- **Atypical marker:** Atypical staff are those members of staff whose contracts involve working arrangements that are not permanent.
- **Academic marker:** Academic staff are those involved in teaching and research. 
- **Contract marker:** The type of contract non-atypical staff are on.
- **Academic Year:** Academic year of the data.
- **Number:** The number of students in categories set out by the other columns.

## The Solutions

Some solutions can be found in solutions.py. These are not the only (and likely not best) way to answer these questions, but they can be used to compare your answers and help if you get stuck.