#__1________________________________________
from functools import wraps

def is_admin(func):
    @wraps(func)
    def wrapper(user_type):
        try:
            if user_type == 'admin':
                return func(user_type)
            else:
                raise ValueError("ValueError: Permission denied")
        except ValueError as e:
            return str(e)
    return wrapper

@is_admin
def show_customer_receipt(user_type: str):
    """
    >>> show_customer_receipt(user_type='user')
    'ValueError: Permission denied'
    >>> show_customer_receipt(user_type='admin')
    SOME VERY DANGEROUS OPERATION
    """
    string = "Some very dangerous operation"
    print(string.upper())

#__2_________________________________________

def catch_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except KeyError:
            print(f"Found 1 error during execution of your function: KeyError no such key")
    return wrapper

@catch_errors
def some_function_with_risky_operation(data):
    """
    >>> some_function_with_risky_operation({'foo': 'bar'})
    Found 1 error during execution of your function: KeyError no such key
    >>> some_function_with_risky_operation({'key': 'bar'})
    bar
    """
    print(data['key'])


#__3_______________________________________________________

def check_types(*types):
    def decorator(func):
        def wrapper(*args, **kwargs):
   
                arguments = [*args]
                arguments.append(kwargs.items())
                value = func(*args,**kwargs)
                Error = ""
                last_type_el = len(types)-1
                    
                for i in range(last_type_el):
                    if not isinstance(arguments[i], types[i]):
                        Error += f"TypeError: Argument {arguments[i]} must be {types[i]}, not {type(arguments[i])}!\n"

                if not isinstance(value, types[last_type_el]):
                        Error += f"TypeError: Returned value {value} must be {types[last_type_el]}, not {type(arguments[i])}!" 
                
                if Error != "":
                    return TypeError(Error)
                return value

        return wrapper
    return decorator

@check_types(int, int, int)
def add(a: int, b: int) -> int:
    return (a + b)

print(add("1", "2"))

"""
####### How can I use it?

def func_ann(func):
    annotation = list(func.__annotations__.values())
    return annotation
"""
#__4___________________________________________

dict_cashe = {}

def cashe(func):
    def wrapper(*args):
        arguments = (args)
        if arguments in dict_cashe.keys():
            print("Value from cashe")
            return dict_cashe[arguments]
        dict_cashe[arguments] = func(*args)
        print("Result function execution")
        return func(*args)
    return wrapper


#__5____________________________________________

from datetime import datetime, timedelta
import time

def rate_limiter(time_now, num_times):
    def decorator(func):
        def wrapper():

            t = time_now+timedelta(seconds=60)
            n_t = 0       

            while t > datetime.now() and n_t <= num_times:

                result = func()
                n_t += 1
            
                if n_t == num_times and t > datetime.now():
                    n_t = 0
                    print(f"Wait for {(t-datetime.now()).total_seconds()} seconds. You have maximum {num_times} calls per minute")
                    
                    time.sleep((t-datetime.now()).total_seconds())
                    t = datetime.now()+timedelta(seconds=60)
                    print(t)
                
            return result

        return wrapper
    return decorator


@cashe
def factorial(n: int) -> int:
    f = 1
    for i in range(1, n+1):
        f *= i
    return f



@rate_limiter(datetime.now(),num_times = 10)
def call_factorial():
    try:
        n = int(input("Enter n: "))
        if n >= 0:
            print(factorial(n))
        else:
            raise ValueError("Enter n > 0")
    except ValueError as e:
        print(e)


call_factorial()






if __name__ == "__main__":
    import doctest
    doctest.testmod()



