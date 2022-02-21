from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

# utils
import numpy as np
import pandas as pd

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'EbolaDB'
app.config['MONGO_URI'] = 'mongodb://localhost/EbolaDB'

mongo = PyMongo(app)

def get_cursor(collection_name):
    collection = mongo.db.get_collection(collection_name)
    return collection.find()

def get_data_frames(collection_name):
    cursor = get_cursor(collection_name)
    return pd.DataFrame(list(cursor))


@app.route('/')
def index():
    return jsonify({'message': 'Hello, World!'})

@app.route('/degs', methods = ['POST'])
def get_degs():

    req = request.get_json()
    print(req)
    cohort = req['cohort']
    comp = req['comp']
    
    cursor = mongo.db.get_collection(cohort+'_DEGs').find({ 'comp': comp })
    degs = pd.DataFrame(list(cursor))[['gene_id','logFC','FDR']].set_index('gene_id')
    degs['logFDR'] = -np.log10(degs['FDR'])
    degs['score'] = degs['logFC']*degs['logFDR'].abs()
    res = degs.drop('FDR',1).to_json()
    return res


# @app.route('/genes/<cohort>/<gene>/<phenovar>', methods=['GET'])
@app.route('/gene-exprs', methods=['POST'])
def get_gene_exprs():

    req = request.get_json()
    cohort      = req['cohort']
    gene        = req['gene']

    pheno = mongo.db.get_collection(cohort+'_pheno').find(projection={'_id': False})
    pheno = pd.DataFrame(list(pheno)).set_index('sample_id')
    pheno = pheno.to_dict()

    collection = mongo.db.get_collection(cohort+'_norm_data')
    cursor = collection.find({ 'gene_id': gene},projection={'_id': False,'gene_id': False})
    gene_exprs = {"exprs": list(cursor)[0]}
    gene_exprs.update(pheno)
    res = {gene: gene_exprs}
        
    return jsonify(res)


@app.route('/gene-corr',methods=['POST'])
def get_gene_corr():
    req = request.get_json()
    cohort = req['cohort']
    gene = req['gene']

    collection = mongo.db.get_collection(cohort+'_corr')
    cursor = collection.find({'from':gene},projection={'_id': False})
    res = pd.DataFrame(list(cursor)).to_json(orient='records')

    return res


if __name__=='__main__':
    app.run(debug=True)



