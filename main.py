import requests
from bs4 import BeautifulSoup



def parse_site(page):
    try:
        page = requests.get("https://kasipkor.kz/prod/top100/student.php?id={}".format(page))

        soup = BeautifulSoup(page.content, "html.parser")

        results = soup.find(id="post-3")
        job_elements = results.find_all("div", class_="post-content")

        for job_element in job_elements:
            title_element = job_element.find("strong")
            return title_element.text.strip()
    except AttributeError:
        return
    except TypeError:
        return

def page_ittiration(n):
    list = []
    f=1
    for i in range(n):
        p = parse_site(f)
        if p != None:
            list.append(int(p))
        f=f+1
    list.sort()
    list.reverse()
    people = ""
    for i, item in enumerate(list):
        people += str(i+1)+':'+str(item)+"\n"
    return( people )

if __name__ == "__main__":
    pass
