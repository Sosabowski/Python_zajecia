import time
import functools

def measure_time(unit='seconds'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            elapsed_time = end_time - start_time
            
            if unit == 'seconds':
                print(f"Funkcja '{func.__name__}' wykonana została w czasie {elapsed_time:.6f} sekund.")
            elif unit == 'microseconds':
                elapsed_time_microseconds = elapsed_time * 1_000_000
                print(f"Funkcja '{func.__name__}' wykonana została w czasie {elapsed_time_microseconds:.6f} sekund.")
            else:
                raise ValueError("jednostka musi być albo 'seconds' albo 'microseconds'.")
                
            return result
        return wrapper
    return decorator

# Przykładowa funkcja do dekoracji
@measure_time(unit='seconds')
def example_function_seconds(n):
    total = 0
    for i in range(n):
        total += i ** 2
    return total

@measure_time(unit='microseconds')
def example_function_microseconds(n):
    total = 0
    for i in range(n):
        total += i ** 2
    return total

@measure_time(unit='nanoseconds')
def example_function_nanoseconds(n):
    total = 0
    for i in range(n):
        total += i ** 2
    return total

# Wywołanie przykładowych funkcji
print(example_function_seconds(10000))
print(example_function_microseconds(10000))
#print(example_function_nanoseconds(10000))