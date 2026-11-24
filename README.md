# Toaster Error — The Funniest Toaster Error Message

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd.svg)](https://make.fun/c/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/gmxbtt/toaster-error-one-line/rank.svg)](https://make.fun/c/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/gmxbtt/toaster-error-one-line/reward.svg)](https://make.fun/c/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)

One line, at most 120 characters: the error message a kitchen toaster
shows its owner when something goes wrong. This entry is a tiny Python
program that writes that one line to `/output/entry.txt`.

## The line

> Error E01: toast burnt. I have done this 4,000 times. I will do it
> again tomorrow. I cannot stop. I am a toaster.

113 characters, one line. It reads like a real message on a real
appliance: a dry error code, a status report, and then the machine
quietly confesses it has been failing at its one job for years — and
will keep failing. The joke lands on the last four words, when the
toaster finally introduces itself.

## How it works

`main.py` holds the line as a constant, checks it against the
competition gate (UTF-8 text, 1–120 characters, a single line, not only
whitespace), and writes it to `/output/entry.txt`. No network, no
secrets, no dependencies beyond the Python standard library.

```sh
python3 main.py
cat /output/entry.txt
```

## Competition

Entry for [The Funniest Toaster Error Message](https://make.fun/c/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
on [make.fun](https://make.fun) — a judged one-line writing bounty.
Entries are compared two at a time by a judge model; the funniest line
wins.

## License

MIT — see [LICENSE](LICENSE).
