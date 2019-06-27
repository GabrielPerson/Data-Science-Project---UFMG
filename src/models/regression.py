import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import linear_model 

class NFLRegression:

    TARGET = "CarAV"

    POSITION_FEATURES = {
        "FB": ['St','G','Rush_Att','Rush_Yds','Rush_TDs','Rec','Rec_Yds','Rec_Tds','carrer_years'],
        # "QB": ['St','G','Cmp','Pass_Att','Pass_Yds','Pass_TD','Pass_Int','Rush_Att','Rush_Yds','Rush_TDs','carrer_years'],
        # "WR": ['St','G','Rush_Att','Rush_Yds','Rush_TDs','Rec','Rec_Yds','Rec_Tds','carrer_years'],
        "RB": ['St','G','Rush_Att','Rush_Yds','Rush_TDs','Rec','Rec_Yds','Rec_Tds','carrer_years'],
        # "TE": ['St','G','Rec','Rec_Yds','Rec_Tds','carrer_years'],
        # "DE": ['St','G','Tkl','Def_Int','Sk','carrer_years'],
        "DT": ['St','G','Tkl','Def_Int','Sk','carrer_years'],
        "LB": ['St','G','Tkl','Def_Int','Sk','carrer_years'],
        "DB": ['St','G','Tkl','Def_Int','Sk','carrer_years'],
    }

    def __init__(self):
        self.df_draft = pd.read_csv('~/Projects/projeto_icd/data/clean_nfl_draft.csv', sep=',')
    
    def build_models(self):
        scores = dict()
        for position, features in self.POSITION_FEATURES.items():
            df = self.df_draft[self.df_draft["Pos"] == position]
            X = df[features].values
            Y = df[self.TARGET].values
            X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.1, random_state=2)
            lm = linear_model.LinearRegression()
            model = lm.fit(X_train, y_train)
            predictions = lm.predict(X_test)
            print(predictions)
           # scores[position] = metrics.precision_score(y_test, predictions)
        
        #print(scores)


if __name__ == "__main__":
    reg = NFLRegression()
    reg.build_models()    