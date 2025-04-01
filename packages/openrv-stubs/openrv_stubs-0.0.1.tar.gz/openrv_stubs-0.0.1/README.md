# Open RV Python Stubs

Type annotated stubs for Open RV's Python API. Work in progress so use at your own risk!

Should be compatible with paid RV as the code base for both Open RV and RV should be from the same source (excluding specific changes for RV that is not available to public).

Currently missing docstring explanation so refer to the built-in help menu:

![mu_menu.png](docs%2Fimages%2Fmu_menu.png)

Fun Trivia: The `rv.commands` is a wrapper for Mu commands:

![mu_api_browser.png](docs%2Fimages%2Fmu_api_browser.png)

## Quick setup

Copy `commands.pyi` to `<openrv_path>/PlugIns/Python/rv`. Take note the `PlugIns` name can also be `plugins` or `Plugins`. Guess it is a quirk for supporting cross-platform application between Linux, macOS and Windows.

![openrv_plugins_path.png](docs%2Fimages%2Fopenrv_plugins_path.png)

PyCharm should automatically detect the `.pyi` stubs and provide autocompletion with type hints:

![pycharm_autocomplete.gif](docs%2Fimages%2Fpycharm_autocomplete.gif)

## TODO

1. Publish to PyPI.
2. Implement the other RV modules with type hints.

## Rant

1. There is no way to browse the Mu's manual outside the API browser despite it being a Qt Web Browser. Need to write a parser that analyse the docs from Open RV's source code to generate the docstring for the respective Mu's command. Not sure on the legality on 'scrapping' the source code docstring but navigating the Mu's API Browser is hellish.
2. The current stubs is manually hand-generated but suffice for my requirements for PyCharm/VS Code to autocomplete and provide the required type hints.
3. Yet another Python stubs. At least this ease my frustration when writing Python tools that requires interaction with Open RV. 
