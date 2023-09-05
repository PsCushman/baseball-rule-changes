SELECT bat_side, COUNT(*) as bat_side_count
FROM handedness
GROUP BY bat_side
ORDER BY bat_side;

-- "L"	93
-- "R"	139
-- "S"	23

SELECT
    bat_side,
    SUM(CASE WHEN zscore_difference_woba > 0 THEN 1 ELSE 0 END) AS count_positive_woba
FROM
    handedness
GROUP BY
    bat_side
ORDER BY
    bat_side;

-- "L"	49
-- "R"	57
-- "S"	12
	
SELECT
    bat_side,
    SUM(CASE WHEN zscore_difference_slg > 0 THEN 1 ELSE 0 END) AS count_positive_slg
FROM
    handedness
GROUP BY
    bat_side
ORDER BY
    bat_side;
	
-- "L"	46
-- "R"	61
-- "S"	13

SELECT
    bat_side,
    SUM(CASE WHEN zscore_difference_babip > 0 THEN 1 ELSE 0 END) AS count_positive_babip
FROM
    handedness
GROUP BY
    bat_side
ORDER BY
    bat_side;
	
-- "L"	53
-- "R"	56
-- "S"	13
	
SELECT
    bat_side,
    SUM(CASE WHEN zscore_difference_wrc > 0 THEN 1 ELSE 0 END) AS count_positive_wrc
FROM
    handedness
GROUP BY
    bat_side
ORDER BY
    bat_side;
	
-- "L"	48
-- "R"	59
-- "S"	11