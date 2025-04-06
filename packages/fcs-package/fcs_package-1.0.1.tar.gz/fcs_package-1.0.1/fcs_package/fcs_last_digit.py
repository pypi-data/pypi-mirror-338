import pandas as pd
from fcs_package import fcs_square

def last_digit_of_squares(n):
    df = pd.DataFrame({'square': fcs_square.generate_squares(n)})
    df['last_digit'] = df['square'] % 10
    return df.groupby('last_digit').count().to_dict()['square']
