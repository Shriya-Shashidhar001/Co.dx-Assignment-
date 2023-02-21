# Below codestring is used to plot scatter plot for iris dataset. 

import plotly.express as px
import pandas as pd
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
        dframe['color']='yellow'
        dframe['color'][70:]='red'
        return dframe
    except Exception as error_msg:
        logger.info(f"Exception occured while reading the dataset"
                    f"Error Info is  {error_msg}")


def getGraph(dframe, filters):
    logger.info(
        "Preparing scatter plot json to plot iris dataset")
    for item in filters:
        if 'All' in filters[item]:
            continue
        elif isinstance(filters[item], list):
            dframe = dframe[dframe[item].isin(filters[item])]
        else:
            dframe = dframe[dframe[item] == filters[item]]
    fig = px.scatter(dframe, x='sepal length (cm)', y='sepal width (cm)', color='color')
    # fig.show()
    logger.info(
        "Successfully prepared scatter plot json to plot iris dataset")
    return io.to_json(fig)


#selected_filters = {"color": 'yellow'}
dframe = read_dataset()
dynamic_outputs = getGraph(dframe, selected_filters)
