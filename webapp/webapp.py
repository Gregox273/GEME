import os, io
from geme import *
from flask import Flask, render_template, request, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

app = Flask(__name__)

best_fits = []

@app.route('/')
@app.route('/homepage')
def home(): 
    return render_template('homepage.html')

@app.route('/index')
def index(): 
    return render_template('index.html')
        

@app.route('/submit', methods=['GET'])
def submission():
    filename = request.args.get('dataset')
    global best_fits
    best_fits = compare_to_all(filename)

    return render_template('timeresultspage.html', 
    origin_data = read_csv(correct_path(filename)).keys()[1], 
    dataset_1 = best_fits[0][2].keys()[1], 
    dataset_2 = best_fits[1][2].keys()[1], 
    dataset_3 = best_fits[2][2].keys()[1], 
    dataset_4 = best_fits[3][2].keys()[1],
    dataset_1_r = best_fits[0][0], 
    dataset_2_r = best_fits[1][0], 
    dataset_3_r = best_fits[2][0], 
    dataset_4_r = best_fits[3][0])
        
        
@app.route("/graph1.png")
def graph1():
    # create plot
    fig, ax1 = plt.subplots()
    if not best_fits[0] == None:
        r, df1, df2 = best_fits[0]

        indices = df1.index if df1.index[0] == 0 else df2.index        

        ax1.plot(indices, df1.iloc[:,1], 'b')
        ax1.set_xlabel('Months')
        ax1.set_ylabel('Original', color='b')
        ax1.tick_params('y', colors='b')

        ax2 = ax1.twinx()
        ax2.plot(indices, df2.iloc[:,1], 'r')
        ax2.set_ylabel('Comparison 1', color='r')
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
    # create plot
    fig, ax1 = plt.subplots()
    if not best_fits[1] == None:
        r, df1, df2 = best_fits[1]

        indices = df1.index if df1.index[0] == 0 else df2.index        

        ax1.plot(indices, df1.iloc[:,1], 'b')
        ax1.set_xlabel('Months')
        ax1.set_ylabel('Original', color='b')
        ax1.tick_params('y', colors='b')

        ax2 = ax1.twinx()
        ax2.plot(indices, df2.iloc[:,1], 'r')
        ax2.set_ylabel('Comparison 2', color='r')
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
    # create plot
    fig, ax1 = plt.subplots()
    if not best_fits[2] == None:
        r, df1, df2 = best_fits[2]

        indices = df1.index if df1.index[0] == 0 else df2.index        

        ax1.plot(indices, df1.iloc[:,1], 'b')
        ax1.set_xlabel('Months')
        ax1.set_ylabel('Original', color='b')
        ax1.tick_params('y', colors='b')

        ax2 = ax1.twinx()
        ax2.plot(indices, df2.iloc[:,1], 'r')
        ax2.set_ylabel('Comparison 3', color='r')
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
    # create plot
    fig, ax1 = plt.subplots()
    if not best_fits[3] == None:
        r, df1, df2 = best_fits[3]

        indices = df1.index if df1.index[0] == 0 else df2.index        

        ax1.plot(indices, df1.iloc[:,1], 'b')
        ax1.set_xlabel('Months')
        ax1.set_ylabel('Original', color='b')
        ax1.tick_params('y', colors='b')

        ax2 = ax1.twinx()
        ax2.plot(indices, df2.iloc[:,1], 'r')
        ax2.set_ylabel('Comparison 4', color='r')
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
