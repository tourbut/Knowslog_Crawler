<script>
    import { Table, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell } from 'flowbite-svelte';
    import { Button, Modal, Label, Input, Checkbox } from 'flowbite-svelte';
    import { Toolbar, ToolbarButton, ToolbarGroup } from 'flowbite-svelte';
    import { PlusOutline } from 'flowbite-svelte-icons';
    export let table_head=[];
    export let table_body=[];
    export let is_editable=false;
    let formModal = false;


</script>

<div>
    <div>
    <Toolbar style="background-color: transparent;">
        <ToolbarButton on:click={() => (formModal = true)}><PlusOutline class="w-4 h-4" /></ToolbarButton>
    </Toolbar>
    </div>
    <div>
    <Table hoverable={true}>
        <TableHead>
            {#each table_head as head}
                    <TableHeadCell>{head}</TableHeadCell>
            {/each}
        </TableHead>
        <TableBody tableBodyClass="divide-y">
            {#each table_body as item}
                <TableBodyRow>
                    {#each Object.values(item) as value}
                        {#if typeof(value) === 'boolean'}
                            <TableBodyCell>
                                <Checkbox bind:checked={value} />
                            </TableBodyCell>
                        {:else}
                            <TableBodyCell>{value}</TableBodyCell>
                        {/if}
                    {/each}
                    {#if is_editable}
                        <TableBodyCell>
                            <button on:click={() => (formModal = true)} class="font-medium text-primary-600 hover:underline dark:text-primary-500">Edit</button>
                        </TableBodyCell>
                    {/if}
                </TableBodyRow>
            {/each}
        </TableBody>
    </Table>
    </div>
</div>

<Modal bind:open={formModal} size="xs" autoclose={false} outsideclose={true} class="w-full">
    <form class="flex flex-col space-y-6" action="#">
      <h3 class="mb-4 text-xl font-medium text-gray-900 dark:text-white">항목 수정</h3>
      <Label class="space-y-2">
        <span>Email</span>
        <Input type="email" name="email" placeholder="name@company.com" required />
      </Label>
      <Label class="space-y-2">
        <span>Your password</span>
        <Input type="password" name="password" placeholder="•••••" required />
      </Label>

      <Button type="submit" class="w-full1">Login to your account</Button>
    </form>
</Modal>