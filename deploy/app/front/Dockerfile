FROM node:16.15-alpine AS build-stage

WORKDIR /app

COPY frontend/event-loop/package.json .
COPY frontend/event-loop/package-lock.json .
RUN npm ci

COPY frontend/event-loop .

RUN npm run build

FROM nginx:1.21-alpine

COPY --from=build-stage /app/dist /usr/share/nginx/html
COPY deploy/nginx/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]