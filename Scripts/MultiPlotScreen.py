# Below codestring is used to plot scatter plot for iris dataset. 

import plotly.graph_objects as go
#import pandas as pd
import json
import plotly.io as io
from sklearn.datasets import load_iris

def getLogger():
    import logging
    logging.basicConfig(filename="UIACLogger.log",
                        format='%(asctime)s %(message)s',
                        filemode='a')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    return logger


logger = getLogger()


def read_dataset():
    # Read dataset from the sklearn
    logger.info("Read dataset file from sklearn")
    try:
        dframe = load_iris(as_frame=True).data
        dframe=dframe[['sepal length (cm)','sepal width (cm)']]
        return dframe
    except Exception as error_msg:
        logger.info("Exception occured while reading the dataset")


def getGraph(dframe):
    logger.info(
        "Preparing five plots json to plot iris dataset")
    # for item in filters:
    #     if 'All' in filters[item]:
    #         continue
    #     elif isinstance(filters[item], list):
    #         dframe = dframe[dframe[item].isin(filters[item])]
    #     else:
    #         dframe = dframe[dframe[item] == filters[item]]
    #create figure
    fig = go.Figure()
    # Add surface trace
    fig.add_trace(go.Scatter(x=dframe['sepal length (cm)'],y=dframe['sepal width (cm)'], mode="markers",visible=True))
    fig.add_trace(go.Bar(x=dframe['sepal length (cm)'],y=dframe['sepal width (cm)'],visible=False))
    fig.add_trace(go.Histogram(x=dframe['sepal length (cm)'],y=dframe['sepal width (cm)'],visible=False))
    fig.add_trace(go.Violin(x=dframe['sepal length (cm)'],y=dframe['sepal width (cm)'],visible=False))
    fig.add_trace(go.Box(x=dframe['sepal length (cm)'],y=dframe['sepal width (cm)'],visible=False))

    # Add dropdown
    button1=dict(method='restyle', label='Scatter Plot',args=[{"visible":[True,False,False,False,False]}])
    button2=dict(method='restyle',label='Bar Chart',args=[{"visible":[False,True,False,False,False]}])
    button3=dict(method='restyle',label='Histogram',args=[{"visible":[False,False,True,False,False]}])
    button4=dict(method='restyle',label='Violin Plot',args=[{"visible":[False,False,False,True,False]}])
    button5=dict(method='restyle',label='Box Plot',args=[{"visible":[False,False,False,False,True]}])
                       
    fig.update_layout(updatemenus=[dict(type='dropdown',
                                            direction="down",
                                            buttons=[button1,button2,button3,button4,button5])])
        
    # Add annotation
    fig.update_layout(updatemenus=[{ 'name': 'Type', 'active': True}])
    # fig.show()
    logger.info("Successfully prepared scatter plot json to plot iris dataset")
    return io.to_json(fig)


# selected_filters = {"sepal length (cm)": 'All'}
dframe = read_dataset()
dynamic_outputs = getGraph(dframe)
