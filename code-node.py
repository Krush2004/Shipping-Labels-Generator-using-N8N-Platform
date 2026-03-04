# ============================================================
# N8N Code Node — Shipping Label Generator (Python Version)
# ============================================================
# ✅ Works on: Self-Hosted N8N only
# ❌ Does NOT work on: N8N Cloud (v2.10.2)
# Language: Python | Mode: Run Once for All Items
#
# NOTE: N8N Cloud's Python sandbox does not properly expose the
# '_input' variable, causing "name '_input' is not defined" error.
# This is a known N8N Cloud limitation, not a code bug.
# For N8N Cloud users, use code-node.js (JavaScript) instead.
# ============================================================

all_labels = []

for item in _input.all():
    d = item.json
    label = (
        '<div style="border:2px solid #333;border-radius:6px;padding:14px;'
        'font-family:Arial,sans-serif;overflow:hidden">'
        '<div style="font-size:13px;font-weight:bold;color:#666;'
        'letter-spacing:1px;border-bottom:1px solid #ccc;'
        'padding-bottom:6px;margin-bottom:8px">SHIP TO</div>'
        '<div style="font-size:22px;font-weight:900;color:#000;'
        f'margin-bottom:14px">{d["Name"]}</div>'
        '<div style="font-size:15px;color:#333;'
        f'margin-bottom:8px">Phone: {d["Phone Number"]}</div>'
        '<div style="font-size:16px;color:#222;line-height:1.4;'
        f'margin-bottom:3px">{d["Address 1"]}</div>'
        '<div style="font-size:16px;color:#222;line-height:1.4;'
        f'margin-bottom:10px">{d["Address 2"]}</div>'
        '<div style="font-size:17px;font-weight:bold;color:#000;'
        'background:#eee;display:inline-block;padding:5px 12px;'
        f'border:1px solid #ccc">Pincode: {d["Pincode"]}</div>'
        '</div>'
    )
    all_labels.append(label)

pages = []
for i in range(0, len(all_labels), 8):
    pages.append(all_labels[i:i + 8])

html = (
    '<!DOCTYPE html><html><head><style>'
    '@page{size:A4;margin:8mm}'
    '*{margin:0;padding:0;box-sizing:border-box}'
    'body{font-family:Arial,sans-serif}'
    '.page{display:grid;grid-template-columns:1fr 1fr;'
    'grid-template-rows:repeat(4,1fr);gap:8mm;'
    'page-break-after:always;padding:8mm;height:277mm}'
    '.page:last-child{page-break-after:avoid}'
    '</style></head><body>'
)

for page in pages:
    html += '<div class="page">' + ''.join(page) + '</div>'
html += '</body></html>'

return [{"json": {"html": html}}]
