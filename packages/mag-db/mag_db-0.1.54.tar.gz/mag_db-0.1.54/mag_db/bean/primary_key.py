from dataclasses import dataclass, field
from typing import Optional

@dataclass
class PrimaryKey:
    """
    描述一个主键约束
    """
    column_names: list[str] = field(default_factory=list, metadata={'description': '主键列名列表'})
    key_seq: list[int] = field(default_factory=list, metadata={'description': '主键列的顺序列表'})
    pk_name: Optional[str] = field(default=None, metadata={'description': '主键的名称'})
    increment: Optional[int] = field(default=None, metadata={'description': '自增列的增量值'})

    @property
    def default_column(self) -> str:
        return self.column_names[0] if self.column_names and len(self.column_names) == 1 else None

    def __str__(self):
        """
        返回主键约束的字符串表示

        返回:
        str: 主键约束的字符串表示
        """
        parts = [f"PRIMARY KEY ({', '.join(self.column_names)})"]
        if self.key_seq and len(self.key_seq) > 0:
            parts.append(f"KEY_SEQ ({', '.join(map(str, self.key_seq))})")
        if self.pk_name:
            parts.append(f"PK_NAME {self.pk_name}")
        if self.increment:
            parts.append(f"INCREMENT {self.increment}")
        return " ".join(parts)