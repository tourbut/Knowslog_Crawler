<script>
    import { Button, Spinner } from "flowbite-svelte";
    import { Hr} from 'flowbite-svelte';
    import { Card,Label, Input, InputAddon, ButtonGroup, Toggle} from 'flowbite-svelte';
    import { Tabs, TabItem } from 'flowbite-svelte';
    import { request_archiving } from "$lib/apis/archive";
    import MarkdownViewer from "$lib/components/archive/MarkdownViewer.svelte";
    import { addToast } from '$lib/common';

    import Sidebar from "$lib/components/common/Sidebar.svelte";
    import { onMount } from 'svelte';
    import { get_archive_list, get_archive } from "$lib/apis/archive";

    let archive_list = []
    let dataLoaded = false

    let _url = ''
    let error = {detail:[]}
    let loading = false;
    let content = "Content will be displayed here"
    let viewer_content = "Viewer Content will be displayed here"
    let viewer_loading = false
    let viewer_orgin_data = ""
    let auto_translate = true
    let auto_summarize = true

    const btn_start = async () => {
  
      if (_url == '') {
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
        auto_translate:auto_translate,
        auto_summarize:auto_summarize
      }
  
      let success_callback = (json) => {
        addToast('info','수집 완료')
        loading = false;
        content = json.content

        archive_list.forEach(item => {
          if (item.category == json.category) {
            item.items.push({
              label: json.title || 'Untitled',  // title이 없을 경우 'Untitled'로 설정
              herf: `/archive/${json.id}`,            // id 기반 URL 설정
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
                  herf: `/archive/${item.id}`,            // id 기반 URL 설정
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
  </script>

<div class="container">
  <div class="bg-gray-50 dark:bg-gray-800" >
    {#if dataLoaded}
        <Sidebar bind:side_menus={archive_list} btn_click={onclick} />
    {/if}
  </div>
  <div class="content">
    <Card class="form-container my-2">
      <div>
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
      </div>
      <div class="my-2">
        <div class="grid gap-6 md:grid-cols-2">
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
        <TabItem open title="Viewer">
          <MarkdownViewer bind:markdown={viewer_content} bind:loading={viewer_loading} bind:orgin_data={viewer_orgin_data} />
        </TabItem>
        <TabItem title="원본">
          <MarkdownViewer bind:markdown={content} bind:loading={loading} />
        </TabItem>
        <TabItem title="번역">
          <MarkdownViewer bind:markdown={content} bind:loading={loading} />
        </TabItem>
        <TabItem title="요약">
          <MarkdownViewer bind:markdown={content} bind:loading={loading} />
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