import yfinance as yf
import smtplib
import time

# --- Configuration ---
STOCK_SYMBOL = "AAPL"  # Apple ka stock price check karenge
THRESHOLD_PRICE = 180  # Agar price 180 se neeche gaya toh alert
CHECK_INTERVAL = 60  # Har 60 seconds baad check karega

# Email Configuration
EMAIL_ADDRESS = "your-email@gmail.com"  # Yahan apni email daalo
EMAIL_PASSWORD = "your-email-password"  # App password use karo
RECEIVER_EMAIL = "receiver-email@gmail.com"  # Jisko alert bhejna hai

# --- Function to send email ---
def send_email(price):
    subject = f"Stock Alert: {STOCK_SYMBOL} Price Alert!"
    body = f"The stock price of {STOCK_SYMBOL} has dropped to ${price}!"
    message = f"Subject: {subject}\n\n{body}"
    
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, RECEIVER_EMAIL, message)
    
    print("✅ Alert Email Sent!")

# --- Main Loop ---
while True:
    stock = yf.Ticker(STOCK_SYMBOL)
    current_price = stock.history(period="1d")['Close'].iloc[-1]
    print(f"Current Price of {STOCK_SYMBOL}: ${current_price}")
    
    if current_price < THRESHOLD_PRICE:
        send_email(current_price)
    
    time.sleep(CHECK_INTERVAL)  # Wait before checking again
