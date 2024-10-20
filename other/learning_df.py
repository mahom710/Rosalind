import pandas as pd

# create some sample df
data_students = {
    'StudentID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [20, 21, 19, 22]
}
students_df = pd.DataFrame(data_students)
data_grades = {
    'StudentID': [1, 2, 5],
    'Math': [85, 90, 78],
    'Science': [92, 85, 80]
}
grades_df = pd.DataFrame(data_grades)

# merge allows to merge dfs sideways
df = pd.merge(students_df, grades_df, how='outer')


# concat allows stacking of dfs
df = pd.concat([students_df,grades_df], ignore_index=True)

#lambda apply
grades_df['CombinedScores'] = grades_df.apply(lambda row: row['Math']+row['Science'], axis=1)