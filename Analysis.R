setwd('~/Programming/LaTeX/Assignments/STAT 841/Final Project')

# Reading in Data
load('tfidf_raw.rdata')
x.copy <- x_raw; y.copy <- y_raw;

# Activation function
act = function(x){
  (1+exp(-x))^(-1)*(1-(1+exp(-x))^(-1))
}


# The function nnet tries to fit a model via neural network.
# The activation function will be logit transform, where
# x is the nxp covariate of the labels, where n is the
#   number of observations, and p is the number of 
# y is a vector of labels
# lambda is the learning rate. Default is 0.01
# rho is the weight parameter. Default is 0,005
# epoch is the number of iteration of the neural network
# seed is the seed to generate random numbers. Default number is 7.
nnet = function(x,y,lambda = 0.01, rho = 0.005, epoch = 10, seed = 7){
  # Setting seed
  set.seed(seed);
  # Defining variables
  n <- nrow(x); p <- ncol(x);
  x <- as.matrix(x);
  W01 <- matrix(data = runif(n = 4*p,min = 0, max = 0.01)
               , nrow = p, ncol = 4);
  W12 <- matrix(data = runif(n = 8, min = 0, max = 0.01)
                , nrow = 4, ncol = 2);
  W23 <- matrix(data = runif(n = 2,min = 0, max = 0.01),
                , nrow = 2, ncol = 1)
  
  for(i in 1:epoch){
    # Forward propagation
    z0 <- x;
    a1 <- z0%*%W01;
    z1 <- apply(X = a1, MARGIN = c(1,2), FUN = function(x){1/(1+exp(-x))});
    a2 <- z1%*%W12;
    z2 <- apply(X = a2, MARGIN = c(1,2), FUN = function(x){1/(1+exp(-x))});
    a3 <- z2 %*% W23;
    # Returning initial yhat
    yhat <- a3;
    
    # Back Propagation
    for(j in 1:n){
      Delta3 <- -2*(y-yhat);
      Delta2 <- (apply(X = a2, MARGIN = c(1,2), FUN = 'act') %*% W23) %*% t(Delta3);
      Delta2_j <- Delta2[,j];
      Delta1 <- apply(X = a1, MARGIN = c(1,2), FUN = 'act') * (t(t(as.vector(rowSums(W12))*Delta2_j)) %*% (rep.int(1,times = 4)));
      
      # Updating weights
      W23 <- W23 - lambda*(t(z2) %*% Delta3 + 2 * rho * W23);
      W12 <- W12 - lambda*(t(z1) %*% t(t(Delta2_j)) %*% rep.int(x = 1, times = 2 ) + 2 * rho * W12);
      W01 <- W01 - lambda*(t(z0) %*% Delta1 + 2 * rho * W01);
    }
    print(yhat)
  }
#  yhat <- as.integer(yhat);
  err <- length(which(yhat != y))/n;
  out <- list(error = err,yhat = yhat);
  
}