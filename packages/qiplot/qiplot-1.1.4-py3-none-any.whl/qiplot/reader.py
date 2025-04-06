import sys, os, re, string
import numpy as np
from glob import glob
import traceback
import logging
from logging.config import fileConfig

dname = glob(os.path.dirname(__file__))[0]
cfgname = dname + '/logconf.py'
fileConfig(cfgname)


class colfile:
    def __init__(self, x, y, e, arr):
        self.x = x
        self.y = y
        self.e = e
        self.arr = arr



def fromstring(s):
    ## check for letters other than e/E
    abpattern = '[a-df-zA-DF-Z:;=]+'
    if len(re.findall(abpattern, s)) > 0:
        return s, 0
    ## check for numbers including scientific notation
    numpattern = '[+\-]?[^A-Za-z]?(?:[0-9]\d*)?(?:\.\d*)?(?:[eE][+\-]?\d+)?'
    pts = re.findall(numpattern, s)
    out = []
    ## return the floats and skip empty lines
    for i in pts:
        try:
            out.append(float(i))
        except ValueError:
            pass
    if len(out) > 0:
        logging.debug('%s ok' %s)
        return out, 1
    else:
        logging.debug('%s fail' %s)
        return s, 0


def linecheck(fname, maxbytes=-1):
    """
    Separates header lines from data lines
    """
    datalines = []
    headerlines = []
    with open(fname, 'r') as f:
#        lines = [l.replace('\r\n', '\n').replace('\r', '\n').strip() for l in f.readlines(maxbytes)]
        lines = [l.strip() for l in f.readlines(maxbytes)]
    for n, line in enumerate(lines):
        cols, numeric = fromstring(line)
        logging.debug('(%-3d %-5s) %s', n, bool(numeric), cols)
        if numeric == 1:
            datalines.append(cols)
        else:
            headerlines.append(f'{n}: {line}')
    logging.debug('end of loop')
    ### find ncols
    n2 = [len(i) for i in datalines].count(2)
    n3 = [len(i) for i in datalines].count(3)
    if n2 > n3:
        datalines = [i for i in datalines if len(i)==2]
    elif n3 > n2:
        datalines = [i for i in datalines if len(i)==3]
    else:
        logging.warning('Something is wrong: same number of lines with 2 or 3 values')
        pass
    logging.debug('Accepted %d lines out of %d', len(datalines), len(lines))
    return datalines, headerlines



def fromcols(fname, usecols=None, maxbytes=-1):
    """
    Assign columns to values read from lines using linecheck()
    """
    data, header = linecheck(fname, maxbytes)
    dar = np.array(data).T
    logging.debug(f'data array shape: {dar.shape}')
    ### find X
    if usecols is None:
        logging.debug('Argument --usecols not specified. Using default columns x=0, y=1, e=2 (if found)')
        x = dar[0]
        y = dar[1]
        try:
            e = dar[2]
        except:
            e = np.zeros(y.shape)
            logging.debug('no third column')
    elif len(usecols) == 2:
        x = dar[usecols[0]]
        y = dar[usecols[1]]
        e = np.zeros(y.shape)
    elif len(usecols) == 3:
        x = dar[usecols[0]]
        y = dar[usecols[1]]
        try:
            e = dar[usecols[2]]
        except Exception as err:
            print(traceback.format_exc())
            e = np.zeros(y.shape)
    return data, header, colfile(x, y, e, dar)



def get_xye(argfiles, usecols, maxbytes, label):
    argfiles = [glob(f'{arg}') for arg in argfiles  ]
    argfiles = sorted(set([j for i in argfiles for j in i]))
    names, data = [], []
    for ind, f in enumerate(argfiles):
        print(f'{ind:<4d}. {f}', end=': ')
        if os.path.isfile(f) is False:
            print('no file')
        else:
            try:
                cf = fromcols(f, usecols, maxbytes)[-1]
                print(f'{len(cf.x)} points')
                data.append([cf.x, cf.y, cf.e])
                if '/' in f:
                    sep = '/'
                elif '\\' in f:
                    sep = '\\'
                else:
                    sep = '\\'
                if label == 'index':
                    names.append(f.split(sep)[-1].split('.')[0].split('_')[-1])
                elif label == 'prefix':
                    names.append(f.split(sep)[-1].split('.')[0])
                elif label == 'dir':
                    names.append('/'.join(os.path.abspath(f).split(sep)[-2:]).split('.')[0])
                elif label == 'full':
                    names.append(os.path.abspath(f))
            except Exception as err:
                print(traceback.format_exc())
                print(err)
                continue
    return data, names
