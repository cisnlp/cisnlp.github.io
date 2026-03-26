---
title: "Schütze Lab - Projects"
layout: textlay
excerpt: "Schütze Lab -- Projects"
sitemap: false
permalink: /projects/

---

# Projects

---

Our primary focus is linguistically-informed Neural Natural Language Processing. Towards that end, we are working on various funded projects, as described below. 

<div markdown='0' class="topic-block">
  <div class="topic-text">
    <h3>Memory</h3>
    <p>The main mechanisms that are currently used for memory in LLMs — the model parameters, long context and RAG — all have drawbacks. In comparison, the memory systems of biological systems, including humans, are much more powerful. We are interested in creating memories that support continuous updating, yet are fully integrated into the main model.</p>
  </div>

  <div class="paper-card">
    <div class="paper-thumb-crop">
      <img src="{{ site.baseurl }}/images/paper_thumbnails/memory-ali.png" />
    </div>
    <a href="https://arxiv.org/pdf/2404.11672" target="_blank">📄 View Paper</a>
  </div>
</div>


<div markdown='0' class="topic-block">
  <div class="topic-text">
    <h3>Interpretability</h3>
    <p>We currently have only a limited understanding of how LLMs work — they still largely are black boxes. To improve interpretability is important for safety, for high-stakes applications like medicine and as a basis for high-quality deep learning research, which is currently difficult given our reliance on heuristics and trial and error. We are working on models of the internal mechanisms of LLMs for phenomena like bias and factual knowledge, with particular focus on how these emerge during training.</p>
  </div>

  <div class="paper-card">
    <div class="paper-thumb-crop">
      <img src="{{ site.baseurl }}/images/paper_thumbnails/interp-dawar.png" />
    </div>
    <a href="https://aclanthology.org/2025.findings-acl.654.pdf" target="_blank">📄 View Paper</a>
  </div>
</div>

<div markdown='0' class="topic-block">
  <div class="topic-text">
    <h3>Multilinguality</h3>
    <p>Current AI models have impressive performance for high-resource languages like English and Chinese, but there are thousands of low-resource languages that they perform poorly on due to lack of training data. To keep these low-resource languages alive, it is essential that AI understands and speaks them.  We were the first to train language models with a broad coverage of several 100s of low-resource languages, we created GlotLID, one of the leading packages for language identification (a crucial part of multilingual infrastructure) and are working on elucidating the mechanisms and representations in LLMs that link words and meanings across languages.</p>
  </div>

  <div class="paper-card">
    <div class="paper-thumb-crop">
      <img src="{{ site.baseurl }}/images/paper_thumbnails/glot-amir.png" />
    </div>
    <a href="https://proceedings.neurips.cc/paper_files/paper/2024/file/1e6057620ed314b0020b3a30284b0f83-Paper-Datasets_and_Benchmarks_Track.pdf" target="_blank">📄 View Paper</a>
  </div>
</div>

<div markdown='0' class="topic-block">
  <div class="topic-text">
    <h3>Agents</h3>
    <p>Many researchers see the ultimate goal of AI research as developing autonomous agents that independently work on tasks for long periods of time and then deliver a finished product to their human (or agentic) manager. In contrast, we believe that human-AI collaboration should instead be collaborative, at least for a large subset of sensitive domains such health, jurisprudence and cybersecurity. One reason is that alignment to human values is imperfect, especially for long periods of sequential decision making. Another reason is that in many cases only the human has full understanding of the real-world context, which necessitates that the human guides the agent as it solves tasks. We have developed the HAI-CO2 framework to realize this vision of human-AI collaboration and are currently developing it for cybersecurity applications.</p>
  </div>

  <div class="paper-card">
    <div class="paper-thumb-crop">
      <img src="{{ site.baseurl }}/images/paper_thumbnails/agents-hinrich.png" />
    </div>
    <a href="https://watermark02.silverchair.com/coli.a.19.pdf?token=AQECAHi208BE49Ooan9kkhW_Ercy7Dm3ZL_9Cf3qfKAc485ysgAAAzAwggMsBgkqhkiG9w0BBwagggMdMIIDGQIBADCCAxIGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMl6CpYNkLXnUpqKivAgEQgIIC46OLabeMxC0oq53Ejl45fRnQq5x86F5npz6yeHqGjZ0lNnkbn2btwGGOyM7fveWJifxMJJ_wp-pmclo-jBEQjEuSRvFtR7gnlN_UgLD_blxulKQ8pKeERUfyL6PB-aZvBFvJ0vkgWZl4Y7jH7oGGSS6copNoiNHRBfzTQqMmVUND2qYxZW5NcAkZQzxqHE8A1aQjU8Cx9feS9SluVEmB-aeG7G_TxOgkbJhKqkc5f_VTYS1RYm82ICJeBqYTblWLlwx4CvLEgbOPa_HbFC_IXhnG_-suGJQe2LTx0toR1M1nyXkwMuNcPPMqr9wECOqm-FD-0ACinZKmCZA9jTwKDCykghfvtTtWemLqCZYTIzwu1W2HLSaCSKr9UHOx8PfsG_XNWLpNNEP9chRrCE1kfMcd0M9wzmm81eEaBiJorVtCaaYOpUJe8bQSoex-zsnvmMie-5c5Fw3Xuo_JT2ZsdXtsEd7wc6ngeE7inStMnl5WPp_IcSmosQnUbt1DlYNhn8G21TafDNmSPYXsCkO6u4KxyFd8U8zbrPlsI5ZOZsASTaR7kwiWljtDyCtOhoV6CfLJLwZOAJCTod_ND1P5naN8rbE-N3uRtcWD0fjaaY3KgxYedthrQWpvRPxy4Jltj1NF1MAXEVrWLQ5DMoP-Pi9gs7H_-SEM0oy-IzrPT718nPW4YHx2V2KOKwcm4f0nsue7VtMY0jX6YJ-9hk_r28rsN18TPGcNVR8tXLdUqQZuJhIiKLbGIE5m9jE0Y56ocYrL1AnKGVDLCN-FL2EaiBztz6Bp02Ug13zoUp_cSuo-hRDawqo6AkYncNQXEvQEqSU7wDo1y097kdCB3MFGM9tW0fxPoCE0_qumvsVwKW3aNGQxADm6W3wFNx0OMUQPxQU8k3yTO-pPgbeztGi5XK-v3x8-VbjnvPbHqZLkhDzHyDsVydUW72TIs9E6KEkij5Z9jeWJhq1whvUniC9ysQAC8G0" target="_blank">📄 View Paper</a>
  </div>
</div>
