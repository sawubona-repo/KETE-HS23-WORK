// ---------------------------------------------------------------------------
// Demo NodeJS Server - String HASHING Service
// --------------------------------------------
// Usage http://<server-ip-address>:7777?md5="xxx" where xxx is the string to hash with MD5
// Incl. Server Side Request/Originator Logging
// 
// Note: delete/deactivate <"type": "module"> in the package.json config file
//
// File: demo-hashingMD5.js
//
// V1 Nov'2021 dbe - initial version, KETE-HS21, based on fibonacci.js example
// V2 Oct'2020 dbe - minor corrections for KETE-HS22
//
// Source: Node.js Web Development - Fifth Edition (packt.com)
// ---------------------------------------------------------------------------
// required packages
var http = require('http');
var url  = require('url');

// var string = 'some string';
var crypto = require('crypto');

// var hash = crypto.createHash('md5').update(string).digest('hex');
// console.log(hash);


//Then define the HASHING function to hash encode a string
const hashing = exports.hashing = function(str) {
    return crypto.createHash('md5').update(str).digest('hex');
}

// ------------------------------------------------------------------------------
// Setup a http server acting on the request parameter
// Usage http://<server-ip-address>:7777?md5="xxx" where xxx is the string to hash
// ------------------------------------------------------------------------------
http.createServer(function (request, response) {
  var urlP = url.parse(request.url, true);
  var xMD5;
    
  response.writeHead(200, {'Content-Type': 'text/plain'});
  
  if (urlP.query['md5']) {
    xMD5 = hashing(urlP.query['md5']);
    response.end('Hashed String '+ urlP.query['md5'] +' = '+ xMD5);
	console.log('-- hashing request: string > '+ urlP.query['md5']);
  } else {
	response.end('USAGE: http://<server-ip-address>:7777?md5=xxx where xxx is the string to hash');
  }
}).listen(7777, );
console.log('Server running at port 7777');
