from typing import Any, get_args, TypeVar

from mag_tools.utils.common.class_utils import ClassUtils
from mag_tools.jsonparser.json_parser import JsonParser
from typing_extensions import get_origin

from mag_db.data.db_output import DbOutput

V = TypeVar('V')

class ResultSetHelper:
    @staticmethod
    def to_maps(result_set: list[dict[str, V]], db_output: DbOutput) -> list[dict[str, V]]:
        return [
            {
                db_output.get_target_name(column_name): row_map.get(column_name, None) for column_name in db_output.column_names
            }
            for row_map in result_set
        ]

    @staticmethod
    def to_beans(result_set: list[dict[str, V]], db_output: DbOutput) -> list[V]:
        result_list = []
        for row_map in result_set:
            kwargs = {}
            for column_name in db_output.column_names:
                target_name = db_output.get_target_name(column_name)
                target_type = ClassUtils.get_field_type_of_class(db_output.result_class, target_name)
                target_type = ClassUtils.get_origin_type(target_type)
                value = row_map.get(column_name)

                if get_origin(target_type) is tuple:
                    args = get_args(target_type)
                    if args:
                        kwargs[target_name] = JsonParser.to_tuple(value, args[0])
                elif get_origin(target_type) is list:
                    args = get_args(target_type)
                    if args:
                        kwargs[target_name] = JsonParser.to_list(value, args[0])
                elif get_origin(target_type) is dict:
                    args = get_args(target_type)
                    if args:
                        kwargs[target_name] = JsonParser.to_map(value, str, args[0])
                else:
                    kwargs[target_name] = value

            result_list.append(db_output.result_class(**kwargs))

        return result_list
