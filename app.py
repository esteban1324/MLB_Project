import streamlit as st
from baseball import get_hitter_stats, get_pitcher_stats, get_statcast_pitcher_stats, get_statcast_batter_stats
from visuals import plot_pitching_stats, plot_pitching_stats2, plot_batting_stats, plot_batting_stats2


st.title('Player Performance Dashboard')
pitcher = st.text_input("Enter Pitcher Name", None)
hitter = st.text_input("Enter Hitter Name", None)
start_year = st.number_input('Year', min_value=1990, max_value=2025, value=2024)
end_year = st.number_input('End Year', min_value=1990, max_value=2025, value=2024)
show_statcast_hitter = st.checkbox('Show Statcast Hitter Data')
show_statcast_pitcher = st.checkbox('Show Statcast Pitcher Data')

# Initialize session state for button clicks
if 'hitter_button_clicked' not in st.session_state:
    st.session_state.hitter_button_clicked = False
    
if 'pitcher_button_clicked' not in st.session_state:
    st.session_state.pitcher_button_clicked = False
 
if st.button('Show Hitter Stats') and hitter:
    st.session_state.hitter_button_clicked = True

if st.button('Show Pitcher Stats') and pitcher:
    st.session_state.pitcher_button_clicked = True
 
 
if st.session_state.hitter_button_clicked and hitter:
    first_name, last_name = hitter.split()
    hitter_stats = get_hitter_stats(first_name, last_name, start_year, end_year)
    st.write(hitter_stats)
    st.plotly_chart(plot_batting_stats(hitter_stats))
    st.plotly_chart(plot_batting_stats2(hitter_stats))
    
    # insert start and end date for statcast data
    if show_statcast_hitter:
        start_date = st.text_input('Start Date')
        end_date = st.text_input('End Date')
        
        # if dates are entered, show statcast data
        if start_date and end_date:
            statcast_data = get_statcast_batter_stats(first_name, last_name, start_date, end_date)
            st.write(statcast_data)  
    

if st.session_state.pitcher_button_clicked and pitcher:
    first_name, last_name = pitcher.split()
    pitcher_stats = get_pitcher_stats(first_name, last_name, start_year, end_year)
    st.write(pitcher_stats)
    st.plotly_chart(plot_pitching_stats(pitcher_stats))
    st.plotly_chart(plot_pitching_stats2(pitcher_stats))

    # insert start and end date for statcast data
    if show_statcast_pitcher:
        start_date = st.text_input('Start Date')
        end_date = st.text_input('End Date')

        
        # if dates are entered, show statcast data
        if start_date and end_date:
            statcast_data = get_statcast_pitcher_stats(first_name, last_name, start_date, end_date)
            st.write(statcast_data)  