<script>
    import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';
    import { APP_NAME,username,user_token } from '$lib/stores';
    import { goto } from '$app/navigation';
    const logout = async () => {
        username.set("");
        user_token.set("");
    }
</script>
<Navbar  >
    <NavBrand href="/">
        <img src="/favicon.png" class="me-3 h-6 sm:h-9" alt="Flowbite Logo" />
        <span class="self-center whitespace-nowrap text-xl font-semibold dark:text-white">{$APP_NAME}</span>
    </NavBrand>
    <NavHamburger  />
    <NavUl >
        <NavLi href="/">Home</NavLi>
        {#if $username}
        <NavLi href="/crawler">Crawler</NavLi>
        <NavLi href="/detail">개인정보</NavLi>
        <NavLi on:click={logout}>Logout</NavLi>
        {/if}
    </NavUl>
</Navbar>

