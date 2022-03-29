def Prime_or_Not(x):
    if x > 1:
        for i in range(2, x//2):
            if x % i == 0:
                return True
            else:
                return False

if __name__ == "__main__":

    x = int(input("Enter any Number: "))

    Prime_Not = Prime_or_Not(x)
    print(Prime_Not)