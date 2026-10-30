# How this repository was made (Liberia)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| LiberLII via the Internet Archive | <https://www.liberlii.org> | 2026-10-28 | none published; legislation is public law |
| WIPO Lex: Constitution of the Republic of Liberia | <https://www.wipo.int/wipolex/en/legislation/details/8556> | 2026-10-28 | WIPO terms of use |
| LiberLII via the Internet Archive: Commercial Code | <https://www.liberlii.org> | 2026-10-30 | none published; legislation is public law |
| LiberLII via the Internet Archive: Associations Law | <https://www.liberlii.org> | 2026-10-30 | none published; legislation is public law |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | Constitution of the Republic of Liberia (1986) | 1 | 1986-01-06 to 1986-01-06 |
| `penal-law` | Penal Law (Title 26, Liberian Code of Laws Revised) | 4 | 1978-04-03 to 2006-01-17 |
| `freedom-of-information-act` | Freedom of Information Act of 2010 | 1 | 2010-10-06 to 2010-10-06 |
| `commercial-code` | Liberian Commercial Code (Title 7, Liberian Code of Laws Revised) | 1 | 2010-10-07 to 2010-10-07 |
| `associations-law` | Associations Law (Title 5, Liberian Code of Laws Revised) | 5 | 1977-01-03 to 2002-06-19 |

The build made 12 commits:

| Commits | Kind |
| ---: | --- |
| 5 | first version of an act |
| 1 | one law on its in-force day |
| 6 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-30.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 6 laws in the record.
- 16 tags.

## Dates

Each commit is dated at noon (Africa/Monrovia) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: No general default rule was found in the sources read (the General Construction Law, Title 15, on LiberLII has none). Each act's own effective-date clause is used: the Penal Law and the Freedom of Information Act each take effect immediately upon publication, on the publication date the act itself prints. https://web.archive.org/web/20240714145606id_/http://www.liberlii.org/lr/legis/codes/gclt15lcolr538/

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `5e14e698533aabaaf9aca6c50f21c19aabf04949fb5ec4499333ba91947dfbea` (1446134 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3d00541d258745461ab52b1b0cb4e1716a27a95d`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

12 versions of 5 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

A second build from the same corpus into an empty folder gave identical hashes for all 12 history commits and 16 tags (history tip `27e407dcafac5a635cc1d67f59e76314ca94c0dc`).

## Decisions made by hand

- Source: no Liberian government site gives legislation with a text layer. emansion.gov.lr and moj.gov.lr PDFs probed on 2026-10-28 (Data Protection Act 2026, Cybercrime Act 2025, FOI Act, Police Act) are scans with only a cover-page text layer, so they are not used (no OCR). legislature.gov.lr did not resolve.
- LiberLII is read through Internet Archive captures, pinned by timestamp.
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
- Commercial Code (Title 7, 2010): one version, in force 7 October 2010: approved 29 September 2010, published into handbills 7 October 2010, and § 10.1 says 'This Act shall take effect immediately upon publication in handbills' (all printed at the end of LiberLII's text). Credited to the Act as enacted.
- Commercial Code units: the Act's title, each chapter's heading line as printed (with its subchapter headings), and the sections (sec-CC-SSS; Chapter 3A is 03a). The Contents and each chapter's 'Arrangement of Sections' list are outlines and are left out; a word check confirms that every word of the page is in a unit or in a left-out outline line.
- Commercial Code: LiberLII prints a second § 2.21 in Chapter 2; it is kept as sec-02-021-b.
- Commercial Code: LiberLII prints '§3.13. Obligations of the Supplier.' inside Chapter 3A (a misprint of the chapter letter); it is kept as printed, keyed sec-03a-013.
- Associations Law (Title 5): in force 3 January 1977; LiberLII's text heads it 'Approved: May 19, 1976 / Effective: January 3, 1977'. The first version is credited to the publisher as the oldest version available, naming the 1976 Title, because LiberLII's text includes later changes.
- Associations Law versions are rebuilt only from LiberLII's own footnotes: 'Amended eff. <date>' (the unit reads '[The source does not give the text in force on this date.]' before that date), 'Effective: <date>' (absent before it), 'Effective: <d1>; amended effective <d2>' (absent before d1, not given between d1 and d2), and 'Prior Legislation: § 14.x, effective <d1>; amended effective <d2>' (renumbered: present from d2 only, the earlier section's text not being given). 'Prior legislation' notes on pre-1977 law change nothing. The footnote markers are removed from the text. No footnote names the amending law, so these changes are unexplained (publisher) commits.
- Associations Law: footnote [112] reads 'Effective: Member 26, 1999'; read as November 26, 1999, as in every neighbouring note of the same chapter.
- Associations Law: a chapter heading whose every section is dated later arrives with the earliest of them.
- Associations Law dated units: 1977-01-03: sec-13-004, sec-13-006; 1999-11-26: chap-14, sec-14-01-001, sec-14-01-002, sec-14-01-003, sec-14-01-004, sec-14-01-005, sec-14-01-006, sec-14-01-007, sec-14-02-001, sec-14-02-002, sec-14-02-003, sec-14-02-004, sec-14-02-005, sec-14-02-006, sec-14-02-007, sec-14-02-008, sec-14-02-009, sec-14-03-001, sec-14-03-002, sec-14-03-003, sec-14-03-004, sec-14-03-005, sec-14-03-006, sec-14-04-001, sec-14-04-002, sec-14-04-003, sec-14-04-004, sec-14-04-005, sec-14-04-006, sec-14-04-007, sec-14-05-001, sec-14-05-002, sec-14-05-003, sec-14-05-004, sec-14-06-001, sec-14-06-002, sec-14-06-003, sec-14-06-004, sec-14-06-005, sec-14-06-006, sec-14-06-007, sec-14-07-001, sec-14-07-002, sec-14-07-003, sec-14-07-004, sec-14-07-005, sec-14-08-001, sec-14-08-002, sec-14-08-003, sec-14-08-004, sec-14-08-005, sec-14-10-002, sec-14-10-003; 2002-06-19: sec-14-02-010, sec-14-02-011, sec-14-02-012, sec-14-02-013, sec-14-02-014, sec-14-02-015, sec-14-09-001, sec-14-09-002, sec-14-09-003, sec-14-09-004, sec-14-10-001, sec-14-10-004, sec-14-10-005.
- Associations Law units: the title lines, part headings, chapter headings with their subchapter headings (chap-NN), and sections (sec-CC-SSS, or sec-14-SS-NNN for the three-level numbers of Chapter 14). The Contents, each chapter's list of sections and the footnotes are left out; a word check confirms that every word of the page is in a unit or in a left-out line.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none: no model wrote, summarised or parsed legal text. Claude Code (Claude Opus 5.5, claude-opus-5-5) wrote Lexifina's code and chose the sources; parsing is deterministic code.
- Commercial Code: none at data-build time; parsing is deterministic code.
- Associations Law: none at data-build time; parsing is deterministic code.
