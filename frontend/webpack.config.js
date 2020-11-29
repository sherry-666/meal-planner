const webpack = require('webpack');
const config = {
    entry:  __dirname + '/scripts/index.js',
    output: {
        path: __dirname + '/static/dist',
        filename: 'bundle.js',
    },
    watch: true,
    resolve: {
        extensions: ['.js', '.jsx', '.css']
    },

    module: {
        rules: [
            {
            test: /\.(js|jsx)?/,
                exclude: /node_modules/,
                use: 'babel-loader'
            }
        ]
    },
};
module.exports = config;
