const BundleTracker = require('webpack-bundle-tracker');
const path = require('path');

const excludes = [
    /node_modules/,
];

const babelLoader = {
    loader: 'babel-loader',
    options: {
        presets: [
            '@babel/preset-react',
        ],
    },
};

const commonConfig = (mode) => {
    const dev = mode === 'development';

    return {
        entry: {
            spa: path.resolve(__dirname, '../src/index.js'),
        },
        module: {
            rules: [
                {
                    test: /\.(js)x?$/,
                    exclude: excludes,
                    use: [babelLoader],
                },
                {
                    test: /\.module\.scss$/,
                    use: [
                        'style-loader',
                        {
                            loader: 'css-loader',
                            options: {
                                modules: {
                                    localIdentName: dev ? '[path][name]__[local]' : '[hash:base64]',
                                    exportLocalsConvention: 'camelCaseOnly',
                                },
                                sourceMap: dev,
                                import: true,
                            },
                        },
                        {
                            loader: 'sass-loader',
                            options: {
                                sourceMap: dev,
                            },
                        },
                    ],
                },
            ],
        },
        resolve: {
            extensions: ['.jsx', '.js'],
            alias: {
                '@': path.resolve(__dirname, '../src'),
            },
            modules: [
                path.resolve(__dirname, '../'),
                'node_modules',
            ],
        },
        output: {
            path: path.resolve(__dirname, '../../static/dist'),
            sourceMapFilename: '[name].js.map',
            filename: '[name].[fullhash].entry.js',
        },
        plugins: [
            new BundleTracker({
                filename: 'webpack-stats.json',
                path: __dirname,
            }),
        ],
    };
};

module.exports = { commonConfig };
