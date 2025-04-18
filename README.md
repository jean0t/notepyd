# Notepyd — Simple, Lightweight Notepad

Notepyd is an amazing notepad application because it focuses on being **simple** and containing only the **essential** features. The executable is extremely **lightweight** at just **12 MB**, making it fast to download and run without unnecessary bloat.

## Features

- **Minimal UI**: Only the core elements you need—menu bar, text area, info bar
- **Fast Startup**: Packed into a single 12 MB executable
- **Essential File Operations**: Open, Save, Save As
- **Live Stats**: Displays file name, word count, and character count in the info bar
- **Keyboard Shortcuts**: Ctrl+O, Ctrl+S, Ctrl+Z, Ctrl+Y

## File Organization

```
notepyd/
├── main.py            # Entry point: creates App instance and starts mainloop
├── app.py             # `App` class (Tk subclass) that wires menus, editor, and info bar
├── config.py          # Application constants (colors, sizes, fonts)
└── widgets/
    ├── navbar.py      # `Navbar` class (tk.Menu subclass) for file/about menus
    ├── editor.py      # `Editor` class (tk.Frame subclass) with Text + scrollbar
    └── infobar.py    # `InfoBar` class (tk.Frame subclass) for live stats
```

Each UI component is encapsulated in its own class (`tk.Menu`, `tk.Frame`, etc.), promoting **clean code**, **easy maintenance**, and **extensibility**.

## Installation

1. Go to the [Releases](https://github.com/jean0t/notepyd/releases) page and download the latest `notepyd-<version>.tar.gz`.
2. Extract it:
   ```bash
   tar xzf notepyd-<version>.tar.gz
   ```
3. (Optional) Install the desktop entry:
   - Copy the `.desktop` file to `~/.local/share/applications/`
   - In the `.desktop` file, set the correct paths for `Exec` and `Icon`:
     ```ini
     [Desktop Entry]
     Name=Notepyd
     Exec=/full/path/to/notepyd/notepyd
     Icon=/full/path/to/notepyd/icon.png
     Type=Application
     Categories=Utility;TextEditor;
     ```
4. Make sure the executable has permissions:
   ```bash
   chmod +x notepyd/notepyd
   ```
5. Launch from your application menu or:
   ```bash
   ~/notepyd/notepyd
   ```

## To-Do

- **User Customization**: Allow changing fonts, colors, and appearance themes
- Syntax highlighting for code snippets
- Tabbed editing for multiple documents
- Search and Replace functionality

---

Enjoy a distraction-free writing experience with Notepyd! Feel free to open issues or submit pull requests for new features.


