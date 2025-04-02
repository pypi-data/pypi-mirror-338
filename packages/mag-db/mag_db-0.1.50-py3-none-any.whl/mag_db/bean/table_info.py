from dataclasses import dataclass, field
from typing import Any, Optional

from mag_db.bean.foreign_key import ForeignKey
from mag_db.bean.primary_key import PrimaryKey
from mag_db.bean.column import Column
from mag_db.bean.table import Table

@dataclass
class TableInfo:
    tables: list[Table] = field(default_factory=list, metadata={'description': '表信息列表'})
    columns: list[Column] = field(default_factory=list, metadata={'description': '列信息列表'})
    primary_key: Optional[PrimaryKey] = field(default=None, metadata={'description': '主键'})
    foreign_keys: list[ForeignKey] = field(default_factory=list, metadata={'description': '外键列表'})
    distinct: bool = field(default=False, metadata={'description': '去除重复的数据行'})
    values: Optional[list[Any]] = field(default_factory=list, metadata={'description': '数据集'})
    where: Optional[str] = field(default=None, metadata={'description': '条件语句'})
    group_by:Optional[str] = field(default=None, metadata={'description': '分组语句'})
    having: Optional[str] = field(default=None, metadata={'description': '过滤语句'})
    order_by: Optional[str] = field(default=None, metadata={'description': '排序语句'})
    charset: Optional[str] = field(default=None, metadata={'description': '字符集'})
    engine: Optional[str] = field(default=None, metadata={'description': '引擎'})
    comment: Optional[str] = field(default=None, metadata={'description': '备注'})
    column_name_map: Optional[dict[str, str]] = field(default=None, metadata={'description': '列名映射表'})
    auto_increment: bool = field(default=False, metadata={'description': '是否自动递增'})

    def __post_init__(self):
        if not self.column_name_map:
            self.column_name_map = TableInfo.__get_column_name_map(self.columns)

    @property
    def table_names(self) -> list[str]:
        return [table.name for table in self.tables]

    def get_column_names(self, is_query: bool = False) -> list[str]:
        column_names = [column.name for column in self.columns]

        # 对于非查询类操作，如主键是自增型，则排除
        if not is_query and self.auto_increment and self.primary_key:
            column_names.remove(self.primary_key.default_column)

        return column_names

    @property
    def default_primary_key(self) -> Optional[str]:
        return self.primary_key.default_column if self.primary_key else None

    def __str__(self):
        foreign_keys_str_list = [foreign_key.__str__() for foreign_key in self.foreign_keys]

        parts = [ f"tables=[{', '.join(self.table_names)}]",
                  f"columns=[{', '.join(self.get_column_names())}]" if self.columns else "",
                  f"primary_key={self.primary_key}" if self.primary_key else "",
                  f"foreign_keys=[{', '.join(foreign_keys_str_list)}]" if len(self.foreign_keys) > 0 else "",
                  f"distinct={self.distinct}",
                  f"values={self.values}" if self.values else "",
                  f"where={self.where}" if self.where else "",
                  f"group_by={self.group_by}" if self.group_by else "",
                  f"having={self.having}" if self.having else "",
                  f"order_by={self.order_by}" if self.order_by else "",
                  f"column_name_map={self.column_name_map}" if self.column_name_map else ""
        ]
        # 过滤掉空字符串
        parts = [part for part in parts if part]
        return f"TableInfo({', '.join(parts)})"

    @classmethod
    def __get_column_name_map(cls, columns: list[Column]) -> dict[str, str]:
        mappings = {}
        for column in columns:
            map_value = column.mapping
            if map_value:
                mappings[column.name] = map_value
        return mappings
