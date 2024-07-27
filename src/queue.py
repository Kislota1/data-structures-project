class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        :param next_node: ссылка на следующий узел в очереди
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.front = None
        self.rear = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next_node = new_node
            self.rear = new_node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента или None, если очередь пуста
        """
        if self.front is None:
            return None
        data = self.front.data
        self.front = self.front.next_node
        if self.front is None:
            self.rear = None
        return data

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        elements = []
        current = self.front
        while current:
            elements.append(str(current.data))
            current = current.next_node
        return "-".join(elements)