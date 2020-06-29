from selenium import webdriver
import requests
import time
import sys
import os

class covid19tracker:
    def __init__(self,statename,cityname):
        self.statename=statename
        self.cityname=cityname

    def load_all(self):
        driver = self.load_driver()
        os.system('cls')
        driver.get("https://www.covid19india.org/")
        os.system('cls')
        time.sleep(5)
        os.system('cls')
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        os.system('cls')
        self.totalindiawise(driver)
        self.todayindiawise(driver)
        temp=self.statewise(driver,self.statename)
        if temp!=0:
            self.citywise(driver,self.cityname,temp)
        driver.close()
        while True:
            print("\n---------------------------------")
            ask=input("Do you want to Search Again Y/N :- ")
            if ((ask.upper()!='Y') and (ask.upper()!='N')):
                print("--OOPS! Wrong input Please try again--")
                continue
            return ask

    def load_driver(self):
        path = os.getcwd()
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument('--headless')
        chromeOptions.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(executable_path=path+"\\chromedriver.exe",options=chromeOptions)
        return driver

    def totalindiawise(self,driver):
        total_cases_india=driver.find_element_by_xpath("/html/body/div/div/div[3]/div[1]/div[2]/div[1]/h1").text
        total_activecases_india=driver.find_element_by_xpath("/html/body/div/div/div[3]/div[1]/div[2]/div[2]/h1").text
        total_recoveredcases_india=driver.find_element_by_xpath("/html/body/div/div/div[3]/div[1]/div[2]/div[3]/h1").text
        total_deceased_india=driver.find_element_by_xpath("/html/body/div/div/div[3]/div[1]/div[2]/div[4]/h1").text
        os.system('cls')
        print("---CASES IN INDIA TILL NOW---")
        print("Total Cases:- ",end='')
        print(total_cases_india)
        print("Active Cases:- ",end='')
        print(total_activecases_india)
        print("Recovered:- ",end='')
        print(total_recoveredcases_india)
        print("Deceased:- ",end='')
        print(total_deceased_india)
        print()

    def todayindiawise(self,driver):
        today_cases_india=driver.find_element_by_xpath("/html/body/div/div/div[3]/div[1]/div[2]/div[1]/h4").text
        today_recoveredcases_india=driver.find_element_by_xpath("/html/body/div/div/div[3]/div[1]/div[2]/div[3]/h4").text
        today_deceased_india=driver.find_element_by_xpath("/html/body/div/div/div[3]/div[1]/div[2]/div[4]/h4").text
        print("---TODAY CASES IN INDIA---")
        print("Total Cases:- ",end='')
        print(today_cases_india)
        print("Recovered:- ",end='')
        print(today_recoveredcases_india)
        print("Deceased:- ",end='')
        print(today_deceased_india)
        print()

    def statewise(self,driver,statename):
        for i in range(2,39):
            x_path_state="/html/body/div/div/div[3]/div[1]/div[5]/div["+str(i)+"]/div[1]/div"
            state=driver.find_element_by_xpath(x_path_state).text
            if statename.lower()==state.lower():
                print("---CASES IN "+state.upper()+" TILL NOW---")
                print("Total Cases:- ",end='')
                x_path_t="/html/body/div/div/div[3]/div[1]/div[5]/div["+str(i)+"]/div[2]/div[2]"
                print(driver.find_element_by_xpath(x_path_t).text)
                print("Active Cases:- ",end='')
                x_path_a="/html/body/div/div/div[3]/div[1]/div[5]/div["+str(i)+"]/div[3]/div"
                print(driver.find_element_by_xpath(x_path_a).text)
                print("Recovered:- ",end='')
                x_path_r="/html/body/div/div/div[3]/div[1]/div[5]/div["+str(i)+"]/div[4]/div[2]"
                print(driver.find_element_by_xpath(x_path_r).text)
                print("Deceased:- ",end='')
                x_path_d="/html/body/div/div/div[3]/div[1]/div[5]/div["+str(i)+"]/div[5]/div[2]"
                print(driver.find_element_by_xpath(x_path_d).text)
                print()
                driver.find_element_by_xpath("/html/body/div/div/div[3]/div[1]/div[5]/div["+str(i)+"]/div[1]").click()
                return i
        print("No State Found i.e "+statename)
        return 0

    def citywise(self,driver,cityname,temp):
        i=temp+3
        while True:
            x_path_state="/html/body/div/div/div[3]/div[1]/div[5]/div["+str(i)+"]/div[1]/div"
            try:
                city=driver.find_element_by_xpath(x_path_state).text
            except:
                print("No City Found i.e "+cityname)
                break
            if cityname.lower()==city.lower():
                print("---CASES IN "+city.upper()+" TILL NOW---")
                print("Total Cases:- ",end='')
                x_path_t="/html/body/div/div/div[3]/div[1]/div[5]/div["+str(i)+"]/div[2]/div[2]"
                print(driver.find_element_by_xpath(x_path_t).text)
                print("Active Cases:- ",end='')
                x_path_a="/html/body/div/div/div[3]/div[1]/div[5]/div["+str(i)+"]/div[3]/div"
                print(driver.find_element_by_xpath(x_path_a).text)
                print("Recovered:- ",end='')
                x_path_r="/html/body/div/div/div[3]/div[1]/div[5]/div["+str(i)+"]/div[4]/div[2]"
                print(driver.find_element_by_xpath(x_path_r).text)
                print("Deceased:- ",end='')
                x_path_d="/html/body/div/div/div[3]/div[1]/div[5]/div["+str(i)+"]/div[5]/div[2]"
                print(driver.find_element_by_xpath(x_path_d).text)
                break
            i+=1

if __name__ == "__main__":
    while True:
        print("\nWELCOME TO COVID-19 TRACKER ")
        statename = input("Enter your State:- ")
        cityname = input("Enter your City:- ")
        ask=covid19tracker(statename,cityname).load_all()
        if ask.upper()=='N':
            sys.exit()



