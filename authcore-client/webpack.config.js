'use strict';
var HtmlWebpackPlugin = require('html-webpack-plugin');


// Webpack config.
module.exports = {
    entry: './src/app.js',
    output: {
        filename: 'app.js',
        hash: true,
        path: __dirname.concat('/dist')
    },
    module: {
        loaders: [
            {
                test: /\.jsx?$/,
                exclude: /node_modules/,
                loader: 'babel',
                query: {
                    presets: ['react', 'es2015']
                }
            }
        ]
    },
    plugins: [new HtmlWebpackPlugin({
        hash: true,
        inject: 'body',
        template: 'index.html'
    })]
};
