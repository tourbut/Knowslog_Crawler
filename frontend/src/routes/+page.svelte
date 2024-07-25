<script>
  import { username } from '$lib/stores';
  import { Alert } from 'flowbite-svelte';
</script>
{#if $username}
  <div class="container mx-auto p-4 max-w-md">
    <h1>{$username}님 반갑습니다.</h1>
  </div>
{/if}
