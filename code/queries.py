# PROBLEM 1
# How many rows are in the 2009 dataset?
# Return a single column called "count" with a single row containing the count.
query_1 = """
select count(*) from "pls_fy2009_pupld09a"
    """

# PROBLEM 2
# How many rows are in the 2014 dataset?
# Return a single column called "count" with a single row containing the count.
query_2 = """
select count(*) from pls_fy2014_pupld14a pfpa 
"""

# PROBLEM 3
# What are the maximum and minimum values for visits for the 2014 dataset?
# Return a two columns called "max" and "man" with a single row containing the respective values

query_3 = """
select max("visits"), min("visits") from pls_fy2014_pupld14a pfpa 

"""

# PROBLEM 4
# Find the total number of visits in each state for the 2014 dataset. Be careful about invalid values.
# Return a two columns called "stabr" and "visits" with rows in descending order of visits.

query_4 = """
select "stabr", sum("visits") "visits"
from pls_fy2014_pupld14a pfpa 
group by "stabr"
order by sum("visits") desc

"""

# PROBLEM 5
# Find the difference in total visits from 2009 to 2014.
# Return a single column called "change_in_visits" with a single row containing the total.

query_5 = """
select ((select sum(visits) 
from "pls_fy2014_pupld14a" where visits >= 0) - 
(select sum("visits") from "pls_fy2009_pupld09a"
where visits >= 0)) "change_in_visits"
"""

# PROBLEM 6
# Find the difference in total visits from 2009 to 2014 for libraries (fscskey) in both dataset.
# Return a single column called "change_in_visits" with a single row containing the total.

query_6 = """
select (sum(pfpa2.visits) - sum(pfpa.visits)) as change_in_visits
from pls_fy2014_pupld14a pfpa inner join pls_fy2009_pupld09a pfpa2 
on pfpa.fscskey = pfpa2.fscskey where pfpa.visits >= 0 and
pfpa2.visits  >= 0
"""
