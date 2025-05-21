# print(type(l))
# print(l[3])
# print(l[::-1])
# l.insert(2,8)
# print(l)
# l[2]=8
# print(l)
# l.append(3)
# print(l)
# print(l.count(2))
# print(len(l))
# l.extend([8,9])
# print(l)
# l.pop()
# print(l)
# print(max(l))
# print(min(l))
# l.sort()
# print(l)
# l.sort(reverse=True)
# print(l)
# l.reverse()
# print(l)
# l2=l.copy()
# print(l2)

# f=lambda x: x**2
# print(f(2))

# l=[1,2,4,5,7,2]
# 
# f= list(filter(lambda x: x%2==0,l))
# print(f)

# f =list( map(lambda x : x+1 ,l))
# print(f)

# from functools import reduce

# l=[1,2,4,5,7,2]

# f=(reduce(lambda x,y: x+y,l))
# print(f)

# l = ['YES' if i%2==0 else 'NO' for i in l]
# print(l)

# l=[x for x in l if x%2==0]
# print(l)

# a=[1,2,3,2,3,4,4]
# # output= {1:1,2:2,3:2,4:2}
# dict={}
# for i in a:
#     if i in dict:
#         dict[i]  += 1
    
#     else:
#         dict[i] = 1

# print(dict)

# lst=[1,2,3,4,1,4,3,5]
# l=[]
# for i in lst:
#     if i not in l:
#         l.append(i)
# print(l)


# l=[1,2,3,4,5,6]
# l2=[4,5,6,7,8]
# o/p=misiing value in l:[7,8]
# op=additional value in l1:[1,2,3]
# op=missing value in l2:[1,2,3]
# op=additional value in l2:[7,8]
# l3=[]
# for val in l2:
#     if val not in l:
#         l3.append(val)
# print(f"additional value in {l3}")

# arr1=[1,5,10,20,40,80]
# arr2=[6,7,20,80,100]
# arr3=[3,4,15,20,30,70,80,120]
# op=[80,20]


# test_tuple=([5,6],[6,7,8,9],[3])
# # output::::(5,6,6,7,8,9,3)
# lst=list(test_tuple)
# print(lst)
# t=[]
# for val in lst:
#     t.extend(val)
# print(t)

# result=tuple(t)
# print(result)

# l=(1,2,3,4,5,6)
# print(type(l))
# print(l[2])
# print(l[0:3])
# print(len(l))
# print(max(l))
# print(min(l))
# print(l.count(2))

# tuple1=(10,2,3,5)
# tuple2=(3,6,4,3)
# # output:: (1000,64,81,125)
# l1=list(tuple1)
# l2=list(tuple2)
# print(l1,l2)
# result=[]
# for i in range(len(l1)):
#     # if i==range(len(l2)) :
#     # print(i)
#     result.append(l1[i]**l2[i])
# print(result)
# final_output=tuple(result)
# print(final_output)
        
# s={1,2,4,5,6,9,6}
# print((s))
# s.add(0)
# print(s)
# s.update(["shital","prashant"],"mn")
# print(s)
# l={5,8}
# print(l | s)
# s.remove(6)
# s.pop()
# print(s)

# d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
# print(type(d))
# print(d.get(1))
# d[1]={12:"hgjh"}
# print(d.keys())
# print(d.values())
# print(d.items())
# d1=({4:"ghj",6:"fghj"})
# final_output={**d,**d1}
# print(final_output)
# d.popitem()
# print(d)


# log={"mahesh":500,"ramesh":400,"mithilesh":400,"sumesh":300,"Jagmohan":1000,"rampyare":800}
# TOtal Labour cost if working day was 50
# out of which mahesh was absent for three days and jagmohan was absent 7 days
# FIND OUT the the total labour cost:
# 

# Input:- Programming Aasan Hai
# Output:- pROGRAMMING aASAN hAI     
# s="Programming Aasan Hai"
# print(s.swapcase())


