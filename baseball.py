#!/usr/bin/python3
from pybaseball import  statcast_pitcher, statcast_batter 
from pybaseball import playerid_lookup, batting_stats, pitching_stats

'''Fangraphs Data for hitting and pitching'''

def get_player_id(first_name, last_name):
    return playerid_lookup(last_name, first_name).iloc[0]['key_fangraphs']

def get_hitter_stats(first_name, last_name, start_year, end_year):
    hitter_id = get_player_id(first_name, last_name)
    hitting_df = batting_stats(start_year, end_year, ind=1)
    hitter_info = hitting_df[hitting_df['IDfg'] == hitter_id]
    mod_stats = hitter_info[['HR', 'AVG', 'OPS', 'wRC+', 'WAR', 
                             'GB%', 'FB%', 'K%', 'BB%', 'Barrel%', 'HardHit%']]
    return mod_stats

def get_pitcher_stats(first_name, last_name, start_year, end_year):
    pitcher_id = get_player_id(first_name, last_name)
    pitching_df = pitching_stats(start_year, end_year, ind=1)
    # mod_stats for pitching 
    pitcher_info = pitching_df[pitching_df['IDfg'] == pitcher_id]
    mod_stats = pitcher_info[['ERA', 'xERA', 'FIP', 'xFIP', 
                            'FB%', 'GB%', 'LD%', 'K%', 'BB%', 'K/9', 'Barrel%', 'HardHit%']]
    return mod_stats

'''extracting statcast hitting and pitching data from MLB players '''

def get_statcast_pitcher_stats(first_name, last_name, start_date, end_date):
    id = playerid_lookup(last_name,first_name)['key_mlbam'].iloc[0]
    statcast_df = statcast_pitcher(start_date, end_date,  id)
    statcast_df = statcast_df[['player_name','pitch_type',
                           'game_date', 'release_speed', 'release_pos_x', 'release_pos_z', 'launch_speed', 
                           'launch_angle', 'effective_speed', 'release_spin_rate', 'release_extension', 
                           'release_pos_y', 'estimated_ba_using_speedangle', 'estimated_woba_using_speedangle', 
                            'babip_value', 'launch_speed_angle', 
                           'at_bat_number', 'pitch_number', 'pitch_name', 
                           ]]
    return statcast_df
    

def get_statcast_batter_stats(first_name, last_name, start_date, end_date):
    id = playerid_lookup(last_name,first_name)['key_mlbam'].iloc[0]
    statcast_df = statcast_batter(start_date, end_date,  id)
    statcast_df = statcast_df[['player_name','pitch_type',
                           'game_date', 'release_speed', 'release_pos_x', 'release_pos_z', 'launch_speed', 
                           'launch_angle', 'effective_speed', 'release_spin_rate', 'release_extension', 
                           'release_pos_y', 'estimated_ba_using_speedangle', 'estimated_woba_using_speedangle', 
                            'babip_value', 'launch_speed_angle', 
                           'at_bat_number', 'pitch_number', 'pitch_name', 
                           ]]
    return statcast_df






    







