import pytest
import tkinter as tk

from unittest.mock import Mock
from notepyd.widgets.editor import Editor

@pytest.fixture
def editor():
    editor = Editor.__new__(Editor)
    editor.text = Mock()
    return editor

def test_get_text_method(editor):
    editor.text.get.return_value = "Hello, World!"

    result = editor.get_text()

    editor.text.get.assert_called_once_with("1.0", tk.END)
    assert result == "Hello, World!"

def test_set_text_deletes_and_inserts(editor):
    editor.set_text("FizzBuzz")

    editor.text.delete.assert_called_once_with("1.0", tk.END)
    editor.text.insert.assert_called_once_with("1.0", "FizzBuzz")
    editor.text.edit_separator.assert_called_once()

def test_focus_on_text(editor):
    editor.focus()
    editor.text.focus_set.assert_called_once()
