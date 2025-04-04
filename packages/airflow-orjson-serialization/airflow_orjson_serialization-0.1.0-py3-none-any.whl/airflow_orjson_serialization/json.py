import orjson

class ORJson:
    @staticmethod
    def dumps(obj, **kwargs):
        """
        Dumps the object to a JSON string.
        """
        return orjson.dumps(obj).decode("utf-8")

    @staticmethod
    def loads(s, **kwargs):
        """
        Loads the JSON string to an object.
        """
        return orjson.loads(s)

