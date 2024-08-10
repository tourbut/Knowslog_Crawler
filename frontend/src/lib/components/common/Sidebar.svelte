<script>
    import { Sidebar, SidebarGroup, SidebarItem, SidebarWrapper,SidebarDropdownWrapper,SidebarDropdownItem,Tooltip } from 'flowbite-svelte';
    import { ChevronDoubleUpOutline, ChevronDoubleDownOutline } from 'flowbite-svelte-icons';

    let spanClass = 'flex-1 ms-3 whitespace-nowrap';

    export let side_menus = [
    { 
        category : 'Top',
        items: [
            {label: 'Home', herf: '/',caption: 'Home'},
            {label: 'About', herf: '/about',caption: 'About'},
        ]
    }]
    ;
    
</script>
  
<Sidebar >
    <SidebarWrapper>
        <SidebarGroup>
            {#each side_menus as menu, index (menu.category)}
            <SidebarDropdownWrapper label={menu.category}>
                <svelte:fragment slot="arrowup">
                    <ChevronDoubleUpOutline class="w-6 h-6" />
                </svelte:fragment>
                <svelte:fragment slot="arrowdown">
                    <ChevronDoubleDownOutline class="w-6 h-6" />
                </svelte:fragment>
                {#each menu.items as item}
                    <SidebarDropdownItem id={item.label} label={item.label} href={item.herf} class={spanClass} />
                    <Tooltip target={item.label} placement="bottom">{item.caption}</Tooltip>
                {/each}
            </SidebarDropdownWrapper>
            {/each}
        </SidebarGroup>
    </SidebarWrapper>
</Sidebar>