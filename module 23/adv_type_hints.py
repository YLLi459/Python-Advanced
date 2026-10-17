from  typing import Optional, List, Union, Any

from PIL.ImImagePlugin import number


def get_name(name: Optional[str] = None) -> str:
    if name:
        return name
    return "Anononymous"

print(get_name("John"))

def process_value(value: Union[int, str]) -> str:
    if isinstance(value, int):
        return f"Number: {value}"
    return f"String: {value}"

print(process_value(123))


def process_anything(value: Any) -> str:
    return f"Processed  {value}"

print(process_anything(123.1231))


def sum_list(numbers: List[int]) -> int:
    return sum(numbers)


numbers: List[int] = [1, 2, 3]
result: int = sum_list(numbers)
print(result)