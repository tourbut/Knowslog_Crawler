<script>
    import '../app.css';
    import { APP_NAME,username,user_token } from '$lib/stores';

    const logout = async () => {
        username.set("");
        user_token.set("");
    }
</script>
<svelte:head>
	<title>
		{$APP_NAME}
	</title>
</svelte:head>
  
<nav class="bg-gray-800 p-4">
  <div class="container mx-auto flex justify-between items-center">
    <div class="flex space-x-4">
      <a href="/" class="text-gray-300 hover:text-white">Home</a>
      {#if $username}
      <a href="/Crawler" class="text-gray-300 hover:text-white">Crawler</a>
      {/if}
    </div>
    {#if $username}
    <div class="flex space-x-4">
      <span class="text-gray-300">{$username}</span>
      <button class="text-gray-300 hover:text-white" on:click={logout}>Logout</button>
    </div>
    {/if}
  </div>
</nav>

<slot></slot>