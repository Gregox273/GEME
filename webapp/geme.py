import numpy as np
import os
from pandas import DataFrame, read_csv

OVERLAP_THRESHOLD = 12

def normalise(x):
    return (x - x.mean())/x.std()

def norm_correlate(x,y):
    norm_x, norm_y = normalise(x), normalise(y)
    mag_x, mag_y = np.linalg.norm(norm_x), np.linalg.norm(norm_y)
    return np.correlate(norm_x, norm_y)/(mag_x*mag_y)

def month_to_int(s):
    n = list(map(int, s.split("-")))
    return 12*n[0] + n[1]-1

def get_start_end(df):
    start = list(df['Month'])[0]
    end = list(df['Month'])[-1]
    start = month_to_int(start)
    end = month_to_int(end)
    return start, end

def get_time_window(dfx, dfy):
    min_x, max_x = get_start_end(dfx)
    min_y, max_y = get_start_end(dfy)
    window_start = max(min_x, min_y)
    window_end = min(max_x, max_y)
    window_width = window_end-window_start
    if window_width < OVERLAP_THRESHOLD:
        return False
    start_x, start_y = window_start - min_x, window_start - min_y
    end_x, end_y = start_x + window_width, start_y + window_width
    index_x = (start_x, end_x)
    index_y = (start_y, end_y)
    return index_x, index_y

def overlap_dataframes(dfx, dfy):
    if not get_time_window(dfx, dfy):
        return False
    range_x, range_y = get_time_window(dfx, dfy)
    data_x = dfx.iloc[range_x[0]:range_x[1]]
    data_y = dfy.iloc[range_y[0]:range_y[1]]
    return data_x, data_y

def compare_datasets(dfx, dfy): #TODO need error handling if no overlap
    if not overlap_dataframes(dfx, dfy):
        return None
    data_x, data_y = overlap_dataframes(dfx, dfy)
    vals_x = data_x.iloc[:,1]
    vals_y = data_y.iloc[:,1]
    r = norm_correlate(vals_x, vals_y)
    return r, data_x, data_y

def month_to_string(s):
    n = list(map(int, s.split("-")))
    mon_str = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"][n[1]-1]
    year_str = str(n[0])[2:]
    return mon_str+year_str

def read_data_frame(s):
    return read_csv(s)

def get_available_datasets():
    is_visible = lambda filename: not filename.startswith('.')
    return list(filter(is_visible, os.listdir('../datasets/time')))

def correct_path(filename):
    return r'../datasets/time/' + filename
    
def compare_to_all(filename):
    # get filenames 
    all_files = get_available_datasets()
    all_files.remove(filename)
    # create paths
    filename = correct_path(filename)
    all_files = list(map(correct_path, all_files))
    # read dataframes
    target_df = read_csv(filename)
    compare_df = list(map(read_csv, all_files))
    # compare target frame to all others
    compare_func = lambda df: compare_datasets(target_df, df)
    comparison = list(map(compare_func, compare_df))
    # remove invalid comparisons
    comparison = list(filter(lambda c: c!=None, comparison))
    # sort by correlation, take top four
    comparison.sort(key = lambda tup: tup[0], reverse=True)
    best_fits = comparison[0:4]
    # pad list if necessary
    if len(best_fits) < 4:
        best_fits = best_fits + [None]*(4-len(a))
    return best_fits
