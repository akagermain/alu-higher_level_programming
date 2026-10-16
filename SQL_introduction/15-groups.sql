-- Lists the number of records for each score in second_table

-- Count the records for each score and sort by the count in descending order
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
