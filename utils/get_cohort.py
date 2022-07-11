from flask import jsonify, g, session,request, json, Response, redirect, flash, render_template, url_for
from application import app 
import json

import plotly
# import plotly.express as px
# import pandas as pd
from utils import get_cohort
from utils import data, plot
from utils import data_handling as dh
from utils.settings import *

def get_cohort():
    information = request.data
    cohort=information.decode('UTF-8').replace("[","").replace("]","").replace('"','').split(",")
    # print(cohort)
    return cohort

def send_data(de_table1,cohort,timepoint):
    volcano = json.dumps(
            plot.plotVolcano(dh.prep_volcano(de_table1), cohort=cohort, timepoint=timepoint),
            cls=plotly.utils.PlotlyJSONEncoder)
    return volcano