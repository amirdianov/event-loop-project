import {WEBSOCKET_URL} from "./consts";

export function initNotifications() {
    const room = prompt("room");
    const ws = new WebSocket(`${WEBSOCKET_URL}/server/${room}/`);
    ws.onclose = console.log;
    ws.onerror = console.log;
    ws.onmessage = console.log;

    function send(data) {
        ws.send(JSON.stringify(data));
    }

    ws.onopen = () => {
        // send({"room": prompt("room")})
        console.log('open');
        setTimeout(() => {
            send({'message': prompt()});
        }, 1000);
    };
}