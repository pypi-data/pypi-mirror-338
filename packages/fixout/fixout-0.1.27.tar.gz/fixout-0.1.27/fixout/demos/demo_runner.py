"""
This is a demo of how to use the open-source version of FixOut
"""

from fixout.artifact import FixOutArtifact
from fixout.runner import FixOutRunner

from demo_data import importGermanData

def demo():
    
    model, X_train, X_test, y_train, y_test, features_name, dic = importGermanData()

    fxo = FixOutRunner("Credit Risk Assessment (German bank)") 

    #sensitive_features = [19,18,8] 
    sensitive_features = ["foreignworker","telephone","statussex"] 

    fxa = FixOutArtifact(model=model,
                         training_data=(X_train,y_train), 
                         testing_data=[(X_test,y_test,"Testing")],
                         features_name=features_name,
                         sensitive_features=sensitive_features,
                         dictionary=dic)
    
    fxo.run(fxa, show=True) 
    

if __name__ == '__main__':

    demo()