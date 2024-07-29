<script>
    import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';
    import { APP_NAME,username,user_token } from '$lib/stores';
    import { DarkMode } from 'flowbite-svelte';
    const logout = async () => {
        username.set("");
        user_token.set("");
    }
    let fluid = false;
</script>
<Navbar {fluid} class="text-black" rounded color="form" let:NavContainer>
    <NavContainer class="mb-px mt-px px-1" {fluid}>
    <NavBrand href="/">
        <img src="/Knowslog_logo.png" class="me-3 h-6 sm:h-9" alt="Flowbite Logo" />
        <span class="self-center whitespace-nowrap text-xl font-semibold dark:text-white">{$APP_NAME}</span>
    </NavBrand>
    <NavHamburger  />
    <NavUl >
        <NavLi href="/">Home</NavLi>
        {#if $username}
        <NavLi href="/crawler">Crawler</NavLi>
        <NavLi href="/chat">Chat</NavLi>
        <NavLi href="/detail">Settings</NavLi>
        <NavLi on:click={logout}>Logout</NavLi>
        {/if}
    </NavUl>
    <div class="ms-auto flex items-center text-gray-500 dark:text-gray-400 sm:order-2">
        <DarkMode class="text-primary-500 dark:text-primary-600 border dark:border-gray-800" />
    </div>
    </NavContainer>
</Navbar>

