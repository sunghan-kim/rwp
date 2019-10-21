#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pandas as pd

# 각 컬럼의 값별 빈도수 데이터프레임을 생성하는 함수 정의
def make_vc_df(df, col) :
    
    df_vc = df[col].value_counts().reset_index()
    df_vc.rename(columns={"index": "value", col: "count"}, inplace=True)
    df_vc.sort_values(by="value", inplace=True)
    
    return df_vc


# 컬럼 순서 변경 (맨뒤 -> 맨 앞)
def move_col_back_to_front(df) :
    
    cols = df.columns.tolist()
    cols = cols[-1:] + cols[:-1]

    return df[cols]


# groupby한 df를 원본 df 기준으로 정렬
def sort_col_by_origin(df_orgn, df, col_sort, col_val) :
    
    col_sort_list = df_orgn[col_sort].unique().tolist()
    col_val_list = []
    
    for i in range(len(col_sort_list)) :
        
        for j in range(len(df)) :
            
            if col_sort_list[i] == df.iloc[j,][col_sort] :
                
                col_val_list.append(df.iloc[j,][col_val])
                
    return pd.DataFrame({col_sort: col_sort_list, col_val: col_val_list})
    
    
    