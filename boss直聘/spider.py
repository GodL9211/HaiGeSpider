#! -*-conding: UTF-8 -*-
# @公众号: 海哥python
import math
import re
import time

from DrissionPage import ChromiumPage
from loguru import logger

from sqlite3_boss import SQLAlchemyDB, Job


driver = ChromiumPage()

shenzhen = "101280600"


def get_list(post_name: str, city: str, page: int):
    # 监听网站数据包，必须在请求之前先执行
    driver.listen.start("/wapi/zpgeek/search/joblist.json")
    driver.get(f"https://www.zhipin.com/web/geek/job?query={post_name}&city={city}&page={page}&pageSize=30")
    logger.debug(f"catching page {page} ...")
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


def pipeline(job_info: dict):
    for job in job_info['zpData']['jobList']:
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
            "areaDistrict": job['areaDistrict'],
            "brandIndustry": job['brandIndustry'],
            "link": f"https://www.zhipin.com/job_detail/{job["encryptJobId"]}.html",
            "desc": clean_html(details)
        }
        db.add(Job(**job_data))
        time.sleep(0.5)


if __name__ == '__main__':
    job_info = get_list("python", shenzhen, 1)
    logger.debug(job_info)

    db = SQLAlchemyDB('sqlite:///boss_job3.db', echo=True)
    # 创建表
    db.create_all()

    totalCount = job_info['zpData']['totalCount']
    pages = math.ceil(totalCount / 30)

    logger.debug(f"shenzhen 共有 {totalCount}个 python 岗位！")

    pipeline(job_info=job_info)

    if pages > 1:
        for page in range(2, pages + 1):
            time.sleep(1.5)
            _job_info = get_list("python", shenzhen, page)
            pipeline(_job_info)
