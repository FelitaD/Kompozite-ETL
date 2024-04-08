# Kompozite technical test - Partie 1: Ingestion and validation de la donneée

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
