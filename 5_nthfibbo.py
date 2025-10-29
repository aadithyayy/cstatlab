def fibo(x):
    if x==1:
        return 1
    elif x==0:
        return x
    else:
        return fibo(x-2)+fibo(x-1)

n=int(input("Enter n value:"))
fi=fibo(n)
print(n,"th fibbonacci number is:",fi)