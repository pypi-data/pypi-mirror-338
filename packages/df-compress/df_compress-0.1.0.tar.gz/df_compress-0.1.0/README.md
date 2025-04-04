# df-compress
A python package to compress pandas DataFrames akin to Stata's `compress` command. This function may proove particularly helpfull if you are dealing with large datasets.

## How to use
After installing the package use the following import: 
```
from df-compress.compress import compress
```

## Example
It follows a reproducible example on `df-compress` usage:
```python
from df_compress import compress
import pandas as pd
import numpy as np

df = pd.DataFrame(columns=["Year","State","Value"])
df.Year = np.random.randint(low=2000,high=2023,size=200).astype(str)
df.State = np.random.choice(['RJ','SP','ES','MT'],size=200)
df.Value= np.random.rand(200,1)

df = compress(df, show_conversions=True)
```
Which will print for you the transformations and memory saved:
```
Initial memory usage: 0.02 MB
Final memory usage: 0.00 MB
Memory reduced by: 0.02 MB (91.5%)

Variable type conversions:
column    from       to  memory saved (MB)
  Year  object    int16           0.009727
 State  object category           0.009178
 Value float64  float32           0.000763
```
## Optional Parameters
The function has three optimal parameters (arguments):
  - `convert_strings` (bool): Whether to attempt to parse object columns as numbers
    - defaults to `True`
  - `numeric_threshold` (float): Indicates the proportion of valid numeric entries needed to convert a string to numeric
    - defaults to `0.999`   
  - show_conversions (bool): whether to report the changes made column by column
    - defaults to `False`

