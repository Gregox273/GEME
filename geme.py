import numpy as np

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
    start_x, start_y = window_start - min_x, window_start - min_y
    end_x, end_y = start_x + window_width, start_y + window_width
    index_x = (start_x, end_x)
    index_y = (start_y, end_y)
    return index_x, index_y
