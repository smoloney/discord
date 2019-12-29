from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
from io import BytesIO 
import time 
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')

fox = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
fox.fullscreen_window()
fox.get('https://challonge.com/gog63')

# element = fox.find_element_by_xpath('/html/body/div[5]/div[3]/div') # find part of the page you want image of
element = fox.find_element_by_xpath('/html/body/div[5]/div[4]/div[2]/div/div[1]') # find part of the page you want image of

location = element.location
print(location)
size = element.size
print(size)

left = location['x']
top = location['y']
right = location['x'] + size['width']
print(right)
bottom = location['y']  + size['height']
# fox.execute_script("window.scrollTo(0, document.body.scrollHeight);")
fox.execute_script("window.scrollTo(0, %d);" %((bottom-top)/3))
# time.sleep(5)
png = fox.get_screenshot_as_png() # saves screenshot of entire page
fox.quit()

im = Image.open(BytesIO(png)) # uses PIL library to open image in memory


im = im.crop((left, top , right, bottom)) # defines crop points
im.save('screenshot.png') # saves new cropped image