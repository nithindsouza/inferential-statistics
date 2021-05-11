library(readxl)
data <- read_excel("C:\\Users\\hp\\Desktop\\inferentialStatsQ7.xlsx")

#plotting boxplot
boxplot(data$`Measure X`)
#there are outliers
#right skewed 

#measures of centrality
summary(data)

#measure of spread
var(data$`Measure X`)
sd(data$`Measure X`)
