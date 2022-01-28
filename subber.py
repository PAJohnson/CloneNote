import json

with open('./CloneNote.html', 'r') as template, open('./index.html', 'w') as index:
    clonenote = template.read()
    note = json.loads(open('./notebook.json', encoding='utf8').read())
    noteStr = json.dumps(note, separators=(',',':'))

    startText = clonenote.split('//// NOTEBOOK_START')[0]
    endText = clonenote.split('//// NOTEBOOK_END')[1]

    indexStr = startText + "var notebook = " + noteStr.replace("'", "\\'") + ";\n" + endText
    index.write(indexStr)