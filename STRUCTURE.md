# Structure

| Folder | What it holds |
| --- | --- |
| `constitution/` | The Constitution of the Republic of Liberia (1986), one file per article (`art-083.md`) |
| `codes/title-NN-<slug>/` | A title of the Liberian Code of Laws Revised, e.g. `codes/title-26-penal-law/`, `codes/title-01-civil-procedure-law/` |
| `acts/<year>/<slug>/` | A separate Act, by the year it took effect, e.g. `acts/2010/freedom-of-information-act/` |

Each folder holds one file per section (`sec-14-070.md` is § 14.70; `sec-012.md` is section 12), a `preamble.md` for
the text before the first section, and a `README.md` with the source and the section headings. No folder holds more
than 1,000 entries.

## Dates

Each version is one commit, dated 12:00 Africa/Monrovia (UTC+0) on the day it took effect, which its `In-force:`
trailer repeats; `In-force-basis:` says which words of the document give that day (for example an Act's "shall take
effect immediately upon publication into handbills" with the printed publication date). Before 1970, which git
cannot store, a commit is dated 1 January 1970 and the real day is in its subject and `In-force:` trailer. No date
in this repository is the day we downloaded anything; a document whose day its source does not give is held.

## Sources

The Constitution, the Penal Law, the Associations Law, the Commercial Code and the Freedom of Information Act come
from LiberLII pages read as Internet Archive copies (see REPRODUCE.md). Later additions are the PDFs Liberian
government agencies publish (the Liberia Land Authority's laws repository, ministries' sites), read from the PDF's
own text layer: no OCR of ours. A copy that is not the official gazette or handbill is tagged `Source-status`.
