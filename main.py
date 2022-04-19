from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep as wait


BASE_URL = 'https://www.giiresearch.com/material_report.shtml'

with open('log.txt', 'w') as log:
	log.write('')
def scrap_data(driver, url):
	driver.get(url)
	driver.find_element_by_xpath('//*[@id="Content_Body"]/form[1]/table[1]/tbody/tr/td[3]/select').click()
	driver.find_element_by_xpath('//*[@id="Content_Body"]/form[1]/table[1]/tbody/tr/td[3]/select/option[3]').click()
	# page_selector_xpath = '//*[@id="Content_Body"]/form[1]/div[2]/button[1]'
	for i in range(2, 11):
		containers = driver.find_elements_by_css_selector('#Content_Body > form:nth-child(1) > table.plist_item')
		for container in containers:
			try:
				name = container.find_element_by_css_selector('.plist_title').text
				published_by = container.find_element_by_css_selector('.plist_pubinfo .plist_info_dd2').text
				publish_code = container.find_element_by_css_selector('.plist_codeinfo .plist_info_dd2').text
				publish_date = container.find_element_by_css_selector('.plist_dateinfo .plist_info_dd2').text
				page_info = container.find_element_by_css_selector('.plist_pageinfo .plist_info_dd2').text
				price = container.find_element_by_css_selector('.plist_priceinfo .plist_info_dd').text
				wait(1)
				with open('database.csv', 'a', encoding= 'utf-8') as file:
					file.write(f'"{name}" ! "{published_by}" ! "{publish_code}" ! "{publish_date}" ! "{page_info}" ! "{price}"'.replace(',', '').replace('!', ','))
					file.write('\n')
				print(f'{name} done!')
			except:
				with open('log.txt', 'a') as log:
					log.write(f'{container} failed \n')
				print('container failed')

		driver.find_element_by_xpath(f'//*[@id="Content_Body"]/form[1]/div[2]/button[{i}]').click()



if __name__ == '__main__':
	with open('database.csv', 'w') as file:
		file.write('\n')
	options = Options()
	options.add_argument('--disable-gpu')
	driver = webdriver.Chrome('chromedriver', options=options)
	scrap_data(driver, BASE_URL)