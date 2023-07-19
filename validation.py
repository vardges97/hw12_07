def check(*kwargs):
    def ded(func):
        def wrapper(*args,**kwargs):
            for name,type in args.item():
                if not isinstance(kwargs[name],type):
                    raise TypeError(f'{name} must have:{type}')
                return func(*args,**kwargs)
            return wrapper
        return ded()