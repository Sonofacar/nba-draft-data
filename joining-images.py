# Imports
import cv2

# Image path
path = '/home/carson/homework/Stat_386/nba-draft-data/images/'

# Standard Stats Comparisons
img1 = cv2.imread(path + 'points_pg.webp')
img2 = cv2.imread(path + 'rebounds_pg.webp')
img3 = cv2.imread(path + 'assists_pg.png')
result = cv2.hconcat([img1, img2, img3])
cv2.imwrite(path + 'final/standard_comparison.webp', result)

# Basic Stats Comparisons
img1 = cv2.imread(path + 'games_density.webp')
img2 = cv2.imread(path + 'years_density.webp')
img3 = cv2.imread(path + 'minutes_density.webp')
result = cv2.hconcat([img1, img2, img3])
cv2.imwrite(path + 'final/basic_comparison.webp', result)

# Advanced Stats Comparisons
img1 = cv2.imread(path + 'winshares_p48.webp')
img2 = cv2.imread(path + 'box_plusminus.webp')
img3 = cv2.imread(path + 'value_over_replacement.webp')
result = cv2.hconcat([img1, img2, img3])
cv2.imwrite(path + 'final/advanced_comparison.webp', result)
