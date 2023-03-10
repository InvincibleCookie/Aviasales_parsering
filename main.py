from selenium import webdriver

city1 = 'KJA'
date1 = '2503'
city2 = 'MOW'
date2 = ''
n_of_tickets = '1'




dates = ['0101', '0201', '0301', '0401', '0501', '0601', '0701', '0801', '0901', '1001', '1101',
         '1201', '1301', '1401', '1501', '1601', '1701', '1801', '1901', '2001', '2101', '2201',
         '2301', '2401', '2501', '2601', '2701', '2801', '2901', '3001', '3101', '0102', '0202',
         '0302', '0402', '0502', '0602', '0702', '0802', '0902', '1002', '1102', '1202', '1302',
         '1402', '1502', '1602', '1702', '1802', '1902', '2002', '2102', '2202', '2302', '2402',
         '2502', '2602', '2702', '2802', '0103', '0203', '0303', '0403', '0503', '0603', '0703',
         '0803', '0903', '1003', '1103', '1203', '1303', '1403', '1503', '1603', '1703', '1803',
         '1903', '2003', '2103', '2203', '2303', '2403', '2503', '2603', '2703', '2803', '2903',
         '3003', '3103', '0104', '0204', '0304', '0404', '0504', '0604', '0704', '0804', '0904',
         '1004', '1104', '1204', '1304', '1404', '1504', '1604', '1704', '1804', '1904', '2004',
         '2104', '2204', '2304', '2404', '2504', '2604', '2704', '2804', '2904', '3004', '0105',
         '0205', '0305', '0405', '0505', '0605', '0705', '0805', '0905', '1005', '1105', '1205',
         '1305', '1405', '1505', '1605', '1705', '1805', '1905', '2005', '2105', '2205', '2305',
         '2405', '2505', '2605', '2705', '2805', '2905', '3005', '3105', '0106', '0206', '0306',
         '0406', '0506', '0606', '0706', '0806', '0906', '1006', '1106', '1206', '1306', '1406',
         '1506', '1606', '1706', '1806', '1906', '2006', '2106', '2206', '2306', '2406', '2506',
         '2606', '2706', '2806', '2906', '3006', '0107', '0207', '0307', '0407', '0507', '0607',
         '0707', '0807', '0907', '1007', '1107', '1207', '1307', '1407', '1507', '1607', '1707',
         '1807', '1907', '2007', '2107', '2207', '2307', '2407', '2507', '2607', '2707', '2807',
         '2907', '3007', '3107', '0108', '0208', '0308', '0408', '0508', '0608', '0708', '0808', '0908',
         '1008', '1108', '1208', '1308', '1408', '1508', '1608', '1708', '1808', '1908', '2008',
         '2108', '2208', '2308', '2408', '2508', '2608', '2708', '2808', '2908', '3008', '3108',
         '0109', '0209', '0309', '0409', '0509', '0609', '0709', '0809', '0909', '1009', '1109',
         '1209', '1309', '1409', '1509', '1609', '1709', '1809', '1909', '2009', '2109', '2209',
         '2309', '2409', '2509', '2609', '2709', '2809', '2909', '3009', '0110', '0210', '0310',
         '0410', '0510', '0610', '0710', '0810', '0910', '1010', '1110', '1210', '1310', '1410',
         '1510', '1610', '1710', '1810', '1910', '2010', '2110', '2210', '2310', '2410', '2510',
         '2610', '2710', '2810', '2910', '3010', '3110', '0111', '0211', '0311', '0411', '0511',
         '0611', '0711', '0811', '0911', '1011', '1111', '1211', '1311', '1411', '1511', '1611',
         '1711', '1811', '1911', '2011', '2111', '2211', '2311', '2411', '2511', '2611', '2711',
         '2811', '2911', '3011', '0112', '0212', '0312', '0412', '0512', '0612', '0712', '0812',
         '0912', '1012', '1112', '1212', '1312', '1412', '1512', '1612', '1712', '1812', '1912',
         '2012', '2112', '2212', '2312', '2412', '2512', '2612', '2712', '2812', '2912', '3012',
         '3112']

def two_weeks(city1, date1, city2, date2, n_of_tickets):
    global dates
    price_min = 9999999999
    min_url = ''
    min_date = ''
    ind = dates.index(date1)
    for i in range(4):
        url = f'https://www.aviasales.ru/search/{city1}{dates[ind + i]}{city2}{date2}{n_of_tickets}'
        driver = webdriver.Chrome()
        driver.set_page_load_timeout(45)
        driver.get(url=url)

        text = str(driver.page_source)
        s = int((text[text.find('<title>') + 7: text.find('???')]).replace('\u2009', ''))
        print(s)
        if s < price_min:
            price_min = s
            min_url = url
            min_date = dates[ind + i]
    print(price_min)
    print(min_url)
    print(min_date)


two_weeks('KJA', '2503', 'MOW', '', '1')
print()
two_weeks('KJA', '2503', 'AER', '', '1')
print()
two_weeks('KJA', '2503', 'BKK', '', '1')


