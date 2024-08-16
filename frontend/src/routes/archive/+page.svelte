<script>
    import { Button, Spinner } from "flowbite-svelte";
    import { Hr} from 'flowbite-svelte';
    import { Card,Label, Input, InputAddon, ButtonGroup, Toggle, Textarea} from 'flowbite-svelte';
    import { Tabs, TabItem } from 'flowbite-svelte';
    import { request_archiving } from "$lib/apis/archive";
    import MarkdownViewer from "$lib/components/archive/MarkdownViewer.svelte";
    import { addToast } from '$lib/common';

    import Sidebar from "$lib/components/common/Sidebar.svelte";
    import { onMount } from 'svelte';
    import { get_archive_list, get_archive, delete_archive } from "$lib/apis/archive";
    
    let open_1 = true
    let open_2 = false
    let open_3 = false
    let open_4 = false

    let archive_list = []
    let dataLoaded = false
    let _url = ''
    let _html =''
    let error = {detail:[]}
    let loading = false;

    let viewer_content = "Viewer Content will be displayed here"
    let viewer_loading = false
    let viewer_orgin_data = ""
  
    let orgin_content = "Content will be displayed here"
    let translate_content = "Content will be displayed here"
    let summarize_content = "Content will be displayed here"

    let auto_translate = true
    let auto_summarize = true

    const btn_start = async () => {
      open_2 = true
      if (_url == '' && _html == '') {
        addToast('warning','URL을 입력해주세요.')
        return
      }
      if (loading == true) {
        addToast('warning','수집 진행 중입니다.')
        return
      }
  
      loading = true;
  
      let params = {
        url: _url,
        html: _html,
        auto_translate:auto_translate,
        auto_summarize:auto_summarize
      }
  
      let success_callback = (json) => {
        addToast('info','수집 완료')
        loading = false;
        
        orgin_content = json.content
        translate_content = json.translate_content
        summarize_content = json.summarize_content
        
        console.log(json)

        archive_list.forEach(item => {
          if (item.category == json.category) {
            item.items.push({
              id: item.id,
              label: json.title || 'Untitled',  // title이 없을 경우 'Untitled'로 설정
              herf: '',            // id 기반 URL 설정
              caption: json.url
            });
          }
          
        });
      }
  
      let failure_callback = (json_error) => {
        error = json_error
        loading = false;
        addToast('error',error.detail)
      }
  
      await request_archiving(params, success_callback, failure_callback);
    };
    
    function get_data()
    {
      let params = {}

      let success_callback = (json) => {
        json.forEach(item => {
                // 카테고리로 그룹화된 객체를 찾음
                let categoryGroup = archive_list.find(group => group.category === item.category);

                // 해당 카테고리가 없으면 새로 추가
                if (!categoryGroup) {
                    categoryGroup = { category: item.category, items: [] };
                    archive_list.push(categoryGroup);
                };

                // 아이템 추가
                categoryGroup.items.push({
                  id: item.id,
                  label: item.title || 'Untitled',  // title이 없을 경우 'Untitled'로 설정
                  herf: '',            // id 기반 URL 설정
                  caption: item.url
                });
            });

            dataLoaded = true
      }

      let failure_callback = (json_error) => {
        error = json_error
        loading = false;
        addToast('error',error.detail)
      }

      get_archive_list(params,success_callback, failure_callback)
    }

    onMount( () => {
        get_data()
    })

    async function onclick(event)
    {
      viewer_loading = true;
      const id = event.target.id;
      let params = {
        
      }

      let success_callback = (json) => {
        viewer_content = json.content
        viewer_orgin_data= json.dom
      }
  
      let failure_callback = (json_error) => {
        error = json_error
        loading = false;
        addToast('error',error.detail)
      }

      await get_archive(id,params, success_callback, failure_callback);
      viewer_loading = false;
    }

    async function btn_item_more_click(event)
    {
      console.log(event.target.id)
      
      if (event.target.id =='') {
        return
      }

      let params = {
        id: event.target.id
      }

      let success_callback = (json) => {
        addToast('info','삭제 완료')
        archive_list.forEach(item => {
          item.items = item.items.filter(item => item.id != event.target.id)
        });
      }

      let failure_callback = (json_error) => {
        error = json_error
        loading = false;
        addToast('error',error.detail)
      }

      await delete_archive(params, success_callback, failure_callback);
    }

    let is_html = false
    let translate_tabon = true
    let summarize_tabon = true

    $ : is_html ? _url = '' : _html = ''
    $ : translate_content != "Content will be displayed here" ? translate_tabon = false : translate_tabon = true 
    $ : summarize_content != "Content will be displayed here" ? summarize_tabon = false : summarize_tabon = true 
</script>

<div class="container">
  <div>
    {#if dataLoaded}
        <Sidebar bind:side_menus={archive_list} btn_click={onclick} btn_item_more_click={btn_item_more_click}/>
    {/if}
  </div>
  <div class="content">
    <Card class="form-container my-2">

      <div>
        {#if is_html}
        <Label for="html" class="mb-2">Html 입력</Label>
        <Textarea id="html" bind:value={_html} />
        <Button color="blue" on:click = {btn_start}>
          {#if loading}
          <Spinner class="me-3" size="4" color="white" />
          {/if}
          Start!
        </Button>
        {:else}
        <Label for="url" class="mb-2">수집 사이트 입력</Label>
        <ButtonGroup class="w-full">
          <InputAddon>https://</InputAddon>
          <Input id="url" type="url" placeholder="knowslog.com" bind:value={_url} />
          <Button color="blue" on:click = {btn_start}>
            {#if loading}
            <Spinner class="me-3" size="4" color="white" />
            {/if}
            Start!
          </Button>
        </ButtonGroup>
        {/if}
      </div>
      <Hr hrClass="h-px my-1 bg-gray-200 border-0 dark:bg-gray-700"/>
      <div class="my-2">
        <div class="grid gap-6 md:grid-cols-3">
          <div>
            <Toggle bind:checked={is_html}>Html 입력</Toggle>
          </div>
          <div>
            <Toggle bind:checked={auto_translate}>자동 번역</Toggle>
          </div>
          <div>
            <Toggle bind:checked={auto_summarize}>자동 요약</Toggle>
          </div>
        </div>
      </div>
    </Card>
    
    <Hr hrClass="h-px my-1 bg-gray-200 border-0 dark:bg-gray-700"/>
    
    <div class="form-tabs">
      <Tabs>
        <TabItem bind:open={open_1} title="Viewer">
          <MarkdownViewer bind:markdown={viewer_content} bind:loading={viewer_loading} bind:orgin_data={viewer_orgin_data} />
        </TabItem>
        <TabItem bind:open={open_2} title="원본">
          <MarkdownViewer bind:markdown={orgin_content} bind:loading={loading} />
        </TabItem>
        <TabItem bind:open={open_3} title="번역" disabled={translate_tabon}>
          <MarkdownViewer bind:markdown={translate_content} bind:loading={loading} />
        </TabItem>
        <TabItem bind:open={open_4} title="요약" disabled={summarize_tabon} >
          <MarkdownViewer bind:markdown={summarize_content} bind:loading={loading} />
        </TabItem>
      </Tabs>
    </div>  
  </div> 
</div>


<style>
  .container {
    display: flex;
    min-height: 100vh /* 브라우저 높이와 동일하게 설정 */
  }
  .content {
    flex: 1; /* 남은 공간을 차지하도록 설정 */
    padding: 1rem; /* 콘텐츠 패딩 설정 */
  }
</style>