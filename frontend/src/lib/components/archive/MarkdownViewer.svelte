<script>
  import { Skeleton } from 'flowbite-svelte';
  import { marked } from 'marked'
  export let markdown = ""
  export let loading = false
</script>

{#if loading}
  <Skeleton size="xl" class="my-8" />
  <Skeleton size="xl" class="my-8" />
  <Skeleton size="xl" class="my-8" />
{:else}
  <div class="bg-gray-50 dark:bg-gray-700 dark:text-white rounded-lg border-gray-300 dark:border-gray-700 divide-gray-300 dark:divide-gray-700 px-2 sm:px-4 py-2.5 w-full text-black">
    <div>
      <div class='dark:text-white prose max-w-none'>{@html marked(markdown)}</div>
    </div>
  </div>
{/if}
