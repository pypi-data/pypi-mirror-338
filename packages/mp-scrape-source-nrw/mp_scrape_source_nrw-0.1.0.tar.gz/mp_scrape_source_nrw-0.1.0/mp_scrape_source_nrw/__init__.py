# SPDX-FileCopyrightText: 2025 Sofía Aritz <sofiaritz@fsfe.org>
#
# SPDX-License-Identifier: AGPL-3.0-only

from mp_scrape_core import DataSource, ModuleDescription, ModuleArgument, ModuleDefinition, ModuleMaintainer
from playwright.async_api import async_playwright
import pandas as pd

import subprocess
import logging

class NRWSource(DataSource):
    def __init__(self, display_browser: bool = False, url: str = "https://www.landtag.nrw.de/home/der-landtag/abgeordnete-und--fraktionen/die-abgeordneten/abgeordnetensuche/liste-aller-abgeordneten.html", retrieve_emails: bool = True):
        """
        Retrieve the information of members from the Nordrhein-Westfalen parliament

        :param bool display_browser: (Display browser) When enabled, a browser window is opened displaying the actions being performed.
        :param str url: (URL) URL from where the data is extracted.
        :param bool retrieve_emails: (Retrieve e-mails) When enabled, e-mails will be retrieved. This takes a long time.
        """
        self.display_browser = display_browser
        self.url = url
        self.retrieve_emails = retrieve_emails

    @staticmethod
    def metadata() -> ModuleDefinition:
        return ModuleDefinition({
            "name": "Nordrhein-Westfalen",
            "identifier": "nrw",
            "description": ModuleDescription.from_init(NRWSource.__init__),
            "arguments": ModuleArgument.list_from_init(NRWSource.__init__),
            "maintainers": [
                ModuleMaintainer({
                    "name": "Free Software Foundation Europe",
                    "email": "mp-scrape@fsfe.org"
                }),
                ModuleMaintainer({
                    "name": "Sofía Aritz",
                    "email": "sofiaritz@fsfe.org"
                }),
            ],
        })
    
    def _extract_title_and_surname(self, val:str):
        surname_parts = val.split(" ")
        title = " ".join([x for x in surname_parts if x.strip().endswith(".") is True])
        surname = " ".join([x for x in surname_parts if x.strip().endswith(".") is False])

        return (title, surname)
    
    async def fetch_data(self, logger: logging.Logger) -> pd.DataFrame:
        logger.warn("installing playwright browsers, if this fails try to run 'playwright install firefox --with-deps'")
        subprocess.run(["playwright", "install", "firefox"])

        async with async_playwright() as p:
            browser = await p.firefox.launch(headless=self.display_browser is False)

            page = await browser.new_page()
            await page.goto(self.url)
            await page.wait_for_load_state()

            member_data = await page.evaluate("""() => {
                const members = Array.from(document.getElementsByTagName("tr"))
                members.shift() // Skip table head

                return members.map(member => {
                    let member_url = member.children[0].children[0]
                    
                    let pm_url = member_url.href
                    let surname = member_url.innerText.split(",")[0].trim()
                    let name = member_url.innerText.split(",")[1].trim()

                    let party = member.children[1].children[0].innerText
                
                    return { pm_url, name, surname, party }
                });
            }""")

            members = pd.DataFrame()
            if self.retrieve_emails is False:
                for member in member_data:
                    title, surname = self._extract_title_and_surname(member["surname"])

                    # FIXME(sofiaritz): Improve
                    df = pd.DataFrame.from_dict({
                        "Title": [title],
                        "Surname": [surname],
                        "Name": [member["name"]],
                        "Party": [member["party"]],
                    }, orient='index').transpose()
                    
                    members = pd.concat([members, df], ignore_index=True, sort=False)   
            else:
                for member in member_data:
                    # FIXME(sofiaritz): Add as param and improve
                    await page.wait_for_timeout(700)
                    await page.goto(member["pm_url"])
                    await page.wait_for_load_state()

                    member_email = await page.evaluate("""() => {
                        return Array.from(document.getElementsByTagName("a"))
                            .filter((link) => link.href.startsWith("mailto:") && link.href.endsWith("landtag.nrw.de"))[0]
                            .href
                            .replace("mailto:", "")
                            .trim()
                    }""")

                    title, surname = self._extract_title_and_surname(member["surname"])

                    # FIXME(sofiaritz): Improve
                    df = pd.DataFrame.from_dict({
                        "Title": [title],
                        "Surname": [surname],
                        "Name": [member["name"]],
                        "Party": [member["party"]],
                        "Email": [member_email],
                    }, orient='index').transpose()
                    
                    members = pd.concat([members, df], ignore_index=True, sort=False)

        return members