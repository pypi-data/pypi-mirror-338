from dataclasses import dataclass, field
from typing import Optional, Type

from mag_db.data.column_names_mapping import ColumnNamesMapping

@dataclass
class DbOutput:
    """
    数据库输出信息类

    @description: 提供基础的分页操作
    @version: 2.5
    @date: 2015
    """
    result_class: Optional[Type] = None
    column_name_mapping: ColumnNamesMapping = field(default_factory=ColumnNamesMapping)
    is_multi_table: bool = False
    column_names: list[str] = field(default_factory=list)

    @classmethod
    def from_class(cls, bean_class: Optional[Type], col_names: list[str], col_name_map: Optional[dict[str, str]] = None):
        output = cls()
        output.column_names = col_names

        if bean_class:
            mapping_from_bean = ColumnNamesMapping.get_by_class(bean_class, col_names, col_name_map)
            output.column_name_mapping = mapping_from_bean
            output.result_class = bean_class

        return output

    def get_target_name(self, column_name):
        target_name = self.column_name_mapping.get_target_name(column_name) if self.column_name_mapping else column_name
        return target_name if target_name else column_name