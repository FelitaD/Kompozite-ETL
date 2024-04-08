# Kompozite technical test - Partie 1: Ingestion and validation de la donneée

# ETL Process

## Extract
The input csv file is passed as an argument to the script.
It results a pandas dataframe.

## Transform
Formatting is made with pandas as well. 
We want to match the format before it is inserted in the database.

## Load
Required fields + types are checked in the load stage by the database constraints.

# Usage

```commandline
python3 main.py -f "data/dummy_meshes_with_errors.csv"
```

# Tests

```commandline
pytest
```

# Issues encountered

In `test_keep_unique_codename`: having inplace=True modified the original fixture even when copied.
