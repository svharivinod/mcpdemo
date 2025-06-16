const { chromium } = require('playwright');

module.exports = async function (input) {
  const query = input?.text || "AI tools 2025";

  const browser = await chromium.launch();
  const page = await browser.newPage();

  await page.goto(`https://www.google.com/search?q=${encodeURIComponent(query)}`);

  const results = await page.$$eval('div.g', items =>
    items.slice(0, 5).map(item => {
      const title = item.querySelector('h3')?.innerText || '';
      const link = item.querySelector('a')?.href || '';
      return title && link ? `${title}\n${link}` : null;
    }).filter(Boolean)
  );

  await browser.close();

  return results.length
    ? results.join('\n\n')
    : "No search results found.";
};
