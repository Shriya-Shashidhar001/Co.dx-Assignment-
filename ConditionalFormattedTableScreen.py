# Below codestring is used to display the scatterplot

import plotly.graph_objects as go
import numpy as np
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
        return dframe
    except Exception as error_msg:
        logger.info(f"Exception occured while reading the dataset"
                    f"Error Info is  {error_msg}")


def get_table():
    dframe=read_dataset()
    font_color=dframe.apply(lambda s: np.where(s.name == "sepal length (cm)", np.where(s>5, "green", "red"),'black')).T.values  
    fig = go.Figure(data=[go.Table(
      header=dict(values=list(dframe.columns),
                  fill_color=["pink","cyan","yellow","green"],
                  font_color="#070707",
                  align='center'),
      cells=dict(values=[dframe['sepal length (cm)'], dframe['sepal width (cm)'], dframe['petal length (cm)'], 
                          dframe['petal width (cm)']],
                  fill_color=["pink","cyan","yellow","green"],
                  font_color= font_color, #'#070707',
                  align='center'))])
    logger.info(
        "Successfully prepared table json for Iris dataset")
    return io.to_json(fig)
    

kpi_json = get_table()
dynamic_outputs = kpi_json
