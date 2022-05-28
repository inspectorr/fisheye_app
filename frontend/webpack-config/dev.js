const { merge } = require('webpack-merge');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const { commonConfig } = require('./common');

const DEV_HOST = '127.0.0.1';
const DEV_PORT = 4321;

// TODO work with server in dev mode

module.exports = merge(commonConfig('development'), {
    mode: 'development',
    plugins: [
        new HtmlWebpackPlugin({
            chunks: ['spa'],
        }),
    ],
    devServer: {
        host: DEV_HOST,
        port: DEV_PORT,
        headers: { 'Access-Control-Allow-Origin': '*' },
        hot: true,
        liveReload: true,
    },
});
