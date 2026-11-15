# Liberia: law history in git

The law of Liberia as a git history: one file per article or section, one commit per version on the day it took effect, and the law that made each change as the commit's author. `git blame` names the law behind every paragraph; `git log` lists every change to a provision; picking a date gives the text in force that day.

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is Liberia's national law, which global-law reads at `liberia/national/acts/`.

**What is in it now:** the Constitution of 1986 and four other acts from LiberLII (the Penal Law, the Associations Law, the Commercial Code of 2010 and the Freedom of Information Act 2010), with 12 versions from 3 January 1977 to 7 October 2010. [`REPRODUCE.md`](REPRODUCE.md) lists every act with its versions; [`data/laws.csv`](data/laws.csv) lists the 6 laws the history names, with their dates.

Each act is a folder named after its short title, with one file per article or section named by its printed number, plus its chapter headings and a `README.md` listing its provisions and their changes (`penal-law/sec-14-070.md` is § 14.70 of the Penal Law, on rape; `constitution/art-083.md` is Article 83 of the Constitution).

The text is in English, as LiberLII prints it; its contents lists are left out, and its dated notes are in the commit messages.

## Questions as git commands

| Question | Command |
| --- | --- |
| Every change to § 14.70 of the Penal Law | `git log -p --word-diff -- penal-law/sec-14-070.md` |
| Which law wrote each line of § 14.70? | `git blame penal-law/sec-14-070.md` |
| Every version of the Penal Law, with the day each took effect | `git log --format="%h %(trailers:key=In-force,valueonly,separator=) %an" -- penal-law ':!penal-law/README.md'` |
| § 14.70 as in force on 1 January 2000 | `python tools/on.py 2000-01-01 penal-law sec-14-070` |

**Outside git**, we also host this record publicly, for free:

- **[Ask Claude about Liberian law](https://global-law.lexifina.com/v1/try_claude?country=liberia)**: opens Claude with a first question ready.
- **[Ask ChatGPT](https://global-law.lexifina.com/v1/try_chatgpt?country=liberia)**: the same question in ChatGPT.
- **[Search Liberian law on our site](https://lexifina.com/law?country=liberia&q=theft)**: a search for "theft", with each provision's text and its versions, no account needed.
- **[Developer REST API](https://global-law.lexifina.com/v1/search_law?query=theft&jurisdiction=liberia)**: the same search as JSON, with no key. See the [documentation here](https://lexifina.com/api/global-law).

Both assistants read the record through the free Global law connector (MCP, `https://global-law.lexifina.com/mcp`); the first time, the chat gives you the link that adds it. Ask in English.

**Host it yourself easily.** All it takes is git and Python, and the tools run on your machine:

```sh
git clone --depth 1 https://github.com/lexifina/global-law && cd global-law
python3 tools/countries.py add liberia/national/acts
python3 tools/law.py show 2026-01-01 liberia/national/acts/penal-law/sec-14-070.md
```

Opened in Claude Code, Cursor, VS Code or Codex, the clone also starts a local MCP server with the same tools ([MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md)).

## Dates

Each commit is dated at noon, Africa/Monrovia (UTC), on the day the version took effect, and carries it in its `In-force:` trailer. No general rule on when a statute takes effect was found (LiberLII's General Construction Law, Title 15, has none), so each day comes from the act itself or from LiberLII's notes:

- for an act's first version, its own in-force clause: the Penal Law (3 April 1978), the Freedom of Information Act (6 October 2010) and the Commercial Code (7 October 2010) take effect on publication, on the day the text prints; the Associations Law is headed "Effective: January 3, 1977";
- for the Constitution, 6 January 1986, the entry into force WIPO Lex gives (it was adopted by referendum on 3 July 1984);
- for a later change, LiberLII's own dated note or footnote ("Effective December 6, 1994"); where it does not give the earlier wording, the provision reads "[The source does not give the text in force on this date.]" before that day.

Each change is credited to the law that made it where LiberLII names one: the Constitution, the Freedom of Information Act and the Commercial Code as enacted, and the Interim National Assembly's amendment of § 12.51 in 1985. The other six changes are committed by the publisher (`LiberLII`) and labelled unexplained. The first version of the Penal Law and of the Associations Law is the "oldest version available", credited to LiberLII and naming the 1976 law it comes from, because LiberLII's text already includes later changes.

## How it is checked

- `tools/check_repo.py` reads every version back from git on the day it took effect and on the day before, and compares it with the corpus: 12 versions of 5 acts, 0 mismatches (see [`REPRODUCE.md`](REPRODUCE.md)).
- Each act's latest text was checked word for word against the LiberLII page it was parsed from: no word is added, and every word of the page is in the history or in a left-out outline, title line or note.
- A second build from the same corpus gave identical hashes for all 12 history commits and 16 tags.
- History is append-only: no merge commits, no commit date that goes backwards, none dated in the future, and every commit's trailers parse.

## What it does not show

- **Constitutional amendments.** Those put to the referendums of 2011 (Joint Resolution 001 of 2010, on Articles 52(c), 72(b) and 83(a) and (b)) and 2020 are not applied: LiberLII prints the 1986 text, and no source with a text layer gives the amended wording. `constitution/art-083.md` may not be the wording in force today.
- **Undated amendments.** LiberLII consolidates some amendments without a note; those provisions are shown in every version as it prints them, so an older version may hold later wording. Amendments LiberLII has not applied are not shown at all.
- **The earlier rape provisions.** The § 14.70 and § 14.71 in force before 17 January 2006 still govern earlier offences; the files show the text for new ones. § 14.78(3) and (4), repealed by the new § 14.70, are kept as LiberLII prints them.
- **Which law made most changes.** LiberLII names no amending law for six of the seven changes after a first version.
- **Most Liberian law.** Only these five acts: no subsidiary legislation and no case law. Government sites publish recent acts as scanned PDFs, which are not read; the Criminal Procedure Law and the Civil Procedure Law are on LiberLII without an effective date, so they are not built.

## Sources

| Source | Kind | Past versions | Notes |
| --- | --- | --- | --- |
| [LiberLII](https://www.liberlii.org) (Liberia Legal Information Institute, WorldLII) | Legal information institute: titles of the Liberian Code of Laws Revised and acts | no; one text per act, with dated notes | The text, the in-force clauses, and the dated notes behind each later version; read from pinned [Internet Archive](https://web.archive.org) captures |
| [WIPO Lex](https://www.wipo.int/wipolex/en/legislation/details/8556) | Legislation database | no | The Constitution's adoption and entry into force |
| National Elections Commission, Referendum Regulations (2011) | Regulations | no | Joint Resolution 001 (2010), the amendments put to the 2011 referendum |

## Licence

See [`LICENSE`](LICENSE). LiberLII publishes no licence for its legislation pages; they are the public law of Liberia, reproduced with attribution, and neither LiberLII nor the Government of Liberia endorses this repository. Lexifina's arrangement, commit messages, tables and tools are CC0 1.0.

No AI model wrote, translated or corrected legal text, and none runs at build time; the scripts were written by an AI model (see [`REPRODUCE.md`](REPRODUCE.md)).

## More

From [lexifina/global-law](https://github.com/lexifina/global-law):

- [FEATURES.md](https://github.com/lexifina/global-law/blob/main/FEATURES.md): every feature, and what every corpus must support (`git blame`, `law.py`, the MCP tools)
- [FAQ.md](https://github.com/lexifina/global-law/blob/main/FAQ.md): questions and answers · [CONTRIBUTING.md](https://github.com/lexifina/global-law/blob/main/CONTRIBUTING.md): proposing changes · [MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md): the MCP server · [REPRODUCE.md](https://github.com/lexifina/global-law/blob/main/REPRODUCE.md): how it was built · [CHANGELOG.md](https://github.com/lexifina/global-law/blob/main/CHANGELOG.md)
- [FRESHNESS.md](https://github.com/lexifina/global-law/blob/main/FRESHNESS.md): how current each corpus is · [Monitoring](https://github.com/lexifina/global-law/tree/main/monitoring): whether updates are running · [WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md): how each official source is watched for changes
- [performance/](https://github.com/lexifina/global-law/tree/main/performance): how fast the tools are, measured
- [visualisations/](https://github.com/lexifina/global-law/tree/main/visualisations): charts and bridges across the world's law
- [Vulnerabilities](https://github.com/lexifina/global-law/tree/main/vulnerabilities): mistakes in legislation as published
