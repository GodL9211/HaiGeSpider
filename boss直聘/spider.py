#! -*-conding: UTF-8 -*-
# @公众号: 海哥python
import math
import re
import time

from DrissionPage import ChromiumOptions, SessionPage, ChromiumPage
from loguru import logger

from sqlite3_boss import SQLAlchemyDB, Job

driver = ChromiumPage()

shenzhen = "101280600"


def get_list(post_name: str, city: str, page: int):
    # 监听网站数据包，必须在请求之前先执行
    driver.listen.start("/wapi/zpgeek/search/joblist.json")
    driver.get(f"https://www.zhipin.com/web/geek/job?query={post_name}&city={city}&page={page}&pageSize=30")

    # 等待数据包内容加载
    resp = driver.listen.wait()

    # 获取数据包内容
    return resp.response.body


def clean_html(html_text: str):
    # 去除 <div> 标签
    cleaned_text = re.sub(r'<div[^>]*>', '', html_text)
    # 去除 </div> 标签
    cleaned_text = re.sub(r'</div>', '', cleaned_text)
    # 去除 <br> 标签
    cleaned_text = re.sub(r'<br>', '\n', cleaned_text)

    logger.debug(cleaned_text)
    return cleaned_text


def get_job_details(job_id: str):
    job_url = f"https://www.zhipin.com/job_detail/{job_id}.html"
    logger.debug(job_url)
    driver.get(job_url)
    detail = driver.eles(".job-sec-text")
    return detail[0].html


def pipline():
    global job, details, job_data
    for job in job_list['zpData']['jobList']:
        details = get_job_details(job["encryptJobId"])
        logger.debug(details)
        job_data = {
            "jobName": job['jobName'],
            "salaryDesc": job['salaryDesc'],
            "jobLabels": str(job['jobLabels']),
            "jobDegree": job['jobDegree'],
            "cityName": job['cityName'],
            "brandName": job['brandName'],
            "brandScaleName": job['brandScaleName'],
            "brandStageName": job['brandStageName'],
            "link": f"https://www.zhipin.com/job_detail/{job["encryptJobId"]}.html",
            "desc": clean_html(details)
        }
        db.add(Job(**job_data))


if __name__ == '__main__':
    job_list = get_list("python", shenzhen, 1)
    logger.debug(job_list)

    db = SQLAlchemyDB('sqlite:///boss_job.db', echo=True)

    resCount = job_list['zpData']['resCount']
    pages = math.ceil(resCount / 30)

    logger.debug(f"shenzhen 共有 {resCount}个 python 岗位！")

    pipline()

    if pages > 1:
        for page in range(9, pages + 1):
            time.sleep(1)
            job_list = get_list("python", shenzhen, page)
            pipline()
