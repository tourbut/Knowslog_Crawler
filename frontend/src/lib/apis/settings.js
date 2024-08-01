import fastapi from "$lib/fastapi";

export async function get_llm_settings(params, success_callback, failure_callback) {
    let url = "/settings/get_llm_settings/"
    await fastapi('get', url, params,success_callback,failure_callback)
}