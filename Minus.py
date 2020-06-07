# Minus is Jump plus automated downloader and archiver.
# (C) 2020 Mitsuhiro Hashimoto (@Adolfoi_) All rights reserved.
# LICENCE: MIT License

from selenium import webdriver
from PIL import ImageGrab
from pynput.keyboard import Key, Controller
from selenium.common.exceptions import NoSuchElementException
import time
import os
import sys
import PySimpleGUI as sg

driver = webdriver.Chrome('./chromedriver')

def ExtractComic(comic_url):
    global driver
    driver = webdriver.Chrome('./chromedriver')
    driver.get(comic_url)
    print('漫画名:' + driver.find_element_by_xpath('//*[@id="page-viewer"]/section[5]/div[1]/h1').text)
    comic_title = driver.find_element_by_xpath('//*[@id="page-viewer"]/section[5]/div[1]/h1').text
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight / 4);')
    driver.implicitly_wait(20)
    episode_element = driver.find_element_by_xpath('//*[@id="page-viewer"]/section[5]/div[2]/div[2]/div[3]/ul/li[5]')
    driver.implicitly_wait(20)
    episode_element.click()
    driver.implicitly_wait(20)
    maximum_window_element = driver.find_element_by_xpath('//*[@id="page-viewer"]/div[2]/ul[1]/li[3]/span')
    driver.implicitly_wait(20)
    maximum_window_element.click()
    time.sleep(6)  # 説明表示が消えるまで待機
    j = 0
    k = 0
    current_title = '[' + str(j + 1) + '話]' + comic_title
    local_path = './' + comic_title
    if not os.path.exists(local_path):
        os.mkdir(local_path)
    im = ImageGrab.grab()  # スクリーンショット撮影
    current_directory = os.getcwd()
    episode_path = current_directory + '/' + comic_title + '/' + current_title
    CaptureComic(im, episode_path, k)
    k = 1
    while True:
        keyboard = Controller()
        keyboard.press(Key.left)
        keyboard.release(Key.left)
        time.sleep(1)  # ディレイをつけて確実に撮影する
        if k == 0:
            time.sleep(1)  # ディレイをつけて確実に撮影する
        current_title = '[' + str(j + 1) + '話]' + comic_title
        im = ImageGrab.grab()  # スクリーンショット撮影
        current_directory = os.getcwd()
        episode_path = current_directory + '/' + comic_title + '/' + current_title
        CaptureComic(im,episode_path,k)
        time.sleep(1)  # ディレイをつけて確実に撮影する
        try:
            next_episode = driver.find_element_by_xpath('//*[@id="viewer-colophon"]/div/div/div/div/p/a').text
            if len(next_episode) > 0:
                print('next_episode:' + next_episode)
            else:
                print('次の話がありません')
            if next_episode == '次の話を読む':
                k = 0
                j += 1
            else:
                k += 1
        except NoSuchElementException:
            print('要素がありませんでした...')
            driver.quit()
            print('Minusを終了します')
            sys.exit()
        # im.show()
     # driver.quit()


def CaptureComic(image,local_path,page_number):
    if not os.path.exists(local_path):
        os.mkdir(local_path)
    image.save(local_path + "/" + str(page_number) + '.png')

def ShowWindow():
    sg.theme('DarkBlue')  # Add a touch of color
    # All the stuff inside your window.
    layout = [  # [sg.Text('Some text on Row 1')],
        [sg.Text('ジャンププラスの漫画のURL'), sg.InputText()],
        [sg.Button('スタート'), sg.Button('キャンセル')]]

    # Create the Window
    window = sg.Window('Minus', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'キャンセル':  # if user closes window or clicks cancel
            break
        if event == sg.WIN_CLOSED or event == 'スタート':  # if user closes window or clicks cancel
            print('You entered ', values[0])
            ExtractComic(values[0])
            break
    window.close()

if __name__ == "__main__":
    # ExtractComic('https://shonenjumpplus.com/episode/10834108156630995329') # 早乙女姉妹は漫画のためなら！？
    # ExtractComic('https://shonenjumpplus.com/episode/10834108156649530410') # 姫様“拷問”の時間です
    # ExtractComic('https://shonenjumpplus.com/episode/10833497643049550135') # ファイアパンチ
    # ExtractComic('https://shonenjumpplus.com/episode/13932016480029111789') # 左ききのエレン
    # ExtractComic('https://shonenjumpplus.com/episode/13932016480028724625') # ヒカルの碁
    # ExtractComic('https://shonenjumpplus.com/episode/13933686331659371586') # 阿波連さんははかれない
    # ExtractComic('https://shonenjumpplus.com/episode/10834108156665560686') # さっちゃん、僕は。
    # ExtractComic('https://shonenjumpplus.com/episode/13932016480028804143') # ROUTE END
    # ExtractComic('https://shonenjumpplus.com/episode/13933686331657344247') # ミタマセキュ霊ティ
    ShowWindow()



