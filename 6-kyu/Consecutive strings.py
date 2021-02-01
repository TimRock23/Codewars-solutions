def longest_consec(strarr, k):
    n = len(strarr)
    max_str = ''
    if n >= k > 0:
        for i in range(n-k+1):
            string = ''.join(strarr[i:i+k])
            if len(string) > len(max_str):
                max_str = string
    return max_str
