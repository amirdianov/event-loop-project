import {fileURLToPath, URL} from 'node:url'

import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [vue()],
    resolve: {
        alias: {
            '@': fileURLToPath(new URL('./src', import.meta.url))
        }
    },
    css: {
        preprocessorOptions: {
            less: {
                math: "always",
                relativeUrls: true,
                javascriptEnabled: true,
            },
        },}
    // },
    // build: {
    //     rollupOptions: {
    //         external: {
    //             css: {
    //                 loaderOptions: {
    //                     less: {
    //                         lessOptions: {
    //                             modifyVars: {
    //                                 'primary-color': '#1DA57A',
    //                                 'link-color': '#1DA57A',
    //                                 'border-radius-base': '2px',
    //                             },
    //                             javascriptEnabled: true,
    //                         },
    //                     },
    //                 },
    //             },
    //         }
    //
    //     }
    // }
                // css: {
                //     preprocessorOptions: {
                //         less: {
                //             math: "always",
                //             relativeUrls: true,
                //             javascriptEnabled: true,
                //         },
                //     },
                // },
    // css: {
    //     loaderOptions: {
    //         less: {
    //             lessOptions: {
    //                 modifyVars: {
    //                     'primary-color': '#1DA57A',
    //                     'link-color': '#1DA57A',
    //                     'border-radius-base': '2px',
    //                 },
    //                 javascriptEnabled: true,
    //             },
    //         },
    //     },
    // },
})
