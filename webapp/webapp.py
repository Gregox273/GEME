import os, io
from geme import *
from flask import Flask, render_template, request, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

app = Flask(__name__)

best_fits = []

@app.route('/')
def main(): 
    return render_template('index.html')
        

@app.route('/submit', methods=['GET'])
def submission():
    filename = request.args.get('dataset')
    global best_fits
    best_fits = compare_to_all(filename)

    return render_template('timeresultspage.html')
        
        
@app.route("/graph1.png")
def graph1():
    # create plot
    fig, ax1 = plt.subplots()
    if not best_fits[0] == None:
        r, df1, df2 = best_fits[0]

        indices = df1.index if df1.index[0] == 0 else df2.index        

        ax1.plot(indices, df1.iloc[:,1], 'b')
        ax1.set_xlabel('Months')
        ax1.set_ylabel('Datset 1', color='b')
        ax1.tick_params('y', colors='b')

        ax2 = ax1.twinx()
        ax2.plot(indices, df2.iloc[:,1], 'r')
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
    # create plot
    fig, ax1 = plt.subplots()
    if not best_fits[1] == None:
        r, df1, df2 = best_fits[1]

        indices = df1.index if df1.index[0] == 0 else df2.index        

        ax1.plot(indices, df1.iloc[:,1], 'b')
        ax1.set_xlabel('Months')
        ax1.set_ylabel('Datset 1', color='b')
        ax1.tick_params('y', colors='b')

        ax2 = ax1.twinx()
        ax2.plot(indices, df2.iloc[:,1], 'r')
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
    # create plot
    fig, ax1 = plt.subplots()
    if not best_fits[2] == None:
        r, df1, df2 = best_fits[2]

        indices = df1.index if df1.index[0] == 0 else df2.index        

        ax1.plot(indices, df1.iloc[:,1], 'b')
        ax1.set_xlabel('Months')
        ax1.set_ylabel('Datset 1', color='b')
        ax1.tick_params('y', colors='b')

        ax2 = ax1.twinx()
        ax2.plot(indices, df2.iloc[:,1], 'r')
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
    # create plot
    fig, ax1 = plt.subplots()
    if not best_fits[3] == None:
        r, df1, df2 = best_fits[3]

        indices = df1.index if df1.index[0] == 0 else df2.index        

        ax1.plot(indices, df1.iloc[:,1], 'b')
        ax1.set_xlabel('Months')
        ax1.set_ylabel('Datset 1', color='b')
        ax1.tick_params('y', colors='b')

        ax2 = ax1.twinx()
        ax2.plot(indices, df2.iloc[:,1], 'r')
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
