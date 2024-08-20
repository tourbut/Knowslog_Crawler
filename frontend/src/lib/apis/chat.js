import fastapi from "$lib/fastapi";

export async function send_message(params, success_callback, failure_callback,streamCallback) {
    let url = "/chat/send_message/"
    await fastapi('stream', url, params,success_callback,failure_callback,streamCallback)
}
