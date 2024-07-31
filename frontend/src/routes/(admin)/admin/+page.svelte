<script>
    import Table from '$lib/components/common/Table.svelte';
    import { Tabs, TabItem } from 'flowbite-svelte';

    import { get_llm_settings } from "$lib/apis/admin";
    import { onMount } from 'svelte';
    import { addToast } from '$lib/common';

    let table_head={
      "출처":"string",
      "타입":"string",
      "모델명":"string",
      "설명":"string",
      "Input Price":"number",
      "Output Price":"number",
      "활성화여부":"boolean"
    }
    let table_body=[]

    async function get_data()
    {
      let params = {}

      let success_callback = (json) => {
        table_body=json
      }

      let failure_callback = (json_error) => {
        addToast('error',json_error.detail)
      }

      await get_llm_settings(params,success_callback, failure_callback)
    }
    
    onMount(async () => {
      await get_data()
    })

    onsubmit = async (event) => {
      event.preventDefault();
      console.log(event.detail)
    }

</script>
<div class="form-tabs">
    <Tabs>
      <TabItem open title="모델">
        <Table btn_click={onsubmit} table_head={table_head} bind:table_body={table_body} is_editable={true}/>
      </TabItem>
    </Tabs>
    
</div>