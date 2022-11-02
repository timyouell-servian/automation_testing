import pandas as pd
import requests
import datetime as dt
import csv

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
    



# save df once
# new_df.to_csv(os.getcwd() + '/data/haaland_transfers.csv', index=False)

# open df, append and save


def get_trans_in():
    ele_df = pd.DataFrame(get_bootstrap_data()['elements'])
    eh_df = ele_df.loc[ele_df['second_name'] == 'Haaland']
    new_df = pd.DataFrame({'Name': [eh_df['second_name'].iloc[0]],
                           'TSB%': [eh_df['selected_by_percent'].iloc[0]],
                           'T_In_GW': [eh_df['transfers_in_event'].iloc[0]],
                           'T_Out_GW': [eh_df['transfers_out_event'].iloc[0]],
                           'datetime': dt.datetime.now()})
    return new_df['T_In_GW'][0]

# run via GitHub Actions

def get_data_row():
    ele_df = pd.DataFrame(get_bootstrap_data()['elements'])
    eh_df = ele_df.loc[ele_df['second_name'] == 'Haaland']
    data = {'Name': eh_df['second_name'].iloc[0],
            'TSB%': eh_df['selected_by_percent'].iloc[0],
            'T_In_GW': eh_df['transfers_in_event'].iloc[0],
            'T_Out_GW': eh_df['transfers_out_event'].iloc[0],
            'datetime': dt.datetime.now()}
    return data


def append_data():
    with open('data/haaland_transfers.csv', "r") as f:
        reader = csv.reader(f)
        for header in reader:
            break
    
    myDict = get_data_row()
    # add row to CSV file
    with open('data/haaland_transfers.csv', "a", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writerow(myDict)
    

def main():
    t_in = get_trans_in()
    print('Total transfers in for Erling Haaland this GW is: ' + str(t_in))
    append_data()
    print('Data appended!')
    

if __name__ == "__main__":
    main()
