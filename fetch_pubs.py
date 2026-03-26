# fetch_pubs.py
import json
from scholarly import scholarly, ProxyGenerator # version 1.4 of scholarly -> has to be this one for the proxies to work

SCHOLAR_ID = "qIL9dWUAAAAJ"  # hinrich's google scholar id
MAX_PUBS = 20

pg = ProxyGenerator()
pg.FreeProxies()
scholarly.use_proxy(pg)


author = scholarly.search_author_id(SCHOLAR_ID)
scholarly.fill(author, sections=["publications"])

# Sort by year descending, then take the most recent 20
sorted_pubs = sorted(
    author["publications"],
    key=lambda p: int(p.get("bib", {}).get("pub_year", 0) or 0),
    reverse=True
)

pubs = []
for pub in sorted_pubs:
    if len(pubs) >= MAX_PUBS:
        break
    scholarly.fill(pub)
    bib = pub.get("bib", {})
    venue = (
        bib.get("venue")
        or bib.get("journal")
        or bib.get("booktitle")      # inproceedings / conference papers
        or bib.get("conference")
        or bib.get("publisher")      # books / book chapters
        or ""
         "") 
    
    # Skip arxiv publications
    if "arxiv" in venue.lower():
        continue

    pubs.append({
        "title": bib.get("title", ""),
        "authors": bib.get("author", ""),
        "year": bib.get("pub_year", ""),
        "proceedings": venue,
        "pdf": pub.get("eprint_url", ""),
        "url": pub.get("pub_url", ""),
        "bib": "",
    })
with open("_data/publist.json", "w") as f:
    json.dump(pubs, f, indent=2)

print(f"Saved {len(pubs)} publications to _data/publist.json")