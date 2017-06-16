import os, io
from geme import *
from flask import Flask, render_template, request, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

app = Flask(__name__)

sliced_df1 = DataFrame([1])
sliced_df2 = DataFrame([1])

@app.route('/')
def main(): 
    return render_template('index.html')
        

@app.route('/submit', methods=['GET'])
def submission():
    global sliced_df1
    global sliced_df2

    dataset = r"../datasets/time/" + request.args.get('dataset')
    df1 = read_data_frame(dataset)
    df2 = read_data_frame(r"../datasets/time/realestate-loans-billions-monthl.csv") #TODO
    r, sliced_df1, sliced_df2 = compare_datasets(df1, df2)
 
    return render_template('timeresultspage.html')
        
        
@app.route("/graph1.png")
def graph1():
    
    # Create Figure
    fig, ax1 = plt.subplots()

    indices = sliced_df1.index if sliced_df1.index[0] == 0 else sliced_df2.index        

    ax1.plot(indices, sliced_df1.iloc[:,1], 'b')
    ax1.set_xlabel('Months')
    ax1.set_ylabel('Datset 1', color='b')
    ax1.tick_params('y', colors='b')

    ax2 = ax1.twinx()
    ax2.plot(indices, sliced_df2.iloc[:,1], 'r')
    ax2.set_ylabel('Dataset 2', color='r')
    ax2.tick_params('y', colors='r')

    fig.tight_layout()
    
    # Create PNG
    canvas=FigureCanvas(fig)
    png_output = io.BytesIO()
    canvas.print_png(png_output)
    response=make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'

    return response
    
@app.route("/graph2.png")
def graph2():
    
    # Create Figure
    fig, ax1 = plt.subplots()

    indices = sliced_df1.index if sliced_df1.index[0] == 0 else sliced_df2.index        

    ax1.plot(indices, sliced_df1.iloc[:,1], 'b')
    ax1.set_xlabel('Months')
    ax1.set_ylabel('Datset 1', color='b')
    ax1.tick_params('y', colors='b')

    ax2 = ax1.twinx()
    ax2.plot(indices, sliced_df2.iloc[:,1], 'r')
    ax2.set_ylabel('Dataset 2', color='r')
    ax2.tick_params('y', colors='r')

    fig.tight_layout()
    
    # Create PNG
    canvas=FigureCanvas(fig)
    png_output = io.BytesIO()
    canvas.print_png(png_output)
    response=make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'

    return response
    
    
@app.route("/graph3.png")
def graph3():
    
    # Create Figure
    fig, ax1 = plt.subplots()

    indices = sliced_df1.index if sliced_df1.index[0] == 0 else sliced_df2.index        

    ax1.plot(indices, sliced_df1.iloc[:,1], 'b')
    ax1.set_xlabel('Months')
    ax1.set_ylabel('Datset 1', color='b')
    ax1.tick_params('y', colors='b')

    ax2 = ax1.twinx()
    ax2.plot(indices, sliced_df2.iloc[:,1], 'r')
    ax2.set_ylabel('Dataset 2', color='r')
    ax2.tick_params('y', colors='r')

    fig.tight_layout()
    
    # Create PNG
    canvas=FigureCanvas(fig)
    png_output = io.BytesIO()
    canvas.print_png(png_output)
    response=make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'

    return response
    
@app.route("/graph4.png")
def graph4():
    
    # Create Figure
    fig, ax1 = plt.subplots()

    indices = sliced_df1.index if sliced_df1.index[0] == 0 else sliced_df2.index        

    ax1.plot(indices, sliced_df1.iloc[:,1], 'b')
    ax1.set_xlabel('Months')
    ax1.set_ylabel('Datset 1', color='b')
    ax1.tick_params('y', colors='b')

    ax2 = ax1.twinx()
    ax2.plot(indices, sliced_df2.iloc[:,1], 'r')
    ax2.set_ylabel('Dataset 2', color='r')
    ax2.tick_params('y', colors='r')

    fig.tight_layout()
    
    # Create PNG
    canvas=FigureCanvas(fig)
    png_output = io.BytesIO()
    canvas.print_png(png_output)
    response=make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'

    return response

    
if __name__ == "__main__":
    app.run()
