const fs = require('fs');
const { Resvg } = require('@resvg/resvg-js');

// 1. logo-full.png: 2400 px wide
const fullSvg = fs.readFileSync('public/brand/logo-full.svg');
const resvgFull = new Resvg(fullSvg, { fitTo: { mode: 'width', value: 2400 } });
fs.writeFileSync('public/brand/logo-full.png', resvgFull.render().asPng());
console.log('Generated public/brand/logo-full.png (2400px wide)');

// 2. logo-full-light.png: 2400 px wide
const fullLightSvg = fs.readFileSync('public/brand/logo-full-light.svg');
const resvgFullLight = new Resvg(fullLightSvg, { fitTo: { mode: 'width', value: 2400 } });
fs.writeFileSync('public/brand/logo-full-light.png', resvgFullLight.render().asPng());
console.log('Generated public/brand/logo-full-light.png (2400px wide)');

// 3. logo-symbol.png: 1024 px tall
const symSvg = fs.readFileSync('public/brand/logo-symbol.svg');
const resvgSym = new Resvg(symSvg, { fitTo: { mode: 'height', value: 1024 } });
fs.writeFileSync('public/brand/logo-symbol.png', resvgSym.render().asPng());
console.log('Generated public/brand/logo-symbol.png (1024px tall)');

// 4. logo-wordmark.png: 1600 px wide
const wmSvg = fs.readFileSync('public/brand/logo-wordmark.svg');
const resvgWm = new Resvg(wmSvg, { fitTo: { mode: 'width', value: 1600 } });
fs.writeFileSync('public/brand/logo-wordmark.png', resvgWm.render().asPng());
console.log('Generated public/brand/logo-wordmark.png (1600px wide)');
