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

Activate venv and install requirements:
```commandline
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run the script with the path to the csv file:
```commandline
python3 main.py -f "data/dummy_meshes_with_errors.csv"
python3 main.py -f "data/dummy_meshes_correct.csv"
```

# Tests

```commandline
pytest
```

# Issues encountered

- In `test_keep_unique_codename`: having inplace=True modified the original fixture even when copied.
- List of strings in SQLite -> replaced with PickleType
- SQLite: I usually use Postgres but tried SQLite to not use a server. The issue was querying SQLite that I solved when replacing pd.to_sql with a more controlled insertion.
- Decoding `roll_pallet` read from SQLite: element returned is b'\x1e\x00\x00\x00\x00\x00\x00\x00'. L'erreur vient de `roll_pallet` qui a une valeur négative, créé une fonction dans Transformer pour y remédier.

# Improvements

- Prendre en compte tous les cas d'usage lorsqu'il y a plus de données: prendre en main les NA et mauvaises entrées pour chaque colonne...
- Utiliser Docker pour rendre le projet plus reproductible
- Tester Loader