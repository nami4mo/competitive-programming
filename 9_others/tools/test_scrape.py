import requests
from bs4 import BeautifulSoup
import sys
from selenium.webdriver import Chrome, ChromeOptions
import re
import os

options = ChromeOptions()
options.add_argument('--headless')
driver = Chrome(options=options)

filename = sys.argv[0]

contest_name = sys.argv[1]
problem = sys.argv[2]

base_url = 'https://atcoder.jp/contests/{contest_name}/tasks/{contest_name}_{problem}'
target_url = base_url.format(contest_name=contest_name, problem=problem)

driver.get(target_url)
html = driver.page_source.encode('utf-8')
soup = BeautifulSoup(html, "lxml").find(class_='lang-ja')
input_contents = []
output_contents = []

for i in range(10):
    pre_sample_input = soup.find(id=f'pre-sample{i*2}')
    pre_sample_output = soup.find(id=f'pre-sample{i*2+1}')
    if pre_sample_input is None or pre_sample_output is None:
        break
    input_contents.append(pre_sample_input.text)
    output_contents.append(pre_sample_output.text)


if input_contents and output_contents:
    os.makedirs(f'./test_case/{contest_name}/{problem}')
    for i, content in enumerate(input_contents):
        with open(f'./test_case/{contest_name}/{problem}/input_{i+1}.txt', 'w') as f:
            f.write(content)
    for i, content in enumerate(output_contents):
        with open(f'./test_case/{contest_name}/{problem}/output_{i+1}.txt', 'w') as f:
            f.write(content)

with open(f'./test_case/{contest_name}/{problem}/test_cnt.txt', 'w') as f:
    f.write(str(len(input_contents)))