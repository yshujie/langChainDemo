from src.demo import fetch_web

def test_fetch_web():
    fetch_web.fetch_web("https://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CorpInfo/stockid/600519.phtml")
    
if __name__ == "__main__":
    test_fetch_web()