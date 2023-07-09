library("readxl")
temp <- read_excel("temperature.xlsx")
library("dplyr")
library("ggplot2")

temp <- temp %>% mutate(year = as.numeric(substr(temp$Month[],1,4)), month = as.numeric(substr(temp$Month[],6,7)))
temp <- temp %>% mutate(season = ifelse(month == 12 | month == 1 | month == 2 , "winter",ifelse(month == 3 | month == 4 | month == 5 , "spring" , ifelse(month == 6 | month == 7 | month == 8, "summer","fall"))))
temp
temp1 <- temp %>% group_by(year,season) %>% summarise(mean_temp = mean(Mean),.groups = "drop_last") 
temp1 <- temp1 %>% filter(!is.na(mean_temp))
ggplot(temp1,aes(x=year,y=mean_temp,fill = season)) + geom_point(size = 1 , color = "red")
