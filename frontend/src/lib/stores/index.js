import { writable } from 'svelte/store';
import { WEB_NAME } from '$lib/constants';

const persist_storage = (key, initValue) => {
    const storedValueStr = sessionStorage.getItem(key)
    const store = writable(storedValueStr != null ? JSON.parse(storedValueStr) : initValue)
    store.subscribe((val) => {
        sessionStorage.setItem(key, JSON.stringify(val))
    })
    return store
}

export const APP_NAME = persist_storage("APP_NAME",WEB_NAME);
export const user_token = persist_storage("user_token",null);