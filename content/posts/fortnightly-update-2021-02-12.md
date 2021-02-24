---
title: Fortnightly Update - 2021-02-12
date: 2021-02-12
author: James
tags:
- status-update
---
The team learned of some existing issues in the [`black`](https://github.com/psf/black/) Python code formatter that we use to format some of our published code, and is providing time to help.

The team has also been working on maintenance and bugfixes since the last fortnightly update:

- Preparations have been put in place to update RecipeRadar when the release of [`SQLAlchemy`](https://github.com/sqlalchemy/sqlalchemy/) v1.4 lands, which is anticipated within the next few weeks

- A serious user-facing bug that prevent recipe scaling was [identified and fixed](https://github.com/openculinary/frontend/issues/191) - we believe that this affected users who retrieved the application between 2021-01-06 and 2021-02-08

- We have migrated handling of fractional amounts in the application to use a purpose-designed library, [`fraction.js`](https://www.npmjs.com/package/fraction.js)

- An updated version of [`hashedixsearch`](https://pypi.org/project/hashedixsearch/) was released

- Progress on collaborative editing has continued, and most recently we've begun experimenting with [`Markdown`](https://en.wikipedia.org/wiki/Markdown) syntax highlighting of shared text

**Coming up next**

There are a few different directions we would like to continue in:

- Ensuring that the credits on the site are updated to reflect more of the contributions included so far

- Providing NPM packaging for our published `feedback.js` modifications could be beneficial long-term, even if we are the only consumers of it for now

- Multi-user and multi-device collaboration, as ever, remains a product area that we would like to progress

- Continuing our blog series on [ingredient parsing](https://blog.reciperadar.com/posts/introduction-to-ingredient-parsing/) would be worthwhile
