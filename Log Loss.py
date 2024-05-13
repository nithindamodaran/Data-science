from sklearn.metrics import log_loss
y_true=[0,1,1,0]
y_pred=[0.1,0.7,0.8,0.2]

loss =log_loss(y_true, y_pred)
print('log loss:',loss)

