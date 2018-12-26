############                         ############
############   aviation-fatalities   ############
############                         ############

#Imports
library(data.table)

# Read from csv and display first 5 lines
path_train <- getwd()
path_train = paste(path_train, 'datasets/train.csv', sep='/')
train_raw <- fread(file=path_train, header=TRUE, sep=",")
head(train_raw, 5)

# check for missing values
sapply(train_raw, function(x) sum(is.na(x)))

# print some basical statistics on this data.frame
summary(train_raw)


