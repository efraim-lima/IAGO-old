// program
const puppeteer = require ('puppeteer');

(async () => {
  const url = 'https://instagram.com/jadepicon'
  const browser = await puppeteer.launch({
    headless: false,
    args: ['--no-sandbox']
  })
  const page = await browser.newPage();
  await page.goto(url,  { waitUntil: "networkidle0" });
  await page.waitFor(2500)
  
  try{
    const REQUIRED_ARGS = ['iago.develop', 'pasteldefrango'];
      
    await page.click(`input[type="text"]`); // Da um click falso no input de login
    await page.keyboard.type(REQUIRED_ARGS[0]); // digita uma string no input
    await page.click('input[type="password"]'); //Da um click falso no input de sennha
    await page.keyboard.type(REQUIRED_ARGS[1]); // digita uma string no input
    
    await page.click(".L3NKy");
    await page.waitFor(2500);
    await page.click("button.aOOlW");
    await page.click("nav a._2dbep.qNELH.kIKUG");
    await page.waitForNavigation();

    let data = await page.evaluate(() => {
      const infos = document.querySelectorAll(".g47SY"); 
      const posts = infos[0].textContent;
      const followers = infos[1].textContent;
      const following = infos[2].textContent;
      return {
          posts,
          followers,
          following,
        };
      });
      console.log(data)


      // Get cookies
      const cookies = await page.cookies();
      console.log(JSON.stringify(cookies))

      // Use cookies in other tab or browser
      const page2 = await browser.newPage();
      await page2.setCookie(...cookies);
      await page2.goto('https://instagram.com'); // Opens page as logged user

      await browser.close();} catch(e) {
        if (e instance of TypeError) {
          console.log(e)
        }
    finally{
      
    }

      console.log('Done.');
})();