import os
from geme import *
from flask import Flask, render_template, request, make_response

app = Flask(__name__)

sliced_df1 = 0

@app.route('/')
def main(): 
    
    return render_template('index.html')
        

@app.route('/submit', methods=['GET'])
def submission():

        dataset = r"../datasets/" + request.args.get('dataset') + ".csv"
        df1 = read_data_frame(dataset)
        df2 = read_data_frame(r"../datasets/realestate-loans-billions-monthl.csv") #TODO
        r, sliced_df1, sliced_df2 = compare_datasets(df1, df2)
     
        print(sliced_df1)
        # use sliced_df1.plot(0) stuff to give a matplotlib plot object
        return render_template('timeresultspage.html')
        
        
@app.route("/graph1.png")
def graph1():
    import io

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    
    fig=Figure()
    #ax=fig.add_subplot(111)
    
    #ax.plot(sliced_df1)
    sliced_df1.plot(0)
    
    canvas=FigureCanvas(fig)
    png_output = io.BytesIO()
    canvas.print_png(png_output)
    response=make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'

    return response
    
@app.route("/graph2.png")
def graph2():
    import io

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    
    fig=Figure()
    ax=fig.add_subplot(111)
    
    ax.plot(sliced_df1)
    
    
    canvas=FigureCanvas(fig)
    png_output = io.BytesIO()
    canvas.print_png(png_output)
    response=make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'

    return response
    
    
@app.route("/graph3.png")
def graph3():
    import io

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    
    fig=Figure()
    ax=fig.add_subplot(111)
    
    ax.plot(sliced_df1)
    
    
    canvas=FigureCanvas(fig)
    png_output = io.BytesIO()
    canvas.print_png(png_output)
    response=make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'

    return response
    
    
@app.route("/graph4.png")
def graph4():
    import io

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    
    fig=Figure()
    ax=fig.add_subplot(111)
    
    ax.plot(sliced_df1)
    
    
    canvas=FigureCanvas(fig)
    png_output = io.BytesIO()
    canvas.print_png(png_output)
    response=make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'

    return response


    
if __name__ == "__main__":
    app.run()
