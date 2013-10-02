import urllib
import re
import cPickle as pickle

from thinkstats import myplot
from thinkstats import Pmf
from thinkstats import Cdf

results_url = 'http://www.mbc-marathon.co.kr/record/index03.php?sno=%d&sex_item_code=M|T&agegroup=&year=2010&mode=r_search_result'
# 순위	참가번호	성명 성별	참가부문	연령대	연령대순위  기록	출발시각	반환(7.65km) 도착시각
# 연령대: 20대이하, 30대, 40대, 50대, 60대 이상


def ConvertHMSToSpeed(hms):
    h, m, s = [float(x) for x in hms.split(':')]
    hour = h + m/60.0 + s/60.0/60.0
    kmh = int(10 / hour * 10) / 10.0
    return kmh

def GetRecords(text):
    records = re.findall(r'\s<tr>[\w\W]+?</tr>\s', text)
    records_list = []
    for record in records:
        attrs = re.findall(r'<td[\w\W]*?>(.+?)</td>', record)
        if len(attrs) != 11:
            continue
        if not '10km' in attrs[4]:
            continue
        if not ':' in attrs[7]:
            continue
        if not ':' in attrs[8]:
            continue
        if not ':' in attrs[9]:
            continue
        if not ':' in attrs[10]:
            continue
        records_list.append(attrs)

    return records_list

def ReadResults():
    pickle_file = 'mbc_marathon_2010.p'
    results = []
    try:
        frec = open(pickle_file, 'rb')
    except:
        frec = None
    if frec:
        results = pickle.load(frec)
        print 'read samples from pickle file'
    else:    
        for idx in range(0, 3451, 30):
            url = results_url % (idx)
            conn = urllib.urlopen(url)
            result = GetRecords(conn.read())
            results.extend(result)
        pickle.dump(results, open(pickle_file, 'wb'))

     
    return results

def FindProfHeo(results):
    for r in results:
        if r[2] == '허준영':
            speed = ConvertHMSToSpeed(r[7])
            #print '허준영 speed:', speed
            #print 'rank:', r[0]
            #print 'rank in 30대:', r[6]
            return (speed, r[0], r[6])


def GetSpeeds(results, column=7):
    speeds = []
    for t in results:
        hms = t[column]
        speed = ConvertHMSToSpeed(hms)
        speeds.append(speed)
    return speeds

def CondFilter(results, age='30대'):
    results_age = []
    for t in results:
        if t[5] == age:
            results_age.append(t)

    return results_age

def main():
    results = ReadResults()
    print '# of samples:', len(results)

    results = CondFilter(results)
    print '# of samples(age=30s):', len(results)

    h_speed, h_rank, h_rank_age = FindProfHeo(results)
    speeds = GetSpeeds(results)
    pmf = Pmf.MakePmfFromList(speeds, 'speeds')
    cdf = Cdf.MakeCdfFromList(speeds, 'speeds')
    if h_speed:
        print '허준영s speed is ', h_speed
        print 'His percentile rank is ', cdf.Prob(h_speed) * 100

    myplot.Clf()
    myplot.Pmf(pmf)
    myplot.Save(root='mbc_marathon_pmf', title='PMF of running speed',
               xlabel='speed (kmh)',
               ylabel='probability')

    myplot.Clf()
    myplot.Cdf(cdf)
    myplot.Save(root='mbc_marathon_cdf', title='CDF of running speed',
               xlabel='speed (kmh)',
               ylabel='probability')

    myplot.Close()


if __name__ == '__main__':
    main()
