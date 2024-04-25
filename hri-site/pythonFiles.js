import fs from 'fs'
import path from 'path'

const pythonFilesDir = path.join('static', 'PythonFiles')
const outputFilePath = path.join('static', 'fileList.json')

const files = fs.readdirSync(pythonFilesDir)
const fileListData = JSON.stringify({ files: files }); // Wrap in an object
fs.writeFileSync(outputFilePath, fileListData)
