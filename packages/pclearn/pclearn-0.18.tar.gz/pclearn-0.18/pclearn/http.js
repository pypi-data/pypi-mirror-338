const http = require('http');
const hostname = '127.0.0.1';
const port = 4000;
const server = http.createServer((req, res) => {
    res.writeHead(200, {'Content-Type': 'text/plain'});
    if (req.url === '/hello') {
        res.end('Hello World!\n');
    } else if (req.url === '/about') {
        res.end('This is the about page.\n');
    } else {
        res.end('Node.js server!\n');
    }
});
server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});
