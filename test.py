import json
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

###########################################################################################################################
main_driver = webdriver.Chrome('C:\chromedriver.exe')

boards = ['design','freebird','film','tech','art','leisure','citizen','local','sport','game','publish','traveling']
dic = {}
for board in boards:
    title_list=[]
    content_list=[]
    count=0
    for page in range(10,100):
        main_driver.get('https://www.flyingv.cc/categories/' +board+ '/all?status=success'+'&page='+str(page))
        time.sleep(2)
        error=0
        for x in range(12):
            try:
                tmp_title = main_driver.find_element_by_xpath('//*[@id="projects"]/div/div['+str(x+1)+']/div/div[3]/p[1]')
                #tmp_title = main_driver.find_element_by_xpath('//*[@id="projects"]/div/div['+str(x+1)+']/div/div[2]/p[1]')
                tmp_content = main_driver.find_element_by_xpath('//*[@id="projects"]/div/div['+str(x+1)+']/div/div[3]/p[3]')
                percenrage = #募款比例
                amount = #金額
                title_list.append(tmp_title.get_attribute('innerHTML'))
                content_list.append(tmp_content.get_attribute('innerHTML'))
                print(title_list[count])
                print(content_list[count])
                print('\n')
                count+=1
                temp_dic = {'title':tmp_title, 'contemt':tmp_content, 'percentage':percentage, 'amount':amount}
            except Exception as e:
                print(str(e))
                error+=1
        if error>10:
            break
    dic[board] = temp_dic
    # with open(board+'.txt', 'w', encoding = 'utf8') as result:
    #     result.write(board+'\n')
    #     for article in range(len(title_list)):
    #         result.write(title_list[article] + '\n' + content_list[article] +'\n')
with open("data.json", 'w', encoding = "utf8") as result:
    json.dump(dic, result)