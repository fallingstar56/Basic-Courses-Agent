"""安全的 Python 代码执行工具（含 sympy）。"""
import io
import sys
import traceback
import multiprocessing
from typing import Tuple


def _execute_code(code: str, result_queue: multiprocessing.Queue) -> None:
    def safe_import(name, globals=None, locals=None, fromlist=(), level=0):
        root_name = name.split(".", 1)[0]
        if root_name in {"math", "sympy"}:
            return __import__(name, globals, locals, fromlist, level)
        raise ImportError(f"禁止导入模块: {name}")

    safe_globals = {
        "__builtins__": {
            "__import__": safe_import,
            "print": print,
            "abs": abs,
            "min": min,
            "max": max,
            "pow": pow,
            "round": round,
            "len": len,
            "range": range,
            "int": int,
            "float": float,
            "str": str,
            "list": list,
            "tuple": tuple,
            "dict": dict,
            "set": set,
            "bool": bool,
            "complex": complex,
            "sum": sum,
            "True": True,
            "False": False,
            "None": None,
            "enumerate": enumerate,
            "zip": zip,
            "sorted": sorted,
            "reversed": reversed,
            "map": map,
            "filter": filter,
            "all": all,
            "any": any,
            "repr": repr,
            "Exception": Exception,
            "ValueError": ValueError,
            "ZeroDivisionError": ZeroDivisionError,
        },
    }
    # 添加安全 math 函数
    import math
    safe_math = {name: getattr(math, name) for name in [
        "sqrt", "sin", "cos", "tan", "asin", "acos", "atan", "atan2",
        "exp", "log", "log10", "pi", "e", "factorial", "gamma", "erf",
        "erfc", "inf", "nan"
    ]}
    safe_globals["math"] = type("math", (object,), safe_math)
    safe_globals["__builtins__"].update(safe_math)

    # 导入 sympy 供符号计算（白名单已限制危险操作）
    try:
        import sympy
        safe_globals["sympy"] = sympy
    except ImportError:
        pass

    old_stdout = sys.stdout
    old_stderr = sys.stderr
    sys.stdout = io.StringIO()
    sys.stderr = io.StringIO()
    try:
        exec(code, safe_globals, safe_globals)
        output = sys.stdout.getvalue()
        error = sys.stderr.getvalue()
        result_queue.put((output, error))
    except Exception:
        result_queue.put(("", traceback.format_exc()))
    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr


def run_python_code(code: str, timeout: int = 5) -> Tuple[str, str]:
    result_queue: multiprocessing.Queue = multiprocessing.Queue(maxsize=1)
    p = multiprocessing.Process(target=_execute_code, args=(code, result_queue))
    p.start()
    p.join(timeout=timeout)
    if p.is_alive():
        p.terminate()
        p.join()
        return "", "代码执行超时，已强制终止。"
    if not result_queue.empty():
        return result_queue.get()
    return "", "代码执行进程未返回结果。"
