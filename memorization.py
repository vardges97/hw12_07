mem = {}
def memorized_fact(f):
    def inn(num):
        if num not in mem:
            mem[num]=f(num)
            print("result saved to memmory")
        else:
            print ("returning result from memory")
        return mem[num]
    return inn

@memorized_fact
def factoral(num):
    if num ==1 or num ==0:
        return 1
    else:
        return num * factoral(num-1)
