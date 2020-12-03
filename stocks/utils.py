import datetime
import re
import yfinance as yf
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from pytz import timezone


def bloomberg(company):
    url = f'https://www.bloomberg.com/search?query={company.name.lower()}'
    headers = {'authority': 'www.bloomberg.com',
               'method': 'GET',
               'path': f'/search?query={company.name.lower()}',
               'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
               'accept-encoding': 'gzip, deflate, br',
               'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
               'cache-control': 'max-age=0',
               'cookie': 'agent_id=f1b1c74c-7c64-4e66-973e-230cbdbff200; session_id=22bd695b-2b78-4d94-8bbd-36f4a0c2f3f3; session_key=968399bf3c8dab3fc0ad901128e95a0a9c1f8513; _sp_krux=false; _sp_v1_ss=1:H4sIAAAAAAAAAItWqo5RKimOUbLKK83J0YlRSkVil4AlqmtrlXQGQlksAJ3zQ2mdAAAA; _sp_v1_opt=1:; _sp_v1_csv=null; _sp_v1_lt=1:; _gcl_au=1.1.1803187726.1604768536; _pxvid=fd23207c-211a-11eb-99c0-0242ac12000a; ccpaUUID=8fc73166-9050-4946-85b1-15715b33cd8d; dnsDisplayed=true; ccpaApplies=true; signedLspa=false; bbgconsentstring=req1fun1pad1; bdfpc=004.5824872840.1604768538343; _pxhd=b320555670451b96d0a69387ba88558d7ab3cafdfe5152b62c786edd2c1113f7:fd23207c-211a-11eb-99c0-0242ac12000a; _rdt_uuid=1604768538816.284a57ff-92c2-4611-905d-12614396aec5; _ga=GA1.2.1105855941.1604768539; __gads=ID=9aec5b44ba264c77:T=1604768538:S=ALNI_MYdw8i_0EdfYL9zau5A4TT1UmZwYA; __tbc=%7Bjzx%7Dt_3qvTkEkvt3AGEeiiNNgNtzXGpy8zYdB8yCXUL-rdjXjvzEFpvz39G17BihLmhrD493nTzoZGvH8BKpFpaGQkKEzX3GECZwN8XlOTfjUWzR-RrLKx8QucWAZFHkhWsSjylU0Z664w9lha1BgkmqDg; __pat=-18000000; _lc2_fpi=b1166d620485--01ephth8z62qezts6d4nzt4cfx; _fbp=fb.1.1604768539714.1984643394; _cc_id=dc32aa361ac17d910ba37260411b09c4; _scid=c0279db4-ef0f-4843-a4a9-6595e6dfc7b3; trc_cookie_storage=taboola%2520global%253Auser-id%3Db80e7b35-9cd7-4246-bfdd-2ce2de505514-tuct68ce4e6; com.bloomberg.player.volume.level=1; ntv_as_us_privacy=1YNN; _ntv_uid=47849ae9-159c-4fb2-9e0d-004164a76232; _sp_v1_uid=1:68:43577af1-2c22-4d2d-841a-37ad70e1c799; _sp_id.3377=734c81db-aec3-4c2a-b3d1-fa71c58c226e.1605548176.1.1605548207.1605548176.5996b6a6-e706-491c-8f61-b38f75c84f96; _reg-csrf=s%3As9lU5_7VViFu8aZqwzOcLys9.%2FT9A1Lg9mDyaiOooRXpTFobOXlRqmwWip%2FRJcNnt9LI; _user-status=anonymous; _gid=GA1.2.1626595836.1607013039; _parsely_session={%22sid%22:3%2C%22surl%22:%22https://www.bloomberg.com/%22%2C%22sref%22:%22%22%2C%22sts%22:1607013039644%2C%22slts%22:1605587024005}; _parsely_visitor={%22id%22:%22pid=0c54395e949300bc5478d7a1db60dbe5%22%2C%22session_count%22:3%2C%22last_session_ts%22:1607013039644}; _li_dcdm_c=.bloomberg.com; bb_geo_info={"country":"US","region":"US"}|1607617840884; _sctr=1|1606975200000; bbAbVisits=; __pvi=%7B%22id%22%3A%22v-2020-12-03-10-30-39-293-PWQ8zVHCDzOmEgw9-0f17c27ab2bfb20c53757726002cecba%22%2C%22domain%22%3A%22.bloomberg.com%22%2C%22time%22%3A1607013069677%7D; _tb_sess_r=https%3A//www.bloomberg.com/; xbc=%7Bjzx%7DMuDMa2ET_r5g5YJ0lQI5QhugLjssFT59o5RO_WT3dtTdp9YDGufU-TIUyY2IODRxMkWiDFbfiHSKRHsEZW7hVsZUT-qo5ypwuU77w7RWUOau1kFzX_F_qP9vhwZix76AsvXGuyjM7fXr03CxGidy-ZHEcpkkQ6DTsCkHCD_JhNY-k8I5xItVl815xQeLdXdewz5_8sVi6QjhSDczSf6vY8s1-TkTx9xqeJMh5qQOQXg6_Wobq8NPtvZcd3kU9QY4ij22uVCYLXb8r7COhts1ZuSZyN5b3FVu4bdqPFC_eog4QCAOqkpIlY3A19Oj1AAJ98vLD-_J_qeULev1MiuQE2IwHMmDe660M4At69xUV_xgo4aQ8vlGSZcQY8kZqjvpG8Ua57Qhjx-YBy-zfiq5TQ; GED_PLAYLIST_ACTIVITY=W3sidSI6IldBREsiLCJ0c2wiOjE2MDcwMTMzODgsIm52IjowLCJ1cHQiOjE2MDcwMTMzNzYsImx0IjoxNjA3MDEzMzgwfV0.; _sp_v1_data=2:232240:1605548172:0:6:0:6:0:0:_:-1; consentUUID=f0f5d2ae-4cb5-46f4-aef3-05756929965b; _uetsid=e135ca60358411ebb9911921b5859477; _uetvid=e1362eb0358411eba45537519dc77dcc; __sppvid=035ea304-668e-4c06-864e-19ad5a685d3c; _tb_t_ppg=https%3A//www.bloomberg.com/search%3Fquery%3DApple; _px2=eyJ1IjoiYjE4N2VkOTAtMzU4NS0xMWViLWIyMGMtNTc4YTQ5ZWQyYmU0IiwidiI6ImZkMjMyMDdjLTIxMWEtMTFlYi05OWMwLTAyNDJhYzEyMDAwYSIsInQiOjE2MDcwMTM2OTAzODYsImgiOiIxOGJjNTM2NDZkYzAyNzU2MWNmNGU1NTM4ZmViNjJhZGE4NzI1MmFiNTU1ZGNjY2M1ZDNmMmYwZjA5NjllYzg0In0=; _px3=de7e11c596bf31cca9cadb43f41487c07d767cf5cc02d72f50b0d005cf24b889:uhhuG26jrQdQS3fn/zJPz2iMwyQfQ9jYn4RkkBOgD7HZ7S0z9e5yMeIyHl1xfUNfJSyTmSg/5qt68eY95BGcmg==:1000:k9fpOjB9mZLC9Mrd/kfRhVDrG6N3b164NXbNzQkfxEpxE4WtlkUhVolwrrstJd9fCwwdreErt8d3BhRYM7tT4NTc/mxiIilaRLXiVmqlV6Uy+pFt0e+air9GQyB/vUhk+6F8sPYcqLxJKh8pRL4ncvVSzWVkYQLZHoIFNWkX7Vg=; outbrain_cid_fetch=true; _reg-csrf-token=jT7k5ckA-Nb-sfKXeGQdl4hlSE3zHmBbOzx8; _pxde=862aaef093290c59d53b4984203437028c28deea182b845e872f945f656c302c:eyJ0aW1lc3RhbXAiOjE2MDcwMTMzOTQ0NzgsImZfa2IiOjAsImlwY19pZCI6W119; _gat_UA-11413116-1=1',
               'referer': f'https://www.bloomberg.com',
               'upgrade-insecure-requests': '1',
               'sec-fetch-dest': 'document',
               'sec-fetch-mode': 'navigate',
               'sec-fetch-site': 'same-origin',
               'sec-fetch-user': '?1',
               'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36}'
    }

    session = requests.Session()
    rq = session.get(url, headers=headers)
    page = rq.content
    soup = BeautifulSoup(page, 'lxml')
    results = soup('div', re.compile('text__'))

    answer = []
    for result in results:
        date = result.find_all('div', re.compile('publishedAt'))[0].text
        date = datetime.strptime(date, '%B %d, %Y').strftime('%m/%d/%Y')
        text = result.find_all('a', re.compile('summary_'))
        if text:
            news = text[0].text[:80] + '...'
            link = text[0]['href']
            answer.append([date, news, link])
    return answer


def price(company):

    stock_prices = {}

    ticker = yf.Ticker(company)
    history = ticker.history(period="1y")
    period = len(history)
    todays_history = ticker.history(period='1d', interval='1m')

    now = datetime.now(timezone('America/New_York')).strftime('%H')

    stock_prices['current_price'] = round(todays_history.iloc[-1].get('Close'), 2)
    stock_prices['current_price_time'] = todays_history.index[-1].strftime('%H:%M:%S')

    stock_prices['last_quarter_price'] = round(history.iloc[(-period//4)].get('Close'), 2)
    stock_prices['last_quarter_date'] = history.index[(-period//4)].strftime('%B %-d, %Y')
    stock_prices['last_quarter_var'] = round(
        ((stock_prices['current_price'] / stock_prices['last_quarter_price']) - 1) * 100, 2)

    stock_prices['last_semester_price'] = round(history.iloc[(-period//2)].get('Close'), 2)
    stock_prices['last_semester_date'] = history.index[(-period//2)].strftime('%B %-d, %Y')
    stock_prices['last_semester_var'] = round(
        ((stock_prices['current_price'] / stock_prices['last_semester_price']) - 1) * 100, 2)

    stock_prices['last_year_price'] = round(history.iloc[1].get('Close'), 2)
    stock_prices['last_year_date'] = history.index[1].strftime('%B %-d, %Y')
    stock_prices['last_year_var'] = round(
        ((stock_prices['current_price'] / stock_prices['last_year_price']) - 1) * 100, 2)

    stock_prices['data'] = [round(float(x), 2) for x in list(history.Close)]
    stock_prices['labels'] = [str(x.strftime("%m.%d.%Y")) for x in list(history.index)]

    return stock_prices
