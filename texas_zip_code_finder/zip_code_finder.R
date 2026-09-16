library(tidyverse)

zips <- read.csv('zip_code_finder.csv')

# # Remove the word "county"
# zips <- zips %>% 
#     mutate(county = str_replace(county, ' County', ''))


# What county is that zip code in?
zips %>% 
    filter(zip_code == 78574)

# Which counties are in that city?
zips %>% 
    filter(city == 'San Antonio')



# Overwrite the old file with county edit
write.csv(zips, 'C:/Users/dusty/OneDrive/Documents/data_science_resources/zip_code_finder.csv')
