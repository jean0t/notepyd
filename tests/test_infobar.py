import pytest

from notepyd.widgets.infobar import InfoBar
from unittest.mock import Mock

@pytest.fixture
def infobar():
    infobar = InfoBar.__new__(InfoBar)
    infobar.file_label = Mock()
    infobar.word_count_label = Mock()
    return infobar


def test_update_file_name_with_name(infobar):
    new_name = 'new_file_name.txt'
    infobar.update_file_name(new_name)

    infobar.file_label.config.assert_called_once_with(text=new_name)


def test_update_file_name_with_name(infobar):
    infobar.update_file_name('')

    infobar.file_label.config.assert_called_once_with(text='Untitled')


def test_update_status(infobar):
    text = 'hello world'
    words = 2
    chars = len(text)
    infobar.update_stats(text)

    infobar.word_count_label.config.assert_called_once_with(text=f'Words: {words} | Chars: {chars}')
