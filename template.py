import pandas as pd
from enums import (
    Countries,
    Regions,
    Student_cols,
    Staff_cols,
    First_year_marker,
    Mode_of_study,
    Mode_of_employment,
    Atypical_marker,
    Contract_marker,
    Academic_marker,
    Category_marker,
    Category_sex,
    Category_domicile,
    Category_total,
)


def main():
    """Main"""
    students_df = pd.read_csv("data/student_enrolments.csv")
    staff_df = pd.read_csv("data/staff_numbers.csv")


if __name__ == "__main__":
    main()
