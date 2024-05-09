def selection_a(arr):
    n=len(arr)
    for i in range(n-1):
        min_i=i
        for j in range(i+1,n):
            if arr[j]<arr[min_i]:
                min_i=j
        arr[i],arr[min_i]=arr[min_i],arr[i]
    return arr


def selection_d(arr):
    n=len(arr)
    for i in range(n-1):
        max_i=i
        for j in range(i+1,n):
            if arr[j] > arr[max_i]:
                max_i=j
        arr[i],arr[max_i]=arr[max_i],arr[i]
    return arr

def menu_driven_sort():
    print("***************selection sort**********************")
    length=int(input("enter no of elements:"))
    arr=[]
    for i in range(length):
        num=int(input("enter element:"))
        arr.append(num)

    while True:
        print("\n1.acending \n2.decending\n3.exit")
        ch=int(input("enter your choice:"))

        if ch==1:
            sel=selection_a(arr)
            print("sorted list is: ")
            print(sel)
            break
        elif ch==2:
            sel=selection_d(arr)
            print("sorted list is: ")
            print(sel)
            break
        elif ch==3:
            print("thanks")
            break
        else:
            print("invalid choice")
            return

    
menu_driven_sort()
