const sheetItems = $('Get row(s) in sheet').all();
const allLabels = sheetItems.map(i => {
    const d = i.json;
    return '<div style="border:2px solid #333;border-radius:6px;padding:14px;font-family:Arial,sans-serif;overflow:hidden"><div style="font-size:13px;font-weight:bold;color:#666;letter-spacing:1px;border-bottom:1px solid #ccc;padding-bottom:6px;margin-bottom:8px">SHIP TO</div><div style="font-size:22px;font-weight:900;color:#000;margin-bottom:14px">' + d['Name'] + '</div><div style="font-size:15px;color:#333;margin-bottom:8px">Phone: ' + d['Phone Number'] + '</div><div style="font-size:16px;color:#222;line-height:1.4;margin-bottom:3px">' + d['Address 1'] + '</div><div style="font-size:16px;color:#222;line-height:1.4;margin-bottom:10px">' + d['Address 2'] + '</div><div style="font-size:17px;font-weight:bold;color:#000;background:#eee;display:inline-block;padding:5px 12px;border:1px solid #ccc">Pincode: ' + d['Pincode'] + '</div></div>';
});
const pages = [];
for (let i = 0; i < allLabels.length; i += 8) { pages.push(allLabels.slice(i, i + 8)); }
let html = '<!DOCTYPE html><html><head><style>@page{size:A4;margin:8mm}*{margin:0;padding:0;box-sizing:border-box}body{font-family:Arial,sans-serif}.page{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(4,1fr);gap:8mm;page-break-after:always;padding:8mm;height:277mm}.page:last-child{page-break-after:avoid}</style></head><body>';
for (const page of pages) { html += '<div class="page">' + page.join('') + '</div>'; }
html += '</body></html>';
return [{ json: { html: html } }];
