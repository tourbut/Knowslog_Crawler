<script>
    import { Navbar, NavBrand, NavLi, NavUl, NavHamburger, Dropdown, DropdownItem, DropdownDivider } from 'flowbite-svelte';
    import { ChevronDownOutline } from 'flowbite-svelte-icons';

    import MessageInput from "./MessageInput.svelte";
    import Message from "./Message.svelte";
    import { send_message, get_messages } from "$lib/apis/chat";
    import { addToast } from '$lib/common';

    export let userllm_list = []
    export let chat_id = ''
    export let selected_userllm={value:0,name:"모델선택"}
    
    let message_list= []
    let user_msg = '';
    
    const sendMessage = async () => {
        if (user_msg == '') {
            return;
        }

        if (selected_userllm.value == 0) {
            addToast('error','모델을 선택해주세요.')
            return;
        }

        let message = {
            name: '',
            msg: user_msg,
            time: new Date().toLocaleString(),
            is_user: true
        }

        let res_msg= {
            name: 'Knowslog Bot',
            msg: '',
            time: new Date().toLocaleString(),
            is_user: false
        }

        message_list = [...message_list, message];
        message_list = [...message_list, res_msg];

        let params = {
            chat_id: chat_id,
            user_llm_id: selected_userllm.value,
            input: user_msg,
        }

        let success_callback = (json) => {
            console.log(json)
        }

        let failure_callback = (json_error) => {
            addToast('error',json_error.detail)
        }

        let streamCallback = (json) => {
            
            if (json.is_done){
                message_list[message_list.length-1].msg = json.content
            }
            else{
                message_list[message_list.length-1].msg += json.content
            }
        }
        await send_message(params, success_callback, failure_callback,streamCallback);
    }

    async function get_data()
    {        
        let params = {
            chat_id: chat_id
        }

        let success_callback = (json) => {
            message_list = json.map(item => {return {
                name:item.name,
                msg:item.content,
                time:item.create_date,
                is_user:item.is_user}})
        }

        let failure_callback = (json_error) => {
            addToast('error',json_error.detail)
        }
        await get_messages(params, success_callback, failure_callback);
    }

    let messageListElement;
    
    $: if (chat_id) {
            get_data();
        }

    $ : if (message_list.length > 0) {
            messageListElement.scrollTop = messageListElement.scrollHeight;
        }

</script>
<div >
    <Navbar rounded color="form">
        <NavHamburger />
        <NavUl >
          <NavLi class="cursor-pointer">
            {selected_userllm.name}<ChevronDownOutline class="w-6 h-6 ms-2 text-primary-800 dark:text-white inline" />
          </NavLi>
          <Dropdown class="w-44 z-20">
            {#each userllm_list as userllm}
                <DropdownItem on:click={()=>{selected_userllm=userllm}}>{userllm.name}</DropdownItem>
            {/each}
          </Dropdown>
        </NavUl>
      </Navbar>
</div>
<div class="flex flex-col gap-4">
    <div class="message-container" bind:this={messageListElement}>
        {#each message_list as message}
            <Message bind:message={message}/>
        {/each}
    </div>  
    <MessageInput bind:message={user_msg} sendMessage={sendMessage}/>
</div>

<style>
    .message-container {
        display: flex;
        flex-direction: column;
        gap: 1rem;                /* Tailwind의 gap-4 */
        min-height: 70vh;         /* 최소 높이 설정 (필요에 따라 조정 가능) */
        max-height: 70vh;         /* 최대 높이 설정 (필요에 따라 조정 가능) */
        overflow-y: auto;         /* 내용이 넘칠 경우 수직 스크롤바 표시 */
    }
</style>