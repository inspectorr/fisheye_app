const { merge } = require('webpack-merge');
const TerserPlugin = require('terser-webpack-plugin');
const { commonConfig } = require('./common');

module.exports = merge(commonConfig('production'), {
    watch: false,
    mode: 'production',
    optimization: {
        minimizer: [
            new TerserPlugin(),
        ],
    },
    output: {
        publicPath: '/static/dist/',
    },
});
