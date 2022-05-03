def recursive_nth_fibo(cislo_prvku):
    if cislo_prvku == 0:
        return 0
    elif cislo_prvku == 1:
        return 1
    else:
        return recursive_nth_fibo(cislo_prvku - 1) + recursive_nth_fibo(cislo_prvku-2)









def main():
    cislo_prvku = int(input("Zadej čislo pozice hledaného prvku: "))
    print(recursive_nth_fibo(cislo_prvku))


if __name__ == "__main__":
    main()
