from dknovautils import commons, iprint_debug, iprint_warn, AT  # type:ignore
from dknovautils.commons import *
import socket


class DkNetwork:

    @classmethod
    def http_get_url_simple_str(
        cls,
        url: str,
        encoding: str = "utf-8",
        timeout: float = 5.0,
        verbose: bool = False,
    ) -> str | None:
        """

        https://stackabuse.com/guide-to-sending-http-requests-in-python-with-urllib3/

        """
        _http = urllib3.PoolManager(timeout=timeout)

        try:
            if verbose:
                iprint_debug(f"get url start {url}")
            r = _http.request("GET", url, timeout=timeout, retries=False)
            # print(json.loads(r.data.decode('utf-8')))
            s = r.data.decode(encoding)
            assert isinstance(s, str)
            return s
        except Exception as e:
            iprint_debug(f"err65715 {url} {e}")
            return None
        finally:
            if verbose:
                iprint_debug(f"get url end {url}")

    @classmethod
    def net_check_shutdown(cls, url: str) -> None:
        """如果url不可正常访问 则马上向本机发出关机指令

        root crontab
            每1,2,3分钟执行一次

            python3.10 -c "from dknovautils import *; DkNetwork.net_check_shutdown('http://192.168.0.1')"

        不要指向外部网站,否则,公网断网则服务器关闭,另外,可能被外网屏蔽,从而无法正常工作.
        可以考虑指向路由器. 如果路由器重启 或者暂时维护,可能会造成服务器关闭. 当然,这个比指向外部网站会好一些.毕竟这个是可控的.



        """
        r = cls.http_get_url_simple_str(url)
        if not r:
            iprint_warn("warn74542 shutdown the system")
            if AT.iswindows:
                os.system("shutdown /s /t 1")
            elif AT.islinux:
                os.system("shutdown -P now")
            else:
                iprint_warn("err65985 unsupported os")

        """

        https://geekdaxue.co/read/lwmacct@linux/shutdown
        https://www.geeksforgeeks.org/python-script-to-shutdown-computer/        

        windows 
        os.system("shutdown /s /t 1")

        linux
        os.system("shutdown -P now")

        """


http_get_url_simple_str = DkNetwork.http_get_url_simple_str


def f_test_http_get_url_simple_str() -> None:
    url = "https://www.baidu.com/"
    r = http_get_url_simple_str(url)
    assert r and len(r) > 10

    url = "http://www.baidu.com/"
    r = http_get_url_simple_str(url)
    assert r and len(r) > 10

    url = "http://192.168.0.1/"
    r = http_get_url_simple_str(url)
    print(r)
    assert r and len(r) > 10

    url = "http://192.168.0.2/"
    r = http_get_url_simple_str(url, verbose=True)
    print(r)
    assert r is None

    print("test end")


def http_scan_urls(
    urls: List[str], *, limit: int = 200, timeout: float = 5.0
) -> List[str]:
    """
    顺序返回能正常获取内容的url list。
    limit是限制打印的对应的值的文本长度。没有多大作用。
    实现中是多线程访问网络。

    """
    # port = 9310
    # urls = [f"http://192.168.0.{i}:{port}" for i in range(1, 256)]

    ma = {}

    def fa(url: str) -> None:
        ma[url] = None
        rs = http_get_url_simple_str(url, timeout=timeout)
        ma[url] = rs

    ths = [threading.Thread(target=fa, args=(url,)) for url in urls]

    for t in ths:
        t.start()

    for t in ths:
        t.join()

    ks = list((u, ma[u].strip()[:limit]) for u in ma if ma[u])
    PRE = "*" * 20
    iprint(f"{PRE} f_scan_url good {PRE}")
    for k, v in ks:
        iprint(f"{k} {v}")

    return [k for k, v in ks]


def is_port_open(dst: str, port: int, desc: str = "", timeout: int = 5) -> bool:
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # set a timeout of 1 second
    s.settimeout(timeout)
    try:
        # try to connect to the port
        s.connect((dst, port))
        # port is open
        # iprint(f"Port {port} is open")
        return True
    except:
        # port is closed
        # iprint(f"Port {port} is closed")
        return False
    finally:
        # always close the socket
        s.close()
