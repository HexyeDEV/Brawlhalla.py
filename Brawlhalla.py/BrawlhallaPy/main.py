import requests

class Brawlhalla:

    def get_ranking(bracket, region, player_name) -> list:
        """
        Get the ranking of a player in a specific region and bracket.
        :param bracket: The bracket to get the ranking for.
        :param region: The region to get the ranking for.
        :param player_name: The name of the player to get the ranking for.
        """
        if region == "Global":
            r = requests.get(f"https://www.brawlhalla.com/rankings/{bracket}?p={player_name}")
            html = r.text
            if "pnameleft" in html and html.count("pnameleft") == 3:
                html = html.split("<tr class=\"odd\">")[1].split("</tr>")[0]
                html = html.split("</td>")
                rank = html[1].replace("<td class=\"pcenter\">", "").replace("</td>", "")
                name = html[3].replace("<td class=\"pnameleft\" colspan=\"2\">", "").replace("</td>", "")
                win_loss = html[5].replace("<td class=\"pcenter\">", "").replace("</td>", "")
                seasonrating = html[6].replace("<td class=\"pcenter\">", "").replace("</td>", "")
                peakrating = html[7].replace("<td class=\"pcenter\">", "").replace("</td>", "")
                return [name, rank, win_loss, seasonrating, peakrating]
            else:
                raise Exception("No player found or found more than one player with that name or the player is not in the leaderboard.")
        else:
            r = requests.get(f"https://www.brawlhalla.com/rankings/{bracket}/{region}?p={player_name}")
            html = r.text
            if "pnameleft" in html and html.count("pnameleft") == 3:
                html = html.split("<tr class=\"odd\">")[1].split("</tr>")[0]
                html = html.split("\n")
                rank = html[1].replace("<td class=\"pcenter\">", "").replace("</td>", "")
                name = html[3].replace("<td class=\"pnameleft\" colspan=\"2\">", "").replace("</td>", "")
                win_loss = html[5].replace("<td class=\"pcenter\">", "").replace("</td>", "")
                seasonrating = html[6].replace("<td class=\"pcenter\">", "").replace("</td>", "")
                peakrating = html[7].replace("<td class=\"pcenter\">", "").replace("</td>", "")
                return [name, rank, win_loss, seasonrating, peakrating]
            else:
                raise Exception("No player found or found more than one player with that name or the player is not in the leaderboard.")