from typing import Any, Optional, Type

import pymysql
from mag_tools.bean.db_list import DbList
from mag_tools.bean.db_page import DbPage
from mag_tools.exception.dao_exception import DaoException
from mag_tools.log.logger import Logger
from mag_tools.enums.log_type import LogType

from mag_db.core.db_session import DBSession
from mag_db.data.db_output import DbOutput
from mag_db.data.result_set_helper import ResultSetHelper
from mag_db.sql.base_executor import BaseExecutor
from mag_db.utils.dao_utils import DaoUtils


class IndexQueryExecutor(BaseExecutor):
    def __init__(self, sql: str, session: DBSession):
        super().__init__(sql, session)

    def execute_sql(self)->list[dict[str, Any]]:
        return self.__fetchall()

    def execute_bean(self, bean_class: Type, column_names: list[str], column_name_map: dict[str, str] = None) -> Any:
        beans = self.execute_beans(bean_class, column_names, column_name_map)
        return beans[0] if beans else None

    def execute_beans(self, bean_class: Type, column_names: list[str], column_name_map: dict[str, str] = None, is_multi_table: bool = False) -> DbList[Any]:
        result_set = self.__fetchall()

        output = DbOutput.from_class(bean_class, column_names, column_name_map)
        output.set_multi_table(is_multi_table)
        data = ResultSetHelper.to_beans(result_set, output)
        return DbList(data)

    def execute_beans_by_page(self, bean_class: Type, column_names: list[str], column_name_map: Optional[dict[str, str]] = None,
                              page: Optional[DbPage] = None, is_multi_table: bool = False) -> DbList:
        result_set = self.__fetchall(page)
        total_count = self.get_count()

        output = DbOutput.from_class(bean_class, column_names, column_name_map)
        output.set_multi_table(is_multi_table)

        data = ResultSetHelper.to_beans(result_set, output)
        return DbList(data, page, total_count)

    def execute_map(self, column_names: list[str]) -> dict[str, Any]:
        maps = self.execute_maps(column_names)
        return maps[0] if maps else {}

    def execute_maps(self, column_names: list[str]) -> DbList[dict[str, Any]]:
        output = DbOutput.from_class(None, column_names)
        result_set = self.__fetchall()
        data = ResultSetHelper.to_maps(result_set, output)
        return DbList(data)

    def execute_maps_by_page(self, column_names: list[str], page: Optional[DbPage] = None) -> DbList:
        result_set = self.__fetchall(page)
        total_count = self.get_count()

        output = DbOutput.from_class(dict, column_names)
        data = ResultSetHelper.to_maps(result_set, output)
        return DbList(data, page, total_count)

    def get_count(self) -> int:
        try:
            count_sql = DaoUtils.get_count_sql(self._sql)

            query_executor = IndexQueryExecutor(count_sql, self._session)
            record = query_executor.execute_map(['COUNT_'])
            return record.get("COUNT_", 0)
        except DaoException as dao:
            Logger.info(LogType.DAO, dao)
            return 0

    def __fetchall(self, page: Optional[DbPage] = None) -> list[dict[str, Any]]:
        self.check()

        try:
            values = self.prepare()

            with self.get_connection() as conn:
                with conn.cursor() as cursor:
                    sql = f"{self._sql} {page.get_sql()}" if page else self._sql
                    if values:
                        cursor.execute(sql, values)
                    else:
                        cursor.execute(sql)

                    column_names = [description[0] for description in cursor.description]
                    return [dict(zip(column_names, row)) for row in cursor.fetchall()]
        except pymysql.MySQLError:
            Logger.throw(LogType.DAO, f"查询时出错: {self._sql}")