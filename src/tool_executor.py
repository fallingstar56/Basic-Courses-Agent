"""安全的 Python 代码执行工具。"""

import io
import sys
import traceback
import multiprocessing
from typing import Tuple

def _execute_code(code: str, return_dict: dict) -> None:
    """在受限命名空间中执行代码，并将 stdout/stderr 写入 return_dict。"""
    # 受限的全局命名空间
    safe_globals = {
        "__builtins__": {
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
            "Exception": Exception,
        },
    }
    # 额外的数学函数（避免导入 math 模块，直接提供常用函数）
    import math
    safe_math = {
        "sqrt": math.sqrt,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "asin": math.asin,
        "acos": math.acos,
        "atan": math.atan,
        "atan2": math.atan2,
        "exp": math.exp,
        "log": math.log,
        "log10": math.log10,
        "pi": math.pi,
        "e": math.e,
        "factorial": math.factorial,
        "gamma": math.gamma,
        "erf": math.erf,
        "erfc": math.erfc,
        "inf": math.inf,
        "nan": math.nan,
    }
    safe_globals["math"] = type("math", (object,), safe_math)
    safe_globals["__builtins__"].update(safe_math)

    old_stdout = sys.stdout
    old_stderr = sys.stderr
    sys.stdout = io.StringIO()
    sys.stderr = io.StringIO()
    try:
        exec(code, safe_globals, {})   # 局部命名空间为空
        output = sys.stdout.getvalue()
        error = sys.stderr.getvalue()
        return_dict["stdout"] = output
        return_dict["stderr"] = error
    except Exception:
        return_dict["stdout"] = ""
        return_dict["stderr"] = traceback.format_exc()
    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr

def run_python_code(code: str, timeout: int = 5) -> Tuple[str, str]:
    """在子进程中运行代码，超时强制结束。"""
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    p = multiprocessing.Process(target=_execute_code, args=(code, return_dict))
    p.start()
    p.join(timeout=timeout)
    if p.is_alive():
        p.terminate()
        p.join()
        return ("", "代码执行超时，已强制终止。")
    return return_dict.get("stdout", ""), return_dict.get("stderr", "")