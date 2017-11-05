# -*- coding: utf-8 -*-
"""
生成社交数据：
10个小团体
根据团体，生成相应的联系数据

并保存为json格式
@author: YZY
"""
import random
import json

initial_group=[[random.randint(1,150) for x in range(random.randint(5,10))]+[0] for y in range(10)]  #生成10个圈子
initial_group=[list(set(initial_group[y]))for y in range(10)]  #去除圈中重复项  同时，核心人物的编号为0


def p2p_date_generate(x,y):                                                    #根据两个人是否在一个圈子，生成相应的交流数据
    for i in range(10):
        if len(set([x,y])&set(initial_group[i]))==2:
            break
    else:
        return  [random.randint(0,3) for i in range(random.randint(0,12))]       #生成的数据，总长为联系时长，单位为月，数据为每月的联系天数
    return   [random.randint(1,5) for i in range(random.randint(13,20))]     #在圈子里的人，总的联系时长比较长，每月联系次数较为频繁
  
      
p2p_date=[[p2p_date_generate(y,x)  for x in range(150)]  for y in range(150)]  #生成好友的联系数据


#strang_group 生成强群组，即所有的圈子包含在群组之中，基于此，生成20个群组，前十个是以初始圈子为基础，随机添加数人，后十个是随机生成的群组
strong_group=[(initial_group[x%10]+[random.randint(1,150) for y in range(random.randint(0,10))],[random.randint(1,150) for y in range(random.randint(5,20))]+[0] )[x>9] for x in range(20)]
strong_group=[list(set(strong_group[x])) for x in range(10)]  #去除圈中重复项

#weak_group 生成弱群组，对圈子的产生有增量作用，不过此处的弱群组为纯粹的随机生成，其增量应该很不是很明显
weak_group=[[random.randint(1,150) for x in range(random.randint(5,20))]+[0] for y in range(20)]
weak_group=[list(set(weak_group[y])) for y in range(20)]  

#生成 群组的联系数据  强群组和弱群组公用一个联系数据
group_date=[[random.randint(0,3) for i in range(random.randint(0,15))]   for x in range(20)]

with open("p2p_date.json",'w',encoding='utf-8') as json_file:
         json.dump(p2p_date,json_file,ensure_ascii=False)
with open("strong_group.json",'w',encoding='utf-8') as json_file:
         json.dump(strong_group,json_file,ensure_ascii=False)

with open("weak_group.json",'w',encoding='utf-8') as json_file:
         json.dump(weak_group,json_file,ensure_ascii=False)
         
with open("group_date.json",'w',encoding='utf-8') as json_file:
         json.dump(group_date,json_file,ensure_ascii=False)

        