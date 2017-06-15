import os, io
from geme import *
from flask import Flask, render_template, request, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

app = Flask(__name__)

sliced_df1 = DataFrame([1])

@app.route('/')
def main(): 
    return render_template('index.html')
        

@app.route('/submit', methods=['GET'])
def submission():
    global sliced_df1

    dataset = r"../datasets/" + request.args.get('dataset') + ".csv"
    df1 = read_data_frame(dataset)
    df2 = read_data_frame(r"../datasets/realestate-loans-billions-monthl.csv") #TODO
    r, sliced_df1, sliced_df2 = compare_datasets(df1, df2)
 
    print(sliced_df1)
    # use sliced_df1.plot(0) stuff to give a matplotlib plot object
    return render_template('timeresultspage.html')
        
        
@app.route("/graph1.png") #TODO generalise this to prevent duplication in graph2, graph3, etc.
def graph1():
    # create plot
    fig = plt.figure()
    plt.plot(sliced_df1.index, sliced_df1.iloc[:,1])
    #plt.xticks(range(len(sliced_df1.iloc[:,0])), sliced_df1.iloc[:,0])
    
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
    fig = plt.figure()
    plt.plot(sliced_df1.index, sliced_df1.iloc[:,1])
    #plt.xticks(range(len(sliced_df1.iloc[:,0])), sliced_df1.iloc[:,0])
    
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
    fig = plt.figure()
    plt.plot(sliced_df1.index, sliced_df1.iloc[:,1])
    #plt.xticks(range(len(sliced_df1.iloc[:,0])), sliced_df1.iloc[:,0])
    
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
    fig = plt.figure()
    plt.plot(sliced_df1.index, sliced_df1.iloc[:,1])
    #plt.xticks(range(len(sliced_df1.iloc[:,0])), sliced_df1.iloc[:,0])
    
    # create png
    canvas=FigureCanvas(fig)
    png_output = io.BytesIO()
    canvas.print_png(png_output)
    response=make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'

    return response


    
if __name__ == "__main__":
    app.run()
