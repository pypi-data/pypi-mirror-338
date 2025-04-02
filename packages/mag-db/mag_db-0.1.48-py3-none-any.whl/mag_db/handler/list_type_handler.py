from mag_tools.jsonparser.json_parser import JsonParser

from mag_db.handler.type_handler import T, TypeHandler


class ListTypeHandler(TypeHandler):
    def set_parameter(self, parameter: T) -> str | None:
        return JsonParser.from_bean(parameter) if isinstance(parameter, list) else None