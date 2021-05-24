const https = require('https');
const sleep = require('sleep');

function sendData(time) {

  var postData = JSON.stringify({
    "time": time
  });

  var options = {
    host: 'https://www.paralleldots.com/',
    port: 443,
    path: '/path',
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Content-Length': postData.length
    }
  };

  var req = https.request(options, (res) => {
    console.log('statusCode:', res.statusCode);
    console.log('headers:', res.headers);

    res.on('data', (d) => {
      process.stdout.write(d);
    });
  });

  req.on('error', (e) => {
    console.error(e);
  });

  req.write(postData);
  req.end();
}
const delay = 60000;
for (var i = 0; i < 3; i++) {
  setTimeout(function () {
    console.log("sending data" + i);
    var timeDate = new Date();
    sendData(timeDate.getTime());
  }, delay * i);

}
