str="aduhiwuetrotnoerutyiweoreqfdfg"

arr=[0]*25

for i in range (len(str)):
    arr[ord(str[i])-97]+=1

for i in range(len(arr)):
    print(chr(i+97)," -> " , arr[i])
    