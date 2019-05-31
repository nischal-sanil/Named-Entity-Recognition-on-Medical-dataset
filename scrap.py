# import libraries
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

# specify the url
main_page = "https://medhelp.org/forums/Leukemia-and-Lymphoma-/show/139?page="
post_page = "https://medhelp.org"

listofdic = []
headers = ['User_ID',"User_Name","Link","Problem_title","Posted_Question"]
driver = webdriver.Chrome(executable_path='G:/Machine Learning/sahicareer/chromedriver_win32/chromedriver.exe')
try:
	for i in range(1,138):
		
		
		print("Fetching link "+main_page+str(i))

		driver.get(main_page+str(i))

		soup = BeautifulSoup(driver.page_source, 'lxml')
		author = soup.find_all('div',attrs={'class':'subj_entry'})

		for info in author:
			dic = {}
			author_info = info.find('div',attrs={'class':'subj_info'})
			link = author_info.h2.a['href']
			dic["Link"] = link
			dic["Problem_title"] = author_info.h2.a.text
			dic["User_ID"] = author_info.find('div',attrs={'class':'username'}).a['id']
			dic["User_Name"] = author_info.find('div',attrs={'class':'username'}).a.text

			driver.get(post_page+link)
			soup_content = BeautifulSoup(driver.page_source, 'lxml')
			

			dic["Posted_Question"] = soup_content.find('div',attrs={'id':'subject_msg'}).text

			listofdic.append(dic)
except:
	print("Stopped, At page "+str(i))

finally:
	driver.quit()
	print(len(listofdic))

	# Output to CSV
	data = pd.DataFrame(listofdic,columns=headers)
	data.set_index('User_ID')
	data.to_csv('output.csv',index =False)