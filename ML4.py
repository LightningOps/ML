import random, numpy as np
import NN
params = [100, 0.0005, 200, 3, 20]
curPop = np.random.choice(np.arange(-15,15,step=0.01),size=(params[0],params[3]),replace=False)
nextPop = np.zeros((curPop.shape[0], curPop.shape[1]))
fitVec = np.zeros((params[0], 2))
for i in range(params[2]):
    fitVec = np.array([np.array([x, np.sum(NN.costFunction(NN.X, NN.y, curPop[x].reshape(3,1)))]) for x in range(params[0])])
    print("(Gen: #%s) Total error: %s\n" % (i, np.sum(fitVec[:,1])))
    winners = np.zeros((params[4], params[3]))
    for n in range(len(winners)):
        selected = np.random.choice(range(len(fitVec)), params[4]/2, replace=False)
        wnr = np.argmin(fitVec[selected,1])
        winners[n] = curPop[int(fitVec[selected[wnr]][0])]
    nextPop[:len(winners)] = winners
    nextPop[len(winners):] = np.array([np.array(np.random.permutation(np.repeat(winners[:, x], ((params[0] - len(winners))/len(winners)), axis=0))) for x in range(winners.shape[1])]).T
    nextPop = np.multiply(nextPop, np.matrix([np.float(np.random.normal(0,2,1)) if random.random() < params[1] else 1 for x in range(nextPop.size)]).reshape(nextPop.shape))
    curPop = nextPop

best_soln = curPop[np.argmin(fitVec[:,1])]
X = np.array([[0,1,1],[1,1,1],[0,0,1],[1,0,1]])
result = np.round(NN.runForward(X, best_soln.reshape(3,1)))
print("Best Sol'n:\n%s\nCost:%s" % (best_soln,np.sum(NN.costFunction(NN.X, NN.y, best_soln.reshape(3,1)))))
print("When X = \n%s \nhThetaX = \n%s" % (X[:,:2], result,))
