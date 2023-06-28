const express = require('express')

const app = express();

const port = 9000

app.get('/', function(req, res){
  res.sendFile(__dirname + '/src/index.html')

});


app.listen(port, () => {
  console.log('Está rodando: ${port}')
});