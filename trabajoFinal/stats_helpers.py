import pandas as pd
def iqr(series:pd.Series) -> pd.Series:
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75) 
    iqr = q3 - q1
    lower_lim = q1 - 1.5 * iqr
    upper_lim =  q3 + 1.5 * iqr
    return series.apply(lambda value: (value > lower_lim) and (value < upper_lim))
