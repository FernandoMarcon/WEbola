from flask import jsonify, g, session,request, json, Response, redirect, flash, render_template, url_for
from application import app 
from flask_sse import sse
import json

import plotly
# import plotly.express as px
# import pandas as pd
from utils import get_cohort
from utils import data, plot
from utils import data_handling as dh
from utils.settings import *

def set_datadir(basedir='data', cohort='USA', dtype='RNASeq'):
    return '/'.join([basedir, cohort, dtype,''])


@app.route('/genes/boxplot/<gene>/<cohort>/<timepoint>')
def genes_boxplot(gene,cohort,timepoint):
    print(cohort)
    print(timepoint)
    pheno_var1='treatment'
    fig = plot.plotGeneExpression(data.data(cohort=cohort,timepoint=timepoint), gene, pheno_var1)
    gene_exprs=json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder)
    return gene_exprs


@app.route('/genes/corr/<gene>/<cohort>/<timepoint>')
def genes_corr(gene,cohort,timepoint):
    corr_thrs = 0.8
    try:
        gene_corr = plot.geneCorr(data.data(cohort=cohort,timepoint=timepoint), gene, corr_thrs)
    except:
        gene_corr = {"error":1}
    return gene_corr



@app.route('/gene_level_analysis',methods = ['GET','POST'])
def gene_level_analysis():
    try:
        timepoint = get_cohort.get_cohort()[1].strip()
        cohort=get_cohort.get_cohort()[0].strip()
    except:
        timepoint="D1"
        cohort="USA"
    
    # print(cohort)
    # print(timepoint)
    
    de_table1 = dh.read_de_table(comp=timepoint, datadir=set_datadir(cohort=cohort),echo=False)
    
    volcano=get_cohort.send_data(de_table1,cohort,timepoint)
    sse.publish(volcano,type='greeting')
    return render_template("gene_level_analysis.html", gene_level_analysis=True, title="Gene-level Analysis", volcano=volcano)
    
    

@app.route('/reactogenicity')
def reactogenicity():
    return render_template("reactogenicity.html", reactogenicity=True, title="Reactogenicity")

@app.route('/immunogenicity')
def immunogenicity():
    return render_template("immunogenicity.html", immunogenicity=True, title="Immunogenicity")

