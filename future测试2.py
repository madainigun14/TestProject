# https://blog.csdn.net/weixin_37901366/article/details/136489638
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/4 20:13
# @Author  : Maple
# @File    : 02-使用future实现并发下载(1).py
# @Software: PyCharm
 
from random import randint
from concurrent import futures
import time
 
"""使用concurrent.futures模块,该类的主要特色：
1. ThreadPoolExecutor和ProcessPoolExecutor类,这两个类实现的接口分别能在不同的线程或进程中执行可调用的对象。
这两个类在内部维护着一个工作线程或进程池，以及要执行的任务队列
"""
 
# 使用futures的map函数
 
 
MAX_WORKERS = 3
CC_LIST = [1, 2, 3, 4, 5, 6]
 
 
def get_randint():
    return randint(1, 10)
 
 
def download_one_img(id):
    print('***', id, '号图片开始下载***')
    download_time = get_randint()
    time.sleep(download_time)
    print('***{}号图片下载完成，花费时长{}s***'.format(id, download_time))
    return str(id) + '号图片内容'
 
 
def download_many_img(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))
    # excutor的__exit__方法会在调用executor.shutdown(wait=True)方法，它会在所有线程都执行完毕前阻塞线程
    with futures.ThreadPoolExecutor(workers) as excutor:
        # map方法返回一个生成器,因此可以通过迭代,获取每个函数的返回值
        # res是一个迭代器,通过遍历获取每一个函数的返回值
        # 调用map函数,任务立刻就开始执行,但是因为workers = 3,所以最开始只会有3个任务启动执行
        #  直到某一个任务执行完成,该线程才会退让给另外一个任务
        res = excutor.map(download_one_img, cc_list)
 
    return len(list(res))
 
 
def main(download_many_img):
    t0 = time.time()
    count = download_many_img(CC_LIST)
    elapsed = time.time() - t0
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elapsed))
 
 
if __name__ == '__main__':
    main(download_many_img)