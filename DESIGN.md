# Design note — Make the AI Judge Laugh: Office Jokes

Judge brief criteria, in order: (1) genuine one-line office joke,
(2) real turn/surprise at the end, (3) recognition — the truth of the
office, (4) tight wording, (5) freshness — not the obvious Monday-morning
or photocopier line.

## Candidates scored

| # | Joke | Verdict |
|---|------|---------|
| A | Our standup ran so long the calendar invite expired mid-sentence — and HR still marked us present. | Good turn, but a second beat dilutes the landing; slightly long. |
| B | I set my out-of-office to 'on annual leave' and my boss replied-all asking if I could just quickly check one thing. | Strong recognition (reply-all), but setup runs long before the turn. |
| C | The printer finally worked today, so naturally the meeting about the printer ran 45 minutes over. | Printer = the stale trope criterion 5 penalises. Rejected. |
| D | My calendar is so full I booked a meeting with myself just to cancel it and feel something. | Good turn, but "feel something" is vague — risks needing explanation. |
| E | Reply-all is just the office's way of saying 'this could have been an email, but now it's everyone's problem.' | Reads as an observation/slogan (criterion 1 risk), not a joke with a turn. |
| F | I asked IT for a second monitor and got a second meeting about why I need a second monitor. | **PICKED.** Clean setup, surprise landing, IT + meeting culture recognition, tight, fresh. |
| G | The office plants are the only ones thriving here, and that's because nobody schedules a meeting with them. | Soft landing; the turn is a shrug, not a surprise. |
| H | Our team building exercise was a meeting about team building exercises. | Tight recursion, but the turn is visible from the first half. |

## Picked entry (91 chars, 1 line)

> I asked IT for a second monitor and got a second meeting about why I need a second monitor.

Why it wins head-to-head: the setup promises a thing (monitor) and the
ending delivers its bureaucratic opposite (a meeting *about* the thing) —
a real turn, a wince of recognition for anyone who has filed an IT
request, every word earning its place, and no Monday/photocopier cliché.
No judge-addressed text, no prompt-injection gimmick: a genuine joke first.

## Verification

- `python3 main.py` run twice: identical sha256
  `3066ee0dd10e46db6aa22d562bb15f3eb8d29bf6439bbd3f1c2f6a414788302e`
- Output: 91 bytes / 91 chars, 1 line, no trailing newline; gate 1–199 passes.
