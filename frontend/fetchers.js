const fetch = (...args) => import('node-fetch').then(({default: fetch}) => fetch(...args));
const http = require('http');
const https = require('https');

async function fetchDegs (cohort, comp, url) {
    const response = await fetch(`${url}/degs`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ cohort, comp })
    });
    const json = await response.json();
    return json;
}


async function fetchGeneExpress(cohort, gene, url) {
    const response = await fetch(`${url}/gene-exprs`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ cohort, gene })
    });
    const json = await response.json();
    return json;
}


async function fetchGeneCorr(cohort, gene, url) {
    const response = await fetch(`${url}/gene-corr`, {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json'
        },
        body: JSON.stringify({cohort, gene})
    });
    const json = await response.json();
    return json;
}



module.exports = { fetchDegs, fetchGeneExpress, fetchGeneCorr };


// const url = 'http://localhost:5000/';
// const cohort = "USA";
// const comp = "D1";

// fetchDegs(cohort, comp).then(function(degs) {
//     console.log(degs);
// });

// fetchGeneExpress(cohort, "BRCA1").then(function(gene_exprs) {
    // console.log(gene_exprs);
// });


// fetchGeneCorr("USA", "ABCB7").then(function(gene_corr) {
//     console.log(gene_corr);
// });