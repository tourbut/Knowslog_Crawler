<script>
    import { marked } from 'marked'
    export let message = {
        id: '1',
        name: 'Jese',
        msg: 'Hello, how can I help you?',
        time: '2024.02.20. 14:30:22',
        is_user: true
    }

    function copyToClipboard() {
    const messageText = document.getElementById(message.id).innerText;
    navigator.clipboard.writeText(messageText).then(() => {
        alert('Message copied to clipboard!');
    }).catch(err => {
        console.error('Could not copy text: ', err);
    });
}
</script>

{#if message.is_user}
<div class="flex items-start gap-2.5 justify-end">
    <div class="flex flex-col w-auto max-w-[320px] leading-1.5 p-4 border-gray-200 bg-gray-100 rounded-e-xl rounded-es-xl dark:bg-gray-700">
       <div class="flex items-center space-x-2 rtl:space-x-reverse">
          <span class="text-sm font-semibold text-gray-900 dark:text-white">{message.name}</span>
          <span class="text-sm font-normal text-gray-500 dark:text-gray-400">{message.time}</span>
       </div>
       <p id={message.id} class="text-sm font-normal py-2.5 text-gray-900 dark:text-white" style="white-space: pre-wrap;">{message.msg}</p>
    </div>
</div>
{:else}
<div class="flex items-start gap-2.5">
    <img class="w-8 h-8 rounded-full" src="/Knowslog_logo.png" alt="Knowslog">
    <div class="relative flex flex-col w-auto max-w-half leading-1.5 p-4 border-gray-200 bg-gray-100 rounded-e-xl rounded-es-xl dark:bg-gray-700">
        <div class="flex items-center space-x-2 rtl:space-x-reverse">
            <span class="text-sm font-semibold text-gray-900 dark:text-white">{message.name}</span>
            <span class="text-sm font-normal text-gray-500 dark:text-gray-400">{message.time}</span>
            <button on:click={copyToClipboard} class="ml-auto text-gray-900 dark:text-gray-400 m-0.5 hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-600 dark:hover:bg-gray-700 rounded-lg py-2 px-2.5 inline-flex items-center justify-center bg-white border-gray-200 border">
                <span id="default-message" class="inline-flex items-center">
                    <svg class="w-3 h-3 me-1.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 18 20">
                        <path d="M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2Zm-3 14H5a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2Zm0-4H5a1 1 0 0 1 0-2h8a1 1 0 1 1 0 2Zm0-5H5a1 1 0 0 1 0-2h2V2h4v2h2a1 1 0 1 1 0 2Z"/>
                    </svg>
                    <span class="text-xs font-semibold">Copy</span>
                </span>
            </button>
        </div>
        <p id={message.id} class="text-sm font-normal py-2.5 text-gray-900 dark:text-white prose" style="white-space: pre-wrap;">{@html marked(message.msg)}</p>
    </div>
</div>
{/if}