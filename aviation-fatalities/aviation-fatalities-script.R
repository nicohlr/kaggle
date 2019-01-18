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

# list occurences of all values of "event" column
table(unlist(train_raw$event))

# convert categorical variable "event" into numerical variable
train_raw$event <- as.numeric(factor(train_raw$event, levels=unique(train_raw$event)))
head(train_raw$event)

# Plots
boxplot(split(train_raw$r, train_raw$event), main='Event by respiration')
boxplot(split(train_raw$ecg, train_raw$event), main='Event by electrocardiogram')


