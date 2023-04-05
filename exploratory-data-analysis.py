# Imports
import numpy as np
import pandas as pd
from plotnine import *
from plotnine_prism import *
import dataframe_image as dfi


# Load data
df = pd.read_csv('homework/Stat_386/nba-draft-data/pick-data.csv')


# Image path
path = 'homework/Stat_386/nba-draft-data/images/'

# Making a theme template
def custom_theme():
    return (theme(panel_background = element_rect(fill = '#242629'),
                  plot_background = element_rect(fill = '#242629'),
                  legend_background = element_rect(fill = '#242629'),
                  legend_key = element_rect(fill = '#242629'),
                  text = element_text(color = 'white'),
                  axis_line = element_line(size = 0, color = '#242629'))) 


# Separate dataframes
## Simple stats
simple = df[['Pick','Years','Games','Minutes_pg']]
simple['Minutes'] = simple.Games * simple.Minutes_pg

## Shooting stats
shooting = df[['Pick','FieldGoal_pcent','ThreePoint_pcent','Freethrow_pcent']]

## Standard stats
standard = df[['Pick','Points_pg','Rebounds_pg','Assists_pg']]

## Advanced stats
advanced = df[['Pick','Winshares_p48','Box_plusminus','Value_over_replacement']]

## Aggregated Table
table = df.groupby(pd.cut(df.Pick, np.arange(0,61,10))).mean().drop('Pick', axis = 1).reset_index().round(decimals = 2).drop('Unnamed: 0', axis = 1)
table.Pick = ['1-10', '10-21', '21-30', '31-40', '41-50', '51-60']


# Used Graphs
## Table
dfi.export(table, path + 'overall-comparison-table.png', table_conversion = 'selenium')

## Standard stats comparisons
(ggplot(standard) +
 geom_smooth(aes('Pick','Points_pg'), color = '#F71480') +
 labs(title = 'Mean Points per Game by Pick', x = 'Pick', y = 'Points per game') +
 scale_color_prism(palette = 'candy_bright') +
 custom_theme()
 ).save(path + 'points_pg.png')
(ggplot(standard) +
 geom_smooth(aes('Pick','Rebounds_pg'), color = '#F71480') +
 labs(title = 'Mean Rebounds per Game by Pick', x = 'Pick', y = 'Rebounds per game') +
 scale_color_prism(palette = 'candy_bright') +
 custom_theme()
 ).save(path + 'rebounds_pg.png')
(ggplot(standard) +
 geom_smooth(aes('Pick','Assists_pg'), color = '#F71480') +
 labs(title = 'Mean Assists per Game by Pick', x = 'Pick', y = 'Assists per game') +
 scale_color_prism(palette = 'candy_bright') +
 custom_theme()
 ).save(path + 'assists_pg.png')

## Shooting Comparisons
shots = pd.melt(shooting, id_vars = ['Pick'])
shots.loc[shots.variable == 'FieldGoal_pcent', 'variable'] = 'Field Goal Percentage'
shots.loc[shots.variable == 'ThreePoint_pcent', 'variable'] = 'Three Point Percentage'
shots.loc[shots.variable == 'Freethrow_pcent', 'variable'] = 'Free Throw Percentage'
(ggplot(shots) +
 geom_jitter(aes('Pick', 'value', color = 'variable'), alpha = .35) +
 geom_smooth(aes('Pick', 'value', color = 'variable')) +
 labs(title = 'Shooting Percentage by Pick', x = 'Pick', y = 'Shooting Percentage') +
 custom_theme() +
 scale_color_prism(palette = 'candy_bright')
 ).save(path + 'shooting.png')

## Basic stats comparisons
(ggplot(simple) +
 geom_density(aes('Games'), color = '#F71480') +
 custom_theme() +
 labs(title = 'Games Played', y = 'Frequency') +
 scale_color_prism(palette = 'candy_bright')
 ).save(path + 'games_density.png')
(ggplot(simple) +
 geom_density(aes('Years'), color = '#F71480') +
 custom_theme() +
 labs(title = 'Years in the League', y = 'Frequency') +
 scale_color_prism(palette = 'candy_bright')
 ).save(path + 'years_density.png')
(ggplot(simple) +
 geom_density(aes('Minutes'), color = '#F71480') +
 custom_theme() +
 labs(title = 'Minutes Played', y = 'Frequency') +
 scale_color_prism(palette = 'candy_bright')
 ).save(path + 'minutes_density.png')

## Shooing Comparisons with minutes limit
shots = pd.melt(shooting.loc[simple.Minutes > 5000, :], id_vars = ['Pick'])
shots.loc[shots.variable == 'FieldGoal_pcent', 'variable'] = 'Field Goal Percentage'
shots.loc[shots.variable == 'ThreePoint_pcent', 'variable'] = 'Three Point Percentage'
shots.loc[shots.variable == 'Freethrow_pcent', 'variable'] = 'Free Throw Percentage'
(ggplot(shots) +
 geom_jitter(aes('Pick', 'value', color = 'variable'), alpha = .35) +
 geom_smooth(aes('Pick', 'value', color = 'variable')) +
 labs(title = 'Shooting Comparison by Pick with Minutes Floor') +
 custom_theme() +
 scale_color_prism(palette = 'candy_bright')
 ).save(path + 'shooting_with_minutes_restriction.png')

## Advanced Stats Comparisons
(ggplot(advanced) +
 geom_smooth(aes('Pick','Winshares_p48'), color = '#F71480') +
 geom_jitter(aes('Pick','Winshares_p48'), alpha = .35, color = '#F71480') +
 labs(title = 'Winshares per 48 Minutes by Pick', y = 'Winshare per 48 Minutes') +
 custom_theme()
 ).save(path + 'winshares_p48.png')
(ggplot(advanced) +
 geom_smooth(aes('Pick','Box_plusminus'), color = '#F71480') +
 geom_jitter(aes('Pick','Box_plusminus'), alpha = .35, color = '#F71480') +
 labs(title = 'Box Plus Minus by Pick', y = 'Box Plus Minus') +
 ylim(-30, 10) +
 custom_theme()
 ).save(path + 'box_plusminus.png')
(ggplot(advanced) +
 geom_smooth(aes('Pick','Value_over_replacement'), color = '#F71480') +
 geom_jitter(aes('Pick','Value_over_replacement'), alpha = .35, color = '#F71480') +
 labs(title = 'Value Over Replacement by Pick', y = 'Value Over Replacement') +
 custom_theme()
 ).save(path + 'value_over_replacement.png')
