import re
import numpy as np
import dateparser

class Singleton(object):
    _instance = None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance

def wspex(string):
    return re.sub(u'\u200a', '', ''.join(string.split()))

def wspex_space(string):
    return re.sub(u'\u200a', '', ' '.join(str(string).split()))

def tofloat(string):
    return float(wspex(string.replace(',', '.')))

def get_parse_date_srs(date_srs):
    return date_srs.apply(lambda date_string: dateparser.parse(date_string, settings={'PREFER_DAY_OF_MONTH': 'first'}))

def percentile(n):
    def percentile_(x):
        return np.percentile(x, n)

    percentile_.__name__ = 'percentile_%s' % n
    return percentile_

def geo_mean(iterable):
    a = np.array(iterable)
    return a.prod()**(1.0/len(a))

def sum_day(wt_srs, srs):
    number = (wt_srs*srs/(wt_srs*srs.notna()).sum()).sum()
    return number