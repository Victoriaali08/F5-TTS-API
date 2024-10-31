#!/bin/bash

# 创建目标目录
mkdir -p .cache/.music

# 下载音色文件
wget -O .cache/.music/results.zip https://github.com/Samge0/ttsmaker-download/releases/download/v0.0.1/results.zip

# 解压output文件夹下的所有mp3文件，不保留output文件夹
unzip -o -j .cache/.music/results.zip "output/*.mp3" -d .cache/.music

# 移除压缩文件
rm -rf .cache/.music/results.zip
