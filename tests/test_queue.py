"""Здесь надо написать тесты с использованием unittest для модуля queue."""
from src.queue import Queue
import unittest

class TestQueue(unittest.TestCase):
    def test_enqueue(self):
        queue = Queue()

        # Проверка начального состояния очереди
        self.assertEqual(str(queue), "")

        # Добавление первого элемента
        queue.enqueue('data1')
        self.assertEqual(str(queue), "data1")

        # Добавление второго элемента
        queue.enqueue('data2')
        self.assertEqual(str(queue), "data1-data2")

        # Добавление третьего элемента
        queue.enqueue('data3')
        self.assertEqual(str(queue), "data1-data2-data3")

    def test_dequeue(self):
        queue = Queue()

        # Проверка удаления из пустой очереди
        self.assertIsNone(queue.dequeue())

        # Добавление элементов
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')

        # Удаление элементов и проверка их значений
        self.assertEqual(queue.dequeue(), 'data1')
        self.assertEqual(queue.dequeue(), 'data2')
        self.assertEqual(queue.dequeue(), 'data3')

        # Проверка состояния очереди после удаления всех элементов
        self.assertIsNone(queue.dequeue())
        self.assertEqual(str(queue), "")