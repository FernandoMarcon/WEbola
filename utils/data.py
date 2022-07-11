from utils import data_handling as dh
from utils.settings import *
import pandas as pd
import os

class data:

        def __init__(self, cohort="USA",timepoint="D1"):
            self.cohort = cohort
            self.timepoint=timepoint
            self.exprs,self.pheno=self.expression()
            self.de_table = self.de()
            self.degs = self.deg()
            self.data_corr=self.correlation()
        
        def set_datadir(self, basedir='data', cohort='USA', dtype='RNASeq'):
            return '/'.join([basedir, cohort, dtype,''])
        
        def expression(self):
            exprs = pd.read_table('data/'+self.cohort+'/RNASeq/'+self.cohort+'_counts.tsv', index_col='genes')
            pheno = pd.read_table('data/'+self.cohort+'/RNASeq/'+self.cohort+'_pheno.tsv', index_col='sample_id')
            return exprs,pheno
        
        def de(self):
            de_table = dh.read_de_table(comp=self.timepoint, datadir=self.set_datadir(cohort=self.cohort),echo=False)
            return de_table
        
        def deg(self):
            degs = dh.prep_volcano(self.de_table)
            return degs
        
        def correlation(self):
            data_corr = self.exprs.loc[self.degs[self.degs['DEG'] == 'Up'].index].transpose().corr()
            return data_corr