<script>
    import { goto } from '$app/navigation';
    import { create_detail, update_detail,get_detail } from "$lib/apis/user";
    import LlmCombo from '$lib/components/detail/LLM_Combo.svelte';
    import InterestsInput from '$lib/components/detail/InterestsInput.svelte';
    import { onMount } from 'svelte';
    import addToast from '$lib/apis/common';
    let error = {detail:[]}
    let name = ""
    let age = 0
    let discord_yn = false
    let email_yn = false
    let llm_model = ""
    let api_key = ""
    let interests = []
    let data_loaded = false

    async function get_data()
    {
      let params = {}
      let success_callback = (json) => {
        if (json != null) {
          data_loaded = true
        }
        name = json.name
        age = json.age
        discord_yn = json.discord_yn
        email_yn = json.email_yn
        llm_model = json.llm_model
        api_key = json.api_key
        interests = json.interests ? json.interests.split('|') : []

      }

      let failure_callback = (json_error) => {
        error = json_error
      addToast('error',error.detail)
      }

      await get_detail(params,success_callback, failure_callback)
    }

    onMount(async () => {
      await get_data()
    })


    async function handleSubmit(event) {
      event.preventDefault();

      const button = event.submitter;
      
      let params = {
            "name": name,
            "age": age,
            "discord_yn": discord_yn,
            "email_yn": email_yn,
            "llm_model": llm_model,
            "api_key": api_key,
            "interests": interests.join('|'),
        }

        let success_callback = (json) => {
          get_data()
        }

        let failure_callback = (json_error) => {
            error = json_error
      addToast('error',error.detail)
        }

        if (button.name == "btn_create") {
          await create_detail(params, success_callback, failure_callback);
        } else if (button.name == "btn_update") {
          await update_detail(params, success_callback, failure_callback);
        }
      }

</script>
<div class="form-container">
    <h5 class="form-title">유저 개인정보</h5>
    <form method="post" class="form-layout" on:submit= {handleSubmit}>
      <div>
        <label for="name" class="form-label">이름</label>
        <input type="text" class="form-input" id="name" bind:value={name}>
        <label for="age" class="form-label">나이</label>
        <input type="number" class="form-input" id="age" bind:value={age} min="0">
      </div>
      <div class="form-inline">
        <label for="discord_yn" class="form-label">디스코드 수신여부</label>
        <input type="checkbox" class="form-input-inline" id="discord_yn" bind:checked={discord_yn}>
        <label for="email_yn" class="form-label">이메일 수신여부</label>
        <input type="checkbox" class="form-input-inline" id="email_yn" bind:checked={email_yn}>
      </div>
      <div>
        <label for="llm_model" class="form-label">LLM 모델</label>
        <LlmCombo bind:llm_model={llm_model} /> <!-- Use the LLM model select component -->
            
        <label for="api_key" class="form-label">API 키</label>
        <input type="password" class="form-input" id="api_key" bind:value={api_key}>
        <label for="interests" class="form-label">관심사</label>
        
        <InterestsInput bind:interests={interests} /> <!-- Use the InterestsInput component -->
      </div>
      {#if data_loaded}
        <button name="btn_update" type="submit" class="form-button">수정</button>
      {:else}
        <button name="btn_create" type="submit" class="form-button">저장</button>
      {/if}
    </form>
</div> 