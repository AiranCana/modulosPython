#!/usr/bin/env python3
import typing
from abc import ABC, abstractmethod


class DataProcessor(ABC):

    _data: list[tuple[int, str]]
    _rank: int

    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        if len(self._data) == 0:
            raise IndexError("No data output")
        return self._data.pop(0)


class NumericProcessor(DataProcessor):

    def __init__(self) -> None:
        super().__init__()
        self._rank = 0
        self._data = []

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, int) or isinstance(data, float):
            return True
        elif isinstance(data, list):
            return all((isinstance(i, int) or isinstance(i, float))
                       for i in data)
        return False

    def ingest(self, data: typing.Any) -> None:
        # data: int | float | list[int | float | ...]
        if isinstance(data, list):
            for i in data:
                if not (isinstance(i, int) or isinstance(i, float)):
                    raise ValueError("Improper numeric data")
                self._data.append((self._rank, str(i)))
                self._rank += 1
        else:
            if not (isinstance(data, int) or isinstance(data, float)):
                raise ValueError("Improper numeric data")
            self._data.append((self._rank, str(data)))
            self._rank += 1


class TextProcessor(DataProcessor):

    def __init__(self) -> None:
        super().__init__()
        self._rank = 0
        self._data = []

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            return all(isinstance(i, str) for i in data)
        return False

    def ingest(self, data: typing.Any) -> None:
        if isinstance(data, list):
            for i in data:
                if not isinstance(i, str):
                    raise ValueError("Improper text data")
                self._data.append((self._rank, i))
                self._rank += 1
        else:
            if not isinstance(data, str):
                raise ValueError("Improper text data")
            self._data.append((self._rank, data))
            self._rank += 1


class LogProcessor(DataProcessor):

    def __init__(self) -> None:
        super().__init__()
        self._rank = 0
        self._data = []

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            return all(isinstance(j, str) and isinstance(v, str)
                       for j, v in data.items())
        if isinstance(data, list):
            if all(isinstance(i, dict) for i in data):
                return all(isinstance(j, str) and isinstance(v, str)
                           for dat in data
                           for j, v in dat.items())
        return False

    def ingest(self, data: typing.Any) -> None:
        try:
            if isinstance(data, list):
                for i in data:
                    if not isinstance(i, dict):
                        raise ValueError(f"{i} no es un log")
                    if not all(isinstance(j, str) and isinstance(v, str)
                               for dat in data
                               for j, v in dat.items()):
                        raise ValueError(f"{i} no es un log correcto")
                    self._data.append((self._rank, f"{i['log_level']}:" +
                                       f" {i['log_message']}"))
                    self._rank += 1
            else:
                if not isinstance(data, dict):
                    raise ValueError(f"{data} no es un log")
                if not all(isinstance(j, str) and isinstance(v, str)
                           for j, v in data.items()):
                    raise ValueError(f"{data} no es un log correcto")
                self._data.append((self._rank, f"{data['log_level']}:" +
                                   f" {data['log_message']}"))
                self._rank += 1
        except KeyError:
            raise ValueError("el log no esta bien formado")


class ExportPlugin(typing.Protocol):

    def __init__(self) -> None:
        super().__init__()

    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("Output:")
        point = False
        for _, s in data:
            if point:
                print(",", end="")
            else:
                point = True
            print(s, end="")
        print()


class CSVExportPlugin():

    def __init__(self) -> None:
        ...

    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        point = False
        for _, s in data:
            if point:
                print(",", end="")
            else:
                point = True
            print(s, end="")
        print()


class JSONExportPlugin():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        point = False
        print("{")
        for i, s in data:
            if point:
                print(", ", end="")
            else:
                point = True
            print(f"item_{i} : \"{s}\"", end="")
        print("}")


class DataStream():

    __procesor: list[DataProcessor]
    __proces: dict[str, DataProcessor]

    def __init__(self) -> None:
        self.__proces = {}
        self.__procesor = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.__procesor.append(proc)
        print("Registering", end=" ")
        if isinstance(proc, NumericProcessor):
            print("Numeric", end=" ")
            self.__proces.update({"Numeric": proc})
        elif isinstance(proc, TextProcessor):
            print("Text", end=" ")
            self.__proces.update({"Text": proc})
        elif isinstance(proc, LogProcessor):
            print("Log", end=" ")
            self.__proces.update({"Log": proc})
        print("Processor")

    def process_stream(self, stream: list[typing.Any]) -> None:
        if len(self.__procesor) != 0:
            for i in stream:
                foun = True
                for j in self.__procesor:
                    if j.validate(i):
                        j.ingest(i)
                        foun = False
                if foun:
                    print("DataStream error - Can't process element in" +
                          f" stream: {i}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if len(self.__proces) == 0:
            print("No processor found, no data", end="\n\n")
        for _, i in self.__proces.items():
            if isinstance(i, NumericProcessor):
                print("Numeric", end=" ")
            elif isinstance(i, TextProcessor):
                print("Text", end=" ")
            elif isinstance(i, LogProcessor):
                print("Log", end=" ")
            print("Processor", end=": ")
            print(f"total {i._rank} items processed, remaining" +
                  f" {len(i._data)} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        lis: list[tuple[int, str]] = []
        for i in self.__procesor:
            lis = []
            for _ in range(nb):
                try:
                    lis += [i.output()]
                except IndexError:
                    ...
            plugin.process_output(lis)


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===", end="\n\n")
    data = DataStream()
    print("Initialize Data Stream...", end="\n\n")
    data.print_processors_stats()
    datas = ['Hello world', [3.14, -1, 2.71], [
            {'log_level': 'WARNING',
             'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO', 'log_message': 'User wil is connected'}
            ], 42, ['Hi', 'five']]
    datas2 = [21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
              [{'log_level': 'ERROR', 'log_message': '500 server crash'},
               {'log_level': 'NOTICE',
                'log_message': 'Certificate expires in 10 days'}],
              [32, 42, 64, 84, 128, 168], 'World hello']
    data.process_stream(datas)
    pri = NumericProcessor()
    sec = TextProcessor()
    ter = LogProcessor()
    csv = CSVExportPlugin()
    json = JSONExportPlugin()
    try:
        data.register_processor(pri)
        data.register_processor(sec)
        data.register_processor(ter)
        print(f"\nSend first batch of data on stream: {datas}")
        data.process_stream(datas)
        print()
        data.print_processors_stats()
        print()
        if True:
            print("Send 3 processed data from each processor to a CSV plugin:")
            data.output_pipeline(3, csv)
        print()
        data.print_processors_stats()
        print(f"\nSend another batch of data: {datas2}")
        data.process_stream(datas2)
        print()
        data.print_processors_stats()
        print()
        if True:
            print("Send 5 processed data from each processor" +
                  " to a JSON plugin:")
            data.output_pipeline(5, json)
        print()
        data.print_processors_stats()
    except Exception as e:
        print(f"Error: {e}")
