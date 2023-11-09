from event_study import config as cfg

# prc_csv is the actual location of the CSV file containing TSLA prices
prc_csv = cfg.get_locs('TSLA')['prc_csv']

def fmt_colnames(df):
    d = {c:c.lower().replace(' ', '_') for c in df.cols}
    return df.rename(columns=d)

from event_study import config as cfg

# ff_csv points to the location of the `ff_daily.csv` above
ff_csv = cfg.FF_FACTORS_CSV