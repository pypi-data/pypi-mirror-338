from sqlparse.sql import Statement

from mag_db.bean.table_info import TableInfo
from mag_db.parser.base_parser import BaseParser


class DeleteParser(BaseParser):
    def _parse(self, stmt: Statement) -> TableInfo:
        # 提取表名及别名
        tables = super()._find_table(stmt, {'FROM'})

        # 提取条件部分
        where = super()._find_where(stmt)

        return TableInfo(tables, where=where)