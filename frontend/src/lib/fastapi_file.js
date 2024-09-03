import { API_URL } from '$lib/constants';
import qs from "qs";
import { user_token } from '$lib/stores';
import { get } from "svelte/store";
import { goto } from '$app/navigation';

const fastapi_file= async (url, file, success_callback, failure_callback) => {
    let _url = API_URL + url;
    let formData = new FormData();
    formData.append('file', file);

    let options = {
        method: 'post',
        headers: {

        },
        body: formData
    };

    const access_token = get(user_token);

    if (access_token) {
        options.headers['Authorization'] = `Bearer ${access_token}`;
    }

    await fetch(_url, options)
        .then(response => {
            response.json()
                .then(json => {
                    if (response.status >= 200 && response.status < 300) {
                        if (success_callback) {
                            success_callback(json);
                        }
                    } else {
                        if (failure_callback) {
                            failure_callback(json);
                        } else {
                            alert(JSON.stringify(json));
                        }
                    }
                })
                .catch(error => {
                    alert(JSON.stringify(error));
                });
        })
        .catch(error => {
            console.error("Fetch error:", error.message || error);
            if (failure_callback) {
                failure_callback(error);
            } else {
                alert("Fetch error: " + JSON.stringify(error));
            }
        });
}

export default fastapi_file;