#!/bin/bash

inVideo="combos"

# Convert .mov to .mp4 using ffmpeg
ffmpeg -i "$inVideo.mov" -vcodec h264 -acodec aac "$inVideo.mp4"

# Remove the original .mov file
rm "$inVideo.mov"