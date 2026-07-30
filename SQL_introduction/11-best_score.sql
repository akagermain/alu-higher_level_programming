-- Lists all records with a score greater than or equal to 10

-- Retrieve the score and name of records with a score of at least 10
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
