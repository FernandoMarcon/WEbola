const { fetchDegs, fetchGeneExpress, fetchGeneCorr } = require('./fetchers');

const url = 'http://localhost:5000/';
const cohort = "USA";
const comp = "D1";
const gene = "ABCB7";

fetchDegs(cohort, comp, url).then(function(degs) {
    console.log(degs);
});


fetchGeneExpress(cohort, gene, url).then(function(gene_exprs) {
    console.log(gene_exprs);
});


fetchGeneCorr(cohort, gene, url).then(function(gene_corr) {
    console.log(gene_corr);
});