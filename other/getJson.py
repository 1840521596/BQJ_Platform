# coding: utf-8
# 获取请求结果
# kind 搜索关键字
# page 页码 默认是1
import math
import time
import pandas as pd
import requests


def get_json(kind, page=1, ):
    # post请求参数
    param = {
        'first': 'true',
        'pn': page,
        'kd': kind
    }
    header = {
        'Host': 'www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    # 设置代理
    # proxies = [
    #     {'http': '140.143.96.216:80', 'https': '140.143.96.216:80'},
    #     {'http': '119.27.177.169:80', 'https': '119.27.177.169:80'},
    #     {'http': '221.7.255.168:8080', 'https': '221.7.255.168:8080'}
    # ]
    # 请求的url
    url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'
    # 使用代理访问
    # response = requests.post(url, headers=header, data=param, proxies=random.choices(proxies))
    response = requests.post(url, headers=header, data=param)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        response = response.json()
        print(response)
        # 请求响应中的positionResult 包括查询总数 以及该页的招聘信息(公司名、地址、薪资、福利待遇等...)
        return response['content']['positionResult']
    return None


if __name__ == '__main__':
    # 默认先查询第一页的数据
    kind = 'python自动化测试工程师'
    # 请求一次 获取总条数
    position_result = get_json(kind=kind)
    # 总条数
    total = position_result['totalCount']
    print('{}开发职位，招聘信息总共{}条.....'.format(kind, total))
    # 每页15条 向上取整 算出总页数
    page_total = math.ceil(total / 15)

    # 所有查询结果
    search_job_result = []
    # for i in range(1, total + 1):
    # 为了节约效率 只爬去前100页的数据
    for i in range(1, 10):
        position_result = get_json(kind=kind, page=i)
        # 每次抓取完成后,暂停一会,防止被服务器拉黑
        time.sleep(15)
        # 当前页的招聘信息
        page_python_job = []
        for j in position_result['result']:
            python_job = []
            # 公司全名
            python_job.append(j['companyFullName'])
            # 公司简称
            python_job.append(j['companyShortName'])
            # 公司规模
            python_job.append(j['companySize'])
            # 融资
            python_job.append(j['financeStage'])
            # 所属区域
            python_job.append(j['district'])
            # 职称
            python_job.append(j['positionName'])
            # 要求工作年限
            python_job.append(j['workYear'])
            # 招聘学历
            python_job.append(j['education'])
            # 薪资范围
            python_job.append(j['salary'])
            # 福利待遇
            python_job.append(j['positionAdvantage'])

            page_python_job.append(python_job)
        print(page_python_job)
        # 放入所有的列表中
        search_job_result += page_python_job
        print('第{}页数据爬取完毕, 目前职位总数:{}'.format(i, len(search_job_result)))
        # 每次抓取完成后,暂停一会,防止被服务器拉黑
        time.sleep(15)
    # 将总数据转化为data frame再输出
    df = pd.DataFrame(data=search_job_result,
                      columns=['公司全名', '公司简称', '公司规模', '融资阶段', '区域', '职位名称', '工作经验', '学历要求', '工资', '职位福利'])
    df.to_csv('lagou.csv', index=False, encoding='utf-8_sig')
