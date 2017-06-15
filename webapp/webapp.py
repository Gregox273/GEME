import os
from geme import *
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main(): 
    
    return render_template('index.html')
        

@app.route('/submit', methods=['GET'])
def submission():

        dataset = r"../datasets/" + request.args.get('dataset') + ".csv"
        df1 = read_data_frame(dataset)
        df2 = read_data_frame(r"../datasets/realestate-loans-billions-monthl.csv") #TODO
        r, sliced_df1, sliced_df2 = compare_datasets(df1, df2)
        
        # Call the correlation function here
        print(dataset)
        # use sliced_df1.plot(0) stuff to give a matplotlib plot object
        return # Serve results page template
    


    
if __name__ == "__main__":
    app.run()
