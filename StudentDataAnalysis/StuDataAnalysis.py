# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 22:56:28 2018

@author: hp
"""

import numpy as np
import pandas as pd
import csv
from datetime import datetime as dt 

''' 1 从csv加载数据 '''
def readcsv_Dict(file):
    with open(file) as fid:
        reader = csv.DictReader(fid)
        return list(reader)

enrollments = readcsv_Dict("./Resources/enrollments.csv")
engagements = readcsv_Dict("./Resources/daily_engagement.csv")
submissions = readcsv_Dict("./Resources/project_submissions.csv")

print(len(enrollments),len(engagements),len(submissions))

''' 2 清洗数据 '''
# 清理 enrollments 表格中的数据类型(取消的日期,参加日期,退出的天数,是否取消,是否是Udacity测试账号)
def parse_date(date):
    if date =='':
        return None
    else:
        return dt.strptime(date, '%Y-%m-%d')

def parse_maybe_int(i):
    if i=='':
        return None
    else:
        return int(i)
    
# 清理 enrollments 表格中的数据类型(取消的日期,参加日期,退出的天数,是否取消,是否是Udacity测试账号)
for enrollment in enrollments:
    enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
    enrollment['join_date'] = parse_date(enrollment['join_date'])
    enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
    enrollment['is_canceled'] = enrollment['is_canceled'] == 'True'
    enrollment['is_udacity'] = enrollment['is_udacity'] == 'True'

# 清理 engagement 的数据类型(时间,课程数量,课程完成数量,项目完成情况,共花费多少时间)
for engagement_record in engagements:
    engagement_record['utc_date'] = parse_date(engagement_record['utc_date'])
    engagement_record['num_courses_visited'] = int(float(engagement_record['num_courses_visited']))
    engagement_record['lessons_completed'] = int(float(engagement_record['lessons_completed']))
    engagement_record['projects_completed'] = int(float(engagement_record['projects_completed']))
    engagement_record['total_minutes_visited'] = float(engagement_record['total_minutes_visited'])
    
# 清理 submissions 的数据类型(项目创建的时间,完成的时间)
for submission in submissions:
    submission['creation_date'] = parse_date(submission['creation_date'])
    submission['completion_date'] = parse_date(submission['completion_date'])

''' 3 修改数据格式 '''
# 将 daily_engagement 表中的 "acct" 重命名为 ”account_key"
for engagement_record in engagements:
    engagement_record['account_key'] = engagement_record['acct']
    del [engagement_record['acct']]
    
''' 4 探索数据 '''
## 计算每张表中的总行数，和独立学生（拥有独立的 account keys）的数量
