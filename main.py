    import time
    import sqlite3
    import requests #this will get the website source code
    import selectorlib #this library helps to extract only particular information from the source code
    import smtplib,ssl

    connection= sqlite3.connect("data.db")

    URL="http://programmer100.pythonanywhere.com/tours/"

    def scrape(url):
        response= requests.get(url)
        source=response.text
        return source


    def extract(source):
        extractor=selectorlib.Extractor.from_yaml_file("extract.yaml")
        value=extractor.extract(source)["tours"]
        return value

    def send_mail(message):
        host="smtp.gmail.com"
        port=465
        username=""
        password=""
        receiver=""
        context=ssl.create_default_context()
        with smtplib.SMTP_SSL(host,port,context=context) as server:
            server.login(username,password)
            server.sendmail(username,receiver,message)

        print("Email was sent !")

    def store(extracted):
        row=extracted.split(",")
        row=[item.strip() for item in row]
        cursor= connection.cursor()
        cursor.execute("INSERT INTO events VALUES(?,?,?)",row)
        connection.commit()

    def read(extracted):
        row=extracted.split(",")
        row=[item.strip()for item in row]
        band, city, date=row
        cursor=connection.cursor()
        cursor.execute("SELECT * FROM events WHERE band=?AND city=? AND date=?",(band, city, date))
        rows=cursor.fetchall()
        print(rows)
        return rows


    if __name__=="__main__":
        while True:
            scraped=scrape(URL)
            extracted=extract(scraped)
            print(extracted)


            if extracted != "No upcoming tours":
                row = read(extracted)
                if not row:
                    store(extracted)
                    send_mail(extracted)
            time.sleep(2)

