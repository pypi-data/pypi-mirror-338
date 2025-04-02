from typing import Optional

from mag_tools.enums.symbol import Symbol

from mag_db.bean.column import Column
from mag_db.bean.table import Table
from mag_db.builder.base_sql import BaseSql
from mag_db.builder.where import Where
from mag_db.enums.operator_type import OperatorType


class Select(BaseSql):
    """
    SELECT语句操作类

    @description: 用于构建SELECT语句。
    @version: v1.0
    @date: 2019/8/30
    """
    def __init__(self, table_names: list[str], fully_column_names: list[str], condition: Optional[Where]):
        """
        构造方法，适用于多表查询

        :param table_names: 表名与别名的列表，tableName1 alias1,tableName2 alias2
        :param fully_column_names: the column names you want to get，格式：表名.列名 AS 别名，其中表名和别名可为空
        :param condition: the condition
        """
        super().__init__()
        self.tables = Table.to_tables(table_names)
        self.columns = self.to_columns(fully_column_names)
        self.where = condition
        self.reset_sql()


    def set_distinct(self):
        """
        设置为去重查询
        """
        super().replace(OperatorType.SELECT.value(), OperatorType.DISTINCT.value())

    def reset_sql(self):
        self.clear()
        self.append_operator(OperatorType.SELECT)
        self.append_columns(self.columns, self.is_multiple_table()).append_from(self.tables).append_condition(self.where)

    def append_from(self, table_names: list[Table]) -> 'Select':
        self.append_operator(OperatorType.FROM)
        self.append_tables(table_names)
        return self

    def append_columns(self, columns: list[Column], is_multiple_table: bool) -> 'Select':
        """
        添加用逗号分开的列名,(col1, col2, col3)

        :param columns: 列名列表
        :param is_multiple_table: 是否多表
        :return: Select
        """
        if not columns:
            return self
        for i, column in enumerate(columns):
            if i > 0:
                self.append_symbol(Symbol.COMMA)
            self.append_column(column, is_multiple_table, is_multiple_table)
        return self

    def is_multiple_table(self) -> bool:
        return len(self.tables) > 1
