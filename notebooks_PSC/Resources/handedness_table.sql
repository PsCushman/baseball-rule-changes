DROP TABLE IF EXISTS handedness;

CREATE TABLE handedness (
    bat_side VARCHAR(2),
    IDfg INT PRIMARY KEY,
    Name VARCHAR(255),
	zscore_difference_woba FLOAT, 
	zscore_difference_slg FLOAT,
	zscore_difference_babip FLOAT, 
	zscore_difference_wrc FLOAT
);
