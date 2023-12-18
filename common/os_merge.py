import os


def merge_line(line_name:str,only_one:str=None):
    # 获取所有的路径
    path_lists = {
        '测试环境':[
            'D://工作相关//工作//合代码//产品测试//iot-data-access',
            'D://工作相关//工作//合代码//产品测试//iot-data-persistence',
            'D://工作相关//工作//合代码//产品测试//iot-data-puller',
            'D://工作相关//工作//合代码//产品测试//werun-alarm',
            'D://工作相关//工作//合代码//产品测试//werun-contingency-plan',
            'D://工作相关//工作//合代码//产品测试//werun-control-config',
            'D://工作相关//工作//合代码//产品测试//werun-energy-consumption',
            'D://工作相关//工作//合代码//产品测试//werun-inspect-offline',
            'D://工作相关//工作//合代码//产品测试//werun-inspect-online',
            'D://工作相关//工作//合代码//产品测试//werun-job-schedule',
            'D://工作相关//工作//合代码//产品测试//werun-knowledge',
            'D://工作相关//工作//合代码//产品测试//werun-maintenance',
            'D://工作相关//工作//合代码//产品测试//werun-material',
            'D://工作相关//工作//合代码//产品测试//werun-notice',
            'D://工作相关//工作//合代码//产品测试//werun-parking',
            'D://工作相关//工作//合代码//产品测试//werun-patrol-video',
            'D://工作相关//工作//合代码//产品测试//werun-rule-monitor',
            'D://工作相关//工作//合代码//产品测试//werun-workorder',
            'D://工作相关//工作//合代码//产品测试//wz_customer_files',
            'D://工作相关//工作//合代码//产品测试//wz-assets',
            'D://工作相关//工作//合代码//产品测试//wz-auth',
            'D://工作相关//工作//合代码//产品测试//wz-eureka',
            'D://工作相关//工作//合代码//产品测试//wz-file',
            'D://工作相关//工作//合代码//产品测试//wz-gateway',
            'D://工作相关//工作//合代码//产品测试//wz-information-publish',
            'D://工作相关//工作//合代码//产品测试//wz-log',
            'D://工作相关//工作//合代码//产品测试//wz-passage',
            'D://工作相关//工作//合代码//产品测试//wz-user',
            'D://工作相关//工作//合代码//产品测试//xxl_job',
            'D://工作相关//工作//合代码//产品测试//wz-video-stream',
            'D://工作相关//工作//合代码//产品测试//iot-test-support',
         ],
        '海外园区': [
            'D://工作相关//工作//合代码//项目//海外园区//iot-data-access',
            'D://工作相关//工作//合代码//项目//海外园区//iot-data-persistence',
            'D://工作相关//工作//合代码//项目//海外园区//iot-data-puller',
            'D://工作相关//工作//合代码//项目//海外园区//werun-alarm',
            'D://工作相关//工作//合代码//项目//海外园区//werun-contingency-plan',
            'D://工作相关//工作//合代码//项目//海外园区//werun-control-config',
            'D://工作相关//工作//合代码//项目//海外园区//werun-energy-consumption',
            'D://工作相关//工作//合代码//项目//海外园区//werun-inspect-offline',
            'D://工作相关//工作//合代码//项目//海外园区//werun-inspect-online',
            'D://工作相关//工作//合代码//项目//海外园区//werun-job-schedule',
            'D://工作相关//工作//合代码//项目//海外园区//werun-knowledge',
            'D://工作相关//工作//合代码//项目//海外园区//werun-maintenance',
            'D://工作相关//工作//合代码//项目//海外园区//werun-material',
            'D://工作相关//工作//合代码//项目//海外园区//werun-notice',
            'D://工作相关//工作//合代码//项目//海外园区//werun-parking',
            'D://工作相关//工作//合代码//项目//海外园区//werun-patrol-video',
            'D://工作相关//工作//合代码//项目//海外园区//werun-rule-monitor',
            'D://工作相关//工作//合代码//项目//海外园区//werun-workorder',
            'D://工作相关//工作//合代码//项目//海外园区//wz_customer_files',
            'D://工作相关//工作//合代码//项目//海外园区//wz-assets',
            'D://工作相关//工作//合代码//项目//海外园区//wz-auth',
            'D://工作相关//工作//合代码//项目//海外园区//wz-eureka',
            'D://工作相关//工作//合代码//项目//海外园区//wz-file',
            'D://工作相关//工作//合代码//项目//海外园区//wz-gateway',
            'D://工作相关//工作//合代码//项目//海外园区//wz-information-publish',
            'D://工作相关//工作//合代码//项目//海外园区//wz-log',
            'D://工作相关//工作//合代码//项目//海外园区//wz-passage',
            'D://工作相关//工作//合代码//项目//海外园区//wz-user',
            'D://工作相关//工作//合代码//项目//海外园区//xxl_job',
            'D://工作相关//工作//合代码//项目//海外园区//wz-video-stream',
            'D://工作相关//工作//合代码//项目//海外园区//iot-test-support',
        ],

    }
    current_number = 1
    path_list = path_lists.get(line_name)
    os_code = ''
    if line_name=='测试环境':
        os_code = ' && git.exe pull --progress -v --no-rebase "origin" && git.exe push --progress "origin" p-dev:p-uat'
    elif line_name == '海外园区':
        os_code = ' && git.exe pull --progress -v --no-rebase "origin" && git.exe push --progress "origin" overseas-1.3.1-dev:overseas-1.3.1-uat'
    for item in path_list:
        if only_one is None:
            os.system(f'd: && cd {item}{os_code}')
            print(item + ' ' + str(current_number))
            current_number = current_number + 1
        elif only_one in item:
            os.system(f'd: && cd {item}{os_code}')
            print(item + ' ' + str(current_number))
            current_number = current_number + 1
    pass


if __name__ == "__main__":
    merge_line('测试环境')
    # merge_line('海外园区')
    pass