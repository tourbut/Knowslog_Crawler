<script>
  import { Card, Button, Label, Input, Checkbox } from 'flowbite-svelte';
  import { goto } from '$app/navigation';
  import { login } from '$lib/apis/user';
  import { addToast } from '$lib/common';
  import { user_token,username,is_admin } from '$lib/stores';
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
      is_admin.set(json.is_admin)
      goto('/')
    }

    let failure_callback = (json_error) => {
      error = json_error
      addToast('error',error.detail)
    }

    await login(params, success_callback, failure_callback);
  }

</script>
{#if $username}
  <div class="container mx-auto p-4 max-w-md">
    <h1>{$username}님 반갑습니다.</h1>
  </div>
{:else}
<Card class="container mx-auto p-4 max-w-md my-8">
  <form class="flex flex-col space-y-6" method="post" on:submit|preventDefault={() => {handleSubmit();}}>
    <h3 class="text-xl font-medium text-gray-900 dark:text-white">Sign in to Knowslog</h3>
    <Label class="space-y-2">
      <span>Email</span>
      <Input type="email" name="email" placeholder="name@company.com" required bind:value={email} />
    </Label>
    <Label class="space-y-2">
      <span>Your password</span>
      <Input type="password" name="password" placeholder="•••••" required bind:value={password} />
    </Label>
    <Button type="submit" class="w-full">Login to your account</Button>
    <div class="text-sm font-medium text-gray-500 dark:text-gray-300">
      Not registered? <a href="/user" class="text-primary-700 hover:underline dark:text-primary-500"> Create account </a>
    </div>
  </form>
</Card>
{/if}