import json


class FormatMixins:
    def to_dict(self):
        d = {}
        for column in self.__table__.columns:
            d[column.name] = str(getattr(self, column.name))

        return d

    def to_json(self):
        return json.dumps(self.to_dict())
