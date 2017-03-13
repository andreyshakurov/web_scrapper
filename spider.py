#! /usr/bin/env python
# -*- coding: utf-8 -*-

import mechanize
from bs4 import BeautifulSoup
import cookielib
import urlparse
import csv


def parse(url):

    cj = cookielib.CookieJar()
    br = mechanize.Browser()
    br.set_cookiejar(cj)
    br.open(url)

    br.select_form(nr=0)
    br.form['username'] = 'Bob'
    br.form['pass'] = 'Bob'
    br.submit()

    url = br.geturl()
    urls = [url]
    visited = [url]

    while len(urls) > 0:
        br.open(urls[0])
        html = br.response().read()
        soup = BeautifulSoup(html, 'html.parser')
        urls.pop(0)
        print len(urls)
        for link in soup.find_all('a'):

            if link.get('class') != ["adm"]:
                link['href'] = urlparse.urljoin("http://0.0.0.0:5000/", link['href'])

                if link['href'] not in visited:
                    urls.append(str(link['href']))
                    visited.append(str(link['href']))

    profile_data = []

    for page in visited:
        br.open(page)
        html = br.response().read()
        soup = BeautifulSoup(html, 'html.parser')

        try:
            username = str(soup.find_all('h1')[0].text)
        except:
            print "Couldn't find username on page ",  page
        try:
            for in_div in soup.find_all('div', class_='friends'):
                friends_list = in_div.find_all('li')
        except:
            print "Couldn't find friends on page ", page

        try:
            for in_div in soup.find_all('div', class_='profile_info'):
                last_seen = str(in_div.find_all('p')[2])
        except:
            print "Couldn't find date on page ", page

        try:
            paragraph = str(soup.find('p',  class_='page_views_counter').get_text())
            profile_data.append({
                'Username': username,
                'Friends': len(friends_list),
                'Last seen(UTC)': last_seen[50:71],
                'Page_views': int(paragraph[21::])
            })
        except:
            print "Couldn't find page views on page ", page

    return profile_data


def save(profile_data, path):
    with open(path, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(('Имя пользователя', 'Последнее подключение', 'Количество посещений страницы', 'Количество друзей'))

        for profile in profile_data:
            writer.writerow((profile['Username'], profile['Last seen(UTC)'], profile['Page_views'], profile['Friends']))


def main():
    save(parse("http://0.0.0.0:5000"), 'Profile_data.csv')


if __name__ == '__main__':
    main()