import clickhouse_connect
from pandas import DataFrame as PandasDataFrame

from dump.config_utils import load_config


CH_TO_PYTHON_TYPE_MAPPER = {
    # Boolean
    "Bool": "bool",
    
    # Integers (signed)
    "Int8": "int8",
    "Int16": "int16",
    "Int32": "int32",
    "Int64": "int64",
    
    # Integers (unsigned)
    "UInt8": "uint8",
    "UInt16": "uint16",
    "UInt32": "uint32",
    "UInt64": "uint64",
    
    # Floating point
    "Float32": "float32",
    "Float64": "float64",
    
    # Temporal
    "timestamp": "timestamp",
    "date": "timestamp",
    
    # Strings
    "String": "object",
}


class ConnectorCH:
    def __init__(
        self,
        db_config_name: str = "click_house",
    ) -> None:
        self.db_config_name = db_config_name
        self.__config = load_config(section=self.db_config_name)

        self._client = None

    @property
    def client(self):
        if self._client is None:
            try:
                self._client = clickhouse_connect.get_client(**self.__config)
                # print("Connected to the ClickHouse server.")
            except Exception as error:
                print(error)
        return self._client


class TableCH(ConnectorCH):
    def __init__(self, db_config_name: str = "click_house") -> None:
        super().__init__(db_config_name)

    def get_df(self, query: str) -> PandasDataFrame:
        return self.client.query_df(query)


class DBUtilsCH(ConnectorPG):
    @staticmethod
    def _validate_output(inp: list):
        return [x[0] for x in inp]

    def get_table_structure(table_name: str, database: str = "default") -> Dict[str, Any]:
    """
        Получает структуру таблицы ClickHouse и возвращает схему в виде словаря
        с соответствиями типов ClickHouse → PyArrow.
        
        Args:
            table_name: Имя таблицы
            database: Имя базы данных (по умолчанию 'default')
        
        Returns:
            Словарь с описанием структуры таблицы
    """
    query = f"""
        SELECT name, type, is_nullable, position
        FROM system.columns
        WHERE table = '{table_name}' AND database = '{database}'
        ORDER BY position
    """

    schema = {}
        for column_name, data_type, is_nullable, position in self.fetchall(query):
            if "int" in data_type and data_type not in TYPE_MAPPER.keys():
                data_type = "integer"
            if ("numeric" in data_type or "decimal" in data_type) and data_type not in TYPE_MAPPER.keys():
                data_type = "decimal"
            if "time" in data_type:
                data_type = "timestamp"

            schema[column_name] = {
                "data_type": TYPE_MAPPER.get(data_type, "str"),
                "is_nullable": is_nullable,
                "position": position,
            }
        return schema