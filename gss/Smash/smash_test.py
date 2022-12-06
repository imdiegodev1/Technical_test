##prime numbers 5, 7, 11, 13

def main():
    return prime_n(input())

def prime_n (n):
    
    n = int(n)

    if n%2 == 0:
        return True
    elif n%3 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    x = main()
    print(x)