import functools
from datetime import datetime
from typing import Callable, Any, Optional, TypeVar, Tuple, Dict

T = TypeVar('T')


def log(filename: Optional[str] = None) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """
    Декоратор для логирования выполнения функций.

    Args:
        filename: Если указан, логи пишутся в файл, иначе - в консоль

    Returns:
        Декорированную функцию с логированием
    """

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @functools.wraps(func)
        def wrapper(*args: Tuple[Any, ...], **kwargs: Dict[str, Any]) -> T:
            start_time = datetime.now()
            func_name = func.__name__
            log_message = ""

            try:
                result = func(*args, **kwargs)
                end_time = datetime.now()
                execution_time = (end_time - start_time).total_seconds()

                log_message = (
                    f"{func_name} ok | Execution time: {execution_time:.4f}s | "
                    f"Result: {result} | Inputs: {args}, {kwargs}"
                )
                return result
            except Exception as e:
                end_time = datetime.now()
                execution_time = (end_time - start_time).total_seconds()

                log_message = (
                    f"{func_name} error: {type(e).__name__} | "
                    f"Execution time: {execution_time:.4f}s | "
                    f"Inputs: {args}, {kwargs} | Error: {str(e)}"
                )
                raise
            finally:
                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(f"{datetime.now()} | {log_message}\n")
                else:
                    print(f"{datetime.now()} | {log_message}")

        return wrapper

    return decorator
