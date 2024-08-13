<script>
    import { Sidebar, SidebarGroup, SidebarItem, SidebarWrapper,SidebarDropdownWrapper,SidebarDropdownItem,Tooltip } from 'flowbite-svelte';
    import { Drawer, Button, CloseButton } from 'flowbite-svelte';
    import { ChevronDoubleUpOutline, ChevronDoubleDownOutline, AngleRightOutline, AngleLeftOutline } from 'flowbite-svelte-icons';
    import { sineIn } from 'svelte/easing';
    let spanClass = 'flex-1 ms-3 whitespace-nowrap w-9/10 overflow-hidden text-ellipsis';
    let is_hidden = true;
    export let side_menus = [
    { 
        category : 'Top',
        items: [
            {id:1,label: 'Home', herf: '/',caption: 'Home'},
            {id:2,label: 'About', herf: '/about',caption: 'About'},
        ]
    }];
    
    export let btn_click;
    let backdrop = false;
    let transitionParams = {
    x: -320,
    duration: 200,
    easing: sineIn
  };
</script>
<div class="relative">
    <div class="absolute top-80">
        <button on:click={() => (is_hidden = false)}><AngleRightOutline size="xl" color="red" /></button>
    </div>
    <Drawer {backdrop} transitionType="fly" {transitionParams} bind:hidden={is_hidden} id="sidebar">
    <div >
        <div class="absolute top-0 right-0">
            <CloseButton color="red" on:click={() => (is_hidden = true)} />
        </div>
        <div>
            <Sidebar >
                <SidebarWrapper>
                    <SidebarGroup>
                        {#each side_menus as menu (menu.category)}
                        <SidebarDropdownWrapper label={menu.category}>
                            <svelte:fragment slot="arrowup">
                                <ChevronDoubleUpOutline class="w-6 h-6" />
                            </svelte:fragment>
                            <svelte:fragment slot="arrowdown">
                                <ChevronDoubleDownOutline class="w-6 h-6" />
                            </svelte:fragment>
                            {#each menu.items as item}
                                <SidebarDropdownItem id={item.id} label={item.label} href={item.herf} class={spanClass} on:click={btn_click} />
                                <Tooltip target={item.id} placement="bottom">{item.label}<br>({item.caption})</Tooltip>
                            {/each}
                        </SidebarDropdownWrapper>
                        {/each}
                    </SidebarGroup>
                </SidebarWrapper>
            </Sidebar>
        </div>
    </div>
    </Drawer>
</div>