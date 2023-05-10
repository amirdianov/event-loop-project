import {WEBSOCKET_URL} from "./consts";

export function initNotifications() {
    const ws = new WebSocket(`${WEBSOCKET_URL}/server/`);
    ws.onclose = console.log;
    ws.onerror = console.log;
    ws.onopen = console.log;
    ws.onmessage = console.log;
}