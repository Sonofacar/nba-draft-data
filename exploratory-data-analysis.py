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
path = '~/homework/Stat_386/nba-draft-data'


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

## Standard stats comparisons
(ggplot(standard.groupby('Pick').mean().reset_index()) +
 geom_line(aes('Pick','Points_pg'), color = '#F71480') +
 labs(y = 'Points per game') +
 scale_color_prism(palette = 'candy_bright') +
 custom_theme()
 ).save(path + 'points_pg.png')
(ggplot(standard.groupby('Pick').mean().reset_index()) +
 geom_line(aes('Pick','Rebounds_pg'), color = '#F71480') +
 labs(y = 'Rebounds per game') +
 scale_color_prism(palette = 'candy_bright') +
 custom_theme()
 ).save(path + 'rebounds_pg.png')
(ggplot(standard.groupby('Pick').mean().reset_index()) +
 geom_line(aes('Pick','Assists_pg'), color = '#F71480') +
 labs(y = 'Assists per game') +
 scale_color_prism(palette = 'candy_bright') +
 custom_theme()
 ).save(path + 'assists_pg.png')


# Testing graphs
(ggplot(simple.groupby('Pick').mean().reset_index()) +
 geom_line(aes('Pick','Years'), color = 'green') +
 theme_prism(palette = 'fir') +
 custom_theme() +
 scale_color_prism(palette = 'candy_bright')
)

(ggplot(simple.groupby('Pick').mean().reset_index()) +
 geom_line(aes('Pick','Games')))
(ggplot(simple.groupby('Pick').mean().reset_index()) +
 geom_line(aes('Pick','Minutes_pg')))

(ggplot(shooting.groupby('Pick').mean().reset_index()) +
 geom_line(aes('Pick','FieldGoal_pcent')))
(ggplot(shooting.groupby('Pick').mean().reset_index()) +
 geom_line(aes('Pick','ThreePoint_pcent')))
(ggplot(shooting.groupby('Pick').mean().reset_index()) +
 geom_line(aes('Pick','Freethrow_pcent')))

(ggplot(standard.groupby('Pick').mean().reset_index()) +
 geom_line(aes('Pick','Points_pg')))
(ggplot(standard.groupby('Pick').mean().reset_index()) +
 geom_line(aes('Pick','Rebounds_pg')))
(ggplot(standard.groupby('Pick').mean().reset_index()) +
 geom_line(aes('Pick','Assists_pg')))

(ggplot(advanced.groupby('Pick').mean().reset_index()) +
 geom_line(aes('Pick','Winshares_p48')))
(ggplot(advanced.groupby('Pick').mean().reset_index()) +
 geom_line(aes('Pick','Box_plusminus')))
(ggplot(advanced.groupby('Pick').mean().reset_index()) +
 geom_line(aes('Pick','Value_over_replacement')))

(ggplot(shooting.loc[simple.Games > 40,:]) +
 geom_jitter(aes('Freethrow_pcent','FieldGoal_pcent')))

(ggplot(shooting.loc[simple.Minutes > 10000, :]) +
 geom_jitter(aes('Pick', 'FieldGoal_pcent'), alpha = .5, color = 'blue') +
 stat_smooth(aes('Pick', 'FieldGoal_pcent'), color = 'blue') +
 geom_jitter(aes('Pick', 'ThreePoint_pcent'), alpha = .5, color = 'green') +
 stat_smooth(aes('Pick', 'ThreePoint_pcent'), color = 'green') +
 geom_jitter(aes('Pick', 'Freethrow_pcent'), alpha = .5, color = 'red') +
 stat_smooth(aes('Pick', 'Freethrow_pcent'), color = 'red') +
 theme_classic()
 )

(ggplot(pd.melt(shooting.loc[simple.Minutes > 5000, :], id_vars = ['Pick'])) +
 geom_jitter(aes('Pick', 'value', color = 'variable'), alpha = .35) +
 geom_smooth(aes('Pick', 'value', color = 'variable')) +
 custom_theme() +
 scale_color_prism(palette = 'candy_bright')
 )

games_density = (ggplot(simple) +
                 geom_density(aes('Games')))
years_density = (ggplot(simple) +
                 geom_density(aes('Years')))
minutes_density = (ggplot(simple) +
                   geom_density(aes('Minutes')))
density_plots = (pw.load_ggplot(games_density)|pw.load_ggplot(years_density)|pw.load_ggplot(minutes_density))

table = df.groupby(pd.cut(df.Pick, np.arange(0,61,10))).mean().drop('Pick', axis = 1).reset_index().round(decimals = 2)
table.Pick = ['1-10', '10-21', '21-30', '31-40', '41-50', '51-60']
dfi.export(table, 'test.png', table_conversion = 'selenium')


(ggplot(simple) +
 geom_density(aes('Games')) +
 custom_theme() +
 labs(title = 'Games Played') +
 scale_fill_prism(palette = 'candy_bright')
 )
(ggplot(simple) +
 geom_density(aes('Years')) +
 custom_theme() +
 labs(title = 'Years in the League') +
 scale_fill_prism(palette = 'candy_bright')
 )
(ggplot(simple) +
 geom_density(aes('Minutes')) +
 custom_theme() +
 labs(title = 'Minutes Played') +
 scale_fill_prism(palette = 'candy_bright')
 ).save('test.png')
