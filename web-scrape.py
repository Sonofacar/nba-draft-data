# Imports
import pandas as pd
import time

# Standard variables
base_url      = 'https://www.basketball-reference.com/draft/NBA_'
Years         = ['2018','2017','2016','2015','2014','2013','2012','2011','2010','2009','2008','2007','2006','2005','2004']
base_url_end  = '.html'
final_columns = ['Pick',
                 'Years',
                 'Games',
                 'Minutes',
                 'FieldGoal_pcent',
                 'ThreePoint_pcent',
                 'Freethrow_pcent',
                 'Minutes_pg',
                 'Points_pg',
                 'Rebounds_pg',
                 'Assists_pg',
                 'Winshares',
                 'Winshares_p48',
                 'Box_plusminus',
                 'Value_over_replacement']
column_names  = ['Rank',
                'Pick',
                'Team',
                'Player',
                'College',
                'Years',
                'Games',
                'Minutes',
                'Points',
                'Rebounds',
                'Assists',
                'FieldGoal_pcent',
                'ThreePoint_pcent',
                'Freethrow_pcent',
                'Minutes_pg',
                'Points_pg',
                'Rebounds_pg',
                'Assists_pg',
                'Winshares',
                'Winshares_p48',
                'Box_plusminus',
                'Value_over_replacement']


# Initializing lists for growing
picks            = []
years            = []
games            = []
minutes          = []
fieldgoal_pcent  = []
threepoint_pcent = []
freethrow_pcent  = []
minutes_pg       = []
points_pg        = []
rebounds_pg      = []
assists_pg       = []
winshares        = []
winshare_p48     = []
box_plusminus    = []
value_over_rep   = []

# main web-scraping loop
for i in Years:
    # Form the url and pull data
    url = base_url + i + base_url_end
    df = pd.read_html(url)[0]
    df.columns = column_names
    df = df.drop([30,31], axis = 0)
    df = df.drop(['Rank','College','Team','Points','Rebounds','Assists'], axis = 1)
    df = df.fillna(0)
    df = df.reset_index(drop = True)
    if (i == '2004'):
        df = df.drop([29], axis = 0)

    # Using the correct types
    df['Pick'] = df['Pick'].astype(int)
    df['Years'] = df['Years'].astype(int)
    df['Games'] = df['Games'].astype(int)
    df['Minutes'] = df['Minutes'].astype(int)
    df['FieldGoal_pcent'] = df['FieldGoal_pcent'].astype(float)
    df['ThreePoint_pcent'] = df['ThreePoint_pcent'].astype(float)
    df['Freethrow_pcent'] = df['Freethrow_pcent'].astype(float)
    df['Minutes_pg'] = df['Minutes_pg'].astype(float)
    df['Points_pg'] = df['Points_pg'].astype(float)
    df['Rebounds_pg'] = df['Rebounds_pg'].astype(float)
    df['Assists_pg'] = df['Assists_pg'].astype(float)
    df['Winshares'] = df['Winshares'].astype(float)
    df['Winshares_p48'] = df['Winshares_p48'].astype(float)
    df['Box_plusminus'] = df['Box_plusminus'].astype(float)
    df['Value_over_replacement'] = df['Value_over_replacement'].astype(float)

    # Globalize the lists
    global picks
    global years
    global games
    global minutes
    global fieldgoal_pcent
    global threepoint_pcent
    global freethrow_pcent
    global minutes_pg
    global points_pg
    global rebounds_pg
    global assists_pg
    global winshares
    global winshare_p48
    global box_plusminus
    global value_over_rep

    # Growing lists
    picks.extend(list(df.Pick))
    years.extend(list(df.Years))
    games.extend(list(df.Games))
    minutes.extend(list(df.Minutes))
    fieldgoal_pcent.extend(list(df.FieldGoal_pcent))
    threepoint_pcent.extend(list(df.ThreePoint_pcent))
    freethrow_pcent.extend(list(df.Freethrow_pcent))
    minutes_pg.extend(list(df.Minutes_pg))
    points_pg.extend(list(df.Points_pg))
    rebounds_pg.extend(list(df.Rebounds_pg))
    assists_pg.extend(list(df.Assists_pg))
    winshares.extend(list(df.Winshares))
    winshare_p48.extend(list(df.Winshares_p48))
    box_plusminus.extend(list(df.Box_plusminus))
    value_over_rep.extend(list(df.Value_over_replacement))

    # Sleep for 3 seconds according to robots.txt
    time.sleep(3)

data = pd.DataFrame(list(zip(picks,
                             years,
                             games,
                             minutes,
                             fieldgoal_pcent,
                             threepoint_pcent,
                             freethrow_pcent,
                             minutes_pg,
                             points_pg,
                             rebounds_pg,
                             assists_pg,
                             winshares,
                             winshare_p48,
                             box_plusminus,
                             value_over_rep)), columns = final_columns)
data.to_csv('homework/Stat_386/post-3/pick-data.csv')
