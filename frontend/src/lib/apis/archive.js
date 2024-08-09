import fastapi from "$lib/fastapi";

export async function request_archiving(params, success_callback, failure_callback) {
    let url = "/archive/run_archiving/"
    await fastapi('post', url, params,success_callback,failure_callback)
}