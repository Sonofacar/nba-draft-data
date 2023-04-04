# Imports
import numpy as np
import pandas as pd
from plotnine import *
from plotnine_prism import *
import dataframe_image as dfi
import cv2


# Load data
df = pd.read_csv('homework/Stat_386/nba-draft-data/pick-data.csv')


# Image path
path = '~/homework/Stat_386/nba-draft-data/'


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
simple = simple.groupby('Pick').mean().reset_index()

## Shooting stats
shooting = df[['Pick','FieldGoal_pcent','ThreePoint_pcent','Freethrow_pcent']]
shooting = shooting.groupby('Pick').mean().reset_index()

## Standard stats
standard = df[['Pick','Points_pg','Rebounds_pg','Assists_pg']]
standard = standard.groupby('Pick').mean().reset_index()

## Advanced stats
advanced = df[['Pick','Winshares_p48','Box_plusminus','Value_over_replacement']]
advanced = advanced.groupby('Pick').mean().reset_index()

## Aggregated Table
table = df.groupby(pd.cut(df.Pick, np.arange(0,61,10))).mean().drop('Pick', axis = 1).reset_index().round(decimals = 2)
table.Pick = ['1-10', '10-21', '21-30', '31-40', '41-50', '51-60']


# Used Graphs
## Table
dfi.export(table, path + 'overall-comparison-table.png', table_conversion = 'selenium')

## Standard stats comparisons
(ggplot(standard.groupby('Pick').mean().reset_index()) +
 geom_line(aes('Pick','Points_pg'), color = '#F71480') +
 labs(title = 'Points per Game by Pick', y = 'Points per game') +
 scale_color_prism(palette = 'candy_bright') +
 custom_theme()
 ).save(path + 'points_pg.png')
(ggplot(standard.groupby('Pick').mean().reset_index()) +
 geom_line(aes('Pick','Rebounds_pg'), color = '#F71480') +
 labs(title = 'Rebounds per Game by Pick', y = 'Rebounds per game') +
 scale_color_prism(palette = 'candy_bright') +
 custom_theme()
 ).save(path + 'rebounds_pg.png')
(ggplot(standard.groupby('Pick').mean().reset_index()) +
 geom_line(aes('Pick','Assists_pg'), color = '#F71480') +
 labs(title = 'Assists per Game by Pick', y = 'Assists per game') +
 scale_color_prism(palette = 'candy_bright') +
 custom_theme()
 ).save(path + 'assists_pg.png')

## Shooting Comparisons
(ggplot(pd.melt(shooting, id_vars = ['Pick'])) +
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
 labs(title = 'Games Played') +
 scale_color_prism(palette = 'candy_bright')
 ).save(path + 'games_density.png')
(ggplot(simple) +
 geom_density(aes('Years'), color = '#F71480') +
 custom_theme() +
 labs(title = 'Years in the League') +
 scale_color_prism(palette = 'candy_bright')
 ).save(path + 'years_density.png')
(ggplot(simple) +
 geom_density(aes('Minutes'), color = '#F71480') +
 custom_theme() +
 labs(title = 'Minutes Played') +
 scale_color_prism(palette = 'candy_bright')
 ).save(path + 'minutes_density.png')

## Shooing Comparisons with minutes limit
(ggplot(pd.melt(shooting.loc[simple.Minutes > 5000, :], id_vars = ['Pick'])) +
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
 labs(title = 'Winshares per 48 Minutes by Pick') +
 custom_theme()
 ).save('winshares_p48.png')
(ggplot(advanced) +
 geom_smooth(aes('Pick','Box_plusminus'), color = '#F71480') +
 geom_jitter(aes('Pick','Box_plusminus'), alpha = .35, color = '#F71480') +
 labs(title = 'Box Plus Minus by Pick') +
 custom_theme()
 ).save('box_plusminus.png')
(ggplot(advanced) +
 geom_smooth(aes('Pick','Value_over_replacement'), color = '#F71480') +
 geom_jitter(aes('Pick','Value_over_replacement'), alpha = .35, color = '#F71480') +
 labs(title = 'Value Over Replacement by Pick') +
 custom_theme()
 ).save('value_over_replacement.png')
