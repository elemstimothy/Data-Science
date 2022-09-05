from functools import cache

# @cache
def main():
    
    arr = []
    for i in range(1, 16):
        while i not in arr:
            arr.append(i) 
            # dope = arr
            print(arr)
            # Because it prints the list multiple times till it's complete 
# fibonacci is a + 


if __name__ == '__main__':
    main()