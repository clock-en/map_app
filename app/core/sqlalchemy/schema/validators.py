from typing import Union


def not_blank(label: str, value: Union[str, int, float]):
    if not value:
        raise ValueError('{}を入力してください'.format(label))


def valid_length(label: str, value: str, min: int = None, max: int = None):
    if (max is None) and (min is not None) and (len(value) < min):
        raise ValueError(
            '{}は{}文字以上で入力してください'.format(label, min))
    if (min is None) and (max is not None) and (max < len(value)):
        raise ValueError(
            '{}は{}文字以内で入力してください'.format(label, max))
    if ((min is not None) and (max is not None)
            and (len(value) < min or max < len(value))):
        raise ValueError(
            '{}は{}文字以上、{}文字以内で入力してください'.format(label, min, max))


def valid_number_value(
    label: str,
    value: Union[int, float],
    min: int = None,
    max: int = None
):
    if (max is None) and (min is not None) and (value < min):
        raise ValueError(
            '{}は{}以上の値で入力してください'.format(label, min))
    if (min is None) and (max is not None) and (max < value):
        raise ValueError(
            '{}は{}以下の値で入力してください'.format(label, max))
    if ((min is not None) and (max is not None)
            and (value < min or max < value)):
        raise ValueError(
            '{}は{}以上、{}以内の値で入力してください'.format(label, min, max))


def valid_float_type(
    label: str,
    value: float,
):
    if not isinstance(value, float):
        raise ValueError(
            '{}は小数で入力してください'.format(label))


def valid_id_value(
    label: str,
    value: Union[int, str],
    min: int,
):
    if isinstance(value, str) or value < min:
        raise ValueError(
            '{}の識別子が不正です'.format(label))
