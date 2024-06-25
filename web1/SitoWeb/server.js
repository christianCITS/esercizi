const express = require('express');
const cors = require('cors')
const app = express();

app.use(cors());

var iPortaTcp = 4201;
var sIpAddress = "127.0.0.1"

app.listen(iPortaTcp,sIpAddress, () => console.log('API is running on http://' + sIpAddress + ':' + iPortaTcp));
const bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({ extended: true }));

//PRIMA ROUTE
app.get('', (req, res) => {
    console.log("Mi hai chiesto la pagina iniziale");
    res.sendFile("index.html", { root: './htdocs' });
    });
    
    //SECONDA ROUTE
app.get('/registrazione', (req, res) => {
    console.log("Mi hai chiesto la pagina iniziale");
    res.sendFile("form.html", { root: './htdocs' });
    });
    //TERZA ROUTE
app.get('/Accesso', (req, res) => {
    console.log("Mi hai chiesto la pagina iniziale");
    res.sendFile("form2.html", { root: './htdocs' });
    });
    //QUARTA ROUTE
app.get('/gestisciDatiForm', (req, res) => {
    console.log("Mi hai chiesto la pagina iniziale");
    res.send("<html><body>Ciao"+ nome + "</body></html>");
    });