def find_maxima(x):
    """Find local maxima of x.

    Input arguments:
    x -- 1D list of real numbers

    Output:
    idx -- list of indices of the local maxima in x
    """
    
    return [i for i, y in enumerate(x) if x[i-1]<=y and x[i+1]<=y]

