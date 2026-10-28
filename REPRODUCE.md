# How this repository was made (Liberia)

This file is written by the build on 2026-10-28, the day the source data was retrieved. Everything below is enough to rebuild this repository hash for hash.

## Sources

| Source | Address | Retrieved | Requests | Licence |
| --- | --- | --- | ---: | --- |
| LiberLII via the Internet Archive (web.archive.org id_ captures) | <https://www.liberlii.org> | 2026-10-28 | 6 | none published; legislation is public law |
| WIPO Lex: Constitution of the Republic of Liberia | <https://www.wipo.int/wipolex/en/legislation/details/8556> | 2026-10-28 | 1 | WIPO terms of use |

Every response is cached by the sha256 of its URL, and the table above lists every source with its retrieval date. Lexifina keeps its fetch scripts privately; `tools/parse.py` reads only the cache and writes `corpus.json`, so the same cache always gives the same corpus.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | Constitution of the Republic of Liberia (1986) | 1 | 1986-01-06 to 1986-01-06 |
| `penal-law` | Penal Law (Title 26, Liberian Code of Laws Revised) | 4 | 1978-04-03 to 2006-01-17 |
| `freedom-of-information-act` | Freedom of Information Act of 2010 | 1 | 2010-10-06 to 2010-10-06 |

The build made 6 commits:

| Commits | Kind |
| ---: | --- |
| 3 | first version of an act |
| 1 | one law on its in-force day |
| 2 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-28.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 4 laws in the record.
- 9 tags.

## Dates

Each commit is dated at noon (Africa/Monrovia) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: No general default rule was found in the sources read (the General Construction Law, Title 15, on LiberLII has none). Each act's own effective-date clause is used: the Penal Law and the Freedom of Information Act each take effect immediately upon publication, on the publication date the act itself prints. https://web.archive.org/web/20240714145606id_/http://www.liberlii.org/lr/legis/codes/gclt15lcolr538/

## Commands, in order

```sh
# fill the cache from the sources listed above (network; Lexifina's fetch scripts are kept privately)
python -X utf8 tools/parse.py                  # cache -> corpus.json (no network)
python -X utf8 tools/build.py <folder> --repo <empty folder> --docs-date 2026-10-28
python -X utf8 tools/check_repo.py <repo> --corpus <folder>/corpus.json --write
python -X utf8 tools/build.py <folder> --repo <another empty folder> --docs-date 2026-10-28 --compare <repo>
```

In the main Lexifina repository these files live as follows:
- `fetch.py`, `parse.py` and `repo/`: in `scripts/liberia-law/`.
- `build.py`, `check_repo.py` (`check.py` there) and `on.py`: in `scripts/gitlaw_common/`, with the corpus format in `SCHEMA.md`.

## Exact inputs

- `corpus.json` sha256 `38c630c679bb394689576aac71fe3318a62adc788d07b0eb6b514b158d08d1c1` (376006 bytes)
- Script blob hashes (`git hash-object`):

| Script | Blob |
| --- | --- |
| build.py | `833a2433a3ea96fd87477ccc7a2ed47dc9e24b48` |
| check.py | `426d4cfb32ce103715be6a00865c0a7bca81a56a` |
| on.py | `644a6c0857fbcc72562032b58d57aa113fee0641` |
| fetch.py | `60a863878ee2185f49e2e082bdcdab494964d8a0` |
| parse.py | `09ea5efec2438ad4139f44d70fbb1e56d70d7099` |

- Tools:
  - Python 3.14.0
  - git version 2.52.0.windows.1
  - curl 8.21.0 (Windows) libcurl/8.21.0 Schannel zlib/1.3.2 WinIDN WinLDAP

## Checks

6 versions of 3 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

A second build from the same corpus into an empty folder gave identical hashes for all 6 history commits and 9 tags (history tip `316f39e0fb190dc15b6f60ef05d869f2059ebb0a`).

These results are from the check run on the build before this one, from the same corpus.

## Decisions made by hand

- Source: no Liberian government site gives legislation with a text layer. emansion.gov.lr and moj.gov.lr PDFs probed on 2026-10-28 (Data Protection Act 2026, Cybercrime Act 2025, FOI Act, Police Act) are scans with only a cover-page text layer, so they are not used (no OCR). legislature.gov.lr did not resolve.
- LiberLII is read only through Internet Archive id_ captures, never from liberlii.org (user decision of 2026-10-28: 'scraping wayback is fair game, dont overdo it'). The captures are pinned in sources.json.
- LiberLII gives one text per act, not dated versions. Its pages carry an internal 'sino date' (Penal Law 3 April 1978, Constitution 1 January 1986, FOI Act 16 September 2010) that is not an as-at date and is not used.
- Constitution: one version, in force 6 January 1986 and adopted 3 July 1984 (WIPO Lex). Art. 94(b) names 12 April 1985 as the planned inauguration; WIPO Lex's in-force date is used.
- Constitution: the 2011 referendum (Joint Resolution 001 (2010), adopted by the Legislature 17 August 2010 per the NEC Referendum Regulations of 28 February 2011) and the 2020 referendum are not applied: LiberLII prints Art. 83(b) unamended, and no source with a text layer gives amended wording.
- Constitution units: preamble, chapter headings (chap-NN), Articles 1-97 (art-NNN), the Schedule (oath), and the signatories (National Constitution Commission, Constitutional Advisory Assembly).
- Penal Law in force 3 April 1978: the Act Adopting a New Penal Law, approved 19 July 1976, published 3 April 1978 (the Title's own cover), says 'This act shall take effect immediately upon publication' (its section 3, printed at the end of § 51.3); LiberLII's Criminal Procedure Law cites the same act and dates for its repeal of §§ 31.3 and 32.1.
- Penal Law versions are rebuilt only from LiberLII's own dated annotations: § 12.51 ('as amended by the interim National Assembly, July 9, 1985'), § 14.54 ('Effective December 6, 1994'), § 14.70 and § 14.71 ('ONLY FOR OFFENSES ... ON OR AFTER JAN 17, 2006' / 'ON OR BEFORE JAN. 16, 2006'). The 2017-04-20 and 2026-07-03 captures give identical text.
- Penal Law § 12.51: the 1985 note is taken as an editorial note and removed from the text; its date is used as the in-force date of the change. The wording before 9 July 1985 is not given, so the 1978 version reads '[The source does not give the text in force on this date.]' (anachronism rule) and the 1985 change is credited to 'Interim National Assembly (9 July 1985)', the body the note names.
- Penal Law § 14.54 (Terrorism) is absent before 6 December 1994; LiberLII names no amending law, so the change is committed as unexplained by the publisher.
- Penal Law § 14.70 (Rape): the text marked for offences on or before 16 January 2006 is the 1978-2006 text, the one marked from 17 January 2006 is today's; § 14.71 gains the source's marker line in 2006. LiberLII names no amending law (unexplained). The earlier texts continue to govern offences committed before 17 January 2006.
- Penal Law § 14.78(3) and (4) are repealed by the new § 14.70(5)(b), but LiberLII still prints them; they are kept as printed, so today's text equals the source.
- Penal Law: provisions LiberLII does not date are shown in every version as it prints them; they may include later amendments LiberLII does not mark (for example any made after 2006). The first version is credited to the publisher as the oldest version available, naming the 1976 Act, not as the act as enacted.
- Penal Law units: part-N, chapter headings with their subchapter headings (chap-NN), and sections (sec-CC-SSS). The Contents list and each chapter's list of sections are outlines and are left out.
- Freedom of Information Act 2010: one version, in force 6 October 2010 (approved 16 September 2010, published into handbills 6 October 2010; Chapter 8: effective on publication into handbills). No amendment is known to LiberLII.
- Criminal Procedure Law (Title 2) and Civil Procedure Law (Title 1) are not built yet: LiberLII gives no effective date for either Title, so a first version cannot be dated from the source.

## What AI did and did not do

The fetch, parse and check scripts were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above, through code that anyone can rerun.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none: no model wrote, summarised or parsed legal text. Claude Code (Claude Opus 5.5, claude-opus-5-5) wrote fetch.py and parse.py and chose the sources; parsing is deterministic code.
