## This is main file

def squre_fun(list):
    sq_lst=[]
    for i in list:
        sq_lst.append(i**2)

    return sq_lst
list1 = [1,2,3,4,4,5,67,89,100]
sq_list=squre_fun(list1)