from vierror import MException
from .Field import Field


class Model:
    def __init__(self, name: str, fields=None):
        if fields is None:
            fields = []
        self.name = name
        self.fields: dict[str, Field] = {}
        self.add_fields(fields)

    def get(self, f_name: str):
        if f_name not in self.fields:
            raise MException("ValiDataModel.GetFieldError", f"字段({f_name})未定义")
        return self.fields[f_name].get()

    def set(self, f_name: str, value):
        if f_name not in self.fields:
            raise MException("ValiDataModel.GetFieldError", f"字段({f_name})未定义")
        self.fields[f_name].set(value)

    def add_field(self, filed: Field):
        if filed.name in self.fields:
            raise MException("ValiDataModel.AddFieldError", f"字段({filed.name})已存在")
        self.fields[filed.name] = filed

    def add_fields(self, fields: list[Field]):
        for field in fields:
            self.add_field(field)


