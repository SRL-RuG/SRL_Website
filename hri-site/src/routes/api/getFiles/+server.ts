// src/routes/api/listFiles.js
import fs from 'fs'
import path from 'path'
export const prerender = true

export async function GET() {
  const directoryPath = path.join('static', 'PythonFiles')
  const files = fs.readdirSync(directoryPath)

  return new Response(JSON.stringify(files), {
    headers: {
      'Content-Type': 'application/json',
    },
  })
}
