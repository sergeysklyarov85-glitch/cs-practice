import numpy as np


def make_hours() -> list[int]:
    hours_array = np.arange(0, 22, 3)
    return hours_array.tolist()


def vector_report(values: list[float]) -> dict:
    arr = np.asarray(values, dtype=float)

    third_element = float(arr[2])
    last_element = float(arr[-1])
    middle_slice = arr[2:6].tolist()
    every_second = arr[::2].tolist()
    reversed_vec = arr[::-1].tolist()

    return {
        "third": third_element,
        "last": last_element,
        "middle": middle_slice,
        "every_second": every_second,
        "reversed": reversed_vec,
    }


def change_vector(values: list[float]) -> list[float]:
    arr = np.asarray(values, dtype=float).copy()
    arr[2:5] = 99
    arr[::2] = -1
    return arr.tolist()


def cap_above(values: list[float], limit: float) -> list[float]:
    arr = np.asarray(values, dtype=float).copy()
    mask = arr > limit
    arr[mask] = limit
    return arr.tolist()


def celsius_to_fahrenheit(values: list[float]) -> list[float]:
    celsius = np.asarray(values, dtype=float)
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit.tolist()