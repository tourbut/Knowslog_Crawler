<script>
  import { Skeleton ,Toggle} from 'flowbite-svelte';
  import { marked } from 'marked'
  export let markdown = ""
  export let orgin_data =""
  export let loading = false
  let is_toggle = false
</script>

{#if loading}
  <Skeleton size="xl" class="my-8" />
  <Skeleton size="xl" class="my-8" />
  <Skeleton size="xl" class="my-8" />
{:else}
<div>
  {#if orgin_data}
    <Toggle bind:checked={is_toggle}>Show HTML</Toggle>
  {/if}
</div>
  <div class="bg-gray-50 dark:bg-gray-700 dark:text-white rounded-lg border-gray-300 dark:border-gray-700 divide-gray-300 dark:divide-gray-700 px-2 sm:px-4 py-2.5 w-full text-black">
    <div>
      {#if (is_toggle==false)}
        <div class='dark:text-white prose max-w-none'>{@html marked(markdown)}</div>
      {:else}
        <div class='dark:text-white prose max-w-none'>{orgin_data}</div>
      {/if}
    </div>
  </div>
{/if}
