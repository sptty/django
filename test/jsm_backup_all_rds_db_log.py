# -*- encoding:utf-8 -*-
# __author__ = 'sptty'
# date = Fri Oct 12 17:26:06 CST 2018
#


import os,urllib,logging,sys,time,json
from aliyunsdkcore.client import AcsClient
from aliyunsdkrds.request.v20140815 import DescribeBinlogFilesRequest
from aliyunsdkrds.request.v20140815 import DescribeDBInstancesRequest


# 获取当前时间和前一天时间
#
def date_format(time_use_format_seconds):
    'format time_seconds to XXXX-MM-DDTHH:mmZ'
    time_struct = time.localtime(time_use_format_seconds)
    # print(time_struct)
    time_format = time.strftime("%Y-%m-%dT%H:%M:%SZ", time_struct)
    return time_format

today = int(time.time())
yestoday = today - 2*86400

today_format = date_format(today)
yestoday_format = date_format(yestoday)


# 创建 AcsClient 实例
#
with open('E:\\03.devops\\django\\test\\jsm_aliyun_id.txt','r') as jsm_aliyun_id:
    jsm_aliyun_id_info = jsm_aliyun_id.readline()
    # print(jsm_aliyun_id_info)

jsm_aliyun_id_info_json = json.loads(jsm_aliyun_id_info)
#
# print(type(jsm_aliyun_id_info_json))
ak = jsm_aliyun_id_info_json['ak']
secret = jsm_aliyun_id_info_json['secret']
region_id = jsm_aliyun_id_info_json['region_id']

client = AcsClient(
    ak,
    secret,
    region_id)


# 获取RDS实例的备份数
#
def jsm_get_rds_backup(client, rds_instance_id, rds_instance_name):
    ''
    request = DescribeBinlogFilesRequest.DescribeBinlogFilesRequest()
    request.set_DBInstanceId(rds_instance_id)
    # 获取昨天到今天凌晨的备份时间
    request.set_StartTime(yestoday_format)
    request.set_EndTime(today_format)

    response = client.do_action_with_exception(request)
    print(response)
    print(type(response))

    # 将返回的字符串数据转换为json，梳理格式
    response_json = json.loads(response)


    # 循环取出所有活的下载链接
    for j in range(0,response_json['TotalRecordCount']):
        # 输出所有下载链接
        print(response_json['Items']['BinLogFile'][j]['DownloadLink'])
        # print(type(response_json['Items']['BinLogFile']))


        logging.basicConfig(
            format='%(asctime)s %(levelname)s %(message)s',
            level=logging.INFO,
            stream=sys.stdout)


        file_path = 'C:\Users\wan\Downloads\\' + rds_instance_name + \
                    '-' + \
                    response_json['Items']['BinLogFile'][j]['LogEndTime'].split(':')[0] + \
                    '-' + \
                    response_json['Items']['BinLogFile'][j]['DownloadLink'].split('?')[0].split('/')[-1]


        if not os.path.isfile(file_path):
            logging.info("File doesn't exist.")
            # replace with url you need
            url = response_json['Items']['BinLogFile'][j]['DownloadLink']

            # if dir 'dir_name/' doesn't exist
            # file_dir = file_path[:-9]
            # if not os.path.exists(file_dir):
            #     logging.info("Mkdir 'dir_name/'.")
            #     os.mkdir(file_dir)

            def down(_save_path, _url):
                try:
                    urllib.urlretrieve(_url, _save_path)
                except:
                    print('\nError when retrieving the URL:', _save_path)

            logging.info("Downloading file.")
            down(file_path, url)
        else:
            logging.info("File exists.")





# 获取RDS所有的实例列表
#
request_rds_list = DescribeDBInstancesRequest.DescribeDBInstancesRequest()
response_rds_list = client.do_action_with_exception(request_rds_list)

response_rds_list_json = json.loads(response_rds_list)


# 获取所有RDS节点备份并调用备份函数备份
#
for i in range(0,response_rds_list_json['TotalRecordCount']):
    # print(i)
    print(response_rds_list_json['Items']['DBInstance'][i]["DBInstanceId"])
    rds_instance_id = response_rds_list_json['Items']['DBInstance'][i]["DBInstanceId"]
    rds_instance_name = response_rds_list_json['Items']['DBInstance'][i]["DBInstanceDescription"]
    # 调用函数进行备份每一个实例的备份文件
    jsm_get_rds_backup(client=client,rds_instance_id=rds_instance_id,rds_instance_name=rds_instance_name)



