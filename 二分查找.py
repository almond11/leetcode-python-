#-*- coding:utf8 -*-
#author : Lenovo
#date: 2018/7/30


def  Binary_search(lis,key):
    min_num=0
    max_num=len(lis)-1  #由于列表索引为0开头
    times=0   #记录查找次数
    while(min_num<=max_num):
        times=times+1
        mid=int((min_num+max_num)/2)
        if lis[mid]<key:    #如果中间值小于查找值 说明查找值在查找表之后
            min_num=mid+1
        elif lis[mid]>key:  #此处为if则查找结果错误
            max_num=mid-1
        else:
            print('查找次数:%s'%times)
            return mid
    return False


lis=[1,5,7,9,10,15,20,78,88]
key=9
res=Binary_search(lis,key)
print(res)