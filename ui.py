# import nicegui
from nicegui import ui

ui.label('Blocked ussers:')


blocked_users=["kobi", "dani"]
users=" ".join(blocked_users)
ui.label(users)#

ui.button('Menu', on_click=lambda: ui.notify('button was pressed'))
ui.button('History', on_click=lambda: ui.notify('button was pressed'))
ui.button('Bot settings', on_click=lambda: ui.notify('button was pressed'))


ui.run()