from dataclasses import dataclass, field
from datetime import date, datetime, time
from enum import Enum
from typing import Any, Optional, TypeVar

from mag_tools.enums.base_enum import BaseEnum
from mag_tools.utils.common.class_utils import ClassUtils
from mag_tools.utils.common.string_utils import StringUtils

from mag_db.data.parameter_cache import ParameterCache
from mag_db.data.column_names_mapping import ColumnNamesMapping
from mag_db.handler.type_constant import TypeConstant
from mag_db.handler.type_handler import TypeHandler
from mag_db.utils.column_utils import ColumnUtils
from mag_db.utils.dao_utils import DaoUtils

T = TypeVar('T')
K = TypeVar('K')
V = TypeVar('V')

@dataclass
class RowParameter:
    """
    一条记录的参数及类型的列表
    """
    parameters: list[Any] = field(default_factory=list, metadata={'description': '数据库记录的参数清单'})
    type_handlers: list[TypeHandler] = field(default_factory=list, metadata={'description': '记录的参数类型列表'})

    def append(self, parameter: Any, type_handler: TypeHandler) -> None:
        self.parameters.append(parameter)
        self.type_handlers.append(type_handler)

@dataclass
class IndexParameters:
    __parameter_cache: ParameterCache = field(default_factory=ParameterCache, metadata={'description': '多条记录的参数清单'})

    def set_value(self, parameter: Any, type_: type = None) -> None:
        type_constant = TypeConstant.STRING
        if type_ is bytes or isinstance(parameter, bytes):
            type_constant = TypeConstant.BYTES
        elif type_ is bool or isinstance(parameter, bool):
            type_constant = TypeConstant.BOOL
        elif type_ is int or isinstance(parameter, int):
            type_constant = TypeConstant.INT
        elif type_ is float or isinstance(parameter, float):
            type_constant = TypeConstant.FLOAT
        elif type_ is date or isinstance(parameter, date):
            type_constant = TypeConstant.DATE
        elif type_ == datetime or isinstance(parameter, datetime):
            type_constant = TypeConstant.DATETIME
        elif type_ is time or isinstance(parameter, time):
            type_constant = TypeConstant.TIME
        elif type_ is tuple or isinstance(parameter, tuple):
            type_constant = TypeConstant.TUPLE

        self.__parameter_cache.set_parameter(parameter, type_constant)

    def set_beans(self, param_beans: list[T], column_names: list[str],
                  column_name_map: Optional[dict[str, str]] = None) -> None:
        if param_beans:
            column_names_mapping = ColumnNamesMapping.get_by_class(type(param_beans[0]), column_names, column_name_map)
            field_names = ColumnUtils.to_field_names(column_names, column_names_mapping)
            for row_index, param_bean in enumerate(param_beans):
                self.__put_bean(param_bean, field_names, row_index)

    def set_field_maps(self, field_maps: list[dict[K, V]], column_names: list[str]) -> None:
        if field_maps:
            column_names_mapping = ColumnNamesMapping.get_by_field_map(field_maps[0], column_names)
            field_names = ColumnUtils.to_field_names(column_names, column_names_mapping)
            for row_index, field_map in enumerate(field_maps):
                self.__put_map(field_map, field_names, row_index)

    def set_fields_of_where(self, params: list[T]) -> None:
        self.__parameter_cache.field_of_where = []
        for param in params:
            if isinstance(param, Enum):
                self.__parameter_cache.field_of_where.append(param.code if isinstance(param, BaseEnum) else param.name)
            else:
                self.__parameter_cache.field_of_where.append(param)

    @property
    def row_count(self) -> int:
        row_count = len(self.__parameter_cache.row_parameters)
        return row_count if row_count > 0 else len(self.__parameter_cache.field_of_where)

    @property
    def sum_of_params(self) -> int:
        return self.__parameter_cache.sum_of_params

    @property
    def field_num(self):
        return len(self.__parameter_cache.field_of_where)

    @property
    def parameters(self)->tuple[tuple[Any,...],...]:
        return self.__parameter_cache.values

    def type_handlers(self, row_index: int = 0)->list[TypeHandler]:
        return self.__parameter_cache.type_handlers(row_index)

    def get_values(self)-> tuple[tuple[Any, ...], ...]:
        return self.__parameter_cache.get_values()

    def clear(self):
        self.__parameter_cache.row_parameters.clear()
        self.__parameter_cache.sum_of_params = 0

    def is_empty(self) -> bool:
        return len(self.__parameter_cache.row_parameters) == 0 and len(self.__parameter_cache.field_of_where) == 0

    # def __set_parameter(self, parameter: Any, type_handler: TypeHandler, row_index: int = 0) -> None:
    #     if row_index < len(self.__row_parameters):
    #         row_parameter = self.__row_parameters[row_index]
    #     else:
    #         row_parameter = RowParameter()
    #         self.__row_parameters.append(row_parameter)
    #
    #     row_parameter.append(parameter, type_handler)
    #
    #     self.__sum_of_params += 1

    def __put_bean(self, param_bean: T, column_names: list[str], row_index: int) -> None:
        for column_name in column_names:
            bean_field_name = StringUtils.hump2underline(column_name)

            try:
                bean_field_value = getattr(param_bean, bean_field_name, None)
                bean_field_type = ClassUtils.get_field_type_of_bean(param_bean, bean_field_name)
                bean_field_type = ClassUtils.get_origin_type(bean_field_type)

                if isinstance(bean_field_value, Enum):
                    bean_field_value = bean_field_value.code if hasattr(bean_field_value, 'code') else bean_field_value.name

                type_handler = DaoUtils.get_type_handler(bean_field_type)
                self.__parameter_cache.set_parameter(bean_field_value, type_handler, row_index)
            except AttributeError:
                pass  # 该列名在bean中不存在，跳过

    def __put_map(self, field_set: dict[str, V], column_names: list[str],  row_index: int) -> None:
        for column_name in column_names:
            field_value = field_set.get(column_name)
            field_type = type(field_value)
            if field_type is None:
                field_type = str

            type_handler = DaoUtils.get_type_handler(field_type)
            self.__parameter_cache.set_parameter(field_value, type_handler, row_index)
