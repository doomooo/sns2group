# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 16:51:36 2017
简单SNS 圈子寻找
@author: YZY
"""
import json
import math
from functools import reduce

#获取数据
with open("p2p_date.json",'r',encoding='utf-8') as json_file:
         p2p_date=json.load(json_file)
         
with open("strang_group.json",'r',encoding='utf-8') as json_file:
         strang_group=json.load(json_file)

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
temp=[p2p_relation[0][i] for x in range(len(p2p_date))]
temp.sort()
group_relation_min=temp[80]



#查询圈子
group_set=[]
for i in range(50):
    group_set+=[set([0,good_relation[0][i]])]    #初始化圈子，即核心人与其50位好友分别组合成一个圈子                                 
    for group_person_len in range(1,16):         #根据假设，圈子最多十五人，此处开始一个一个扩充
        temp=[0,0]                           #记录下一个扩充人选的编号和总亲密度
        if group_person_len <6:           
            for group_person_i in list(set(all_person)-group_set[i]):    #扩充人选不在圈子内，且在150人之中
                for group_i in range(i):
                    group_set[i].add(group_person_i)                      
                    if group_set[i]<=group_set[group_i]:                #判断组合成的新圈子是否在之前的圈子中，是的话，则换下一个
                        group_set[i].remove(group_person_i)
                        continue
                    else:
                        group_set[i].remove(group_person_i)
                all_relation=reduce(lambda x,y:x+p2p_relation[group_person_i][y],list(group_set[i]),0)    #计算扩从人选的总亲密度
                temp=([group_person_i,all_relation],temp)[temp[1]>all_relation]            #比较亲密度值
            if temp[1]/len(group_set[i])>group_relation_min:
                group_set[i].add(temp[0])
            else:
                break
        else:
            temp_list=reduce(lambda x,y:set(x)|set(y),[good_relation[x] for x in list(group_set[i])] )  #获取所有圈子里人的 50位熟悉好友 组成扩选中心
            for group_person_i in list(temp_list-group_set[i]):
                for group_i in range(i):
                    group_set[i].add(group_person_i)
                    if group_set[i]<=group_set[group_i]:
                        group_set[i].remove(group_person_i)
                        continue
                    else:
                        group_set[i].remove(group_person_i)
                all_relation=reduce(lambda x,y:x+p2p_relation[group_person_i][y],list(group_set[i]),0)
                temp=([group_person_i,all_relation],temp)[temp[1]>all_relation]
            if temp[1]/len(group_set[i])>group_relation_min:
                group_set[i].add(temp[0])
            else:
                break
            
            
        

