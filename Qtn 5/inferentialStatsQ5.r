library(readr)
df <- read_csv("C:\\Users\\hp\\Desktop\\inferentialStatsQ5.csv")

#dropping first column
df <- df[,2:3]

#mean median and range of data
summary(df)

#variance and standard deviation
var(df$Points)
var(df$Score)
sd(df$Points)
sd(df$Score)
