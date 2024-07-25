<script>
    import '../app.css';
    import Navigation from '$lib/components/Navigation.svelte';
    import { APP_NAME,user_token } from '$lib/stores';
    import { goto } from '$app/navigation';
    import { onMount } from 'svelte';

    onMount(async () => {
      if ($user_token === "" && location.pathname !== '/login') {
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

<Navigation />
<slot></slot>