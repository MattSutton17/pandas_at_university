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

    uni_names = get_uni_name_dict(students_df)

    print(
        f"Q1: The ratio of female to male students at the University of Sussex in 2020/21 was {round(q1_answer(students_df),1)}:1"
    )

    print(
        "Q2: The top 10 Scottish HE providers in descending order of the number of academic staff:"
    )
    for i, UKPRN in enumerate(q2_answer(staff_df)[0:10], 1):
        print(f"{i}: {uni_names[UKPRN]}")

    print(
        f"Q3: The HE provider with the most EU students in 2020/21 was {uni_names[q3_answer(students_df)]}"
    )

    q4_UKPRN, q4_growth = q4_answer(students_df)

    print(
        f"Q4: The HE provider in Wales with the largest growth in students was {uni_names[q4_UKPRN]}, with an increase of {q4_growth} students."
    )

    print("Q5: The top 5 HE providers for ratio of students to academic staff are:")
    for i, UKPRN in enumerate(q5_answer(students_df, staff_df), 1):
        print(f"{i}: {uni_names[UKPRN]}")


def get_uni_name_dict(students_df):
    """Returns a dictionary to convert UKPRNs to the name of the university"""
    uni_names = (
        students_df.groupby(by=Student_cols.UKPRN.value)[
            Student_cols.HE_provider_name.value
        ]
        .agg("min")
        .to_dict()
    )
    return uni_names


def q1_answer(students_df):
    """Returns the answer to question 1"""
    students_filtered = students_df[
        (students_df[Student_cols.UKPRN.value] == 10007806)
        & (students_df[Student_cols.academic_year.value] == "2020/21")
        & (students_df[Student_cols.category_marker.value] == Category_marker.sex.value)
    ]

    students_grouped = students_filtered.groupby(by=[Student_cols.category.value])[
        Student_cols.number.value
    ].sum()

    return (
        students_grouped[Category_sex.female.value]
        / students_grouped[Category_sex.male.value]
    )


def q2_answer(staff_df):
    """Returns the answer to question 2"""
    staff_filtered = staff_df[
        (staff_df[Staff_cols.country.value] == Countries.scotland.value)
        & (staff_df[Staff_cols.academic_marker.value] == Academic_marker.academic.value)
    ]

    staff_grouped = staff_filtered.groupby(
        by=[
            Staff_cols.UKPRN.value,
            Staff_cols.academic_year.value,
        ]
    )[Staff_cols.number.value].sum()

    staff_annual_avg = (
        staff_grouped.reset_index()
        .groupby(by=[Staff_cols.UKPRN.value])[Staff_cols.number.value]
        .agg("mean")
    )

    staff_annual_avg = staff_annual_avg.reset_index().sort_values(
        by=Staff_cols.number.value,
        ascending=False,
    )

    return staff_annual_avg[Staff_cols.UKPRN.value]


def q3_answer(students_df):
    """Returns the answer to question 3"""
    students_filtered = students_df[
        (students_df[Student_cols.academic_year.value] == "2020/21")
        & (
            students_df[Student_cols.category_marker.value]
            == Category_marker.domicile.value
        )
        & (students_df[Student_cols.category.value] == Category_domicile.EU.value)
    ]

    students_grouped = students_filtered.groupby(by=[Student_cols.UKPRN.value])[
        Student_cols.number.value
    ].sum()

    students_grouped_sorted = students_grouped.reset_index().sort_values(
        by=Student_cols.number.value, ascending=False
    )

    return students_grouped_sorted[Student_cols.UKPRN.value].iloc[0]


def q4_answer(students_df):
    """Returns the answer to question 4"""
    students_filtered = students_df[
        (students_df[Student_cols.country.value] == Countries.wales.value)
        & (
            students_df[Student_cols.category_marker.value]
            == Category_marker.total.value
        )
    ]

    students_grouped = students_filtered.groupby(
        by=[
            Student_cols.UKPRN.value,
            Student_cols.academic_year.value,
        ]
    )[Student_cols.number.value].sum()

    students_year_pivot = (
        students_grouped.reset_index()
        .pivot(
            index=[Student_cols.UKPRN.value],
            columns=Student_cols.academic_year.value,
            values=Student_cols.number.value,
        )
        .fillna(0)
    )

    students_year_pivot["Growth"] = (
        students_year_pivot["2020/21"] - students_year_pivot["2019/20"]
    )

    students_growth_sorted = students_year_pivot.sort_values(
        by="Growth", ascending=False
    )

    students_growth_sorted = students_growth_sorted.reset_index()

    return (
        students_growth_sorted[Student_cols.UKPRN.value].iloc[0],
        students_growth_sorted["Growth"].iloc[0],
    )


def q5_answer(students_df, staff_df):
    """Returns the answer to question 5"""
    students_filtered = students_df[
        (students_df[Student_cols.academic_year.value] == "2020/21")
        & (
            students_df[Student_cols.category_marker.value]
            == Category_marker.total.value
        )
    ]

    students_grouped = (
        students_filtered.groupby(
            by=[
                Student_cols.UKPRN.value,
            ]
        )[Student_cols.number.value]
        .sum()
        .to_frame()
    )

    staff_filtered = staff_df[
        (staff_df[Staff_cols.academic_year.value] == "2020/21")
        & (staff_df[Staff_cols.academic_marker.value] == Academic_marker.academic.value)
    ]

    staff_grouped = (
        staff_filtered.groupby(
            by=[
                Staff_cols.UKPRN.value,
            ]
        )[Staff_cols.number.value]
        .sum()
        .to_frame()
    )

    joined_df = students_grouped.join(
        staff_grouped, how="inner", lsuffix=" of students", rsuffix=" of staff"
    )

    joined_df["ratio"] = joined_df["Number of students"] / joined_df["Number of staff"]

    joined_df = joined_df.reset_index().sort_values(by="ratio", ascending=True)

    return joined_df[Staff_cols.UKPRN.value].iloc[0:5]


if __name__ == "__main__":
    main()
