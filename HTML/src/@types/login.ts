// program
const puppeteer = require ('puppeteer-extra');
const fs = require('fs');
const cookiesPath = "HTML/src/@types/cookies/cookies.txt";
const StealthPlugin = require('puppeteer-extra-plugin-stealth');
puppeteer.use(StealthPlugin());


puppeteer.launch({ headless: true }).then(async (profile) => {
  const ACCESS = ['iago.develop', 'pasteldefrango'];
  const url = 'https://www.instagram.com/accounts/login/'
  // const cookie = [{
  //   name: 'IAGO_dev',
  //   value: 'iago.develop',
  //   domain: '.instagram.com',
  //   httpOnly: true,
  //   secure: true,
  // },
  // {
  //   name: 'IAGO_dev2',
  //   value: 'iago.develop',
  //   domain: '.instagram.com',
  //   httpOnly: true,
  //   secure: true,
  // }
  // ]

  const proxies = {
    'session_1': 'http://185.126.200.167:3128',
    'session_2': 'http://116.228.227.211:443',
    'session_3': 'http://185.126.200.152:3128',
    'session_4': 'http://103.161.164.109:8181',
    'session_5': 'http://206.253.164.110:80',
    'session_6': 'http://139.99.237.62:80',
    'session_7': 'http://190.26.201.194:8080',
    'session_8': 'http://185.255.46.121:8080',
    'session_9': 'http://164.70.119.208:3128',
    'session_10': 'http://223.29.214.6:80',
    //     https://freeproxylists.net/
    
  };

  const server = new ProxyChain.Server({
    port: 8080,
    prepareRequestFunction: ({ request }) => {
        // At this point of code we should decide what proxy
        // to use from the proxies list.
        // You can chain your browser requests by header 'session-id'
        // or just pick a random proxy from the list
        const sessionId = request.headers['session-id'];
        const proxy = proxies[sessionId];
        return { upstreamProxyUrl: proxy };
    }
  });

  const chromeOptions = {
    headless: false, 
    slowMo: 10,
    defaultViewport: null,
    args: [
      "--no-sandbox", 
      "--disable-setuid-sandbox",
      "--proxy-server=http://103.161.164.109:8181"
    ],
  };
 
  
  const browser = await puppeteer.launch(chromeOptions)
  const page = await browser.newPage();
  await page.authenticate({
    username: ACCESS[0],
    password: ACCESS[1]
});
  const userAgent =
   "Mozilla/5.0 (X11; Linux x86_64)" +
   "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.39 Safari/537.36";
  await page.setUserAgent(userAgent);
  
    // If the cookies file exists, read the cookies.
  const previousSession = fs.existsSync(cookiesPath)
  if (previousSession) {
    const content = fs.readFileSync(cookiesPath, 'utf8');
    const cookiesArr = JSON.parse(content);
    if (cookiesArr.length !== 0) {
      for (let cookie of cookiesArr) {
        await page.setCookie(... cookie)
      }
      console.log('Cookie has been loaded in the browser')
    }
  }

  await page.goto(url,  { waitUntil: "networkidle0" });
  //await page.waitFor(2500)

    // Write Cookies
  const cookiesObject = await page.cookies()
  fs.writeFileSync(cookiesPath, JSON.stringify(cookiesObject));
  console.log('Session has been saved to ' + cookiesPath);
    
  try{ 
    const entrar = page.waitForSelector('button.sqdOP.L3NKy.y3zKF')
    await page.click(entrar)
    await page.click(`input[type="text"]`); // Da um click falso no input de login
    await page.keyboard.type(ACCESS[0]); // digita uma string no input
    await page.click('input[type="password"]'); //Da um click falso no input de sennha
    await page.keyboard.type(ACCESS[1]); // digita uma string no input
    await page.click(".L3NKy");
    //await page.waitFor(2500);
    await page.click("button.aOOlW");
    await page.click("nav a._2dbep.qNELH.kIKUG");
    await page.waitForNavigation();
    

    // Get cookies
    const cookies = await page.cookies();
    console.log(JSON.stringify(cookies))
  
    // Use cookies in other tab or browser
    const page2 = await browser.newPage();
    await page2.goto('https://instagram.com/');
    // await page2.setCookie(... cookie);//aqui temos os cookies que estão comentados no topo da página
    const cookiesString = await fs.readFile('./cookies/cookies.json');
    const cookieless = JSON.parse(cookiesString);
    await page.setCookie(...cookieless);
  } catch (e) {
      await page.click(`input[type="text"]`); // Da um click falso no input de login
      await page.keyboard.type(ACCESS[0]); // digita uma string no input
      await page.click('input[type="password"]'); //Da um click falso no input de sennha
      await page.keyboard.type(ACCESS[1]); // digita uma string no input
      await page.click(".L3NKy"); // click no Login
      // const cookies = await page.cookies();
      // await fs.writeFile('./cookies/cookies.json', JSON.stringify(cookies, null, 2));
      // console.log(JSON.stringify(cookies))
      //await page.waitForXPath('//*[@id="react-root"]/section/main/div/div/div/section/div/button');
      await page.click('//*[@id="react-root"]/section/main/div/div/div/section/div/button');
    
      // Get cookies
    
      // await page.click("button .sqdOP.L3NKy.y3zKF");
      //await page.click("nav a._2dbep.qNELH.kIKUG");
      await page.waitForNavigation();
      
      // Use cookies in other tab or browser
      const page2 = await browser.newPage();
      await page2.goto('https://instagram.com/'); // Opens page as logged user
      const cookiesString = await fs.readFile('./cookies/cookies.json');
      const cookieless = JSON.parse(cookiesString);
      await page.setCookie(...cookieless);

      await browser.close();
      console.log(e)  
    } finally {
    let data = await page.evaluate(() => {
      const name = document.querySelector('.Yk1V7').textContent;
      const bio = document.querySelector('.QGPIr')
      const category = document.querySelector('._829vi');
      const description = document.querySelector('.QGPIr span')
      const link = document.querySelector('.heKAw')
      const infos = document.querySelectorAll(".g47SY"); 
      const posts = infos[0].textContent;
      const followers = infos[1].textContent;
      const following = infos[2].textContent;
      return {
        name,
        category,
        description,
        link,
        bio,
        posts,
        followers,
        following,
      }    
    });
  console.log(data)
  }




      console.log('Done.');
})('jadepicon');

//     /* 
//     https://freeproxylists.net/
    
//     103.161.164.109   8181
//     206.253.164.110   80
//     139.99.237.62     80
//     190.26.201.194    8080
//     185.255.46.121    8080
//     164.70.119.208    3128
//     223.29.214.6      80
    
//     */