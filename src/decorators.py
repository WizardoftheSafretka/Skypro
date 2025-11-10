from typing import Callable, Any

def log(filename: str | None = None) -> Callable:
    def decorator(func: Callable) -> Any:
        def wrapper(*args, **kwargs) -> Any:
            try:
                result = func(*args, **kwargs)
                massage = f"Функция {func.__name__}выполнена!"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(massage + "\n")
                else:
                    print(massage)
                return result
            except Exception as e:
                massage = (f"Функция {func.__name__} невыполнена! Произошла ошибка {type(e).__name__}: {e}", f"входные параметры: {args, kwargs}.")
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(massage + "\n")
                else:
                     print(massage)
        return wrapper
    return decorator