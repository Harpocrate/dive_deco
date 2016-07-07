#  -*- coding: utf-8 -*-
# ######################
# ###### M-VALUES ######
# ######################

import numpy as np


def load_m_values():
    m_val_raw = np.genfromtxt('mvalues.csv', delimiter=';', dtype=np.float64)   # read file
    m_val = np.arange(m_val_raw.size, dtype=np.float64).reshape([2, 16, 3])     # init var
    m_val[0, :, :] = m_val_raw[:, 0:3]      # load data into var
    m_val[1, :, :] = m_val_raw[:, 3:6]
    return m_val
