<script>
  import { Button, Spinner } from "flowbite-svelte";
  import { Heading, P, Hr} from 'flowbite-svelte';
  import { Label, Input, InputAddon, ButtonGroup, Checkbox } from 'flowbite-svelte';
  import { request_crawler } from "$lib/apis/crawler";
  import { user_token,username } from '$lib/stores';
  import { marked } from 'marked'
  import { addToast } from '$lib/common';

  let _url = ''
  let error = {detail:[]}
  let loading = false;
  let markdown = "Content will be displayed here"

  const btn_start = async () => {

    if (loading == true) {
      addToast('warning','Already Crawling')
      return
    }

    loading = true;
    let params = {
        url: _url
    }

    let success_callback = (json) => {
      addToast('info','Crawling Success')
          loading = false;
          markdown = json.content
      }

    let failure_callback = (json_error) => {
          error = json_error
      addToast('error',error.detail)
      }
    console.log(_url)
    await request_crawler(params, success_callback, failure_callback);
  };
  
</script>

<div class="grid grid-cols-1 md:grid-cols-2 gap-8 py-8 px-6">
  <div>
    <Label for="url" class="mb-2 text-xl">수집 사이트 입력</Label>
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
  <div>
    <Label for="url" class="mb-2 text-xl">수집 사이트 입력</Label>
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
</div>

<Hr hrClass="h-px my-1 bg-gray-200 border-0 dark:bg-gray-700"/>

<div class="grid grid-cols-1 md:grid-cols-2 gap-8 py-8 px-6">
  <div class="bg-gray-50 dark:bg-gray-700 dark:text-white rounded-lg border-gray-300 dark:border-gray-700 divide-gray-300 dark:divide-gray-700 px-2 sm:px-4 py-2.5 w-full text-black">
    <div>
      <div class='dark:text-white prose'>{@html marked(markdown)}</div>
    </div>
  </div>
  <div class="bg-gray-50 dark:bg-gray-700 dark:text-white rounded-lg border-gray-300 dark:border-gray-700 divide-gray-300 dark:divide-gray-700 px-2 sm:px-4 py-2.5 w-full text-black">
    <div>
      <div class='dark:text-white prose'>{@html marked(markdown)}</div>
    </div>
  </div>
</div>