#!/bin/bash

## 切换到目标目录
#cd /var/lib/jenkins/workspace/flask/report/templates
#
## 获取当前日期的字符串表示，格式为YYYYMMDD
#current_date=$(date +"%Y%m%d")
#
## 删除非当前日期相关的文件
#for file in *; do
#    # 提取文件名中的日期部分
#    file_date=$(echo $file | grep -oE '[0-9]{8}')
#    if [ ! -z "$file_date" ] && [[ "$file" != *"$current_date"* ]]; then
#        rm -f $file
#        echo "Deleted file: $file"
#    fi
#done

# 优化后提升执行效率
# 获取当前日期的字符串表示，格式为YYYYMMDD
current_date=$(date +"%Y%m%d")

# 使用find命令定位并删除文件
find . -type f -name "[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]*" \
! -name "*$current_date*" -print0 | xargs -0 -P $(nproc) rm -f

echo "Deleted files."