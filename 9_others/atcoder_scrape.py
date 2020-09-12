import requests
from bs4 import BeautifulSoup
import string 
import sys
from selenium.webdriver import Chrome, ChromeOptions
import re

options = ChromeOptions()
options.add_argument('--headless')
driver = Chrome(options=options)

alp = string.ascii_lowercase

contest_name = sys.argv[1]
base_url = 'https://atcoder.jp/contests/{contest_name}/tasks/{contest_name}_{problem}'

for problem in alp[:1]:
    target_url = base_url.format(contest_name=contest_name, problem=problem)
    driver.get(target_url)
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, "lxml")
    for i in range(10):
        pre_sample_input = soup.find(id=f'pre-sample{i*2}')
        pre_sample_output = soup.find(id=f'pre-sample{i*2+1}')
        if pre_sample_input is None or pre_sample_output is None:
            break

        with open(f'./{problem}_input_{i+1}.txt', 'w') as f:
            f.write(pre_sample_input.text)
        with open(f'./{problem}_output_{i+1}.txt', 'w') as f:
            f.write(pre_sample_output.text)