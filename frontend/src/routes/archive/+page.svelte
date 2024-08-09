<script>
    import { Button, Spinner } from "flowbite-svelte";
    import { Hr} from 'flowbite-svelte';
    import { Card,Label, Input, InputAddon, ButtonGroup, Toggle} from 'flowbite-svelte';
    import { Tabs, TabItem } from 'flowbite-svelte';
    import { request_archiving } from "$lib/apis/archive";
    import MarkdownViewer from "$lib/components/archive/MarkdownViewer.svelte";
    import { addToast } from '$lib/common';
  
    let _url = ''
    let error = {detail:[]}
    let loading = false;
    let content = "Content will be displayed here"
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
      }
  
      let failure_callback = (json_error) => {
        error = json_error
        loading = false;
        addToast('error',error.detail)
      }
  
      await request_archiving(params, success_callback, failure_callback);
    };
    
  </script>
  
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
      <TabItem open title="원본">
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
  