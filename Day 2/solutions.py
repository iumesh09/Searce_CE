"""Problem on Maximum element"""

if  __name__ == "__main__":

    stack = []

    #Input
    for i in range(int(input())):
        q = list(map(int, input().split()))


        #It will push the element into stack
        if q[0] == 1:
            if stack:
                stack.append(max(stack[-1], q[1]))
            else:
                stack.append(q[1])

        # It will delete the element10
        elif q[0] == 2:
            stack.pop()

        # It will print the Maximum element in the stack
        else:
            print(stack[-1])