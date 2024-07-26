<script>
    import { Button, Spinner } from "flowbite-svelte";
    import { request_crawler } from "$lib/apis/crawler";
    import { user_token,username } from '$lib/stores';
    import { marked } from 'marked'
    
    import { addToast } from "$lib/apis/common";

    let _url = ''
    let error = {detail:[]}
    let loading = false;
    let markdown = 'Preview'
    const handleSubmit = async () => {

      loading = true;
      let params = {
          url: _url
      }

      let success_callback = (json) => {
            console.log(json)
            loading = false;
            markdown = json.content
        }

      let failure_callback = (json_error) => {
            error = json_error
      addToast('error',error.detail)
        }
      console.log(_url)
      await request_crawler(params, success_callback, failure_callback);
    }
  
</script>

<div class="form-container">
    <h5 class="form-title">웹 크롤링</h5>
    <form method="post" class="form-layout" on:submit|preventDefault={() => {handleSubmit();}}>
      <div>
        <label for="url" class="form-label">URL</label>
        <input type="text" class="form-input" id="url" bind:value={_url}>
      </div>
      <div class="flex flex-wrap items-center gap-2">
        <Button type="submit">
          <Spinner class="me-3" size="4" color="white" />
          Start!
        </Button>
      </div>
    </form>
</div>
<div>
    <h5 class="form-title">미리보기</h5>
<div class='prose'>{@html marked(markdown)}</div>
</div>