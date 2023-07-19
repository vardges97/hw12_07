def log_ing(func):
    import logging
    print(func.__name__)
    logging.basicConfig(filename='logi.log',lvl = logging.info)
    def wrapper(*args,**kwargs):
        logging.info(f"ran with args:{args},and kwargs {kwargs}")
        return func(*args,**kwargs)
    return wrapper