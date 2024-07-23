"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import pytest
from src.stack import Node, Stack

def test_node_initialization():
    node = Node(5)
    assert node.data == 5
    assert node.next_node is None

    node_with_next = Node('a', node)
    assert node_with_next.data == 'a'
    assert node_with_next.next_node == node

def test_stack_initialization():
    stack = Stack()
    assert stack.top is None

def test_stack_push():
    stack = Stack()
    stack.push('data1')
    assert stack.top.data == 'data1'
    assert stack.top.next_node is None

    stack.push('data2')
    assert stack.top.data == 'data2'
    assert stack.top.next_node.data == 'data1'
    assert stack.top.next_node.next_node is None

def test_stack_str():
    stack = Stack()

    assert str(Stack()) == ""



