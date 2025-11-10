from typing import Any, Callable


def log(filename: str | None = None) -> Callable:
    def decorator(func: Callable) -> Any:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                massage = f"Функция {func.__name__} выполнена!"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(massage + "\n")
                else:
                    print(massage)
                return result
            except Exception as e:
                msg = (
                    f"Функция {func.__name__} не выполнена! Произошла ошибка {type(e).__name__}: {e},"
                    f"входные параметры: {args, kwargs}."
                )
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(msg + "\n")
                else:
                    print(massage)
                raise

        return wrapper

    return decorator
