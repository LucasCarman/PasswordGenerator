from nicegui import ui
from passwordgenerator import *
from asyncio import *

async def copyPass():
    ui.notify("Password Copied")
    await ui.run_javascript(f'navigator.clipboard.writeText(getElement({resultLabel.id}).innerText)')

async def create():
    passwordResult = str(createPassword(lengthSelect.value, upperCheck.value))
    await ui.run_javascript(f'getElement({resultLabel.id}).innerText = "{passwordResult}"')

async def copy_text():
    await ui.run_javascript()
with ui.left_drawer(top_corner=True, bottom_corner=True).style('background-color: black'):
     ui.label()
with ui.right_drawer(top_corner=True, bottom_corner=True).style('background-color: black'):
     ui.label()
with ui.header().style('margin:auto;'):
        ui.label('Password Generator').style('margin:auto')
with ui.column().style('margin: auto').classes('items-center'):
    lengthSelect = ui.select([6, 7, 8, 9, 10, 11, 12], value=6)
    upperCheck = ui.checkbox('Upper Case Included?')
    createButton = ui.button('CREATE', on_click= create)
    resultLabel = ui.label()
    copyButton = ui.button("Copy Password", on_click=copyPass)
ui.colors(primary="#9f0b1a", accent="#555")
ui.run()