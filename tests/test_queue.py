"""Здесь надо написать тесты с использованием unittest для модуля queue."""
from src.queue import Queue
import unittest

class TestQueue(unittest.TestCase):
    def test_enqueue(self):
        queue = Queue()
        queue.enqueue(1)
        self.assertEqual(queue.top.data, 1)
        queue.enqueue(2)
        self.assertEqual(queue.top.data, 2)
        queue.enqueue(3)
        self.assertEqual(queue.top.data, 3)

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 1)

    def test_dequeue_empty(self):
        queue = Queue()
        with self.assertRaises(IndexError):
            queue.dequeue()

    def test_enqueue_dequeue(self):
        queue = Queue()
        queue.enqueue(1)
        self.assertEqual(queue.dequeue(), 1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(queue.dequeue(), 2)