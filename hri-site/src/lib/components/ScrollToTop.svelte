<script>
  import { onMount } from 'svelte'

  let showButton = false

  function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }

  function handleScroll() {
    showButton = window.scrollY > 0
  }

  onMount(() => {
    window.addEventListener('scroll', handleScroll)
    return () => {
      window.removeEventListener('scroll', handleScroll)
    }
  })
</script>

<style>
  .scroll-to-top {
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 1000;
    /* Add more styles as needed */
  }
</style>

{#if showButton}
  <button on:click={scrollToTop} class="scroll-to-top btn bg-info">
    Scroll to Top
  </button>
{/if}
