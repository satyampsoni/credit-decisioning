from loggerr import logger
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import pandas as pd

STAGE_NAME  = "Data Preprocessing"

class Datapreprocess:
    def __init__(self) -> None:
        pass
    def preprocess_data(self, data):
        data.dropna(inplace=True)
        data.drop(columns=["Loan_ID"], inplace=True)
        data["Loan_Amount_Term"] = data["Loan_Amount_Term"].fillna(data["Loan_Amount_Term"].mode()[0])


# Fill the missing values for categorical data.ddrfcc
        data["Gender"] = data["Gender"].fillna(data["Gender"].mode()[0])
        data["Married"] = data["Married"].fillna(data["Married"].mode()[0])
        data["Dependents"] = data["Dependents"].fillna(data["Dependents"].mode()[0])
        data["Self_Employed"] = data["Self_Employed"].fillna(data["Self_Employed"].mode()[0])
        
        label_encoder = preprocessing.LabelEncoder()
        data["Gender"] = label_encoder.fit_transform(data["Gender"])
        data["Married"] = label_encoder.fit_transform(data["Married"])
        data["Self_Employed"] = label_encoder.fit_transform(data["Self_Employed"])
        data["Property_Area"] = label_encoder.fit_transform(data["Property_Area"])
        data["Education"] = label_encoder.fit_transform(data["Education"])
        data["Loan_Status"] = label_encoder.fit_transform(data["Loan_Status"])
        
        
        st = StandardScaler()
        data["ApplicantIncome"] = st.fit_transform(data[["ApplicantIncome"]])
        
        preprocess_data = data
      
        path = "data/preprocess_data.csv"
        preprocess_data.to_csv(path)
        
        return path
        

if __name__ == "__main__":

    try:
        df = pd.read_csv("data/credit-data.csv")
        logger.info(f" >>>> stage {STAGE_NAME} <<<< started !")
        obj = Datapreprocess()
        preprocess_data = obj.preprocess_data(df)
        
        logger.info(f" >>>> stage {STAGE_NAME} <<<< Completed ! \n\n x==================x")
        
    except Exception as e:
        logger.exception(e)
        raise e