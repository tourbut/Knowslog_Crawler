<script>
    import { goto } from '$app/navigation';
	  import { login } from '$lib/apis/user';
    import Error from "$lib/components/Error.svelte";
    import { user_token,username } from '$lib/stores';
    let error = {detail:[]}
    let email = ''
    let password = ''
  
    const handleSubmit = async () => {
      
      let params = {
          username: email,
          password: password
      }
  
      let success_callback = (json) => {
              user_token.set(json.access_token)
              username.set(json.username)
              goto('/')
          }
  
      let failure_callback = (json_error) => {
              error = json_error
          }
  
      await login(params, success_callback, failure_callback);
    }
  
  </script>
  {#if $username}
    <div class="container mx-auto p-4 max-w-md">
      <h1>{$username}님 반갑습니다.</h1>
    </div>
  {:else}
  <div class="form-container">
      <h5 class="form-title">로그인</h5>
      <form method="post" class="form-layout" on:submit|preventDefault={() => {handleSubmit();}}>
        <div>
          <label for="email" class="form-label">Email</label>
          <input type="text" class="form-input" id="email" bind:value={email}>
        </div>
        <div>
          <label for="password1" class="form-label">PW</label>
          <input type="password" class="form-input" id="password1" bind:value={password}>
        </div>
        <button type="submit" class="form-button">로그인</button>
        <Error error={error} />
      </form>
  </div>
  
  <div class="container mx-auto p-4 max-w-md">
    <button class="form-button" on:click={() => {goto('/user');}}>회원가입</button>
  </div>
  {/if}