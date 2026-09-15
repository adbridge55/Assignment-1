# Assignment-1

# Film Permits (Updated September 2026) -- Three Data Questions + Why I Chose This Dataset?

## Why I Chose This Dataset?
I chose this dataset because I wanted to work with a dataset of real
data that is relevant to me. I've lived in NYC my whole life and I've witnessed
a lot of film events so I thought this would be a nice opportunity to learn a bit
more about them since they happen so often. The dataset also met all 
the assignment requirements without the csv file being too large for my 
computer to comfortably download.

## Three Data Questions

# Question: Which borough has the most film permit activity (all EventTypes included)?
# output: Manhattan
Why the data structure supports this question:
The data is organized in a two dimensional tabular structure (dataframe):
a table with rows and columns. Each row is an event and the Borough
column in that row stores what Borough the event was in; going through
the entire Borough column provides a Borough corresponding to each event. 
Pandas has a .mode() function which can easily find which borough appears the 
most often in the Borough column (answering the question "Which borough has 
the most film permit activity?").

# Question: How many Shooting Permit events started before 10 am?
# output: 12247
Why the data structure supports this question:
Events with both "Shooting Permit" in their EventType column
and a time before 10 am in their StartDateType column are the shooting
permit events that started before 10 am. We are able to combine conditions
in the data structure, filtering for events that meet both the "Shooting Permit" 
and before 10 am conditions, allowing us to answer the question. Additionally
the Pandas dataframe supports the Pandas'datatype DateTime which is helpful
for coding the second condition because it lets us use the .dt accessor .dt.hour.

# Question: How many events had a listed duration of longer than 5 hours?
# output: 18235
Why the data structure supports this question:
We are provided with both the start and end times of the events,
by subtracting the start time from the end time we get the length 
of the event. The data structure allows us to perform this subtraction
(and other math operations between quantitative columns) between columns
Counting the events that have a length of longer than 5 hours gives us
the answer to "How many events lhad a listed duration of longer than 5 hours?".

What the Data Cannot Answer

A question I might want to answer is: "What events are part of the same project?" For example, one 
film project might require both a Rigging Permit and a Shooting Permit (two separate events). This
dataset cannot answer the question because it does not provide a category about larger projects. It 
cannot tell us anything about the relationship between events. The data also doesn't have any information
on the content of the things being shot or the sucess of the event. An assumption that would be misleading 
is assuming that these events were successful or that every event occured, the data provides information 
about permits for activity but nothing about the actual event.
