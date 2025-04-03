"""
Фильтр для логирования, который пропускает повторяющиеся сообщения."

# Пример использования:
    logger.addFilter(DuplicateMessageFilter("1:1 5:5 10:10"))
    # logger.addFilter(DuplicateMessageFilter([FilterRange(1, 1), FilterRange(5, 5), FilterRange(10, 10)]))

    # Тестирование - первые 5, потом пропуски до 10, 20, 30
    for i in range(35):
        logger.info("some message text")

    # Проверка смены сообщения
    logger.info("new message text")  # Должно показаться (счетчик сбросится)
    for i in range(15):
        logger.info("new message text")  # Первые 5, потом 10-е

"""

from dataclasses import dataclass
import logging
from typing import List, Union


@dataclass
class FilterRange:
    "Конфигурация диапазона фильтрации."
    # Нижняя граница диапазона. Сообщение с номером N удовлетворяет диапазону, если N >= count
    # (если сообщение удовлетворяет нескольким диапазонам, будет выбран диапазон с минимальным count).
    count: int
    # Шаг вывода сообщений в данном диапазоне. Сообщение с номером N будет выведено, если N % step == 0.
    step: int


def _normalize_ranges(ranges: List[FilterRange]) -> List[FilterRange]:
    "Проверка и нормализация диапазонов фильтрации."
    # Проверка на положительные значения.
    for r in ranges:
        if r.count <= 0 or r.step <= 0:
            raise ValueError(
                "'count' and 'step' in the ranges must be positive integers."
            )
    # Проверка на уникальность диапазонов (значений count).
    unique_counts = {r.count for r in ranges}
    if len(unique_counts) != len(ranges):
        raise ValueError("'count' values in the ranges must be unique.")
    # Сортировка по count.
    ranges = sorted(ranges, key=lambda x: x.count)
    # Если ни один диапазон не задан, или для первого диапазона не выполняется 'count = step = 1'.
    if not ranges or ranges[0].count != 1 or ranges[0].step != 1:
        raise ValueError("First range must have 'count = step = 1'.")
    # Проверка на сортировку по step.
    for i in range(len(ranges) - 1):
        if ranges[i].step >= ranges[i + 1].step:
            raise ValueError("Ranges must be sorted by step.")
    return ranges


def _ranges_from_string(ranges: str) -> List[FilterRange]:
    "Преобразование строкового представления диапазонов в список объектов FilterRange."
    try:
        return [
            FilterRange(*map(int, s.split(":", maxsplit=2))) for s in ranges.split(" ")
        ]
    except Exception as e:
        msg = "Invalid format for ranges. Expected 'count:step' pairs separated by spaces."
        raise ValueError(msg) from e


class DuplicateMessageFilter(logging.Filter):
    def __init__(self, ranges: Union[str, List[FilterRange]]):
        super().__init__()
        self.last_message = None
        self.counter = 0
        if isinstance(ranges, str):
            ranges = _ranges_from_string(ranges)
        self.ranges = _normalize_ranges(ranges)

    def filter(self, record: logging.LogRecord) -> bool:
        "Фильтрация сообщений."
        current_message = record.getMessage()

        if current_message != self.last_message:
            self.last_message = current_message
            self.counter = 0

        self.counter += 1

        # Проверяем диапазоны в обратном порядке.
        for r in reversed(self.ranges):
            if self.counter >= r.count:
                # Нашли нужный диапазон.
                if r.count == 1:
                    return True  # Для первого дипазона показываем все сообщения без изменений.
                if self.counter % r.step == 0:
                    record.msg = f"{record.msg} ({self.counter} equal lines)"
                    return True
                return False

        raise ValueError("First range must have count = step = 1.")
