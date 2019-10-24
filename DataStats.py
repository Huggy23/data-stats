"""
CPSC-51100, SUMMER 2019
NAME: JASON HUGGY
PROGRAMMING ASSIGNMENT #5
"""

import pandas as pd
pd.set_option('display.max_columns', None)

df_full = pd.read_csv('cps.csv')


# Create a new data frame with the values that need to be transferred for the 
# final product
df = df_full[['School_ID', 'Short_Name', 'Is_High_School', 'Zip', 
              'Student_Count_Total', 'College_Enrollment_Rate_School']]


# Splits the Grades_Offered_All column by commas. 
df_full['Grades_Offered_All'] = df_full.Grades_Offered_All.str.split(',')


# Returns the first and last grade in Grades_Offered_All for each school
df['Lowest_Grade_Offered'] = df_full.Grades_Offered_All.str.get(0)
df['Highest_Grade_Offered'] = df_full.Grades_Offered_All.str.get(-1)


# Removes all non-digits from the results, then removes all zeros
df_full['School_Hours'] = df_full.School_Hours.str.replace('\D', '')
df_full['School_Hours'] = df_full.School_Hours.str.replace('0', '')


# Returns the integer of the first number, which represents the starting hour
# Returned as a float to calculate column mean
df['School_Starting_Hour'] = df_full.School_Hours.str.get(0).astype(float)


# Replaces NaN values with column mean for college enrollement, but set to zero
# for starting hour to match final results
df.College_Enrollment_Rate_School.fillna(df.College_Enrollment_Rate_School.mean(), inplace = True)
df.School_Starting_Hour.fillna(0, inplace = True)


# Starting hour changed back to integer
df.School_Starting_Hour = df.School_Starting_Hour.astype(int)


# Selects all schools that are: hs = high schools, no_hs = not high schools 
hs = df[df.Is_High_School == True]
no_hs = df[df.Is_High_School == False]


df.set_index('School_ID', inplace=True)
print(df.head(10))


# Calculates the mean and standard deviation for College Enrollment Rate for 
# high schools only. Use hs.
print('College Enrollment Rate for High Schools = '+ '%.2f'%hs.College_Enrollment_Rate_School.mean() 
+ ' (sd=' + '%.2f'%hs.College_Enrollment_Rate_School.std() + ')')


# Calculates the mean and standard deviation of total student count for non-high schools only. Use no_hs.
print('Total Student Count for non-High Schools = '+ '%.2f'%no_hs.Student_Count_Total.mean() + ' (sd=' 
      + '%.2f'%no_hs.Student_Count_Total.std() + ')')


# Returns the count of each starting hour, as well as how many schools are not in the loop. Zipcodes used below are in the loop
print('Distribution of Starting Hours')
print('8am:', df[df.School_Starting_Hour == 8].School_Starting_Hour.count())
print('7am:', df[df.School_Starting_Hour == 7].School_Starting_Hour.count())
print('9am:', df[df.School_Starting_Hour == 9].School_Starting_Hour.count())
print('Number of schools outside the Loop:', len(df[(df.Zip != 60601) & (df.Zip != 60602) & (df.Zip != 60603) & 
                                                    (df.Zip != 60604) & (df.Zip != 60605) & (df.Zip != 60606) & 
                                                    (df.Zip != 60607) & (df.Zip != 60616)]))







