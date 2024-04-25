<script lang="ts">
  import { onMount } from 'svelte'
  import { base } from '$app/paths'

  let pythonFiles = [] // Stores metadata of Python files including name and content
  let isLoading = true // Indicates if the app is loading data

  onMount(async () => {
    try {
      const fileListResponse = await fetch(`${base}/fileList.json`)
      const fileListResult = await fileListResponse.json()
      const files = fileListResult.files

      // Fetch content for each file and store it in pythonFiles array
      const fetchFileContentsPromises = files.map(async (filePath) => {
        const codeResponse = await fetch(`${base}/PythonFiles/${filePath}`)
        const code = await codeResponse.text()
        return { name: filePath, code: code } // Return an object containing file name and its content
      })

      // Wait for all file contents to be fetched
      pythonFiles = await Promise.all(fetchFileContentsPromises)
    } catch (error) {
      console.error('Error fetching files:', error)
    } finally {
      isLoading = false
    }
  })
  function scrollToElement(file) {
    const element = document.getElementById(file)
    if (element) {
      element.scrollIntoView({ behavior: 'smooth', block: 'start' })
    }
  }
</script>

<div>
  {#each pythonFiles as file}
    <button
      class="btn bg-accent text-accent-content m-2"
      on:click={() => scrollToElement(file.name)}>
      {file.name}
    </button>
  {/each}
</div>

<div>
  {#if isLoading}
    <p>Loading...</p>
  {:else}
    {#each pythonFiles as file}
      <h2 id={file.name} class="text-3xl font-bold m-5">{file.name}</h2>
      <div class="mockup-code m-5">

        {@html file.code
          .split('\n')
          .map((line, index) => {
            return `<pre data-prefix="${index + 1}"><code>${line}</code></pre>`
          })
          .join('\n')}
      </div>
    {/each}
  {/if}
</div>
