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


def procesing(pri: DataProcessor, d: typing.Any, tryi: int,
              proces: str, value: str = "value") -> None:
    print(f"Procesing data: {d}")
    pri.ingest(d)
    print(f"Exceptin {tryi} ", end="")
    if tryi == 1:
        print("values...")
    else:
        print("value...")
    for _ in range(tryi):
        i, v = pri.output()
        print(f"{proces} {value} {i}: {v}")


if __name__ == "__main__":
    try:
        print("=== Code Nexus - Data Processor ===", end="\n\n")
        pri = NumericProcessor()
        sec = TextProcessor()
        ter = LogProcessor()
        print("Testing Numeric Processor...")
        print(f"Trying to validate input '42': {pri.validate(42)}")
        print(f"Trying to validate input 'Hello': {pri.validate('Hello')}")
        print("Test invalid ingestion of string 'foo'" +
              " without prior validation:")
        try:
            pri.ingest("foo")
        except ValueError as e:
            print(f"Got exception: {e}")
        d = [1, 2, 3, 4, 5]
        procesing(pri, d, 3, "Numeric")
        print("\nTesting Text Processor...")
        print(f"Trying to validate input '42': {sec.validate(42)}")
        f = ['Hello', 'Nexus', 'World']
        procesing(sec, f, 1, "Text")
        print("\nTesting Log Processor...")
        print(f"Trying to validate input 'Hello': {pri.validate('Hello')}")
        g = [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
             {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
        procesing(ter, g, 2, "Log", "entry")
        procesing(pri, d, 1, "Numeric")
    except Exception as e:
        print(f"Error detected: {e}")
