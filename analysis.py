#Read CSV file -------------
import pandas as pd

csv_dataset = "film_permits.csv"

df = pd.read_csv(csv_dataset)

#---------------------------

#1. Print the first 2 rows
# print(df.head(2))
print(df.loc[[0, 1]])

#2. Print the first row
print(df.loc[0])

#3. Print rows 10–19
print(df.loc[10:20])

#4. Print column names
print(df.columns)

#5. Print the first 10 values of one column
print(df['Borough'].head(10))

#6. Print the first 10 rows of three columns
print(df[['EventID', 'EventType', 'StartDateTime']].head(10))

#-----------------------------

#7. Three Questions

# Which borough has the most film permit activity (all EventTypes included)?
borough_mode = df['Borough'].mode()
print(borough_mode)

# How many Shooting Permit events started before 10 am?
df["StartDateTime"] = pd.to_datetime(df["StartDateTime"])
early_shooting_permit_number = ((df["EventType"] == "Shooting Permit") & (df["StartDateTime"].dt.hour < 10)).sum()
print(early_shooting_permit_number)

# How many events lasted longer than 5 hours?
df["EndDateTime"] = pd.to_datetime(df["EndDateTime"], format = "mixed") #StartDateTime alr done above
df["Duration"] = (df["EndDateTime"] - df["StartDateTime"])
long_events_sum = (df["Duration"].dt.total_seconds() > (5 * 3600)).sum()
print(long_events_sum)




