# Below codestring is used to plot scatter plot for iris dataset. 

import plotly.express as px
import pandas as pd
import json
import plotly.io as io
import numpy as np

def getLogger():
    import logging
    logging.basicConfig(filename="UIACLogger.log",
                        format='%(asctime)s %(message)s',
                        filemode='a')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    return logger


logger = getLogger()


def generate_dataset():
    # Generating dataset to plot graph
    logger.info("Generate dataset for x and y")
    try:
        x=np.random.randint(0,100,50)
        y=[i*3 for i in x]
        dframe = pd.DataFrame({'x':x, 'y':y})
        return dframe
    except Exception as error_msg:
        logger.info(f"Exception occured while generating the dataset"
                    f"Error Info is  {error_msg}")


def getGraph(dframe, filters):
    logger.info(
        "Preparing line plot json to plot dataset")
    for item in filters:
        if 'All' in filters[item]:
            continue
        elif isinstance(filters[item], list):
            dframe = dframe[dframe[item].isin(filters[item])]
        else:
            dframe = dframe[dframe[item] == filters[item]]
    fig = px.line(dframe, x="x", y="y", title='Line chart for x=y^3 relationship')
    # fig.show()
    logger.info(
        "Successfully prepared scatter plot json to plot iris dataset")
    return io.to_json(fig)


#selected_filters = {"x": '1'}
dframe = generate_dataset()
dynamic_outputs = getGraph(dframe, selected_filters)
