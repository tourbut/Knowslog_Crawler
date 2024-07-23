<div class="flex justify-center items-center">
    <div class="animate-spin rounded-full h-16 w-16 border-t-4 border-blue-500"></div>
</div>
  
<style>
.animate-spin {
    animation: spin 1s linear infinite;
}

@keyframes spin {
    0% {
    transform: rotate(0deg);
    }
    100% {
    transform: rotate(360deg);
    }
}
</style>