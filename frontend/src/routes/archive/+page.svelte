<script>
    import { Button, Spinner } from "flowbite-svelte";
    import { Hr} from 'flowbite-svelte';
    import { Card,Label, Input, InputAddon, ButtonGroup, Toggle, Textarea} from 'flowbite-svelte';
    import { Tabs, TabItem } from 'flowbite-svelte';
    import { request_archiving } from "$lib/apis/archive";
    import MarkdownViewer from "$lib/components/archive/MarkdownViewer.svelte";
    import { addToast } from '$lib/common';

    import Sidebar from "$lib/components/common/Sidebar.svelte";
    import FileUploader from "$lib/components/archive/FileUploader.svelte";
    import { onMount } from 'svelte';
    import { get_archive_list, get_archive, delete_archive, upload_flies} from "$lib/apis/archive";

    let archive_list = []
    let dataLoaded = false
    let _url = ''
    let _html =''
    let error = {detail:[]}
    let loading = false;

    let orgin_content = "Content will be displayed here"
    let orgin_data = ""

    let translate_content = "Content will be displayed here"
    let summarize_content = "Content will be displayed here"

    let auto_translate = true
    let auto_summarize = true

    const btn_start = async () => {
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

    const onclick = async (id) => {
      
      if (id =='') {
        return
      }

      let params = {
        
      }

      let success_callback = (json) => {
        orgin_content = json.content
        orgin_data= json.dom
        translate_content = json.translate_content
        summarize_content = json.summarize_content
      }
  
      let failure_callback = (json_error) => {
        error = json_error
        loading = false;
        addToast('error',error.detail)
      }

      await get_archive(id,params, success_callback, failure_callback);
    }

    const btn_item_more_click = async (id) =>
    {
      if (id =='') {
        return
      }

      let params = {
        id: id
      }

      let success_callback = (json) => {
        addToast('info','삭제 완료')
        archive_list.forEach(item => {
          item.items = item.items.filter(item => item.id != id)
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

    let files = null;
    let file_value = null;

    const file_upload = async () => {

      if (files == null) {
        addToast('warning','파일을 선택해주세요.')
        return
      }

      let file_ext = files[0].name.split('.').pop().toLowerCase();

      if (!['txt','TXT','pdf','PDF','xlsx','XLSX','csv','CSV'].includes(file_ext)) {
        addToast('warning','지원하지 않는 파일 형식입니다.')
        return
      }

      if (loading == true) {
        addToast('warning','파일 업로드 중입니다.')
        return
      }
      loading = true;

      let success_callback = (json) => {
        addToast('info','업로드 완료')
        loading = false;
      }
  
      let failure_callback = (json_error) => {
        error = json_error
        loading = false;
        addToast('error',error.detail)
      }
      await upload_flies(files[0], success_callback, failure_callback);
    }
</script>

<div class="container">
  <div>
    {#if dataLoaded}
        <Sidebar bind:side_menus={archive_list} btn_click={onclick} btn_item_more_click={btn_item_more_click}/>
    {/if}
  </div>
  <div class="content">
    <div class="mx-auto p-1 max-w-sm">
      <Tabs contentClass="">
        <TabItem open={true}>
          <span slot="title">웹</span>
          <Card>
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
        </TabItem>
        <TabItem >
          <span slot="title">파일</span>
          <Card>
            <div>
              <Label for="file" class="mb-2">파일 업로드</Label>
              <FileUploader bind:files={files} bind:value={file_value} />
              <Button on:click={file_upload}>Upload</Button>
            </div>
          </Card>
        </TabItem>
      </Tabs>
    </div>
    
    <Hr hrClass="h-px my-1 bg-gray-200 border-0 dark:bg-gray-700"/>
    
    <div class="form-tabs">
      <Tabs>
        <TabItem open={true} title="원본">
          <MarkdownViewer bind:markdown={orgin_content} bind:loading={loading} bind:orgin_data={orgin_data}/>
        </TabItem>
        <TabItem title="번역" disabled={translate_tabon}>
          <MarkdownViewer bind:markdown={translate_content} bind:loading={loading} />
        </TabItem>
        <TabItem title="요약" disabled={summarize_tabon} >
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
    padding: 0rem; /* 콘텐츠 패딩 설정 */
  }
</style>