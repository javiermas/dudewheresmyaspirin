# Dude where's my aspirin
'test'
For development purposes, install the package via:

```
pip install -e .
```

After that, you should be able to import it with the usual:

```
import aspirin
```


## Instructions for sharing features

Every feature should be placed in a separate file, it should consist of a main function (and subfunctions if needed) that takes a pandas DataFrame indexed by [INDEX] and return a pandas DataFrame with the same index and only the feature columns.
E.g.:
File lagged_readings.py:
```
def lagged_readings(data, lags):
    for i in range(1, lags):
      features = do lags
  
    return features
```

Every preprocessor should be placed in a separate file, it should consist of a main function (and subfunctions if needed) that takes a pandas DataFrame indexed by [INDEX] and return THE SAME DataFrame with the corresponding modifications.
E.g.:
File fill_missing_values.py:
```
def fill_missing_values(data):
    data = do filling
    return data
```

To understand how these function will be used, check the pipeline:

https://github.com/javiermas/dudewheresmyaspirin/blob/master/aspirin/jobs/pipeline.py

The pipeline receives a dataframe, a list of preprocessor functions and a list of feature functions and applies the first ones, overwriting the input dataframe and the second ones, by appending their output to a list that then gets combined into a single feature dataframe. 


Please make sure to put the file in the features folder.

