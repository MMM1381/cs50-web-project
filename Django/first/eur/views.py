from django.shortcuts import render
import yfinance as yf

# Create your views here.
def index(request):
    data = yf.download(tickers='EURUSD=X', period='max', interval='1d')
    close=data["Close"].iloc[0].item()
    open=data["Open"].iloc[0].item()
    high=data["High"].iloc[0].item()
    low=data["Low"].iloc[0].item()
    return render(request,"eur\price.html",{
        "Open":open,
        "High":high,
        "Low":low,
        "Close":close,
        "ok":open<close
    })