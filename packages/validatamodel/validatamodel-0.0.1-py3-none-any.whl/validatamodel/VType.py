from vierror import MException


def v_s_not_null(value: str, name: str = ""):
    if value is None:
        raise MException("FieldVerifyError", f"字段({name})值为null")
    return value

def v_s_is_empty(value: str, name: str = ""):
    if value.strip() == "":
        raise MException("FieldVerifyError", f"字段({name})值为空")

def v_s_trim(value: str, name: str = ""):
    try:
        return value.strip()
    except Exception as e:
        raise MException("FieldVerifyError", f"字段({name})去除两端空格")

def v_s_lower(value: str, name: str = ""):
    try:
        return value.lower()
    except Exception as e:
        raise MException("FieldVerifyError", f"字段({name})转换小写失败")

def v_s_upper(value: str, name: str = ""):
    try:
        return value.upper()
    except Exception as e:
        raise MException("FieldVerifyError", f"字段({name})转换大写失败")


def v_s_len_dec(lt: int = None, gt: int = None, le: int = None, ge: int = None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs, lt=lt, gt=gt, le=le, ge=ge)
        return wrapper
    return decorator

def v_s_len(value: str, lt: int = None, gt: int = None, le: int = None, ge: int = None, name: str = ""):
    value_len = len(value)
    if not lt and value_len >= lt:
        raise MException("FieldVerifyError", f"字段({name})长度应<{lt}，但实际为{value_len}")
    if not gt and value_len <= gt:
        raise MException("FieldVerifyError", f"字段({name})长度应>{lt}，但实际为{value_len}")
    if not le and value_len > le:
        raise MException("FieldVerifyError", f"字段({name})长度应<={lt}，但实际为{value_len}")
    if not ge and value_len < ge:
        raise MException("FieldVerifyError", f"字段({name})长度应>={lt}，但实际为{value_len}")
    return value

def v_s_in_dec(enum_value: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs, enum_value=enum_value)
        return wrapper
    return decorator

def v_s_in(value: str, enum_value: list, name: str = ""):
    if value not in enum_value:
        raise MException("FieldVerifyError", f"字段({name})的可选值为{enum_value}，当前字段值为{value}")
    return value


