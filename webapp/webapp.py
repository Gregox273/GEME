import os
from geme import *
from flask import Flask, render_template, request, make_response

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
        
        
@app.route("/test.png")
def simple():
    import datetime
    import io
    import random

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter

    fig=Figure()
    ax=fig.add_subplot(111)
    x=[]
    y=[]
    now=datetime.datetime.now()
    delta=datetime.timedelta(days=1)
    for i in range(10):
        x.append(now)
        now+=delta
        y.append(random.randint(0, 1000))
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas=FigureCanvas(fig)
    png_output = io.BytesIO()
    canvas.print_png(png_output)
    response=make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'

    return response
    


    
if __name__ == "__main__":
    app.run()
