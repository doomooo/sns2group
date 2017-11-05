# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 16:51:36 2017
强群组下 圈子寻找
@author: YZY
"""
import json
import math
from functools import reduce

#获取数据
with open("p2p_date.json",'r',encoding='utf-8') as json_file:
         p2p_date=json.load(json_file)
         
with open("strong_group.json",'r',encoding='utf-8') as json_file:
         strong_group=json.load(json_file)

with open("weak_group.json",'r',encoding='utf-8') as json_file:
         weak_group=json.load(json_file)
     
with open("group_date.json",'r',encoding='utf-8') as json_file:
         group_date=json.load(json_file)

all_person=[x for x in range(150)]

def get_relation(date):
    relation=0;
    for i in range(len(date)):
        relation=relation*math.exp(-0.5/(5+i/12))+date[i]
    return relation

#获取两人之间的亲密度
p2p_relation=[[(get_relation(p2p_date[x][y]),0)[x==y]  for y in range(len(p2p_date))] for x in range(len(p2p_date))]

#获取前50好友
good_relation=[]
for i in range(len(p2p_date)):
    temp_relation=[[x,p2p_relation[i][x]] for x in range(len(p2p_date))]
    temp_relation.sort(key=lambda x:x[1])  
    good_relation+=[[temp_relation[len(p2p_date)-x-1][0] for x in range(50)]]

#获取圈子的亲密度阈值
temp=[p2p_relation[0][x] for x in range(len(p2p_date))]
temp.sort()
group_relation_min=temp[80]



#查询圈子
for i in range(len(strong_group)):
    for group_remove_person in range(len(strong_group[i])-5):                  #每个群组最少剩5人
        temp=[100,1000]
        for all_person_in_group in strong_group[i]:
            if all_person_in_group==0:             #跳过核心人选
                continue
            else:
                all_relation=reduce(lambda x,y:x+p2p_relation[all_person_in_group][y],strong_group[i],0)/len(strong_group[i])  #获取某人的圈子亲密度
                temp=([all_person_in_group,all_relation],temp)[temp[1]<all_relation]   
        if temp[1]>group_relation_min:
            continue
        strong_group[i].remove(temp[0])                                        #移出亲密度最低的
        
    
    
    
    
    
