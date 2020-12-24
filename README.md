# Automated-Season-shopper-using-selenium
<strong>With Pylint Rating 10/10</strong>
<hr>
This Automated season shopper project takes you through complete shopping from opening the window to the payment with the help of selenium and python.
<br><strong>Key points according to which This project works</strong>
<ul>
 <li> It uses the test website: https://weathershopper.pythonanywhere.com/ </li>
  <li> At first it choosed the temperature according to which it will go to the season whether it needs Moisturizers or sunscreens </li>
  <li> At sunscreens it will take least priced SPF-50 and SPF-30 products</li>
   <li> At Moisturizers it will take least priced ALOE and ALMOND products</li>
   <li> It will go to payment cart and fills dummy account details and clicks over pay which will endup with a page showing payment successfull</li>
 </ul>
 <br><strong> Tips to use</strong>
 <ul>
   <li> Install selenium into your system<br>
    <pre>pip3 install selenium</pre</li>
   <li> Install webdriver with the steps below<br>
   provide executable permission to driver_installer<br>
   <pre>chmod -x driver_installer.sh</pre><br>
   execute the driver_installer<br>
   <pre>./driver_installer.sh</pre></li> 
   <li> If you have firefox browser then it's ok, if you have any other browser like chrome just change the line "browser = webdriver.Firefox()" in app.py with your browses compati    ble line like for chrome its "browser = webdriver.Chrome()"</li>
   <li> execute the app.py<br>
     <pre>python3 app.py</pre></li>
 </ul>
 <hr><hr>
 Thank you

