import {WEBSOCKET_URL} from "./consts";

export function initNotifications() {
    const room = prompt("room");
    const ws = new WebSocket(`${WEBSOCKET_URL}/server/${room}/`);
    ws.onclose = console.log;
    ws.onerror = console.log;
    ws.onmessage = (message) => {
        const data = JSON.parse(message.data);
        if (data.event_title) {
            alert(data.event_title)
        } else {
            console.log(message)
        }

    };

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