import fastapi from "$lib/fastapi";

export async function request_crawler(params, success_callback, failure_callback) {
    let url = "/crawler/run_crawler/"
    await fastapi('post', url, params,success_callback,failure_callback)
}