# this script generates thumbnails for the papers on the projects page


# generate_thumbnails.py
import fitz  # pip install pymupdf
import os
import requests

papers = {
    "memory-ali": "https://arxiv.org/pdf/2404.11672",
    "interp-dawar": "https://aclanthology.org/2025.findings-acl.654.pdf",
    "glot-amir": "https://proceedings.neurips.cc/paper_files/paper/2024/file/1e6057620ed314b0020b3a30284b0f83-Paper-Datasets_and_Benchmarks_Track.pdf",
    "agents-hinrich": "https://watermark02.silverchair.com/coli.a.19.pdf?token=AQECAHi208BE49Ooan9kkhW_Ercy7Dm3ZL_9Cf3qfKAc485ysgAAAzAwggMsBgkqhkiG9w0BBwagggMdMIIDGQIBADCCAxIGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMl6CpYNkLXnUpqKivAgEQgIIC46OLabeMxC0oq53Ejl45fRnQq5x86F5npz6yeHqGjZ0lNnkbn2btwGGOyM7fveWJifxMJJ_wp-pmclo-jBEQjEuSRvFtR7gnlN_UgLD_blxulKQ8pKeERUfyL6PB-aZvBFvJ0vkgWZl4Y7jH7oGGSS6copNoiNHRBfzTQqMmVUND2qYxZW5NcAkZQzxqHE8A1aQjU8Cx9feS9SluVEmB-aeG7G_TxOgkbJhKqkc5f_VTYS1RYm82ICJeBqYTblWLlwx4CvLEgbOPa_HbFC_IXhnG_-suGJQe2LTx0toR1M1nyXkwMuNcPPMqr9wECOqm-FD-0ACinZKmCZA9jTwKDCykghfvtTtWemLqCZYTIzwu1W2HLSaCSKr9UHOx8PfsG_XNWLpNNEP9chRrCE1kfMcd0M9wzmm81eEaBiJorVtCaaYOpUJe8bQSoex-zsnvmMie-5c5Fw3Xuo_JT2ZsdXtsEd7wc6ngeE7inStMnl5WPp_IcSmosQnUbt1DlYNhn8G21TafDNmSPYXsCkO6u4KxyFd8U8zbrPlsI5ZOZsASTaR7kwiWljtDyCtOhoV6CfLJLwZOAJCTod_ND1P5naN8rbE-N3uRtcWD0fjaaY3KgxYedthrQWpvRPxy4Jltj1NF1MAXEVrWLQ5DMoP-Pi9gs7H_-SEM0oy-IzrPT718nPW4YHx2V2KOKwcm4f0nsue7VtMY0jX6YJ-9hk_r28rsN18TPGcNVR8tXLdUqQZuJhIiKLbGIE5m9jE0Y56ocYrL1AnKGVDLCN-FL2EaiBztz6Bp02Ug13zoUp_cSuo-hRDawqo6AkYncNQXEvQEqSU7wDo1y097kdCB3MFGM9tW0fxPoCE0_qumvsVwKW3aNGQxADm6W3wFNx0OMUQPxQU8k3yTO-pPgbeztGi5XK-v3x8-VbjnvPbHqZLkhDzHyDsVydUW72TIs9E6KEkij5Z9jeWJhq1whvUniC9ysQAC8G0"
}

os.makedirs("images/paper_thumbnails", exist_ok=True)

for name, url in papers.items():
    r = requests.get(url)
    doc = fitz.open(stream=r.content, filetype="pdf")
    page = doc[0]
    pix = page.get_pixmap(dpi=150)
    pix.save(f"images/paper_thumbnails/{name}.png")
    print(f"Saved {name}.png")