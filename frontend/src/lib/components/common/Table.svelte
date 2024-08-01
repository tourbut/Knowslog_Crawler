<script>
    import { Table, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell } from 'flowbite-svelte';
    import { Button, Modal, Label, Input, FloatingLabelInput , Checkbox } from 'flowbite-svelte';
    import { Toolbar, ToolbarButton, ToolbarGroup } from 'flowbite-svelte';
    import { PlusOutline } from 'flowbite-svelte-icons';
    export let table_head=[
        {id:0,name:"col1",type:"string",desc:"샘플컬럼1"},
        {id:1,name:"col2",type:"boolean",desc:"샘플컬럼2"}
    ];
    export let table_body=[];
    export let is_editable=false;
    export let btn_click;
    export let form_data={}
    export let formModal = false;
    let is_new=false;

    function btn_edit(data)  {
        //console.log(data);
        form_data=data;
        formModal = true;
        is_new=false;
    }


</script>

<div>
    <div>
    <Toolbar style="background-color: transparent;">
        <ToolbarButton on:click={() => (formModal = true, is_new=true)}><PlusOutline class="w-4 h-4" /></ToolbarButton>
    </Toolbar>
    </div>
    <div>
    <Table hoverable={true}>
        <TableHead>
            {#each table_head as item}
                <TableHeadCell>{item.desc}</TableHeadCell>
            {/each}
            {#if is_editable}
                <TableHeadCell></TableHeadCell>
            {/if}
        </TableHead>
        <TableBody tableBodyClass="divide-y">
            {#each table_body as item}
                <TableBodyRow>
                    {#each table_head as head}
                    {#if (head.type === 'boolean')}
                    <TableBodyCell>
                        <Checkbox bind:checked={item[head.name]} />
                    </TableBodyCell>
                    {:else}
                    <TableBodyCell>{item[head.name]}</TableBodyCell>
                    {/if}
                    {/each}
                    {#if is_editable}
                        <TableBodyCell>
                            <button on:click={btn_edit(item)} class="font-medium text-primary-600 hover:underline dark:text-primary-500">
                                Edit
                            </button>
                        </TableBodyCell>
                    {/if}
                </TableBodyRow>
            {/each}
        </TableBody>
    </Table>
    </div>
</div>

<Modal bind:open={formModal} size="xs" autoclose={false} outsideclose={true} class="w-full">
    <form class="flex flex-col space-y-3" action="#">
        {#if (is_new)}
        <h3 class="mb-4 text-xl font-medium text-gray-900 dark:text-white">항목 추가</h3>
        {:else}
        <h3 class="mb-4 text-xl font-medium text-gray-900 dark:text-white">항목 수정</h3>
        {/if}
        {#each table_head as head}
            {#if (head.type === 'boolean')}
            <Label class="text-gray-500 dark:text-gray-400 mt-4 flex items-center">
                {head.desc} <Checkbox class="ms-2" bind:checked={form_data[head.name]}  />
            </Label>
            {:else}
                <FloatingLabelInput style="filled" id="floating_filled" name="floating_filled" type="text" bind:value={form_data[head.name]}>
                    {head.desc}
                </FloatingLabelInput>
            {/if}
        {/each}
      <Button name={is_new ? "btn_new":"btn_update"} type="submit" class="w-full1" on:click={btn_click}>저장</Button>
    </form>
</Modal>