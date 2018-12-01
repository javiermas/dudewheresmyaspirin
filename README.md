__Hola__

For development purposes, install the package via:

```
pip install -e .
```

After that, you should be able to import it with the usual:

```
import aspirin
```


#Instructions for sharing features

Every feature should be placed in a separate file, it should consist of a main function (and subfunctions if needed) that takes a pandas DataFrame indexed by [INDEX] and return a pandas DataFrame with the same index and only the feature columns.
E.g.:
File lagged_readings.py:
```
def lagged_readings(data, lags):
  for i in range(1, lags):
    features = do lags
  
  return features
```


Please make sure to put the file in the features folder.

