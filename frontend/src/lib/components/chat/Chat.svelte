<script>
    import MessageInput from "./MessageInput.svelte";
    import Message from "./Message.svelte";
    import { send_message } from "$lib/apis/chat";
    import { v4 as uuidv4 } from "uuid";
    import { addToast } from '$lib/common';
    
    let message_list= []

    let user_msg = '';

    const sendMessage = async () => {
        let message = {
            id : uuidv4(),
            name: 'Shin',
            msg: user_msg,
            time: new Date().toLocaleString(),
            is_user: true
        }

        let res_msg= {
            id : uuidv4(),
            name: 'bot',
            msg: '',
            time: new Date().toLocaleString(),
            is_user: false
        }

        message_list = [...message_list, message];
        message_list = [...message_list, res_msg];

        let params = {
            input: user_msg
        }

        let success_callback = (json) => {
            console.log(json)
        }

        let failure_callback = (json_error) => {
            console.log(json_error)
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
</script>

<div class="flex flex-col gap-4">
    <div class="message-container">
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
        max-height: 80vh;         /* 최대 높이 설정 (필요에 따라 조정 가능) */
        min-height: 80vh;         /* 최소 높이 설정 (필요에 따라 조정 가능) */
        overflow-y: auto;         /* 내용이 넘칠 경우 수직 스크롤바 표시 */
    }
</style>