"""
read raw_data from files
"""

# !/usr/bin/env python
# coding=utf-8

# Read data and read tree fuctions for INFORMS data
# attributes ['age', 'workcalss', 'final_weight', 'education', 'education_num', 'matrital_status',
# 'occupation','relationship', 'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week', '
# native_country', 'class']
# QID ['age', 'workcalss', 'education', 'matrital_status', 'race', 'sex', 'native_country']
# SA ['occopation']


GL_ATT_NAMES = ['age', 'workcalss', 'final_weight', 'education',
                'education_num', 'matrital_status', 'occupation', 'relationship',
                'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week',
                'native_country', 'class']
GL_QI_INDEX = [0, 1, 3, 5, 8, 9, 13]
GL_SA_INDEX = 6

__DEBUG = False


def read_data():
    """
    read microda for *.txt and return read data
    """
    data = []
    qi_set = set(GL_QI_INDEX)
    data_file = open('data/adult.data', 'rU')
    for line in data_file:
        line = line.strip()
        if len(line) == 0:
            continue
        line = line.replace(' ', '')
        temp = line.split(',')
        ltemp = []
        for i in range(len(temp)):
            if i in qi_set:
                ltemp.append(temp[i])
        ltemp.append(temp[GL_SA_INDEX])
        data.append(ltemp)
    return data
