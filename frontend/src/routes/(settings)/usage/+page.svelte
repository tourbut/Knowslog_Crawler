<script>
    import { Tabs, TabItem } from 'flowbite-svelte';
    import { addToast } from '$lib/common';
    import { onMount } from 'svelte';
    import { get_userusage} from "$lib/apis/settings";
    import Table from '$lib/components/common/Table.svelte';
    import Combo from '$lib/components/common/Combo.svelte';

    let usage_table_head=[
      {id:0,name:"usage_date",type:"date",desc:"이용일자"},
      {id:1,name:"source",type:"string",desc:"출처"},
      {id:2,name:"name",type:"string",desc:"모델명"},
      {id:3,name:"input_token",type:"integer",desc:"Input Token"},
      {id:4,name:"output_token",type:"integer",desc:"Output Token"},
      {id:5,name:"cost",type:"float",desc:"비용"},
    ];

    let ComboMenu = [
      { value: 'day', name: '일별 사용량' },
      { value: 'month', name: '월별 사용량' },
    ]
    let query_type = 'day'

    let usage_table_body=[];
    
    async function get_data()
    {
      let params = {}

      let success_callback = (json) => {
        usage_table_body=json
      }

      let failure_callback = (json_error) => {
        addToast('error',json_error.detail)
      }

      await get_userusage(params,success_callback, failure_callback)
    }
    onMount(async () => {
      await get_data()
    })

    $: if (query_type == 'day')
    {
        usage_table_head[0].desc = '이용일자'
    }
    else
    {
        usage_table_head[0].desc = '이용월'
        //같은 월끼리 token cost sum
        

    }

</script>
<div class='form-tabs'>  
    <Tabs>
        <TabItem open title="비용">
            <Combo bind:ComboMenu={ComboMenu} bind:selected_name={query_type} />
            <Table is_plus={false} bind:table_head={usage_table_head} bind:table_body={usage_table_body}/>
        </TabItem>
    </Tabs>
</div>