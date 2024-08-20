<script>
    import Chat from "$lib/components/chat/Chat.svelte";
</script>

<div class="chat-container">
    <Chat />
</div>

<style>
   .chat-container {
        flex: 1;                     /* 남은 공간을 차지하도록 설정 */
        margin-left: auto;           /* 좌우 중앙 정렬 */
        margin-right: auto;          /* 좌우 중앙 정렬 */
        padding: 1rem;               /* padding: 1rem (Tailwind의 p-4에 해당) */
        min-height: 100vh;           /* 브라우저 높이와 동일하게 설정 */
        max-width: 64rem;            /* 최대 너비 64rem (Tailwind의 max-w-5xl에 해당) */
    }
</style>