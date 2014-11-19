setwd('~/Programming/LaTeX/Assignments/STAT 841/Final Project')

# Reading in raw data
options(stringsAsFactors = F)
# library(data.table)
# p.raw <- fread(input = 'phrases_raw_counts.csv')
#p.raw <- read.csv('phrases_raw_counts.csv',header = T)
#p_tfidf.raw <- read.csv('phrases_tfidf.csv',header = T)
# s.raw <- read.csv('sentences_raw_counts.csv',header = T)
# s_tfidf.raw <- read.csv('sentences_tfidf.csv',header = T)

# Copy of the data
#p.copy <- p.raw
#p_tfidf.copy <- p_tfidf.raw
# s.copy <- s.raw
# s_tfidf.copy <- s_tfidf.raw

# Separate the data into 10 subfiles
write.csv(s.raw[1:853,],file = 's_raw_counts1.csv')
write.csv(s.raw[854:1706,],file = 's_raw_counts2.csv')
write.csv(s.raw[1707:2559,],file = 's_raw_counts3.csv')
write.csv(s.raw[2560:3412,],file = 's_raw_counts4.csv')
write.csv(s.raw[3413:4265,],file = 's_raw_counts5.csv')
write.csv(s.raw[4266:5118,],file = 's_raw_counts6.csv')
write.csv(s.raw[5119:5971,],file = 's_raw_counts7.csv')
write.csv(s.raw[5972:6824,],file = 's_raw_counts8.csv')
write.csv(s.raw[6825:7676,],file = 's_raw_counts9.csv')
write.csv(s.raw[7677:8528,],file = 's_raw_counts10.csv')
################################################################
write.csv(s_tfidf.raw[1:853,],file = 's_tfidf1.csv')
write.csv(s_tfidf.raw[854:1706,],file = 's_tfidf2.csv')
write.csv(s_tfidf.raw[1707:2559,],file = 's_tfidf3.csv')
write.csv(s_tfidf.raw[2560:3412,],file = 's_tfidf4.csv')
write.csv(s_tfidf.raw[3413:4265,],file = 's_tfidf5.csv')
write.csv(s_tfidf.raw[4266:5118,],file = 's_tfidf6.csv')
write.csv(s_tfidf.raw[5119:5971,],file = 's_tfidf7.csv')
write.csv(s_tfidf.raw[5972:6824,],file = 's_tfidf8.csv')
write.csv(s_tfidf.raw[6825:7676,],file = 's_tfidf9.csv')
write.csv(s_tfidf.raw[7677:8528,],file = 's_tfidf10.csv')

# Dimensionality reduction

