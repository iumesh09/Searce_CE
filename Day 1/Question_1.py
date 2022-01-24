"""Program to print Array Elements in Reverse Order"""

def reverse(lst):
    """Reverse function which is used to Reverse agiven array"""
    for i in range(len(lst)-1,-1,-1):
        print(lst[i], end=" ") 

if __name__ == "__main__":
    #Integer, Q, which represents the number of integers in P
    Q = int(input())
    #P is made up of Q space-separated numbers on the second line
    P = list(map(int,input().strip().split()))[:Q]
    reverse(P)
    