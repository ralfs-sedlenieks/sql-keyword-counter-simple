# SQL keyword counter

A Python script that counts the keywords in SQL queries.

## How to use

First, the keyword list must be created in the same directory as the script.
This can be done in MySQL by running the query `SELECT * FROM mysql.help_keyword;`,
dropping the ID column and storing the result in a CSV file called `keywords.csv`

A file containing 4 SQL queries is also required and must be specified using the `--targetfile` or `-f` parameter.
The queries should be separated by a line "###" and all keywords must be separated by spaces from surrounding symbols.
Both relative and absolute paths should work, but Windows paths must be in quotes.

Script can be run from the command line with the command `python sqlcompl.py --targetfile=queries.txt`
