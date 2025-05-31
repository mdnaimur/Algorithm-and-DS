MAX_SIZE = 5
top = -1

stack_array = [None] * MAX_SIZE


def push(value):
    global top
    if top >= MAX_SIZE-1:
        raise Exception("Stack overflow")
    top += 1
    stack_array[top] = value


def pop():
    global top
    if top < 0:
        raise Exception("Stack underflow: stack is empty")
    # value = stack_array[top]
    stack_array[top] = None
    # print("[DEBUG]: Inside pop", value)
    top -= 1
    # return value


def peek():
    if top < 0:
        raise Exception(" Stack underflow: no data here now")
    return stack_array[top]


push(2)
push(20)
push(22)
print(stack_array)
push(222)
push(224)
# push(33)
pop()
# pop()
print(stack_array)

print(peek())
