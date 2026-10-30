# Liberia: law history in git

The law of Liberia as a git history: one file per provision, one commit per law on the day it took effect, and the law that made each change as the commit's author. `git blame` names the law behind every paragraph; `git log` lists every change to a section; `tools/on.py` gives the text in force on any day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `lr/`.

**What is in it now**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitution/` | Constitution of the Republic of Liberia (1986) | 1 | As adopted by the referendum of 3 July 1984, in force 6 January 1986. No amendment is applied: see below |
| `penal-law/` | Penal Law, Title 26 of the Liberian Code of Laws Revised | 4 | 1978 to 2006, rebuilt from the source's own dated notes |
| `freedom-of-information-act/` | Freedom of Information Act of 2010 | 1 | As enacted, in force 6 October 2010 |

The Penal Law's four versions:

| In force | Change | Author |
| --- | --- | --- |
| 1978-04-03 | The Penal Law as LiberLII prints it, with the provisions it dates later shown as they stood before | publisher: oldest version available (Act Adopting a New Penal Law, 1976) |
| 1985-07-09 | § 12.51 (unlawful rewarding of public servants), "as amended by the interim National Assembly, July 9, 1985" | Interim National Assembly (9 July 1985) |
| 1994-12-06 | § 14.54 (Terrorism) inserted, "(Effective December 6, 1994)" | publisher: unexplained (the source names no law) |
| 2006-01-17 | § 14.70 (Rape) replaced, including gang rape; § 14.71 limited to earlier offences | publisher: unexplained (the source names no law) |

Each folder's `README.md` lists every provision, how often it changed and when.

## A lawyer's questions as git commands

| Question | Command |
| --- | --- |
| What did § 14.70 of the Penal Law say on 1 January 2000? | `python tools/on.py 2000-01-01 penal-law sec-14-070` |
| Article 83 of the Constitution today | `python tools/on.py 2026-10-28 constitution art-083` |
| The same, with raw git (bash) | `git show $(git rev-list -1 --before="2000-01-01T23:59:59Z" main -- penal-law/sec-14-070.md):penal-law/sec-14-070.md` |
| The same, in PowerShell | `$r = git rev-list -1 --before="2000-01-01T23:59:59Z" main -- penal-law/sec-14-070.md; git show "$($r):penal-law/sec-14-070.md"` |
| Who wrote each line of § 12.51? | `git blame penal-law/sec-12-051.md` |
| Every change to § 14.70, word by word | `git log -p --word-diff penal-law/sec-14-070.md` |
| Every law in the record, in order | `git log --reverse --format="%ad %an" --date=short main` |
| Everything one law changed | `git show law/ina-1985-07-09` (tags `law/<key>` mark each law's commit) |
| The whole act on a date | `python tools/on.py 1990-01-01 penal-law` |
| Which law gave a provision its wording on a date | `python tools/on.py --law 2006-01-17 penal-law sec-14-070` |

Files are named by the printed number: `art-083` is Article 83; `sec-14-070` is § 14.70 of the Penal Law; `sec-01-03` is Section 1.3 of the Freedom of Information Act; `chap-NN` holds a chapter's heading (and, in the Penal Law, its subchapter headings); `preamble`, `schedule`, `signatories` and `enactment` are what they say.

After a rebuild, refresh tags with `git fetch --force --tags`: a plain fetch keeps stale tags.

## Dates

- Each commit is dated at **noon, Africa/Monrovia (UTC), on the day the change took effect**. The in-force day is also in the `In-force:` trailer, which the tools read.
- **No general default rule was found.** LiberLII's General Construction Law (Title 15) has no rule on when a statute takes effect, so each act's own clause is used. Both acts built here say they "take effect immediately upon publication" (into handbills, for the 2010 Act).
- **Constitution: 6 January 1986**, adopted 3 July 1984 (WIPO Lex, "Entry into force: January 6, 1986; Adopted: July 3, 1984"). Its Art. 94(b) ties its coming into force to an inauguration it schedules for 12 April 1985; WIPO Lex gives 6 January 1986, and that date is used.
- **Penal Law: 3 April 1978.** The Act Adopting a New Penal Law was approved 19 July 1976 and published 3 April 1978 (the Title's own cover), and its section 3, printed at the end of § 51.3, says "This act shall take effect immediately upon publication". LiberLII's Criminal Procedure Law cites the same Act and dates for its repeal of §§ 31.3 and 32.1.
- **The later Penal Law dates are LiberLII's own notes:** "as amended by the interim National Assembly, July 9, 1985" (§ 12.51), "(Effective December 6, 1994)" (§ 14.54), and "(ONLY FOR OFFENSES COMMITTED ON OR AFTER JAN 17, 2006.)" against "(ONLY FOR OFFENSES ON OR BEFORE JAN. 16, 2006.)" (§§ 14.70, 14.71). The 1985 note gives one date, which is taken as the day the change took effect.
- **Freedom of Information Act: 6 October 2010.** Approved 16 September 2010, published 6 October 2010; Chapter 8: "This Act shall take effect immediately upon the publication into Hand-Bills."
- `--before="YYYY-MM-DD"` alone uses your clock's time of day, so a law that took effect that day may be missed before noon. Use `T23:59:59Z` as above, or the tool.

## How it is checked

- Every version is read back from git on the day it took effect and on the day before (`tools/check_repo.py`); both must match `corpus.json`. Results are in `REPRODUCE.md`.
- Health checks: no merge commits on `main`, commit dates never go backwards, nothing dated in the future, and every commit's trailers parse with `git interpret-trailers --parse`.
- **Against the source today** (`tools/verify.py`): for each act, every word of the latest version is printed on the LiberLII page it was parsed from (0 words added in all three acts, apart from the headings "Signatories" and "Enactment", which this repository names itself). Every word the page prints is in the repository, apart from what is left out on purpose: the Constitution's title line; in the Penal Law the Contents list, each chapter's list of sections, the earlier text of § 14.70 (which is in the older versions), and the dated notes listed above (which are in the commit messages). On 2026-10-28 every one of the Penal Law's 1,639 unaccounted words was one of these.
- The Penal Law captures of 20 April 2017 and 3 July 2026 are byte-identical, so LiberLII's text did not change in that time.
- The repository is rebuilt from the same data a second time and must give identical hashes.

## What "author" means

- The author of a commit is the law that made the change, at an address that cannot exist (`<law key>@liberlii.invalid`), so `git blame` names the law. The committer is Lexifina.
- Where the source names no law for a change, the commit is by the publisher, LiberLII, and is labelled "unexplained". The amending laws are not guessed.
- The Penal Law's first version is by the publisher as the **oldest version available**, naming the 1976 Act: it is LiberLII's text with only the dated changes taken out, not a verified text of the Act as enacted.

## What it does not show

- **Constitutional amendments.** Joint Resolution 001 (2010) proposed amending Arts. 52(c), 72(b), 83(a) and 83(b), and went to a referendum on 23 August 2011; a further referendum followed in 2020. LiberLII prints the 1986 text with none of them, and no source with a text layer gives amended wording, so none is applied. The 2011 result for Proposition 4 (Art. 83(b), elections by simple rather than absolute majority) was disputed before the Supreme Court. **`constitution/art-083.md` may not be the wording in force today.**
- **Undated amendments to the Penal Law.** LiberLII consolidates some amendments without a note. Provisions it does not date are shown in every version as it prints them, so older versions may hold wording that came later. Amendments LiberLII has not applied are not shown at all.
- **The earlier wording of § 12.51** (before 9 July 1985) is not given by the source; that file reads "[The source does not give the text in force on this date.]" before 1985.
- **§ 14.78(3) and (4)** are repealed by the new § 14.70(5)(b) (2006), but LiberLII still prints them, and they are kept as printed.
- **The earlier § 14.70 and § 14.71 still govern offences committed on or before 16 January 2006.** The file for a section shows the text for new offences.
- **Other law.** Only these three acts. Liberia's government sites publish recent acts as scanned PDFs (for example the 2026 data protection act and the Cybercrime Act of 2025 on emansion.gov.lr, and the FOI and Police Acts on moj.gov.lr), and this repository does not read scans. The Criminal Procedure Law and Civil Procedure Law are on LiberLII, but it gives no effective date for either, so they are not built yet.
- This is not legal advice, and it is not an official text.

## How it is built

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file. `tools/build.py` writes this repository from that file, and the same corpus always gives the same commit hashes; `REPRODUCE.md` gives the details and the checks. A model (Claude) wrote Lexifina's code; it wrote no legal text, and no model runs when the history is built.

No model wrote, summarised or parsed any legal text.

## Sources

- **LiberLII**, the Liberia Legal Information Institute (www.liberlii.org), part of the WorldLII family. Pinned captures: Constitution 2024-05-24 (`col1986235`), Penal Law 2026-07-03 (`plt26lcolr367.html`, identical to 2017-04-20), Freedom of Information Act 2024-06-30 (`foia222`), General Construction Law 2024-07-14, Criminal Procedure Law 2017-08-09.
- **WIPO Lex**, Constitution of the Republic of Liberia (<https://www.wipo.int/wipolex/en/legislation/details/8556>), for the dates of adoption and entry into force.
- **National Elections Commission, Referendum Regulations** (28 February 2011, via aceproject.org), for Joint Resolution 001 (2010).
- Probed and not used: emansion.gov.lr and moj.gov.lr (scanned PDFs), legislature.gov.lr (does not resolve), necliberia.org (403).

## Licence

See [LICENSE](LICENSE). The legal texts are from LiberLII, read through the Internet Archive; LiberLII publishes no licence for its legislation pages, and Liberian legislation is public law. Lexifina's own contributions are dedicated to the public domain under CC0 1.0.

## Liberia

English is Liberia's official language, so this README has no second-language section.
