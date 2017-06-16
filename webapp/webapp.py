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
    r, df1, df2 = best_fits[0]
    fig = plt.figure()
    plt.plot(df1.index, df1.iloc[:,1])
    #plt.xticks(range(len(df1.iloc[:,0])), df1.iloc[:,0])
    
    # create png
    canvas=FigureCanvas(fig)
    png_output = io.BytesIO()
    canvas.print_png(png_output)
    response=make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'

    return response
    
@app.route("/graph2.png")
def graph2():
    # create plot
    r, df1, df2 = best_fits[1]
    fig = plt.figure()
    plt.plot(df1.index, df1.iloc[:,1])
    #plt.xticks(range(len(df1.iloc[:,0])), df1.iloc[:,0])
    
    # create png
    canvas=FigureCanvas(fig)
    png_output = io.BytesIO()
    canvas.print_png(png_output)
    response=make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'

    return response
    
@app.route("/graph3.png")
def graph3():
    # create plot
    r, df1, df2 = best_fits[2]
    fig = plt.figure()
    plt.plot(df1.index, df1.iloc[:,1])
    #plt.xticks(range(len(df1.iloc[:,0])), df1.iloc[:,0])
    
    # create png
    canvas=FigureCanvas(fig)
    png_output = io.BytesIO()
    canvas.print_png(png_output)
    response=make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'

    return response
    
@app.route("/graph4.png")
def graph4():
    # create plot
    r, df1, df2 = best_fits[3]
    fig = plt.figure()
    plt.plot(df1.index, df1.iloc[:,1])
    #plt.xticks(range(len(df1.iloc[:,0])), df1.iloc[:,0])
    
    # create png
    canvas=FigureCanvas(fig)
    png_output = io.BytesIO()
    canvas.print_png(png_output)
    response=make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'

    return response
    
if __name__ == "__main__":
    app.run()
