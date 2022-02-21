const express = require('express');
const bodyParser = require('body-parser');
const { response } = require('express');
const url = 'http://127.0.0.1:5000';

const app = express();
app.use(bodyParser.json());

app.post('/degs', async (req, res) => {
    const cohort = "USA";
    const comp = "D1";
    
    const fetch_response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "cohort": cohort,
            "comp": comp,
        })
    });
    const json = await fetch_response.json();
    response.json(json);

    console.log(json);

});


app.get('/', async (req, res) => {
    const fetch_response = await fetch(url);
    const json = await fetch_response.json();
    response.json(json);
});