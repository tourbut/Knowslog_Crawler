<script>
    import { goto } from '$app/navigation';
	  import { login } from '$lib/apis/user';
    import Error from "$lib/components/Error.svelte";
    import { user_token,username } from '$lib/stores';



  </script>
  {#if $username}
    <div class="container mx-auto p-4 max-w-md">
      <h1>{$username}님 반갑습니다.</h1>
    </div>
  {/if}