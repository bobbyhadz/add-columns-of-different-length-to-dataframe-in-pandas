# Add columns of a different Length to a DataFrame in Pandas

import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl'],
    'experience': [10, 13, 15],
})


additional_cols = pd.DataFrame({
    'salary': [1500, 1200, 2500, 3500]
})

df2 = pd.concat([df, additional_cols], axis=1)

print(df2)