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
        else:
            print("No processor found, no data", end="\n\n")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
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


def operate(li: list[tuple[int, DataProcessor]]) -> None:
    print("Consume some elements from the data processors: ", end="")
    for n, pro in li:
        if isinstance(pro, NumericProcessor):
            print("Numeric", end=" ")
        elif isinstance(pro, TextProcessor):
            print("Text", end=" ")
        elif isinstance(pro, LogProcessor):
            print("Log", end=" ")
        print(f"{n}, ", end="")
        [pro.output() for _ in range(n)]
    print()


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===", end="\n\n")
    data = DataStream()
    print("Initialize Data Stream...")
    datas = ['Hello world', [3.14, -1, 2.71], [
            {'log_level': 'WARNING',
             'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO', 'log_message': 'User wil is connected'}
            ], 42, ['Hi', 'five']]
    data.process_stream(datas)
    pri = NumericProcessor()
    sec = TextProcessor()
    ter = LogProcessor()
    try:
        data.register_processor(pri)
        print(f"\nSend first batch of data on stream: {datas}")
        data.process_stream(datas)
        data.print_processors_stats()
        print()
        print("Registering other data processors")
        data.register_processor(sec)
        data.register_processor(ter)
        print("Send the same batch again")
        data.process_stream(datas)
        data.print_processors_stats()
        print()
        n = [(3, pri), (2, sec), (1, ter)]
        operate(n)
        data.print_processors_stats()
    except Exception as e:
        print(f"Error: {e}")
