from nicegui import ui
import care_json

def root():
    ui.separator()
    ui.sub_pages({'/': main, '/HistoryPage': hist_page, '/BotSettingsPage': bot_settings_page})

def main():
    ui.label('Main page content')
    ui.label('Welcome to the Discord Bot checker')
    ui.link('Go to History page', '/HistoryPage')
    ui.link('Go to Bot Settings page', '/BotSettingsPage')


def hist_page():
    ui.label('History page content')
    ui.link('Go to main page', '/')

    grid = ui.aggrid({
        'columnDefs': [
            {'headerName': 'Time', 'field': 'time', 'filter': 'agTextColumnFilter', 'floatingFilter': True},
            {'headerName': 'Operation', 'field': 'operation', 'filter': 'agTextColumnFilter', 'floatingFilter': True, 'cellClassRules': {
            'bg-yellow-300': 'x=="kick"',
            'bg-red-300': 'x=="ban"',
            'bg-green-300': 'x==="timeout"',
        }},
            {'headerName': 'Pfp', 'field': 'avatar_url','filter': 'agTextColumnFilter', 'floatingFilter': False},
            {'headerName': 'Username', 'field': 'username', 'filter': 'agTextColumnFilter', 'floatingFilter': True}
        ],
        'rowData': care_json.get_history(),
        'rowSelection': {'mode': 'multiRow'},
    }).classes('w-[calc(100vh-2rem)] ')

    def update():
        grid.options['rowData'][0]['state'] += 1

def bot_settings_page():
    ui.label('Bot settings page content')
    ui.link('Go to main page', '/')

    time_dur = 0
    tries_before_kick = 0
    tries_before_ban = 0

    def user_input():
        ui.input(label="timeout duration:",
                 validation={"invalid input": lambda value: int(value) > -1 if value.isdigit() else False},
                 on_change=lambda x: care_json.save_timeout_duration(x.value), value=0).props(
            'rounded outlined dense')
        ui.input(label="how many tries before kick: ", value=-1,
                 validation={"invalid input": lambda value: int(value) >= -1 if value.isdigit() else False},
                 on_change=lambda x: care_json.save_kick_amount(x.value)).props(
            'rounded outlined dense')
        ui.input(label="how many tries before ban: ", value=-1,
                 validation={"invalid input": lambda value: int(value) >= -1 if value.isdigit() else False},
                 on_change=lambda x: care_json.save_ban_amount(x.value)).props(
            'rounded outlined dense')

    def input_saving_timeout(x):
        global time_dur
        time_dur = x
        print("time, ", time_dur)

    def input_saving_kick(x):
        global tries_before_kick
        tries_before_kick = x
        print("kick,", tries_before_kick)

    def input_saving_ban(x):
        global tries_before_ban
        tries_before_ban = x
        print("ban, ", tries_before_ban)

    user_input()

ui.run(root)