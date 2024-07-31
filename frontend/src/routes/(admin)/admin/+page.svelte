<script>
    import Table from '$lib/components/common/Table.svelte';
    import { Tabs, TabItem } from 'flowbite-svelte';

    import { get_llm_settings } from "$lib/apis/admin";
    import { onMount } from 'svelte';
    import { addToast } from '$lib/common';

    let table_head=["출처","타입","모델명","설명","Input Price","Output Price","활성화여부"]
    let table_body=[]

    async function get_data()
    {
      let params = {}

      let success_callback = (json) => {
        
        console.log(typeof(json[0].is_active))
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

</script>
<div class="form-tabs">
    <Tabs>
      <TabItem open title="모델">
        <Table table_head={table_head} bind:table_body={table_body} is_editable={true}/>
      </TabItem>
    </Tabs>
    
</div>