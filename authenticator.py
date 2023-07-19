

def authenticate_access(func):
    def wrapfunc(*args,**kwargs):
        passwrord=input("enter password ")
        ret_val= {}
        if passwrord=="algernop":
            ret_val['password']="correct"
            ret_val['calculation']=func(*args,**kwargs)
        else:
            ret_val["pass"]="incorrect"

        return ret_val

    return wrapfunc
@authenticate_access
def func_1(input1,input2):
    res = input1+input2
    return res

print(func_1(2,3))
