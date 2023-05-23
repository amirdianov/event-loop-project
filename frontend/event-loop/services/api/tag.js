import {check_token} from "../token_verify";
import store from "@/store";
import {instance} from "./instance";


export async function getTags() {
    await check_token(store.state.login.tokens, instance)
    const response = await instance.get(`/tags`)
    return response.data
}
