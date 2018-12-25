library(data.table)

path_train <- getwd()
path_train = paste(path_train, 'datasets/train.csv', sep='/')
train_raw <- fread(file=path_train, header=TRUE, sep=",")
head(train_raw, 5)
