---
type: raw
source_type: article
source_url: https://lucumr.pocoo.org/2026/4/28/before-github/
date_ingested: 2026-04-29
batch: morning
tags: [#coding, #business]
status: processed
processed_date: 2026-05-01
approved_by: julius
---
# Before GitHub
## Armin Ronacher

**Link gốc:** https://lucumr.pocoo.org/2026/4/28/before-github/
**Published:** 2026-04-28
**Author:** Armin Ronacher (creator của Pocoo, Flask, Jinja2, v.v.)

---

## Tóm tắt

Armin Ronacher — người đã sống qua era trước GitHub — chia sẻ suy nghĩ về sự thay đổi của Open Source từ "small world có reputation và trust" sang "frictionless publishing nhưng kèm micro-dependency problem". Ông lo ngại GitHub đang suy yếu và đặt câu hỏi: điều gì sẽ xảy ra với lịch sử Open Source khi central platform này không còn là default home nữa?

---

## Thế giới trước GitHub

### Open Source là "smaller world"
- Số lượng projects có thể depend on realistic hơn nhiều
- **Reputation mattered trực tiếp** — bạn biết maintainers, mailing lists, ai đã around nhiều năm
- Dependency không chỉ là package name, mà là project với history, website, maintainer, release process, community
- Không add dependencies casually — phải understand where it came from

### Self-hosted infrastructure là norm
- Developer tự run Trac, Subversion repositories, tarballs, documentation
- Nhiều người vừa là developer vừa là system administrator
- Pocoo collective (Georg + Armin) run server riêng: shared Subversion, Trac, mailing lists

### Subversion made "running your own forge" natural
- Centralized: cần server, ai đó operate nó
- Project có home literal: hostname, directory, Trac instance, mailing list archive

### Irony của DVCS
- Git và Mercurial distributed — ai cũng có full repository
- Lẽ ra giảm need for a single center
- **Nhưng GitHub trở thành center mới** — distributed version control system thắng rồi centralized service thắng

---

## Những gì GitHub cho chúng ta

### Quà tặng cho Open Source
- Tạo project và discover project dễ dàng
- Contributing accessible với people chưa bao giờ subscribe mailing list
- Issue trackers, pull requests, release pages, wikis, API access, webhooks, CI
- **Normalized: Open Source happens in the open, with visible history and collaboration**

### GitHub as Library
- GitHub trở thành **library và index** của software commons
- Abandoned projects vẫn findable — forks, old issues, old discussions đều online
- Ngay cả các nước bị sanction (Iran), GitHub vẫn giữ available vì leadership cũ quan tâm

**Đối chiếu:** PyPI vẫn có metadata của project cũ nhưng actual packages đã gone — server ngừng serve. Đó là normal trước large platforms.

---

## npm và Dependency Explosion

### Micro-dependency problem
- GitHub + npm tạo cảm giác **không có cost** để create, publish, discover, install, depend on small packages
- Pre-GitHub: reputation và longevity là part of dependency selection by necessity, often required vendoring
- With npm-style ecosystems: package graph grows faster than anybody's ability to reason about it

### Trust system xung quanh GitHub
- Khi depend on tiny package → muốn see repository → maintainer exists? → issues? → recent changes? → other projects use it? → code is what it claims?
- GitHub became part of the trust system
- **When trust in GitHub erodes → affects whole supply chain culture**

---

## GitHub đang dying

### GitHub đang mất đi những gì làm nó "feel inevitable"
- instability
- product churn
- Copilot AI noise
- unclear leadership
- feeling platform không còn designed for community đã make it valuable

### Leadership vacuum
- "The site has no leadership! It's a miracle that things are going as well as they are."
- Agentic coding revolution tạo enormous pressure

### Examples of people leaving
- **Ghostty** (Mitchell Hashimoto) → moving away from GitHub
- **Strudel** → moved to Codeberg
- **Tenacity** → moved to Codeberg

### Nhưng có thể đây là điều tốt
- Healthy cho Open Source stop pretending một company nên là default home of everything
- Git designed for a world with many homes

---

## Cost của Dispersion

### Going back to many forges
- Tăng decentralization, restore autonomy
- Less dependent on whims of Microsoft leadership
- Different communities choose different workflows

### Nhưng có thể làm web forget again
- Code distributed in theory, social context often not
- Issues, reviews, design discussions, release notes, security advisories, old tarballs — **fragile, disappear easily**
- Mailing lists (từng carry nhiều context) không keep up với needs của today

---

## Đề xuất: Cần một Archive

### Ý tưởng
- Public, boring, well-funded archive cho Open Source software
- Something with power of endowment hoặc public funding
- Job: not to win developer productivity market, just make sure important things don't disappear

### Cần preserve
- Source archives
- Release artifacts
- Metadata
- Enough project context to understand what happened

### Điều kiện
- **Không tied to business model hoặc leadership mood của single company**

### Đã thấy gì xảy ra
- Google Code died
- Bitbucket changed
- Personal servers và good intentions → projects lost

---

## Kết luận

> "I do not want to go back to the old web of broken tarball links and abandoned Trac instances. I also do not want Open Source to pretend that the last twenty years were normal or permanent. GitHub wrote a remarkable chapter of Open Source, and if that chapter is ending, the next one should learn from it and also from what came before."

---

## Liên quan

- Ghostty leaving GitHub (item 5 trong digest hôm nay)
- pip/PEP 740 trust model (liên quan đến dependency trust)
- npm/xkcd-SupplyChain (liên quan đến micro-dependency problem)