from unittest import TestCase

import sqlparse

from mag_db.parser.create_parser import CreateParser
from mag_db.parser.delete_parser import DeleteParser
from mag_db.parser.drop_parser import DropParser
from mag_db.parser.insert_parser import InsertParser
from mag_db.parser.query_parser import QueryParser
from mag_db.parser.update_parser import UpdateParser


class TestAllParser(TestCase):
    def test_create_parser(self):
        _sql = '''
        CREATE TABLE IF NOT EXISTS table_name1 (
            id INT  COMMENT '主键ID', 
            name VARCHAR(50) NOT NULL COMMENT '名称',
            length1 DECIMAL(10,2) NULL COMMENT '长度,缺省值为0',
            created_at TIMESTAMP(6) DEFAULT CURRENT_TIMESTAMP COMMENT "创建时间,缺省为当天", 
            FOREIGN KEY (id,name) REFERENCES other_table(id,name),
            CONSTRAINT pk_name PRIMARY KEY (id, name) 
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='示例表';
        '''

        _stmt = sqlparse.parse(_sql)[0]
        parser = CreateParser(_stmt)
        print(f'SQL: {parser.sql}')

        if parser.table_info:
            print(parser.table_info)

    def test_drop_parser(self):
        _sql = "DROP TABLE IF EXISTS table_name1;"

        _stmt = sqlparse.parse(_sql)[0]
        parser = DropParser(_stmt)
        if parser.table_info:
            print(parser.table_info)

    def test_insert_parser(self):
        _sql = "INSERT INTO table_name1 (column1, column2) VALUES ('value1', 'value2');"

        _stmt = sqlparse.parse(_sql)[0]
        _parser = InsertParser(_stmt)
        if _parser.table_info:
            print(_parser.table_info)

    def test_delete_parser(self):
        _sql = "DELETE FROM table_name1 AS t WHERE id = 1;"

        _stmt = sqlparse.parse(_sql)[0]

        parser = DeleteParser(_stmt)
        if parser.table_info:
            print(parser.table_info)

    def test_query_parser(self):
        _sql = "SELECT t.column1 AS c1, t.column2 AS c2 FROM table_name1 AS t WHERE t.id IN (1, 2, 3) AND t.name = 'John' GROUP BY t.column1 HAVING COUNT(t.column1) > 1 ORDER BY t.column2;"
        _stmt = sqlparse.parse(_sql)[0]
        _parser = QueryParser(_stmt)
        if _parser.table_info:
            print(_parser.table_info)

    def test_update_parser(self):
        _sql = "UPDATE table_name1 AS t SET t.column1 = 'value1', t.column2 = 'value2' WHERE id = 1;"

        _stmt = sqlparse.parse(_sql)[0]
        _result = UpdateParser(_stmt)
        if _result.table_info:
            print(_result.table_info)