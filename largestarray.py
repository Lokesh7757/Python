def largest(array,n):
    ans = max(array)
    return ans;

if __name__ == '__main__':
    array = [10,56,89,70,56.33]
    n = len(array)
    print("largest Number is:",largest(array,n))