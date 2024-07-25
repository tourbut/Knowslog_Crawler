<script>
    export let interests = [];
    let newInterest = '';

    function addInterest() {
        if (newInterest.trim()) {
            interests = [...interests, newInterest.trim()];
            newInterest = '';
        }
    }

    function removeInterest(index) {
        interests = interests.filter((_, i) => i !== index);
    }
</script>

<div>
    <div class="flex items-center mb-4">
        <input type="text" id="new-interest" class="form-input p-2 border border-gray-300 rounded flex-grow" bind:value={newInterest} placeholder="관심사 추가">
        <button type="button" class="ml-2 px-4 py-2 bg-gray-200 border border-gray-300 rounded" on:click={addInterest}>추가</button>
    </div>
    <ul>
        {#each interests as interest, index}
            <li class="flex items-center mb-2">
                <span class="flex-grow">{interest}</span>
                <button type="button" class="ml-2 px-2 py-1 bg-red-500 text-white border border-red-500 rounded" on:click={() => removeInterest(index)}>삭제</button>
            </li>
        {/each}
    </ul>
</div>