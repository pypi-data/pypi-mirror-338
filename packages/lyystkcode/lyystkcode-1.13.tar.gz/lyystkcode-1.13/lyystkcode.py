import os
import sys
import pandas as pd
import baostock as bs
import json
import lyytools
import time
import tushare as ts
from datetime import datetime, timedelta, time as datetime_time
from sqlalchemy import create_engine, text
from lyylog2 import log
import lyycalendar
import lyyak as ak

instance_lyycalendar = lyycalendar.lyycalendar_class()
# lyymysql = lyymysql.lyymysql_class()
pro = ts.pro_api(token="2ad5763004f5cab36da48ea691473aa14a6464f2966deb3c24f85169")

from cachetools import cached, TTLCache

# 创建一个缓存，最大存储 1000 个元素，每个元素的超时时间是 24 小时（86400 秒）
cache = TTLCache(maxsize=1000, ttl=86400)


def ak获取公司上市时间(bs股票代码表df, 股票代码, debug=False):
    """
    bs股票代码表df为读取的bs本地备份 Csv文件。优先从本地查询。
    股票代码使用9位形如"sh.600000"
    """
    # print("通过akshare获取上市时间")
    stk_code_num = lyytools.万能股票代码(股票代码, "000000")
    if bs股票代码表df.shape[0] > 1000:
        tj = 'code=="' + 股票代码 + '"'
        上市时间 = bs股票代码表df.query(tj)["ipoDate"]
        if debug:
            print(股票代码 + "本地查到上市时间：" + 上市时间)
        if len(上市时间) > 0:
            return 上市时间.values[0]
    else:
        公司信息 = lyyf_akshare_get_name.stock_individual_info_em(stk_code_num)
        上市时间 = str(公司信息["value"].loc[3])
        returntext = 上市时间[:4] + "-" + 上市时间[4:6] + "-" + 上市时间[6:8]
        if debug:
            print("上市时间：" + 股票代码, returntext)
        return returntext


def get_codelist_from_mysql(conn, debug=False):
    table_name = "stock_all_codes"
    columns = ["code", "name", "tradeStatus", "ipoDate"]
    # 构建查询
    query = f"SELECT {', '.join(columns)} FROM {table_name}"
    df = pd.read_sql(text(query), conn)
    return df

    # pro = ts.pro_api()
    # #查询当前所有正常上市交易的股票列表
    # data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    # 或者：
    # #查询当前所有正常上市交易的股票列表
    # data = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')


def ak获取股票简称(stk_code_num, debug=False):
    print("codex=", stk_code_num)
    stk_code_num = str(stk_code_num).zfill(6)
    公司信息 = lyyf_akshare_get_name.stock_individual_info_em(stk_code_num)
    股票简称 = str(公司信息["value"].loc[5])
    print("ak获取股票简称结果：", stk_code_num + "，" + 股票简称)
    return 股票简称


def 查询股票简称(code, if_ak=True, if_tushare=True, debug=False):
    """
    先在本地数据库查询，再通过akshare查询，实在不行通过狗日的tushare查询
    """

    name = ak获取股票简称(code, debug)
    if name is None or len(name) < 1:
        name = tushare_get_name(code)
    return name


def tushare_get_all_codes(cache_file="", debug=False):
    """
    从tushare获取当天所有股票代码。如果有2小时内缓存则使用缓存。
    Read from cache file: tushare.csv
            ts_code  symbol     name area industry  list_date
    0     000001.SZ  000001     平安银行   深圳       银行   19910403
    1     000002.SZ  000002      万科A   深圳     全国地产   19910129
    """
    if cache_file is None or len(cache_file) < 1:
        cache_file = "tushare.csv"

    if debug:
        print("# 判断文件是否在cache_time内修改")
    if os.path.exists(cache_file):
        time_str = "09:15"  # 你可以更改这个时间字符串进行测试
        # 将字符串转换为时间对象
        current_time = datetime.strptime(time_str, "%H:%M").time()
        before_trade_time = time(8, 50) < current_time < time(9, 25) 
        if 文件很新鲜(cache_file, 12) or before_trade_time:
            print("文件很新鲜: " + cache_file + ", 或者时间在开盘前，使用缓存")
            df = pd.read_csv(cache_file, index_col=0, dtype={"symbol": str})
            return df
    else:
        print("cache file is not exist, download from tushare pro...")
        # 调用tushare库的get_stock_basics方法获取中国A股股票列表
        try:
            df = pro.stock_basic(exchange="", list_status="L", fields="ts_code,symbol,name,area,industry,list_date")
            new_cols = [c.replace("symbol", "code") if c == "symbol" else c.replace("list_date", "ipoDate") if c == "list_date" else c for c in df.columns]
            df.columns = new_cols
            # df.rename(columns={'ts_code': 'code'}, inplace=True)
            mask = df["ts_code"].str.contains("bj", case=False)
            df.drop(df.index[mask], inplace=True)
            df["code"] = df["code"].str[:6]
            df.drop(["ts_code", "industry", "area"], axis=1, inplace=True)
            df.reset_index(drop=True, inplace=True)
            df["tradeStatus"] = 1
            print("tushare_all_codes_len=", df.shape[0])
            df.to_csv(cache_file)  # 缓存到文件

        except Exception as e:
            print("接口连接异常，没办法只能读取旧缓存现有股票代码文件先。Read from cache file: " + cache_file, e)
            df = pd.read_csv(cache_file, index_col=0, dtype={"symbol": str})
    return df


def tushare_get_name(stk_code_num, df=None, col=None):
    print("tushare_get_namexxx", stk_code_num)
    if df is None:
        print("df is none, try to get tushare_df")
        df = tushare_get_all_codes()
        col = "code"
    # 根据股票代码查询股票简称信息
    stk_code_num = str(stk_code_num).zfill(6)
    name_list = df.loc[df[col] == stk_code_num, "name"].tolist()
    print("name_list=", name_list)
    name = name_list[0] if len(name_list) > 0 else ""
    print(stk_code_num, ",tushare_get_name结果：", name)
    return name


def all_code_to_mysql(df, debug=False):
    """
    2023/4/12最新代码表存mysql
    """
    print("function all_code_to_mysql")
    table_name = "stock_all_codes"
    import lyymysql

    conn = lyymysql.conn
    effect_rows = 0

    total = len(df)  # 总行数

    for index, row in df.iterrows():
        # 进度条
        percent = int((index + 1) / total * 100)
        print("\r[%-50s] %d%% " % ("=" * percent, percent), end="")

        # 判断是否在列表中,如果不在则插入
        # if row['code'] not in codes:
        insert_query = f"INSERT INTO {table_name} (code, name, tradeStatus, ipoDate) VALUES ({row['code']}, '{row['name']}', {row['tradeStatus']}, '{row['ipoDate']}')"
        result = conn.execute(lyymysql.text(insert_query))
        effect_rows += result.rowcount
        conn.commit()
    print(f"\n effect_rows = {effect_rows}")
    return effect_rows


def delete_all_code(conn, table_name, debug=False):
    """
    删除stock_all_codes表中的所有数据
    """
    delete_query = f"DELETE FROM {table_name}"
    import lyymysql

    result = conn.execute(lyymysql.text(delete_query))
    effect_rows = result.rowcount
    conn.commit()
    if debug:
        print(f"Deleted {effect_rows} rows.")


def is_null(x):
    return x == 0 or x.strip() == "" or pd.isna(x)


def 处理空值_公司(conn):
    table_name = "stock_all_codes"
    query = f"SELECT * FROM {table_name} WHERE name IS NULL or ipoDate IS NULL"
    result = conn.execute(text(query)).fetchall()
    if len(result) > 1:
        print("处理空值")
        for row in result:
            stk_code_num = row["code"]
            公司信息 = lyyf_akshare_get_name.stock_individual_info_em(stk_code_num)
            ipoDate = str(公司信息["value"].loc[3])
            name = str(公司信息["value"].loc[5])
            update_query = f"UPDATE {table_name} SET name={name}, ipoDate={ipoDate} WHERE code = {row['code']}"
            conn.execute(text(update_query))
            conn.commit()
        print("处理公司名字空值完成")


def handle_null(x, func):
    if is_null(x):
        return func(x)
    else:
        return x


def is_null(x):
    if isinstance(x, int):
        return x == "" or pd.isna(x)
    elif isinstance(x, str):
        return x == "" or pd.isna(x)
    else:
        return pd.isna(x)


def 处理空值(df):
    name_null = df["name"].apply(is_null)
    df.loc[name_null, "name"] = df.loc[name_null, "code"].apply(查询股票简称)
    import lyymysql

    conn = lyymysql.conn
    sql = "SELECT code, name FROM stock_all_codes"
    result = conn.execute(text(sql)).fetchall()
    mapping = dict(result)

    for index, row in df.iterrows():
        code = row["code"]
        name = row["name"]
        if code in mapping:
            if name != mapping[code]:
                sql = f"UPDATE stock_all_codes SET name = '{name}' WHERE code = {code}"
                print("update_sql=", sql)
                conn.execute(text(sql))
        else:
            sql = "INSERT INTO stock_all_codes (code, name) VALUES (:code, :name)"
            conn.execute(text(sql), code=code, name=name)
            print("insert sql=", sql)
    conn.commit()


def convert_df_to_list(target):
    if isinstance(target, pd.DataFrame):
        return target["code"].tolist()
    else:
        return target


def get_stkcode_anywhere(cache_file, timeout=2, debug=False):

    if os.path.isfile(cache_file):
        if debug:
            print("# 读取保存的cache文件,path=", cache_file)
        # 获取当前时间和一小时前的时间
        if 文件很新鲜(cache_file, 12):
            if debug:
                print("cache文件还比较新鲜,直接读取之")
            df = pd.read_csv(cache_file)
            if len(df) > 1000:
                return convert_df_to_list(df)
            else:
                raise "cache文件读取后行数不对."
        else:
            if debug:
                print("cache文件太老了,重新下载")
    try:
        if debug:
            print("trytushare获取股票代码表")
        df = tushare_get_all_codes()
        if len(df) > 1000:
            print("最后使用tushare获取股票代码表")
            return convert_df_to_list(df)
    except Exception as e:
        print("tushare获取股票代码表失败", e)
    try:
        df = baostock获取股票代码表()
        if len(df) > 1000:
            print("最后是从baostock获取股票代码表")
            return convert_df_to_list(df)
    except Exception as e:
        print("baostock获取股票代码表失败", e)
    # df = pd.read_sql_table('stock_all_codes', lyymysql.conn)
    if len(df) > 1000:
        print("最后是从mysql获取股票代码表，可能过时")
        return convert_df_to_list(df)


def perfact_new_stkcode_list(cache_file=".", interval=12, nextfuntion=None, timeout=0.6):
    """
    检查文件是否很新鲜，如果是，则不需要重新下载

    Returns:
        _type_: _description_
    """
    home_dir = os.path.dirname(os.path.abspath(__file__))
    cache_file = home_dir + "/stk_code_dict.json"

    if os.path.isfile(cache_file):
        print(f'cache_file "{cache_file}" exists')
        now = datetime.now()
        print("dfsaf")
        one_hour_ago = now - timedelta(hours=interval)
        print("22222")
        mod_time = datetime.fromtimestamp(os.path.getmtime(cache_file))
        print("dxxxx")
        # if mod_time >= one_hour_ago and mod_time <= now:
        #     print("cache_file is fresh, just read it")
        with open(cache_file, "r", encoding="utf-8") as f:
            stk_code_dict = json.load(f)
            return stk_code_dict

    # print("no file or not so fresh, download new")
    try:
        stk_code_dict = nextfuntion()
    except Exception as e:
        print("还是读缓存吧，nextfuntion() error", e)
        # print(stk_code_dict)
        with open(cache_file, "w", encoding="utf-8") as f:
            json.dump(stk_code_dict, f, ensure_ascii=False, indent=4)
            # calc timeout and filter faster to return
            return stk_code_dict
    print("no result")


def 文件很新鲜(
    file,
    interval=1,
):
    """
    检查文件是否很新鲜，如果是，则不需要重新下载

    Returns:
        _type_: _description_
    """
    if os.path.isfile(file):
        now = datetime.now()
        one_hour_ago = now - timedelta(hours=interval)
        mod_time = datetime.fromtimestamp(os.path.getmtime(file))
        if mod_time >= one_hour_ago and mod_time <= now:
            return True
        else:
            return False
    else:
        return False


def baostock获取股票代码表(output_path=None, day=None, filter_list=None, debug=False):
    """
    自动下载股票代码表，并不断更新。
    filter_list为过滤列表，如果不为空，筛选指定市场的代码。['sz.00','sh.30','sh.6'] 也可以['bj.']获取北交所

    """
    debug = True
    bs.login()

    if day is None:
        if debug:
            print("参数day为空，使用lyycalendar获取最近有数据日期,")
        day = instance_lyycalendar.最近有数据日期(debug=True)
        day = datetime.strptime(str(day), "%Y%m%d").strftime("%Y-%m-%d")
        if debug:
            print("参数day为空，使用lyycalendar获取最近有数据日期,day=", day)

    else:
        print("参数day不为空，使用指定日期", day)

    if debug:
        print("in baostock获取股票代码表day=", day)
    rs = bs.query_all_stock(day)

    data_list = []
    while (rs.error_code == "0") & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())

    codes_df = pd.DataFrame(data_list, columns=rs.fields)  #           code tradeStatus code_name    # 397   sh.600000           1      浦发银行    # 398   sh.600004           1      白云机场

    # codes_df.to_csv("all_codes_bs_original.csv", encoding="utf-8", index=False)
    if debug:
        print("原始code行数为：", codes_df.shape[0])
    if filter_list is not None:
        query_txt = " or ".join([f"code.str.contains('{x}')" for x in filter_list])
        if debug:
            print("query=", query_txt)
    else:
        query_txt = 'code.str.contains("sz.00") or code.str.contains("sz.30") or code.str.contains("sh.6")'
    df_bs = codes_df.query(query_txt).copy()
    if output_path is not None:
        df_bs.to_csv(output_path, encoding="utf-8", index=False)

    if debug:
        print("bs获取股票代码表成功,返回长度为：", len(df_bs))

    df_bs.rename(columns={"code_name": "name"}, inplace=True)

    # df_bs["code"]=df_bs["code"].apply(lambda x: x.replace("s","").replace("z","").replace("h","").replace(".",""))
    df_bs.loc[:, "code"] = df_bs["code"].str.extract(r"(\d+)").astype(int)
    if len(df_bs) < 100:
        print("股票代码表小于100，貌似不正确,df_bs=", df_bs)
    return df_bs


def get_market(code):
    code_str = str(code).zfill(6)
    if code_str.startswith("6"):
        market = 1
    elif code_str.startswith("0") or code_str.startswith("3"):
        market = 0
    else:
        market = 2  #
    return market


def get_cache(file, interval=1, nextfuntion=None):
    """
    检查文件是否很新鲜，如果是，则不需要重新下载

    Returns:
        _type_: _description_
    """
    now = datetime.now()
    one_hour_ago = now - timedelta(hours=interval)
    mod_time = datetime.fromtimestamp(os.path.getmtime(file))
    if mod_time >= one_hour_ago and mod_time <= now:
        return True
    else:
        return False


def get_bjs_codes_info_df(debug=False):
    import requests, re, json
    import pandas as pd

    code_lis, name_lis, all_zb_lis, lt_zb_lis, date_lis, ss_lis, dq_lis = [], [], [], [], [], [], []
    url = "https://www.bse.cn/nqxxController/nqxxCnzq.do?callback=jQuery331_1700981144965"
    for pg in range(0, 12):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
        }
        data = {"page": pg, "typejb": "T", "xxfcbj[]": "2", "xxzqdm": "", "sortfield": "xxzqdm", "sorttype": "asc"}
        r = requests.post(url, headers=headers, data=data).text
        data = json.loads(re.findall(r"jQuery\d+_\d+\((.*)\)", r)[0])[0]["content"]
        for ii in data:
            code = ii["xxzqdm"]
            name = ii["xxzqjc"]
            all_zb = round(ii["xxzgb"] / 100000000, 2)
            lt_zb = round(ii["xxfxsgb"] / 100000000, 2)
            date_ss = ii["fxssrq"]
            ss_hy = ii["xxhyzl"]
            dq = ii["xxssdq"]
            code_lis.append(code)
            name_lis.append(name)
            all_zb_lis.append(all_zb)
            lt_zb_lis.append(lt_zb)
            date_lis.append(date_ss)
            ss_lis.append(ss_hy)
            dq_lis.append(dq)

            if debug:
                print(code, name, all_zb, lt_zb, date_ss, ss_hy, dq)

    df = pd.DataFrame({"代码": code_lis, "名称": name_lis, "总股本": all_zb_lis, "流通股本": lt_zb_lis, "上市日期": date_lis, "所属行业": ss_lis, "地区": dq_lis})
    return df


def get_bjs_stkcode_list(source_df=None, debug=False):
    """
    从北交所获取流通股本
    """
    if source_df is None:
        cache_file = "bjs_code_list.csv"
        if 文件很新鲜(cache_file, 24):
            source_df = pd.read_csv(cache_file, encoding="utf-8", index_col=None, dtype=str)
        else:
            source_df = get_bjs_codes_info_df()
            source_df.to_csv(cache_file, index=False, encoding="utf_8_sig")

    newdf = source_df[["代码", "流通股本"]]
    result_dict = {code: liutongguben for code, liutongguben in zip(newdf["代码"], newdf["流通股本"])}
    if debug:
        print("get_bjs_liutongguben_dict, len=", len(result_dict), result_dict)
    return result_dict


def get_bjs_liutongguben_dict(source_df=None, debug=False):
    """
    从北交所获取流通股本
    """
    if source_df is None:
        cache_file = "bjs.csv"
        if 文件很新鲜(cache_file, 24):
            source_df = pd.read_csv(cache_file, encoding="utf-8", index_col=None, dtype=str)
        else:
            source_df = get_bjs_codes_info_df()
            source_df.to_csv(cache_file, index=False, encoding="utf_8_sig")

    newdf = source_df[["代码", "流通股本"]]
    result_dict = {code: liutongguben for code, liutongguben in zip(newdf["代码"], newdf["流通股本"])}
    if debug:
        print("get_bjs_liutongguben_dict, len=", len(result_dict), result_dict)
    return result_dict


def get_流通A股(api, code, debug=False):
    市场代码 = get_market(code)

    def get_info_file_name(company_info_ordered_dict):
        for item in company_info_ordered_dict:
            print("F10ITEM=", item)
            if item.get("name") == "股本结构":
                print("找到股本结构了，item==", item.get("name"))
                file_name = item.get("filename")
                start = item.get("start")
                length = item.get("length")
                print("file_name=", file_name)
                return file_name, start, length
            print("糟糕！找了一圈也没有找到股本相关文件")

    def extract_number(t):
        import re

        number = re.findall(r"\d+\.?\d*", t)
        number = float(number[0])
        number_billion = number / 10000 if "万" in t else number
        return number_billion

    def get_实际流通A股_from_股本结构(guben):
        for i in range(len(guben)):
            if "实际流通A股" in guben[i]:
                print("找到了实际流通A股字段", i, guben[i])
                lt = guben[i]
                lt = [word.strip() for word in lt.split("｜") if len(word) > 1]
                ltz = lt[1]
                ltz_number_billion = extract_number(ltz)
                return ltz_number_billion
            else:
                # print(i,guben[i])
                if i == len(guben):
                    print("字段中找不到实际流通A股，快检查下。")

    company_info_ordered_dict = api.get_company_info_category(市场代码, code)
    print("company_info_ordered_dict=", company_info_ordered_dict)  # result= [OrderedDict([('name', '最新提示'), ('filename', '300288.V11'), ('start', 0), ('length', 14745)]), OrderedDict([('name', '公司概况'), ('filename', '300288.V04'), ('start', 0), ('length', 13398)]), OrderedDict([('name', '财务分析')]

    file_name, start, length = get_info_file_name(company_info_ordered_dict)

    result = api.get_company_info_content(市场代码, code, file_name, start, length)

    if result is None:
        result = api.get_company_info_content(市场代码, code, file_name, 0, 18000000)
        print("result=", result)
        return result

    print("result=", result)
    guben = result.split("\n")
    ltz_number_billion = get_实际流通A股_from_股本结构(guben)

    # print("lt=", lt)#lt= ['流通A股', '6621.9087万', '6094.3979万', '-', '-', '-', '-']
    # print("ltz_number_billion=", ltz_number_billion)  #ltz= 0.66219087
    # print("result=", result[5].split('|')[2])
    return ltz_number_billion


def 获取流通市值(debug=False):

    import tushare as ts

    # 设置你的tushare token
    pro = ts.pro_api(token="2ad5763004f5cab36da48ea691473aa14a6464f2966deb3c24f85169")

    # 获取股票列表
    stock_list = pro.stock_basic(exchange="", list_status="L", fields="ts_code,symbol,name,area,industry,list_date")

    # 选择股票代码，例如：000001.SZ
    stock_code = "000001.SZ"

    # 获取股票的流通市值
    df = pro.daily(ts_code=stock_code)

    circulating_market_cap = df["amount"].iloc[-1]

    if debug:
        print(f"{stock_code}的流通市值为：{circulating_market_cap}")
    return circulating_market_cap


# df_all_info = lyystkcode.get_all_codes_dict_em()
# #序号,代码,名称,最新价,涨跌幅,涨跌额,成交量,成交额,振幅,最高,最低,今开,昨收,量比,换手率,市盈率-动态,市净率,总市值,流通市值,涨速,5分钟涨跌,60日涨跌幅,年初至今涨跌幅

# dict_all_code_name = df_all_info.set_index('代码')['名称'].to_dict()
# dict_all_turn_code = df_all_info.set_index('代码')['流通市值亿'].to_dict()
# dict_all_code_guben = df_all_info.set_index('代码')['流通股本亿'].to_dict()


def 获取所有股票流通市值字典(debug=False):
    # 获取所有 A 股的实时行情数据
    df = get_all_codes_dict_em()
    # 序号,代码,名称,最新价,涨跌幅,涨跌额,成交量,成交额,振幅,最高,最低,今开,昨收,量比,换手率,市盈率-动态,市净率,总市值,流通市值,涨速,5分钟涨跌,60日涨跌幅,年初至今涨跌幅
    # 提取流通市值
    df["流通市值亿"] = df["流通市值"] / 10**8
    # 创建流通市值字典
    circulating_market_cap_dict = df.set_index("代码")["流通市值亿"].to_dict()
    if debug:
        print(circulating_market_cap_dict)
    return circulating_market_cap_dict


def _get_all_codes_dict_em(cache_file, debug=False):
    if debug:
        print("文件不新鲜，从东财获取")
    df_not_clean = ak.stock_zh_a_spot_em()
    df = df_not_clean[~(df_not_clean['流通市值'].isna() | (df_not_clean['流通市值'] == 0))].copy()

    df.dropna(subset="最新价", inplace=True)

    df["流通股本亿"] = (df["流通市值"] / df["最新价"]) / pow(10, 8)
    df["流通市值亿"] = round(df["流通市值"] / pow(10, 8), 2)
    if len(df) > 5000:
        df.to_csv(cache_file, encoding="utf-8", index=False)
    else:
        if verify:
            print("[lyystkcode][get_all_codes_dict_em] error! Stock codes less that 5000. Please check!")
    if debug:
        print("东财df=", df)
    return df


def return_code_type(df, cache_file, filterNew=False, return_format="df"):
    if filterNew == True:
        df = df[df["名称"].str.contains("N") == False]
    if df is None or len(df) < 1000:
        print("get_all_codes_dict_em获取的代码不足1000个。请检查。还不如从缓存读取")
        df = pd.read_csv(cache_file, encoding="utf-8", index_col=False, dtype={"代码": str, "名称": str, "序号": float, "最新价": float, "涨跌幅": float, "涨跌额": float, "成交量": float, "成交额": float, "振幅": float, "最高": float, "最低": float, "今开": float, "昨收": float, "量比": float, "换手率": float, "市盈率-动态": float, "市净率": float, "总市值": float, "流通市值": float, "涨速": float, "5分钟涨跌": float, "60日涨跌幅": float, "年初至今涨跌幅": float})
    if return_format == "df":
        to_return = df
    elif return_format == "dict":
        to_return = df.set_index("代码")["名称"].to_dict()
    elif return_format == "list":
        to_return = df["代码"].to_list()
    print("get_all_codes_dict_em,df=\n", df)
    return to_return

def get_all_codes_dict_em(cache_file="stock_zh_a_spot_em.csv", return_format="df", filterNew=False, interval=12, nextfuntion=None,verify=False, debug=False):
    # 从东财获取所有股票代码表，返回DataFrame或者list
    # filterNew表示是否过滤新股
    debug = True
    df = None
    if os.path.isfile(cache_file):
        current_time = datetime.now().time()
        before_trade_time = datetime_time(8, 50) < current_time < datetime_time(9, 25) #开盘前这段时间最新价为空值。
        if 文件很新鲜(cache_file, 12) or before_trade_time:
            df = pd.read_csv(cache_file, encoding="utf-8", index_col=False, dtype={"代码": str, "名称": str, "序号": float, "最新价": float, "涨跌幅": float, "涨跌额": float, "成交量": float, "成交额": float, "振幅": float, "最高": float, "最低": float, "今开": float, "昨收": float, "量比": float, "换手率": float, "市盈率-动态": float, "市净率": float, "总市值": float, "流通市值": float, "涨速": float, "5分钟涨跌": float, "60日涨跌幅": float, "年初至今涨跌幅": float})
            if debug: print("文件很新鲜，直接读取之")
            return return_code_type(df, cache_file, filterNew=filterNew, return_format=return_format)
    else:
        print("文件不存在。接下来的分支等同于(文件不新鲜且不是开盘前)。")

    df = _get_all_codes_dict_em(cache_file=cache_file, debug=debug)
    return return_code_type(df, cache_file, filterNew=filterNew, return_format=return_format)


def get_code_name_dict():
    df = get_all_codes_dict_em()
    d = df.set_index("代码")["名称"].to_dict()
    if len(d) < 1000:
        raise Exception("get_code_name_dict获取的代码不足1000个。无法继续请检查。")
    return d


if __name__ == "__main__":

    print(get_code_name_dict())

    # df=get_all_codes_dict_em()

    sys.exit()
    circulating_market_cap_dict = 获取所有股票流通市值字典()
    print(circulating_market_cap_dict)
    # 获取流通市值(debug=True)
    sys.exit()
    get_bjs_liutongguben_dict(debug=True)
    # df['liutongguben'] = round(df['总股本(万股)'] / 10000, 2)
    # print(df)

    """
    baostock多一行 tradeStatus，股票代码数量跟tushare一样。可能tushare表示当天能查到的即表示开盘。
    tushare还有些最新的没有股票名字。
    """
    # print(tushare_get_name("600000"))
    # df = baostock获取股票代码表()
    # print("df_bs,len=",len(df))
    # print(df.sample(5))
    # result = all_code_to_mysql(df)
    # print("added line result=",result)

    baostock获取股票代码表("D:\\UserData\\resource\\bs.csv")

    log("tushare获取股票代码表")
    df_tu = tushare_get_all_codes("D:\\UserData\\resource\\tushare.csv")
    log("df_tu,len=" + str(len(df_tu)))
    print(df_tu)

    conn = lyyf_mysql.engine.connect()

    stk_list = df_tu["code"].tolist()
    log("len(stk_list)=" + str(len(stk_list)))
    debug = False

    if debug:
        if "002499" in stk_list:
            print("002499 in stk_list")
        if 2499 in stk_list:
            print("2499 in stk_list")

    if len(df_tu) > 5000:
        delete_all_code(conn, "stock_all_codes", debug=True)

    log("tushare获取的股票代码表存入mysql")
    result = all_code_to_mysql(df_tu)
    log("added line result=", result)

    log("处理空值_公司")
    df = get_codelist_from_mysql(conn)
    # time.sleep(11111111)

    # all_codes_df = bs_ak_full_codes()
    # print("code len = ",all_codes_df.shape[0])
    # 定义函数get_name
