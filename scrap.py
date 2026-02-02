import requests
from bs4 import BeautifulSoup
import time

# 1.Define the URL to scrape
url = "https://www.flipkart.com/search?q=electronics&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
# 2.Send a GET request to the URL
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
time.sleep(2)
response = requests.get(url, headers=headers, timeout=10)
# 3.Check if the request was successful
if response.status_code == 200:
    
    # 4.Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    # 5.Extract and print the title of the page
    title = soup.title.string
    print("Page Title:", title)
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
    exit()
# 6.Extract and print all hyperlinks on the page
links = soup.find_all('a')
print("Hyperlinks on the page:")
for link in links:
    href = link.get('href')
    if href:
        print(href)
# 7.Extract and print all paragraph texts on the page
paragraphs = soup.find_all('p')
print("Paragraphs on the page:")
for para in paragraphs:
    print(para.get_text())
# 8.Extract and print all image sources on the page
images = soup.find_all('img')
print("Image sources on the page:")
for img in images:
    src = img.get('src')
    if src:
        print(src)
# 9.Extract and print all headings (h1 to h6) on the page
for i in range(1, 7):
    headings = soup.find_all(f'h{i}')
    print(f"Headings h{i} on the page:")
    for heading in headings:
        print(heading.get_text())
# 10.Extract and print all list items on the page
list_items = soup.find_all('li')
print("List items on the page:")
for item in list_items:
    print(item.get_text())
print("List items on the page:")
#11. Extract and print all div elements with a specific class (example: 'example-class')
divs = soup.find_all('div', class_='example-class')
print("Div elements with class 'example-class':")
for div in divs:
    print(div.get_text())
    
#12. Extract and print all span elements with a specific id (example: 'example-id')
spans = soup.find_all('span', id='example-id')
print("Span elements with id 'example-id':")
for span in spans:
    print(span.get_text())
#13. Extract and print all form elements on the page
forms = soup.find_all('form')
print("Form elements on the page:")
for form in forms:
    print(form.get_text())
#14. Extract and print all script elements on the page
scripts = soup.find_all('script')
print("Script elements on the page:")
for script in scripts:
    print(script.get_text())
#15. Extract and print all meta tags on the page
metas = soup.find_all('meta')
print("Meta tags on the page:")
for meta in metas:
    print(meta.get_text())
    # print(meta.get_text())
    print(meta.get('content'))
    # print(meta.get('content'))
    # End of script
#16. Extract and print all stylesheets linked in the page
stylesheets = soup.find_all('link', rel='stylesheet')
print("Stylesheets linked in the page:")
for sheet in stylesheets:
    href = sheet.get('href')
    if href:
        print(href)
#17. Output the total number of each element found
print(f"Total hyperlinks: {len(links)}")
print(f"Total paragraphs: {len(paragraphs)}")
print(f"Total images: {len(images)}")
print(f"Total list items: {len(list_items)}")
print(f"Total divs with class 'example-class': {len(divs)}")
print(f"Total spans with id 'example-id': {len(spans)}")
print(f"Total forms: {len(forms)}")
print(f"Total scripts: {len(scripts)}")
print(f"Total meta tags: {len(metas)}")
print(f"Total stylesheets: {len(stylesheets)}")
print("Web scraping completed.")

# 18. Save the extracted data to a text file
with open('Stored.txt', 'w', encoding='utf-8') as file:
    file.write(f"Page Title: {title}\n\n")
    
    file.write("Hyperlinks on the page:\n")
    for link in links:
        href = link.get('href')
        if href:
            file.write(href + '\n')
    file.write("\nParagraphs on the page:\n")
    for para in paragraphs:
        file.write(para.get_text() + '\n')
    file.write("\nImage sources on the page:\n")
    for img in images:
        src = img.get('src')
        if src:
            file.write(src + '\n')
    for i in range(1, 7):
        headings = soup.find_all(f'h{i}')
        file.write(f"\nHeadings h{i} on the page:\n")
        for heading in headings:
            file.write(heading.get_text() + '\n')
    file.write("\nList items on the page:\n")
    for item in list_items:
        file.write(item.get_text() + '\n')
    file.write("\nDiv elements with class 'example-class':\n")
    for div in divs:
        file.write(div.get_text() + '\n')
    file.write("\nSpan elements with id 'example-id':\n")
    for span in spans:
        file.write(span.get_text() + '\n')
    file.write("\nForm elements on the page:\n")
    for form in forms:
        file.write(form.get_text() + '\n')
    file.write("\nScript elements on the page:\n")
    for script in scripts:
        file.write(script.get_text() + '\n')
    file.write("\nMeta tags on the page:\n")
    for meta in metas:
        file.write(str(meta) + '\n')
    file.write("\nStylesheets linked in the page:\n")
    for sheet in stylesheets:
        href = sheet.get('href')
        if href:
            file.write(href + '\n')
    print("Extracted data saved to 'stored.txt'.")
# End of script

    