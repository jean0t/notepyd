import pytest
import builtins
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox

from notepyd.widgets.navbar import Navbar
from unittest.mock import Mock, mock_open, patch

@pytest.fixture
def app_context():
    """
    creates a context that is needed by navbar
    """
    context = Mock()
    context.editor = Mock()
    context.current_file = None
    context.set_current_file = Mock()
    return context

@pytest.fixture
def navbar(app_context):
    """
    creates a navbar instance without its __init__
    """
    nvbar = Navbar.__new__(Navbar)
    nvbar.app = app_context

    # because it didnt run __init__ we need to bound the `self`
    # to the class methods manually
    nvbar.open_file = Navbar.open_file.__get__(nvbar, Navbar)
    nvbar.save_file = Navbar.save_file.__get__(nvbar, Navbar)
    nvbar.save_as_file = Navbar.save_as_file.__get__(nvbar, Navbar)
    nvbar.show_about = Navbar.show_about.__get__(nvbar, Navbar)
    nvbar.show_shortcuts = Navbar.show_shortcuts.__get__(nvbar, Navbar)

    return nvbar


def test_open_file_success(navbar):
    """
    the user actually selects and opens a file
    """
    fake_path = '/fake/file/path.txt'
    fake_content = 'File was Opened!'

    with patch.object(tkinter.filedialog, 'askopenfilename', return_value=fake_path):
        m_open = mock_open(read_data=fake_content)
        with patch.object(builtins, 'open', m_open):
            navbar.open_file()

    navbar.app.editor.set_text.assert_called_once_with(fake_content)
    navbar.app.set_current_file.assert_called_once_with(fake_path)


def test_open_file_cancel(navbar):
    """
    test the open file if the user clicks cancel instead of
    selecting a file
    """
    with patch.object(tkinter.filedialog, 'askopenfilename', return_value=''):
        navbar.open_file()

    navbar.app.editor.set_text.assert_not_called()
    navbar.app.set_current_file.asset_not_called()

def test_save_file_existing(navbar):
    """
    if file exists and the user selects 'save' in the navbar
    it will save the file automatically
    """
    fake_path = '/fake/file.txt'
    fake_content = 'Data modified to be saved'
    navbar.app.current_file = fake_path
    navbar.app.editor.get_text.return_value = fake_content

    m_open = mock_open()
    with patch.object(builtins, 'open', m_open):
        navbar.save_file()

    m_open.assert_called_once_with(fake_path, 'w', encoding='utf-8')

    handle = m_open()
    handle.write.assert_called_once_with(fake_content)

def test_save_file_calls_save_as(navbar):
    """
    when save file doesn't corresponds to any actual file
    the save as file function is called to create a new file
    """
    called = {}
    def fake_save_as():
        called['yes'] = True

    navbar.save_as_file = fake_save_as
    navbar.app.current_file = None
    navbar.save_file()
    assert called.get('yes', False) is True

def test_save_as_file(navbar):
    """
    save as file function called correctly and path to the file
    updated after that
    """
    fake_path = '/fake/path.txt'
    with patch.object(tkinter.filedialog, 'asksaveasfilename', return_value=fake_path):
        m_open = mock_open()
        with patch.object(builtins, 'open', m_open):
            navbar.save_as_file()

    m_open.assert_called_once_with(fake_path, 'w', encoding='utf-8')
    navbar.app.set_current_file.assert_called_once_with(fake_path)

def test_show_about(navbar):
    with patch.object(tkinter.messagebox, 'showinfo') as mock_info:
        navbar.show_about()

    mock_info.assert_called_once()

def test_show_shortcuts(navbar):
    with patch.object(tkinter.messagebox, 'showinfo') as mock_info:
        navbar.show_shortcuts()

    mock_info.assert_called_once()
