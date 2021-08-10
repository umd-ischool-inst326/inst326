---
title: "Regular Expressions"
subtitle:
revealjs-url: "../../lib/reveal.js.4.0.2"
theme: "inst326_gabriel"
transition: "slide"
---

#

<a title="Daderot [Public domain], via Wikimedia Commons" href="https://imgs.xkcd.com/comics/regular_expressions.png"><img width="450" src="images/regex.png"></a>

#

## Intro to Regular Expressions

- Strings of text that are used in order to match characters in other bodies of text.
- The ability to use Regular Expressions is built into many text editors and programming languages.

#

## Here are Some Examples

| Example            | Matches                                    |
|--------------------|--------------------------------------------|
| [b-chm-pP]at\|ot   | bat, cat, hat, mat, nat, oat, pat, Pat, ot |
| \\d                | 0,1,2,3,4,5,6,7,8,9                        |
| \\d{5}(-\\d{4})?   | Matches a US zip code                      |

#

## Regular Expressions Syntax

#

## Characters
| Regular Expression    | Matches                                                                                  | Example        | Sample   |
|-----------------------|------------------------------------------------------------------------------------------|----------------|----------|
| "any string"          | The string                                                                               | word           | word     |
| \\d                   | Any digit from 0-9                                                                       | number:\\d     | number:5 |
| \\w                   | Any word character                                                                       | \\w\\w         | _Q       |

#

## Characters (continued)
| Regular Expression    | Matches                                                                                  | Example        | Sample   |
|-----------------------|------------------------------------------------------------------------------------------|----------------|----------|
| \\s                   | Any whitespace character                                                                 | \\s            | " "      |
| \\t                   | Tab                                                                                      | T\\t\\w{2}     | T     ab |
| \\D, \\W, \\S         | Any character that is not a digit, word character or whitespace character.               | \\D\\W\\S      | s=2      |

#

## Quantifiers

| Regular Expression | Matches                                | Example     | Sample     |
|--------------------|----------------------------------------|-------------|------------|
| +                  | One or more of the item stated before. | w+          | wwww       |
| {X}                | Exactly X amount of times.             | w{3}        | www        |
| {X,Y}              | Match X to Y amount of times. (greedy) | w{2,4}      | wwww       |
| *                  | Zero or more times (greedy)            | A\*B\*C\*   | AACCCCCC   |

#

## Quantifiers (continued)

| Regular Expression | Matches                                | Example    | Sample      |
|--------------------|----------------------------------------|------------|-------------|
| +                  | One or more times (greedy)             | \\d+       | 1234555     |
| ?                  | Once or none. / Makes quantifiers lazy | words?     | words, word |
| ?                  | Once or none. / Makes quantifiers lazy | \\w{2,4}?  | ab in abcd  |

#

## More Characters

| Regular Expression | Matches                                                 | Example  | Sample                          |
|--------------------|---------------------------------------------------------|----------|---------------------------------|
| .                  | Any character except new line.                          | .        | w                               |
| .*                 | Any character any amount of times except new line.      | .*       | This is an entire line of text. |
| \                  | Escapes special characters for the purpose of matching. | \\.{3}   | ...                             |

#

## Logic

| Regular Expression | Matches                                | Example                  | Sample                                                 |
|--------------------|----------------------------------------|--------------------------|--------------------------------------------------------|
| \|                 | Or/alternating                         | 1{2}\|2{2}               | 11221122 or 11 or 22                                   |
| (...)              | Capturing groups.                      | (\\d{3})\\s\\d{3}-\\d{4} | 301 999-2222 (captures 301)                            |
| [...]              | One of the characters in the brackets. | T[ao]p                   | Tap or Top                                             |
| [...-...]          | Indicates range.                       | [a-z]                    | One lowercase letter.                                  |
| [^x]               | One character that is not x            | [^a-z]{3}                | A1!                                                    |
| ^                  | Start of the string or line            | ^abc.*                   | Abc (assuming that this is the beginning of the string |
| $                  | End of string or line                  | .*? the end$             | this is the end                                        |

#

## Applications for Regular Expressions

::: incremental
- Web Scraping
    - For finding specific data points that we are interested in within a website
        - Say for example addresses or complete first and last names within a webpage
- Data Wrangling
    - For extracting data from large and complex data files (usually unstructured data)

:::

#

## Applications for Regular Expressions (continued)

::: incremental

- Wikipedia
    - For verifying the names of articles
    - [Wikipedia Blacklist](https://en.wikipedia.org/wiki/MediaWiki:Titleblacklist)

:::

#

## Re Module

::: incremental

- Module that provides regular expression matching operations 


:::

#

## Re Module (continued)
- There is a problem, in Python the character “\\” (used to escape special character in Regular Expressions) will escape strings in Python
    - This causes issues when using the backslash for any reason
    - We would constantly need to use double backslashes such as “\\”

#

## Re Module (continued)
- The solution is to use Python’s raw string notation for regular expression patterns
    - backslashes are not handled in any special way in a string literal prefixed with 'r'. 
        - r"\\n" is a two-character string containing '\\' and 'n'
        - "\\n" is a one-character string containing a newline

#
