from bs4 import BeautifulSoup as Soup 
from functions import fetch

class Parser:
    def __init__(self):
        pass

    async def getInfo(self,fourAnimeLink,episodeNum):
        page_html = await fetch(fourAnimeLink)
        page_soup = Soup(page_html,"html.parser")
        result = {}
        image = page_soup.find("div",{"class":"cover"}).img["src"]
        title = page_soup.find("p",{"class":"single-anime-desktop"}).text.strip()
        genres_cont = page_soup.find("div",{"class":["ui","tag","horizontal","list"]}).find_all("a")
        del genres_cont[0] # Contains the anime name which is not needed
        genres = ""
        for i in range(len(genres_cont)):
            if i == len(genres_cont)-1:
                genres += f"{genres_cont[i].text.strip()}"
            else:
                genres += f"{genres_cont[i].text.strip()},"
        
        episodes_cont = page_soup.find("ul",{"class":["episodes","range","active"]}).find_all("li")
        episode_link = episodes_cont[episodeNum-1].a["href"]

        episode_direct = await self.getEpisode(episode_link)

        result["image"] = image
        result["genres"] = genres
        result["episode"] = episode_direct
        result["title"] = title

        return result

    async def getEpisode(self,episode_link):
        page_html = await fetch(episode_link)
        page_soup = Soup(page_html,"html.parser")
        return page_soup.find("video",{"id":"video1"}).source["src"]
