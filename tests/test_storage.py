import unittest
import sys
from pathlib import Path

# Přidání kořenového adresáře projektu do vyhledávací cesty Pythonu (umožní běh odkudkoliv)
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.storage import Queue, Stack, Storage



class TestStorageHierarchy(unittest.TestCase):

    def test_abstract_storage_instantiation(self):
        """Ověří, že třídy dědí ze Storage."""
        stack = Stack()
        queue = Queue()
        self.assertIsInstance(stack, Storage)
        self.assertIsInstance(queue, Storage)

    # --- Testy pro Stack (LIFO) ---

    def test_stack_lifo_order(self):
        """Ověří princip LIFO (Last In, First Out)."""
        stack = Stack()
        stack.push(10)
        stack.push(20)
        stack.push(30)

        self.assertEqual(stack.pop(), 30)
        self.assertEqual(stack.pop(), 20)
        self.assertEqual(stack.pop(), 10)

    def test_stack_empty_pop_raises_error(self):
        """Ověří vyvolání výjimky při pop() z prázdného zásobníku."""
        stack = Stack()
        with self.assertRaises(IndexError):
            stack.pop()

    # --- Testy pro Queue (FIFO) ---

    def test_queue_fifo_order(self):
        """Ověří princip FIFO (First In, First Out)."""
        queue = Queue()
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)

        self.assertEqual(queue.dequeue(), 10)
        self.assertEqual(queue.dequeue(), 20)
        self.assertEqual(queue.dequeue(), 30)

    def test_queue_empty_dequeue_raises_error(self):
        """Ověří vyvolání výjimky při dequeue() z prázdné fronty."""
        queue = Queue()
        with self.assertRaises(IndexError):
            queue.dequeue()

    # --- Testy pro společné metody ze Storage ---

    def test_common_methods_size_and_empty(self):
        """Ověří metody size() a is_empty()."""
        stack = Stack()
        self.assertTrue(stack.is_empty())
        self.assertEqual(stack.size(), 0)

        stack.push(42)
        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.size(), 1)

    def test_common_method_clear(self):
        """Ověří metodu clear()."""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.size(), 2)

        queue.clear()
        self.assertTrue(queue.is_empty())
        self.assertEqual(queue.size(), 0)


if __name__ == "__main__":
    unittest.main()
