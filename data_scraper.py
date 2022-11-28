from bs4 import BeautifulSoup
import urllib.request, sys, time
import requests
import pandas as pd
from datetime import date, timedelta
import csv



import os
import requests

cookies = {
    'MicrosoftApplicationsTelemetryDeviceId': '8cc42c62-6c50-1a3f-7fcc-21a83a207fc0',
    'MicrosoftApplicationsTelemetryFirstLaunchTime': '1669441054220',
    'wsjregion': 'na%2Cus',
    'gdprApplies': 'false',
    'ccpaApplies': 'true',
    'usr_bkt': 'rGgki1wrhs',
    '_pcid': '%7B%22browserId%22%3A%22laxi2e54j764p6gd%22%7D',
    'cX_P': 'laxi2e54j764p6gd',
    'cX_S': 'laxi2e6nh32tp8al',
    '_sp_sampled_user': 'false',
    'cX_G': 'cx%3A1k4hbj1lpd4sz2jkamj16kiqvt%3A36rkmkrerjt79',
    '_rdt_uuid': '1669440999823.09a8e400-2be6-4743-99f2-aa7e0602c8d3',
    '_gcl_au': '1.1.1483563698.1669441000',
    'ln_or': 'd',
    '_am_sp_djcsses.1fc3': '*',
    '_ncg_id_': '7fa2e031-c7bf-4f11-bc1f-81733b2c94fc',
    'AMCVS_CB68E4BA55144CAA0A4C98A5%40AdobeOrg': '1',
    '_li_dcdm_c': '.wsj.com',
    '_lc2_fpi': '7880a1137012--01gjs704n7t4p6cbk42bpphtjt',
    '_schn': '_8su8uk',
    '_scid': '7cfa8eda-4bb4-4260-9004-0bb4dd159516',
    '_ncg_domain_id_': '7fa2e031-c7bf-4f11-bc1f-81733b2c94fc.1.1669440999.1732512999',
    'hok_seg': 'none',
    's_cc': 'true',
    '_ncg_g_id_': '493fcd4c-0ef9-446e-bcf5-a701d63b9e1f.3.1669441000.1732512999',
    '_pin_unauth': 'dWlkPU9URTBOREUwWlRBdFpUa3lPQzAwTVRNd0xUa3dPR0l0TWpJd1pqSTJObUk0TWpRMA',
    '_sctr': '1|1669363200000',
    'DJSESSION': 'country%3Dus%7C%7Ccontinent%3Dna%7C%7Cregion%3Dca%7C%7Ccity%3Dlosangeles%7C%7Clatitude%3D33.9733%7C%7Clongitude%3D-118.2487%7C%7Ctimezone%3Dpst%7C%7Czip%3D90001-90068%2B90070-90084%2B90086-90089%2B90091%2B90093-90096%2B90099%2B90189',
    '_ncg_sp_ses.5378': '*',
    'djvideovol': '1',
    'djcs_route': 'a67c42f1-7098-4931-afb5-88294e9040e7',
    'TR': 'V2-76b3799d301496fb89020fae6b1f8bd8e8bbf90723db466ba0cd5de8078973de',
    'ab_uuid': '9a3e457b-0133-420d-905a-018449d1f6df',
    'sc.ASP.NET_SESSIONID': 'uksl1viflkah03p4fgyoya5h',
    'AMCV_CB68E4BA55144CAA0A4C98A5%40AdobeOrg': '1585540135%7CMCIDTS%7C19323%7CMCMID%7C71550376401585605761139195447725108676%7CMCAID%7CNONE%7CMCOPTOUT-1669463871s%7CNONE%7CMCAAMLH-1670061471%7C9%7CMCAAMB-1670061471%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-19330%7CvVersion%7C4.4.0',
    's_sq': 'djglobal%3D%2526c.%2526a.%2526activitymap.%2526page%253DWSJ_Summaries_Tech%2526link%253DSIGN%252520OUT%2526region%253Droot%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c',
    'djcs_secid': 'ZjlhMTYyMTEtMmZhMy00ZTUxLTllNjEtZTkzYzVlMzFmNzIx.s0xx67IJ0iCwzij1gzDCEG06kTENgT3ImV2neiabI_8',
    'sub_type': 'WSJ-SUB',
    'djcs_auto': 'M1669410224%2Fte8xk088v3UFpgqiJPoSJ7prdBOGREt0HZH28blT6nAIn1cT6OrSU9MiHZLdvjhwu5jy35Az4HCUr%2BcmsN%2F1e%2Fgt1wRxBkOwpflfhf9tCmB48D32b7znUhTsoPR3M%2FqMrKWlNGhuC6jr3iTb9OlG1mhsnilbjjL5zls529frvR%2BFq34aWerZUhPJJltFG0W65h%2FDmLgvB%2FC5W89T0BUWKtt6Hs%2F3hucPONf4zcGLhfm6f1d7WhvaR%2Fer%2FCaEevf0FXBQq3uc5K6Z57d9%2BP6ogEcTuigs4zqOwEqpTFRjoHOYAL2lZ3BZ%2FvpnBSVmOfEy1uPvx55QsbKRKPqaYq9%2FbpVp5TP4IH6ioA1DI4paHTFj0mdR3adIChCCOGHdv7%2FK72%2FOJirBjRfJTIU7%2B2qe%2FA%3D%3DG',
    'djcs_session': 'M1669452228%2F0hLh1NNzLztk7VmsVC03sMcEyDuu1dLAvvEAEZlZGc%2FdlSwaU4TcBGLZNrX8eI%2Bd8%2FYZ6EBGLc00WSnz9rnwZF8Ru3jvs4SfZFijn4S9sFd9xlrOdUtZ2peZt3MjEAsq1U7Sa0tLTNAN32R4I1vyoAftWnUGbL3aID9FH9vlrAZ7sguf6NDH2i8kXYWNrh3vzx7fr9ffuvdTERKejP49xRLnkKIXC%2Fw31A%2B1MB8OljGDActjvgmCSJ0eCYUQJ4MMpsYZyBtnuhgsN244R1nevLdHDkiOpvwAM7fOIifNogyDWt3d0wJ8cQ%2F5PdXyrIYeqjhZrV2oPGSdlnUwAxUlQ3HyaLcUNssJ%2BBJQLnZl4YR0HyXMX7weDQI01mGMwDGoj2ls%2FPswNz3cBNJju7krMuQXmEelDRrczoe4q9XKYojWO8ks%2F4%2FsK8UMOWvtuWa9rWcdW5JSVXpL3PG0lEgWqDEwhsrVN0toAjLeQlnJk3nC4HRuaO4HPoznPrWbyIEsNxvbrp6KDKPB5p83umpG90PeHZUwFzj6iqCIWHyUfkg%3DG',
    'usr_prof_v2': 'eyJwIjp7InBzIjowLCJxIjowfSwiYSI6eyJlZCI6InRydWUiLCJyIjoiMjAyMi0wNS0yM1QwMDowMDowMC4wMDBaIiwiZSI6IjIwMjUtMDgtMjZUMDA6MDA6MDAuMDAwWiIsInMiOiIyMDIyLTA1LTIzVDAwOjAwOjAwLjAwMFoiLCJzYiI6IkVkdWNhdGlvbmFsIiwiZiI6IjIgWWVhciIsIm8iOiJTdHVkZW50IERpZ2l0YWwgUGFjayIsImF0IjoiU1RVREVOVCIsInQiOjZ9LCJjcCI6eyJlYyI6IkxhcHNpbmciLCJwYyI6MC4wMDU3LCJwc3IiOjAuNDE3NTcsInRkIjoxODYsImFkIjoxMSwicWMiOjcsInFvIjoxMywic2NlbiI6eyJjaGUiOjAuMDA1ODEsImNobiI6MC4wMDA4NCwiY2hhIjowLjAwNTcsImNocCI6MC4wMDU5M319LCJvcCI6eyJpIjoiNjU1YjhlYzAiLCJqIjp7fX0sImljIjo2fQ%3D%3D',
    #'utag_main': #f'v_id:0184b2700f52001ffdea01dc023305081001407900978{_sn:3$_se:17$_ss:0$_st:1669459601423$vapi_domain:wsj.com$ses_id:1669456056620%3Bexp-session$_pn:17%3Bexp-session$_prevpage:WSJ_Summaries_Archive_NewsArchive%3Bexp-1669461401429}',
    '_ncg_sp_id.5378': '7fa2e031-c7bf-4f11-bc1f-81733b2c94fc.1669441000.3.1669457802.1669449456.663f447f-b7ed-4e62-a660-294246323610',
    '_uetsid': '4d38d9606d4c11eda9516b691d6a0ced',
    '_uetvid': '4d38ef606d4c11edb9039742a2dc40ba',
    '_pctx': '%7Bu%7DN4IgrgzgpgThIC5QHYBsAjAzMgnDgJpgAwCMALDqgGboAcORATEVQIZQYlW3r61Q90VBskaZ86MqgysiAY3wBWfAKLJ6ycVESgADjChUAlgA9EIAO4QAViAA0IAC4BPXdoQgAwgA0QAXz8HSFgAZUdWR0hzVgA7AHsY%2BxAII0coAEl8cxxGXMwSWlQSTFpFRjJChiJ-IA',
    'outbrain_cid_fetch': 'true',
    's_tp': '29043',
    's_ppv': 'WSJ_Summaries_Archive_NewsArchive%2C2%2C2%2C714',
    '_am_sp_djcsid.1fc3': '2171c4de-f06d-4c05-8803-be67cf9bab91.1669441000.1.1669457812.1669441000.4779adab-4d5c-46df-90b1-948262ffb468',
}

headers = {
    'authority': 'www.wsj.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': f'MicrosoftApplicationsTelemetryDeviceId=8cc42c62-6c50-1a3f-7fcc-21a83a207fc0; MicrosoftApplicationsTelemetryFirstLaunchTime=1669441054220; wsjregion=na%2Cus; gdprApplies=false; ccpaApplies=true; usr_bkt=rGgki1wrhs; _pcid=%7B%22browserId%22%3A%22laxi2e54j764p6gd%22%7D; cX_P=laxi2e54j764p6gd; cX_S=laxi2e6nh32tp8al; _sp_sampled_user=false; cX_G=cx%3A1k4hbj1lpd4sz2jkamj16kiqvt%3A36rkmkrerjt79; _rdt_uuid=1669440999823.09a8e400-2be6-4743-99f2-aa7e0602c8d3; _gcl_au=1.1.1483563698.1669441000; ln_or=d; _am_sp_djcsses.1fc3=*; _ncg_id_=7fa2e031-c7bf-4f11-bc1f-81733b2c94fc; AMCVS_CB68E4BA55144CAA0A4C98A5%40AdobeOrg=1; _li_dcdm_c=.wsj.com; _lc2_fpi=7880a1137012--01gjs704n7t4p6cbk42bpphtjt; _schn=_8su8uk; _scid=7cfa8eda-4bb4-4260-9004-0bb4dd159516; _ncg_domain_id_=7fa2e031-c7bf-4f11-bc1f-81733b2c94fc.1.1669440999.1732512999; hok_seg=none; s_cc=true; _ncg_g_id_=493fcd4c-0ef9-446e-bcf5-a701d63b9e1f.3.1669441000.1732512999; _pin_unauth=dWlkPU9URTBOREUwWlRBdFpUa3lPQzAwTVRNd0xUa3dPR0l0TWpJd1pqSTJObUk0TWpRMA; _sctr=1|1669363200000; DJSESSION=country%3Dus%7C%7Ccontinent%3Dna%7C%7Cregion%3Dca%7C%7Ccity%3Dlosangeles%7C%7Clatitude%3D33.9733%7C%7Clongitude%3D-118.2487%7C%7Ctimezone%3Dpst%7C%7Czip%3D90001-90068%2B90070-90084%2B90086-90089%2B90091%2B90093-90096%2B90099%2B90189; _ncg_sp_ses.5378=*; djvideovol=1; djcs_route=a67c42f1-7098-4931-afb5-88294e9040e7; TR=V2-76b3799d301496fb89020fae6b1f8bd8e8bbf90723db466ba0cd5de8078973de; ab_uuid=9a3e457b-0133-420d-905a-018449d1f6df; sc.ASP.NET_SESSIONID=uksl1viflkah03p4fgyoya5h; AMCV_CB68E4BA55144CAA0A4C98A5%40AdobeOrg=1585540135%7CMCIDTS%7C19323%7CMCMID%7C71550376401585605761139195447725108676%7CMCAID%7CNONE%7CMCOPTOUT-1669463871s%7CNONE%7CMCAAMLH-1670061471%7C9%7CMCAAMB-1670061471%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-19330%7CvVersion%7C4.4.0; s_sq=djglobal%3D%2526c.%2526a.%2526activitymap.%2526page%253DWSJ_Summaries_Tech%2526link%253DSIGN%252520OUT%2526region%253Droot%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c; djcs_secid=ZjlhMTYyMTEtMmZhMy00ZTUxLTllNjEtZTkzYzVlMzFmNzIx.s0xx67IJ0iCwzij1gzDCEG06kTENgT3ImV2neiabI_8; sub_type=WSJ-SUB; djcs_auto=M1669410224%2Fte8xk088v3UFpgqiJPoSJ7prdBOGREt0HZH28blT6nAIn1cT6OrSU9MiHZLdvjhwu5jy35Az4HCUr%2BcmsN%2F1e%2Fgt1wRxBkOwpflfhf9tCmB48D32b7znUhTsoPR3M%2FqMrKWlNGhuC6jr3iTb9OlG1mhsnilbjjL5zls529frvR%2BFq34aWerZUhPJJltFG0W65h%2FDmLgvB%2FC5W89T0BUWKtt6Hs%2F3hucPONf4zcGLhfm6f1d7WhvaR%2Fer%2FCaEevf0FXBQq3uc5K6Z57d9%2BP6ogEcTuigs4zqOwEqpTFRjoHOYAL2lZ3BZ%2FvpnBSVmOfEy1uPvx55QsbKRKPqaYq9%2FbpVp5TP4IH6ioA1DI4paHTFj0mdR3adIChCCOGHdv7%2FK72%2FOJirBjRfJTIU7%2B2qe%2FA%3D%3DG; djcs_session=M1669452228%2F0hLh1NNzLztk7VmsVC03sMcEyDuu1dLAvvEAEZlZGc%2FdlSwaU4TcBGLZNrX8eI%2Bd8%2FYZ6EBGLc00WSnz9rnwZF8Ru3jvs4SfZFijn4S9sFd9xlrOdUtZ2peZt3MjEAsq1U7Sa0tLTNAN32R4I1vyoAftWnUGbL3aID9FH9vlrAZ7sguf6NDH2i8kXYWNrh3vzx7fr9ffuvdTERKejP49xRLnkKIXC%2Fw31A%2B1MB8OljGDActjvgmCSJ0eCYUQJ4MMpsYZyBtnuhgsN244R1nevLdHDkiOpvwAM7fOIifNogyDWt3d0wJ8cQ%2F5PdXyrIYeqjhZrV2oPGSdlnUwAxUlQ3HyaLcUNssJ%2BBJQLnZl4YR0HyXMX7weDQI01mGMwDGoj2ls%2FPswNz3cBNJju7krMuQXmEelDRrczoe4q9XKYojWO8ks%2F4%2FsK8UMOWvtuWa9rWcdW5JSVXpL3PG0lEgWqDEwhsrVN0toAjLeQlnJk3nC4HRuaO4HPoznPrWbyIEsNxvbrp6KDKPB5p83umpG90PeHZUwFzj6iqCIWHyUfkg%3DG; usr_prof_v2=eyJwIjp7InBzIjowLCJxIjowfSwiYSI6eyJlZCI6InRydWUiLCJyIjoiMjAyMi0wNS0yM1QwMDowMDowMC4wMDBaIiwiZSI6IjIwMjUtMDgtMjZUMDA6MDA6MDAuMDAwWiIsInMiOiIyMDIyLTA1LTIzVDAwOjAwOjAwLjAwMFoiLCJzYiI6IkVkdWNhdGlvbmFsIiwiZiI6IjIgWWVhciIsIm8iOiJTdHVkZW50IERpZ2l0YWwgUGFjayIsImF0IjoiU1RVREVOVCIsInQiOjZ9LCJjcCI6eyJlYyI6IkxhcHNpbmciLCJwYyI6MC4wMDU3LCJwc3IiOjAuNDE3NTcsInRkIjoxODYsImFkIjoxMSwicWMiOjcsInFvIjoxMywic2NlbiI6eyJjaGUiOjAuMDA1ODEsImNobiI6MC4wMDA4NCwiY2hhIjowLjAwNTcsImNocCI6MC4wMDU5M319LCJvcCI6eyJpIjoiNjU1YjhlYzAiLCJqIjp7fX0sImljIjo2fQ%3D%3D; utag_main=v_id:0184b2700f52001ffdea01dc023305081001407900978{_sn:3$_se:17$_ss:0$_st:1669459601423$vapi_domain:wsj.com$ses_id:1669456056620%3Bexp-session$_pn:17%3Bexp-session$_prevpage:WSJ_Summaries_Archive_NewsArchive%3Bexp-1669461401429;} _ncg_sp_id.5378=7fa2e031-c7bf-4f11-bc1f-81733b2c94fc.1669441000.3.1669457802.1669449456.663f447f-b7ed-4e62-a660-294246323610; _uetsid=4d38d9606d4c11eda9516b691d6a0ced; _uetvid=4d38ef606d4c11edb9039742a2dc40ba; _pctx=%7Bu%7DN4IgrgzgpgThIC5QHYBsAjAzMgnDgJpgAwCMALDqgGboAcORATEVQIZQYlW3r61Q90VBskaZ86MqgysiAY3wBWfAKLJ6ycVESgADjChUAlgA9EIAO4QAViAA0IAC4BPXdoQgAwgA0QAXz8HSFgAZUdWR0hzVgA7AHsY%2BxAII0coAEl8cxxGXMwSWlQSTFpFRjJChiJ-IA; outbrain_cid_fetch=true; s_tp=29043; s_ppv=WSJ_Summaries_Archive_NewsArchive%2C2%2C2%2C714; _am_sp_djcsid.1fc3=2171c4de-f06d-4c05-8803-be67cf9bab91.1669441000.1.1669457812.1669441000.4779adab-4d5c-46df-90b1-948262ffb468',
    'sec-ch-ua': '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56',
}

wsjData = []


def writeCSV(data, year):
    headlines = []
    dates = []
    summaries = []
    for i in data:
        headlines.append(i[0])
        dates.append(i[1])
        summaries.append(i[2])
    newData = {
        'headlines' : headlines,
        'dates' : dates,
        'summaries' : summaries
    } 
    df = pd.DataFrame(newData)
    df.to_csv('wsjData_{}.csv'.format(year), index=True, header=True)
    # print(df.head)
    # with open('wsjdata', 'w', encoding = 'UTF8', newline = '') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(["headline", "date", "summary"])
    #     writer.writerows(data)
    #     # for row in data:
    #     #     writer.writerow(row)

def parseArticle(articles):
    for a in reversed(articles):
        newUrl = a.find('a')['href']
        page  = requests.get(newUrl, cookies=cookies, headers=headers)
        soup = BeautifulSoup(page.text.encode("utf-8"), "html.parser")
        # title = soup.find_all('h1')
        # datetime = soup.find_all('time')
        
        # for string in soup.strings:
        #     print(repr(string))
        headline = ""
        date = ""
        if soup.h1 is not None and soup.h1.string is not None:
            headline = soup.h1.string
        if soup.time is not None and soup.time.string is not None:
            date = soup.time.string

        # print(headline.strip())
        # print(date.strip())

        # get all paragraphs in text accessible without paywall
        paragraph = soup.find_all('p', attrs = {"class":"css-xbvutc-Paragraph e3t0jlg0"})
        summary = ''
        counter = len(paragraph)
        for p in paragraph:
            if p is None:
                continue
            if p.string is not None:
                # print(p.string)
                summary += p.string
            else:
                temp = p.children
                for s in temp:
                    # print(s.string)
                    if s.string is None:
                        continue
                    elif "css" in s.string:
                        continue
                    else:
                        summary += s.string
            counter -= 1
            if counter != 0:
                summary += ' '
        # print(summary.strip())
        row = [headline.strip(), date.strip(), summary.strip()]
        wsjData.append(row)

def scraper(start_date, end_date):
    delta = timedelta(days=1)
    while start_date <= end_date:
        year = start_date.strftime("%Y")
        month = start_date.strftime("%m")
        day = start_date.strftime("%d")
        # print(year, month, day)
        response = requests.get('https://www.wsj.com/news/archive/{}/{}/{}'.format(year, month, day), cookies=cookies, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        parseArticle(articles = soup.find_all('article'))
        # for a in articles:
        #     newUrl = articles[0].find('a')['href']
        #     parseArticle(newUrl)
        start_date += delta
        
        
for i in range(2017, 2013, -1):
    scraper(date(i, 1, 1), date(i, 12, 31))
    writeCSV(wsjData, i)
    wsjData.clear()
    

response = requests.get('https://www.wsj.com/news/archive/2022/01/01', cookies=cookies, headers=headers)

# soup = BeautifulSoup(response.content, "html.parser")
# # print(soup.main)
# articles = soup.find_all('article')
# # print(articles)
# for a in articles:
#     print(a.find('a')['href'])
    
# newUrl = articles[0].find('a')['href']
# page  = requests.get(newUrl, cookies=cookies, headers=headers)
# soup = BeautifulSoup(page.text, "html.parser")
# # title = soup.find_all('h1')
# # datetime = soup.find_all('time')
# headline = soup.h1.string
# date = soup.time.string

# # get all paragraphs in text accessible without paywall
# paragraph = soup.find_all('p', attrs = {"class":"css-xbvutc-Paragraph e3t0jlg0"})

# print(soup.h1.string)
# print(soup.time.string)
# print(paragraph[0].string) # get the first paragraph - use as summary
    
# url = "https://www.wsj.com/articles/colorado-wildfire-destroys-nearly-1-000-homes-11641083822"
# archive = "https://www.wsj.com/news/archive/2022/01/01"
# try:
#     # page = requests.get(url)
#     page = requests.get(archive)
# except:
#     error_type, error_obj, error_info = sys.exc_info()
#     print("Error: ", url)
#     print(error_type, error_info.tb_lineno)
# soup = BeautifulSoup(page.text, "html.parser")
# #print(page.status_code)
# #print(page.text)

# # soup = BeautifulSoup(page.text, "html.parser")
# # with open('test.txt', 'w') as f:
# #     f.write(page.text)
# # articles = soup.find_all('div', attrs = {"class" : "style--column--1p190TxH style--column-top--3Nm75EtS style--column-12--1x6zST_y "})
# # articles = soup.find_all('div')

# #print(type(tag))
# for link in soup.findAll('a'):
#     print(link.get('href'))
# # print(soup.article.prettify())
# # print(soup.main.prettify())



# # print(articles[0].descendants)
# # for i in articles[0].descendants:
# #     print(i)
# # for article in articles:
# #     print(article.find('article').prettify())
#     #print(article.find('article')['href'])
# # print(type(articles), articles[0].contents)
# # print(type(articles[0].contents))

# #<article class="WSJTheme--story--XB4V2mLz WSJTheme--padding-top-large--2v7uyj-o styles--padding-top-large--3rrHKJPO WSJTheme--padding-bottom-large--2lt6ga_1 styles--padding-bottom-large--2vWCTk2s WSJTheme--border-bottom--s4hYCt0s " data-id="WP-WSJ-0000088117"><div class="WSJTheme--float-media-left--3hSCSxfj WSJTheme--lh-image--3GrOkk6o "> <div class="WSJTheme--image--1RvJrX_o WSJTheme--media--2zsLCB98 WSJTheme--image-above--pBsXD1hr " style="width:100px"><a class="" href="https://www.wsj.com/articles/colorado-wildfire-destroys-nearly-1-000-homes-11641083822" tabindex="0"><img src="https://images.wsj.net/im-460684?width=100&amp;height=67" alt="" height="67" width="100" class="WSJTheme--image--At42misj " srcset="https://images.wsj.net/im-460684?width=100&amp;height=67, https://images.wsj.net/im-460684?width=100&amp;height=67&amp;pixel_ratio=1.5 1.5x, https://images.wsj.net/im-460684?width=100&amp;height=67&amp;pixel_ratio=2 2x, https://images.wsj.net/im-460684?width=100&amp;height=67&amp;pixel_ratio=3 3x"></a></div> </div><div class="WSJTheme--overflow-hidden--qJmlzHgO "> <div class="WSJTheme--lh-flashline--1p_5hKeB "> <div class="WSJTheme--articleType--34Gt-vdG "> <span class="" href="">U.S.</span></div> </div><div class=""> <div class="WSJTheme--headline--7VCzo7Ay "><h2 class="WSJTheme--headline--unZqjb45 reset WSJTheme--heading-standard-s--2eMU4jl4 WSJTheme--standard--2eOdD903 typography--serif-display--ZXeuhS5E WSJTheme--small--2f09SjbK "><a class="" href="https://www.wsj.com/articles/colorado-wildfire-destroys-nearly-1-000-homes-11641083822"><span class="WSJTheme--headlineText--He1ANr9C ">Colorado Wildfire Destroys Nearly 1,000 Homes</span></a></h2></div> </div><div class="WSJTheme--lh-timestamp--_ZCwpfk9 "> <div class="WSJTheme--timestamp--2zjbypGD "><p aria-label="Updated 11:19 PM ET" class="WSJTheme--timestamp--22sfkNDv ">11:19 PM ET</p></div> </div> </div></article>
