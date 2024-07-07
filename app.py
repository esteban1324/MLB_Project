import streamlit as st
from MLB_Project.baseball import get_hitter_stats, get_pitcher_stats
#from visuals import plot_hitter_stats, plot_pitcher_stats

st.title('Player Performance Dashboard')
# Enter either a Pitcher or Hitter of your choice 
pitcher = st.text_input("Enter Pitcher Name", None)
hitter = st.text_input("Enter Hitter Name", None)
start_year = st.number_input('Year', min_value=1990, max_value=2024, value=2023)
end_year = st.number_input('End Year', min_value=1990, max_value=2024, value=2023)

if st.button('Show Hitter Stats') and hitter:
    first_name, last_name = hitter.split()
    hitter_stats = get_hitter_stats(first_name, last_name, start_year, end_year)
    st.write(hitter_stats)
    #plot_hitter_stats(hitter_stats)
    
if st.button('Show Pitcher Stats') and pitcher:
    first_name, last_name = pitcher.split()
    pitcher_stats = get_pitcher_stats(first_name, last_name, start_year, end_year)
    st.write(pitcher_stats)
    #plot_pitcher_stats(pitcher_stats)