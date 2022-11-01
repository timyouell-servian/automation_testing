import pandas as pd
import requests
import datetime as dt

base_url = 'https://fantasy.premierleague.com/api/'

def get_bootstrap_data() -> dict:
    """
    Options
    -------
        ['element_stats']
        ['element_types']
        ['elements']
        ['events']
        ['game_settings']
        ['phases']
        ['teams']
        ['total_players']
    """
    resp = requests.get(f'{base_url}bootstrap-static/')
    if resp.status_code != 200:
        raise Exception(f'Response was status code {resp.status_code}')
    else:
        return resp.json()
    

ele_df = pd.DataFrame(get_bootstrap_data()['elements'])

eh_df = ele_df.loc[ele_df['second_name'] == 'Haaland']

new_df = pd.DataFrame({'Name': [eh_df['second_name'].iloc[0]],
                       'TSB%': [eh_df['selected_by_percent'].iloc[0]],
                       'T_In_GW': [eh_df['transfers_in_event'].iloc[0]],
                       'T_Out_GW': [eh_df['transfers_out_event'].iloc[0]],
                       'datetime': dt.datetime.now()})

# save df once

# open df, append and save

# run via GitHub Actions



