<script>
    import { Input, Label, Helper, Button, Checkbox, A,InputAddon,ButtonGroup } from 'flowbite-svelte';
    import {Select,Toggle } from 'flowbite-svelte';
    import { ChevronDownOutline, EyeOutline, EyeSlashOutline } from 'flowbite-svelte-icons';

    import { get_llm_settings } from "$lib/apis/settings";
    import { addToast } from '$lib/common';
    import { onMount } from 'svelte';

    let is_apishow = false;

    let api_name="";
    let api_key="";
    let active_yn=false;
    let instruct_prompt="";
    let response_prompt="";
    let selected = 'openai';
    let source = [
        { value: 'openai', name: 'OpenAI' },
        { value: 'claude', name: 'Claude' },
        { value: 'gemini', name: 'Gemini' }
    ];

    async function get_data()
    {
      let params = {}

      let success_callback = (json) => {
        console.log(json)
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
<div class='form-container'>  
  <form>
    <div class="mb-4">
        <div>
            <Label for="api_key" class="mb-2">API Key</Label>
            <div class="grid gap-6 mb-1 md:grid-cols-2">
                <div class="mb-1">
                    <Select items={source} bind:value={selected} placeholder="Source" />
                </div>
                <div class="mb-1">
                    <Select items={source} bind:value={selected} placeholder="Source" />
                </div>
            </div>
            <div class="mb-1">
            <ButtonGroup class="w-full">
                <InputAddon>
                    <button on:click={() => (is_apishow = !is_apishow)}>
                        {#if is_apishow}
                        <EyeOutline class="w-6 h-6" />
                        {:else}
                        <EyeSlashOutline class="w-6 h-6" />
                        {/if}
                    </button>
                </InputAddon>
                <Input bind:value={api_key} id="api_key" type={is_apishow ? 'text' : 'password'} placeholder="Your API here" />
            </ButtonGroup>
            </div>
            <div>
                <Toggle bind:checked={active_yn}>활성화</Toggle>
            </div>
        </div>
    </div>

    <div class="mb-1">
        <div>
            <Label for="prompt" class="mb-2">Prompt</Label>
        </div>
    </div>

    <Button type="submit">저장</Button>
  </form>
</div>