// Promise mode
const captureHar = require('capture-har');

captureHar({
  url: 'http://www.google.com'
}, { withContent: false }).then(har => {
    console.log(JSON.stringify(har, null, 2));
  });

// // Stream mode
// const CaptureHar = require('capture-har').CaptureHar;

// const captureHar = new CaptureHar(require('request'));
// captureHar.start({ url: 'http://www.google.com' })
//   .on('data', data => // data event will contain the response body as it is received)
//   .on('end', () => {
//     const har = captureHar.stop();
//     // har will contain the HAR object
//     })