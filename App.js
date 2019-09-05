let express = require('express')
let path = require('path')

const app = express()
 
app.use(express.static(path.join(__dirname, 'html')))

app.get('', (req, res) => {
    res.sendFile(path.join(__dirname, 'html/index.html'))
})

app.listen(6262, () => {
    console.log('Express app is listening on port 6262')
})