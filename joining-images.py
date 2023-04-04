# Imports
import cv2

# Image path
path = '~/homework/Stat_386/nba-draft-data/'

# Standard Stats Comparisons
img1 = cv2.imread(path + 'points_pg.webp')
img2 = cv2.imread(path + 'rebounds_pg.webp')
img3 = cv2.imread(path + 'assists_pg.png')
result = cv2.hconcat([img1, img2, img3])
cv2.imwrite(path + 'standard_comparison.webp')

# Basic Stats Comparisons
img1 = cv2.imread(path + 'games_density.webp')
img2 = cv2.imread(path + 'years_density.webp')
img3 = cv2.imread(path + 'minutes_density.webp')
result = cv2.hconcat([img1, img2, img3])
cv2.imwrite(path + 'basic_comparison.webp')

# Advanced Stats Comparisons
img1 = cv2.imread(path + 'winshares_p48.webp')
img2 = cv2.imread(path + 'box_plusminus.webp')
img3 = cv2.imread(path + 'value_over_replacement.webp')
result = cv2.hconcat([img1, img2, img3])
cv2.imwrite(path + 'advanced_comparison.webp')
