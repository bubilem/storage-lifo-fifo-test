from abc import ABC
from typing import List


class Storage(ABC):
    """Abstraktní společný předek pro ukládání čísel."""

    def __init__(self) -> None:
        # Chráněný atribut odpovídající #List[int] items
        self._items: List[int] = []

    def size(self) -> int:
        """Vrátí aktuální počet prvků."""
        return len(self._items)

    def is_empty(self) -> bool:
        """Vrátí True, pokud je úložiště prázdné, jinak False."""
        return self.size() == 0

    def clear(self) -> None:
        """Vyprázdní celé úložiště."""
        self._items.clear()


class Stack(Storage):
    """Zásobník – funguje na principu LIFO (poslední dovnitř, první ven)."""

    def push(self, value: int) -> None:
        """Vloží hodnotu na vrchol zásobníku."""
        self._items.append(value)

    def pop(self) -> int:
        """Odebere a vrátí hodnotu z vrcholu zásobníku.

        Vyvolá IndexError, pokud je zásobník prázdný.
        """
        if self.is_empty():
            raise IndexError("Nelze volat pop() na prázdném zásobníku.")
        return self._items.pop()


class Queue(Storage):
    """Fronta – funguje na principu FIFO (první dovnitř, první ven)."""

    def enqueue(self, value: int) -> None:
        """Zařadí hodnotu na konec fronty."""
        self._items.append(value)

    def dequeue(self) -> int:
        """Odebere a vrátí hodnotu ze začátku fronty.

        Vyvolá IndexError, pokud je fronta prázdná.
        """
        if self.is_empty():
            raise IndexError("Nelze volat dequeue() na prázdné frontě.")
        return self._items.pop(0)
