def fib(n):
    if n < 1:
        return 1
    elif n == 1 :
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
def Fib_Search(arr,x):
    n = 0
    while fib(n) < len(arr):
        n = n + 1
    offset = -1
    for j in range(len(arr)):
            if type(arr[j]) == list:
                hasil_fibo = Fib_Search(arr[j],x)
                if hasil_fibo == -1:
                    arr[j] = "z"
                else:
                    print(x," ditemukan di indeks ", int(j)," pada kolom ",hasil_fibo)
                    exit()
    while (fib(n) > 1):
        i = min(offset + fib(n-2), len(arr) - 1)
        if (x > arr[i]):
            n = n-1
            offset = i
        elif (x < arr[i]):
            n = n-2
        else:
            return i
    if (fib(n-1) and arr[offset + 1] == x):
        return offset + 1
    return -1
def linearsearch(arr,x):
    for l in range(len(arr)):
        if type(arr[l]) == list:
            hasil_x = linearsearch(arr[l],x)
            if hasil_x == -1:
                return -1
            else:
                print(f'{x} ditemukan pada indeks {l} kolom {hasil_x}')
                exit()
        elif arr[l] == x:
            return l
    return -1

list_ASLAB = ['Arsel','Avivah','Daiva',['Wahyu','Wibi']]
while True:
    print(f'''
Daftar Nama ASLAB
=============
|No | Nama  |
=============
 1  Arsel 
 2  Avivah
 3  Daiva 
 4  Wahyu 
 5  Wibi  
=============
''')
    print('''
    ======================
    | 1. Linear Search   |
    | 2. Fibonacci Search|
    ======================
    ''')
    t1 = int(input("Masukan metode search yang ingin digunakan : "))
    input_nama = input("Masukan data yang ingin dicari indeksnya : ")
    if t1 == 1:
        search_linear = linearsearch(list_ASLAB,input_nama)
        if search_linear == -1:
            print(input_nama," tidak ditemukan")
        else:
            print(input_nama," ditemukan di indeks ",search_linear)
        exit()
    elif t1 == 2:
        search_fib = Fib_Search(list_ASLAB,input_nama)
        if search_fib == -1:
            print(input_nama," tidak ditemukan")
        else:
            print(input_nama," ditemukan di indeks ",search_fib)
        exit()

    else:
        print("Masukan input dengan benar")