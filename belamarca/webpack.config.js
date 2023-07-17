var path = require("path");
var webpack = require("webpack");
var BundleTracker = require("webpack-bundle-tracker");
const { CleanWebpackPlugin } = require("clean-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
  context: __dirname,
  entry: "./assets/main.js",
  output: {
    path: path.resolve("./static/webpack_bundles/"),
    filename: "[name]-[fullhash].js",
    publicPath: '/static/webpack_bundles/',
  },
  watchOptions: {
    ignored: /node_modules/,
    poll: 1000,
  },
  module: {
    rules: [
      {
        test: /\.m?js$/,
        exclude: /(node_modules)/,
        use: {
          loader: "babel-loader",
          options: {
            presets: ["@babel/preset-env"],
          },
        },
      },
      {
        test: /\.(png|gif|jpg|mp4)$/,
        loader: "url-loader",
        options: {
          limit: 8000,
          name: "[name].[md5:fullhash:hex:12].[ext]",
        },
      },
      {
        test: /\.(ttf|eot|woff|woff2)$/,
        use: {
          loader: "file-loader",
          options: {
            name: '[name].[ext]',
            outputPath: 'fonts/'
          }
        },
      },
      {
        test: /\.(ogv|mp4|m4v|webm)$/,
        use: {
          loader: "file-loader",
        },
      },
      {
        test: /\.(scss|css)$/,
        use: [
          MiniCssExtractPlugin.loader,
          "css-loader",
          "postcss-loader",
          "sass-loader",
        ],
      },
    ],
  },
  plugins: [
    new BundleTracker({
      path: path.resolve('./'),
      filename: "webpack-stats.json",
    }),
    new MiniCssExtractPlugin({
      filename: "main-[fullhash].css",
    }),
    new CleanWebpackPlugin(),
    new webpack.ProvidePlugin({
      $: 'jquery',
      jQuery: 'jquery',
      'window.jQuery': 'jquery'
    }),
  ],
};
