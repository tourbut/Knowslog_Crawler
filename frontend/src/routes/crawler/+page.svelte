<script>
    import { request_crawler } from "$lib/apis/crawler";
    import Error from "$lib/components/Error.svelte";
    import { user_token,username } from '$lib/stores';
    import Spinner from "$lib/components/Spinner.svelte";
    let _url = ''
    let error = {detail:[]}
    let loading = false;

    const handleSubmit = async () => {

      loading = true;
      let params = {
          url: _url
      }

      let success_callback = (json) => {
            console.log(json)
            loading = false;
        }

      let failure_callback = (json_error) => {
            error = json_error
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
      <button type="submit" class="form-button">수집</button>
      <Error error={error} />
    </form>

    {#if loading}
        <div class="fixed inset-0 flex justify-center items-center bg-gray-800 bg-opacity-75">
            <Spinner />
        </div>
    {/if}

</div>