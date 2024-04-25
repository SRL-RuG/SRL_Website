<script>
  import { onMount } from 'svelte'
  import path from 'path'
  import fs from 'fs'

  export let code = ''
  export let filePath = ''
  let isLoading = false
  import { base } from '$app/paths'
  let stringfilePath = ''

  async function loadCode() {
    isLoading = true // Indicate loading state
    stringfilePath = filePath.toString()
    console.log('Loading code from:', '/PythonFiles/' + stringfilePath) // Use template literals
    const response = await fetch('PythonFiles/' + stringfilePath)

    code = await response.text()
    isLoading = false // Loading finished
  }
  onMount(loadCode)
  // Get name of file to display in the mock-up code
  let fileName = filePath
</script>

<!--  a component that  receveives the path to a local .py file and puts in the mock-up code
    daisyUI component -->

<h2 class="text-3xl font-bold m-5">{fileName}</h2>
<div class="mockup-code m-5">

  {@html code
    .split('\n')
    .map((line, index) => {
      return `<pre data-prefix="${index + 1}"><code>${line}</code></pre>`
    })
    .join('\n')}
</div>
