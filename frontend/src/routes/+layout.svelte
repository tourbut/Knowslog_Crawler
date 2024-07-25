<script>
    import '../app.css';
    import { APP_NAME,username,user_token } from '$lib/stores';
    import { onMount } from 'svelte';
    import { goto } from '$app/navigation';
    const logout = async () => {
        username.set("");
        user_token.set("");
    }

    onMount(async () => {
      if ($user_token === "") {
        alert("로그인이 필요합니다.");
        await goto('/login');
      } 
    })
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
      <a href="/crawler" class="text-gray-300 hover:text-white">Crawler</a>
      {/if}
    </div>
    {#if $username}
    <div class="flex space-x-4">
      <span class="text-gray-300">{$username}</span>
      <a href="/detail" class="text-gray-300 hover:text-white">개인정보</a>
      <button class="text-gray-300 hover:text-white" on:click={logout}>Logout</button>
    </div>
    {/if}
  </div>
</nav>

<slot></slot>