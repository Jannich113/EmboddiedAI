from cProfile import label
from statistics import linear_regression
from turtle import color
import numpy as np
from sklearn.linear_model import RANSACRegressor, LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt



class RANSAC():


    def __init__(self,data_X,data_y) -> None:
        self.X = data_X
        self.y = data_y



    def LinearReg(self):
        # init 
        regressor = LinearRegression()
        # fitting simple linear regression to the data set
        regressor.fit(self.X, self.y)
        predictions_linear_Reg = regressor.predict(self.X)
        print(r2_score(self.y, predictions_linear_Reg))
        self.plotData(self.X, self.y, regressor.predict(self.X), 'Linear Reg')



    def RansacReg(self):
        #init ransac
        Ransac = RANSACRegressor()

        Ransac.fit(self.X, self.y)

        #inlier mask
        inlier_mask = Ransac.inlier_mask_
        print(inlier_mask)

        # count number of outliers 
        count = 0
        for i in inlier_mask:
            if i == False:
                count +=1

        ## print the number of inliers and outliers if wanted

        # prediction the output 
        predictions_Ransac = Ransac.predict(self.X)

        # R^2 score for evaluating the model performance 
        print(r2_score(self.y, predictions_Ransac))
        # plot the data
        self.plotData(self.X, self.y, predictions_Ransac, 'Ransac')
        


    def plotData(X_da,y_da, reg, n: str):
        # setting the size of the figure 
        plt.figure(figsize=(10,8))
        # plotting scatter plot of the data 
        plt.scatter(X_da,y_da)

        plt.plot(X_da, reg, color='green', label=n)
        plt.title('Line fit')
        plt.xlabel('x axis')
        plt.ylabel('y axis')
        plt.legend()
        plt.show

    