import {WEBSOCKET_URL} from "./consts";

let ws;

function open(roomId) {
    ws = new WebSocket(`${WEBSOCKET_URL}/server/${roomId}/`);
}

export function initNotifications(roomId, onMessage) {
    // const room = prompt("room");
    // const ws = new WebSocket(`${WEBSOCKET_URL}/server/${roomId}/`);
    open(roomId);
    ws.onclose = () => {
        open(roomId);
    };
    ws.onerror = () => {
        open(roomId);
    };
    ws.onmessage = (message) => {
        const data = JSON.parse(message.data);
        // if (data.event_title) {
        //     alert(data.event_title)
        // } else {
        //     console.log(message)
        // }
        onMessage(data)

    };
    ws.onopen = () => {
        // send({"room": prompt("room")})
        console.log('open');
        // setTimeout(() => {
        //     send({'message': prompt()});
        // }, 1000);
    };

    function send(data) {
        ws.send(JSON.stringify(data));
    }

    return send


}