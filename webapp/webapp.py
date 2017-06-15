import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main(): 
    
    return render_template('index.html')
        

@app.route('/submit', methods=['GET'])
def submission():

        dataset = request.args.get('dataset')
        # Call the correlation function here
        print(dataset)
        return # Serve results page template
    


    
if __name__ == "__main__":
    app.run()
